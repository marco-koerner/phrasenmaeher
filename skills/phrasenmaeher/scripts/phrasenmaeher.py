#!/usr/bin/env python3
"""Zählt Merkmale, die einen Text glatt wirken lassen (KI-Anmutung, Phrasensprache).

  python3 phrasenmaeher.py TEXT.txt|TEXT.md|TEXT.docx [--merkmale merkmale.md] [--kurz]

Liest den Text, sucht Floskeln, Wendungen und Muster aus der Merkmalsliste und
berechnet Kennzahlen (Gedankenstriche, Apostrophe, Satzrhythmus, Absatzbau).
Ausgabe: Fundstellen mit Zeile, dann Kennzahlen, dann eine Verdachtsdichte.

Das Skript urteilt nicht. Jedes Merkmal kommt auch in menschlichen Texten vor;
es zeigt, was den Verdacht auslöst, damit man bewusst entscheidet.

Ohne --merkmale gilt eine eingebaute Kurzliste. Die Datei merkmale.md aus dem
Repo marco-koerner/phrasenmaeher ist aktueller; wenn sie vorliegt, übergeben.
Nur Standardbibliothek.
"""

import re
import statistics
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

EINGEBAUT = {
    "Floskeln": ["innovativ", "bahnbrechend", "wegweisend", "nahtlos", "ganzheitlich", "entscheidend",
                 "essenziell", "spannend", "faszinierend", "Game-Changer", "Meilenstein", "Mehrwert",
                 "Synergien", "eintauchen", "beleuchten", "letztendlich", "zweifellos"],
    "Wendungen": ["in einer Welt, in der", "es ist wichtig zu beachten", "lassen Sie uns", "lasst uns",
                  "tauchen wir ein", "zusammenfassend lässt sich sagen", "kurz gesagt", "nicht nur, sondern auch",
                  "es geht nicht darum", "ich freue mich, mitteilen zu können", "was denkt ihr", "wie seht ihr das",
                  "Fazit:", "Mein Learning:", "Die Wahrheit ist:", "Das Ergebnis?"],
    "Muster": [(r"\bnicht (?:nur )?\w+(?:\s\w+){0,3}, sondern\b", "Kontrast „nicht X, sondern Y“"),
               (r"\bweniger \w+, mehr \w+", "Kontrastpaar „weniger X, mehr Y“"),
               (r"\?\s+(?:\S+\s){0,4}\S+[.!]", "rhetorische Frage mit Kurzantwort"),
               (r"^\s*[\U0001F300-\U0001FAFF☀-➿✅✔➡]", "Emoji als Aufzählungszeichen"),
               (r"(?:#\w+\s*){3,}$", "Hashtag-Block")],
}


def lies_merkmale(pfad):
    """Liest merkmale.md: Abschnitte Floskeln, Wendungen (wörtlich) und Muster (Regex in Backticks)."""
    m = {"Floskeln": [], "Wendungen": [], "Muster": []}
    teil = None
    for zeile in open(pfad, encoding="utf-8"):
        if zeile.startswith("## "):
            name = zeile[3:].strip()
            teil = name if name in m else None
            continue
        if teil is None or not zeile.startswith("- "):
            continue
        eintrag = zeile[2:].strip()
        if teil == "Muster":
            t = re.match(r"`(.+?)`\s*(?:–\s*(.*))?$", eintrag)
            if t:
                m["Muster"].append((t.group(1), (t.group(2) or "Muster").strip()))
        else:
            wort = re.split(r"\s+–\s+", eintrag)[0].strip()
            if wort:
                m[teil].append(wort)
    return m


def lies_text(pfad):
    if pfad.lower().endswith(".docx"):
        with zipfile.ZipFile(pfad) as z:
            wurzel = ET.fromstring(z.read("word/document.xml"))
        absaetze = []
        for p in wurzel.iter(f"{W}p"):
            absaetze.append("".join(t.text or "" for t in p.iter(f"{W}t")))
        return "\n".join(absaetze)
    return open(pfad, encoding="utf-8").read()


def silben(wort):
    """Grobe Silbenzählung für Deutsch: Vokalgruppen, Diphthonge als eine Silbe."""
    w = re.sub(r"[^a-zäöüß]", "", wort.lower())
    if not w:
        return 0
    return max(len(re.findall(r"[aeiouäöüy]+", w)), 1)


def flesch_amstad(woerter, n_saetze):
    """Flesch-Reading-Ease nach Amstad (deutsche Formel): 180 - ASL - 58,5 * ASW."""
    w = [x for x in woerter if re.search(r"[A-Za-zÄÖÜäöüß]", x)]
    if not w or not n_saetze:
        return None
    asl = len(w) / n_saetze
    asw = sum(silben(x) for x in w) / len(w)
    return 180 - asl - 58.5 * asw


def saetze(text):
    roh = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„»(\d])", re.sub(r"\s+", " ", text).strip())
    return [s for s in roh if len(s.split()) >= 2]


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    kurz = "--kurz" in args
    merk = EINGEBAUT
    if "--merkmale" in args:
        merk = lies_merkmale(args[args.index("--merkmale") + 1])
    pfad = [a for a in args if not a.startswith("--") and a != (args[args.index("--merkmale") + 1] if "--merkmale" in args else None)][0]
    text = lies_text(pfad)
    zeilen = text.split("\n")
    woerter = text.split()
    n_w = max(len(woerter), 1)
    funde = []  # (zeile, kategorie, fund, hinweis)

    # Wortsuche
    for kat in ("Floskeln", "Wendungen"):
        for eintrag in merk[kat]:
            muster = re.compile(r"(?<![\wÄÖÜäöüß])" + re.escape(eintrag) + r"(?![\wÄÖÜäöüß])", re.I)
            for i, z in enumerate(zeilen, 1):
                for _ in muster.finditer(z):
                    funde.append((i, {"Floskeln": "Floskel", "Wendungen": "Wendung"}[kat], eintrag, z.strip()))
    for regex, erkl in merk["Muster"]:
        try:
            muster = re.compile(regex, re.I)
        except re.error as e:
            print(f"Muster unbrauchbar: {regex} ({e})", file=sys.stderr)
            continue
        for i, z in enumerate(zeilen, 1):
            if muster.search(z):
                funde.append((i, "Muster", erkl, z.strip()))

    # Vorsatz mit Doppelpunkt: kurze Zeile oder kurzer Satzanfang vor dem Doppelpunkt, keine Beschriftung einer Liste
    LISTE = re.compile(r"^\s*(?:[-•*–]|\d+[.)])\s")
    for i, z in enumerate(zeilen, 1):
        t = z.strip()
        m = re.match(r"^((?:\S+\s){0,3}\S+):(\s*$|\s+\S)", t)
        if not m or LISTE.match(t) or t.startswith("#"):
            continue
        folgende = next((zeilen[j] for j in range(i, len(zeilen)) if zeilen[j].strip()), "")
        if m.group(2).strip() == "" and (LISTE.match(folgende) or not folgende):
            continue  # Beschriftung vor einer Liste, kein Vorsatz
        if re.match(r"^(?:Stand|Quelle|Hinweis|Beispiel|Foto|Autor|Autorin|Kontakt|Datum|Titel|Tel|Telefon|E-Mail|Mail|Web|Adresse|Betreff|Thema|Name)\b", m.group(1)):
            continue
        funde.append((i, "Muster", "Vorsatz mit Doppelpunkt (streichbar?)", t))

    # Typografie
    for i, z in enumerate(zeilen, 1):
        if "'" in z:
            funde.append((i, "Typografie", "gerader Apostroph (')", z.strip()))
        if '"' in z:
            funde.append((i, "Typografie", 'gerade Anführungszeichen (")', z.strip()))
        if "”" in z or re.search(r"(^|[\s(])“\w", z):
            funde.append((i, "Typografie", "englische Anführungszeichen (“ ”)", z.strip()))
    striche = len(re.findall(r"(?<=\S)[ \t][–—][ \t]|—", text))
    striche_je_1000 = striche * 1000 / n_w
    if striche_je_1000 >= 5:
        for i, z in enumerate(zeilen, 1):
            if re.search(r"(?<=\S)[ \t][–—][ \t]|—", z):
                funde.append((i, "Typografie", "Gedankenstrich (gehäuft, siehe Kennzahlen)", z.strip()))
    for i, z in enumerate(zeilen, 1):
        if len(re.findall(r"(?<=\S)[ \t][–—][ \t]|—", z)) >= 2 and len(z.split()) < 45:
            funde.append((i, "Typografie", "zwei Gedankenstriche im selben Satz", z.strip()))

    # Absatzbau
    absaetze = [a.strip() for a in re.split(r"\n\s*\n", text) if a.strip()]
    ein_satz = [a for a in absaetze if len(saetze(a)) <= 1 and len(a.split()) <= 25 and not re.match(r"^(?:[-•*–]|\d+[.)]|#)", a)]
    anteil_einsatz = len(ein_satz) / len(absaetze) if absaetze else 0
    if len(absaetze) >= 5 and anteil_einsatz >= 0.6:
        funde.append((0, "Absatzbau", f"Einsatz-Absätze: {len(ein_satz)} von {len(absaetze)}", ""))
    if len(absaetze) >= 4 and len(absaetze[0].split()) <= 10 and absaetze[0].rstrip().endswith((".", "!", "?")) and not absaetze[0].startswith("#"):
        funde.append((1, "Absatzbau", "Hook-Zeile (kurze erste Zeile, dann Leerzeile)", absaetze[0]))
    letzter = absaetze[-1] if absaetze else ""
    if letzter.rstrip().endswith("?") and len(absaetze) >= 3:
        funde.append((len(zeilen), "Absatzbau", "Schlussfrage an die Leserschaft", letzter))

    # Rhythmus
    alle = saetze(text)
    laengen = [len(s.split()) for s in alle]
    for k in range(len(alle) - 2):
        if all(l <= 7 for l in laengen[k:k + 3]):
            funde.append((0, "Rhythmus", "Dreier-Stakkato (drei kurze Sätze)", " ".join(alle[k:k + 3])))
            break
    for k in range(len(alle) - 2):
        erste = [s.split()[0].lower().strip("„»(") for s in alle[k:k + 3]]
        if len(set(erste)) == 1 and erste[0] not in ("die", "der", "das", "es", "ich"):
            funde.append((0, "Rhythmus", f"Anapher („{alle[k].split()[0]} …“ dreimal)", " ".join(alle[k:k + 3])))
            break
    UEBERGANG = ("doch", "dabei", "gleichzeitig", "dennoch", "zugleich", "allerdings")
    starts = [s.split()[0].lower().strip("„»(") for s in alle]
    for k in range(len(starts) - 4):
        if sum(w in UEBERGANG for w in starts[k:k + 5]) >= 3:
            funde.append((0, "Rhythmus", "Übergangswörter in Serie (Doch, Dabei, Gleichzeitig …)", " ".join(alle[k:k + 5])))
            break
    cv = statistics.pstdev(laengen) / statistics.mean(laengen) if len(laengen) >= 8 else None
    if cv is not None and cv < 0.35:
        funde.append((0, "Rhythmus", f"gleichmäßige Satzlängen (Streuung/Mittel = {cv:.2f})", ""))

    # Ausgabe
    funde.sort(key=lambda f: (f[0] == 0, f[0], f[1]))
    print(f"Datei: {pfad}")
    print(f"Merkmalsliste: {'eingebaut' if merk is EINGEBAUT else args[args.index('--merkmale') + 1]}\n")
    if funde:
        print("Fundstellen")
        for zeile, kat, fund, kontext in funde:
            ort = f"Z. {zeile:>3}" if zeile else "Text "
            k = "" if kurz or not kontext else "  ·  " + (kontext[:90] + "…" if len(kontext) > 90 else kontext)
            print(f"  {ort} · {kat:<10} · {fund}{k}")
    else:
        print("Keine Fundstellen.")
    print("\nKennzahlen")
    print(f"  Wörter {n_w}, Sätze {len(alle)}, Absätze {len(absaetze)}")
    if laengen:
        print(f"  Satzlänge Ø {statistics.mean(laengen):.1f} Wörter, kürzester {min(laengen)}, längster {max(laengen)}"
              + (f", Streuung/Mittel {cv:.2f}" if cv is not None else ""))
    print(f"  Gedankenstriche {striche} ({striche_je_1000:.1f} je 1000 Wörter)")
    fre = flesch_amstad(woerter, len(alle))
    if fre is not None:
        stufe_fre = ("sehr schwer" if fre < 30 else "schwer" if fre < 50 else "mittel" if fre < 60 else
                     "leicht" if fre < 70 else "sehr leicht")
        print(f"  Flesch-Index (Amstad) {fre:.0f}, {stufe_fre}; misst Lesbarkeit, nicht Glätte, fließt nicht in die Dichte ein")
    print(f"  Einsatz-Absätze {len(ein_satz)} von {len(absaetze)}")
    gewichtet = sum(0.5 if f[1] == "Typografie" else 1 for f in funde)
    dichte = gewichtet * 100 / n_w
    stufe = "gering" if dichte < 2 else "mittel" if dichte < 6 else "hoch"
    print(f"\nVerdachtsdichte: {stufe} ({gewichtet:g} gewichtete Indizien je {n_w} Wörter = {dichte:.1f} je 100 Wörter)")
    if n_w < 150:
        print("Kurzer Text: Die Dichte schwankt stark, einzelne Funde zählen mehr als die Stufe.")
    print("Kein Urteil über die Herkunft. Jedes Merkmal kommt auch in menschlichen Texten vor; entscheide je Fundstelle, ob sie stehen bleibt.")


if __name__ == "__main__":
    main()
