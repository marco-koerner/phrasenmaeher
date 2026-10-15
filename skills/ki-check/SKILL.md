---
name: ki-check
description: Prüft, ob ein deutscher Text nach KI aussieht, und zeigt die Stellen, die den Verdacht auslösen (Floskeln, Wendungen, Gedankenstriche, Apostrophe, Vorsätze mit Doppelpunkt, Dreier-Stakkato, Hook-Zeile, Schlussfrage, gleichförmiger Rhythmus). Nutze diesen Skill, wenn jemand fragt, ob ein Text „nach KI klingt“, „KI-ig“ wirkt, nach Floskeln oder KI-Anmutung geprüft werden soll, egal ob eigener Text (vor dem Absenden) oder fremder Text (etwa ein LinkedIn-Post). Liefert Indizien mit Fundstelle und eine Einschätzung, kein Urteil über die Herkunft, und schreibt nichts um.
---

# KI-Check

Prüft die Oberfläche eines Textes auf Merkmale, die Leserinnen und Leser an KI denken lassen. Zwei Teile: ein Skript zählt, was sich zählen lässt; danach liest Claude, was sich nur lesend finden lässt. Ergebnis sind Fundstellen und eine Einschätzung. **Kein Urteil über die Herkunft, keine Umformulierung.** Jedes Merkmal kommt auch in menschlichen Texten vor, der Gedankenstrich ist korrekte Typografie; es zählt die Häufung, und ob eine Stelle stehen bleibt, entscheidet die Autorin oder der Autor.

## Merkmalsliste

Die Liste der Floskeln, Wendungen und Muster liegt als `merkmale.md` im Repo `marco-koerner/ki-check` und wird in Projekten als **Projektwissen über GitHub** eingebunden. Sie wächst mit jedem Fund; das Skript hat nur eine eingebaute Kurzfassung.

- Liegt `merkmale.md` im Projektwissen (oder wurde sie in den Chat gegeben): Inhalt unverändert als Datei `merkmale.md` ablegen und dem Skript mit `--merkmale` übergeben.
- Liegt sie nicht vor: Skript ohne `--merkmale` laufen lassen und in der Ausgabe sagen, dass nur die eingebaute Kurzliste galt.

## Ablauf

1. **Text als Datei ablegen** (.txt, .md oder .docx). Eingefügten Text unverändert speichern, Absätze erhalten; die Zeilennummern der Ausgabe beziehen sich auf diese Datei.
2. **Skript:** `python3 scripts/ki_check.py TEXT --merkmale merkmale.md` (`--kurz` ohne Zitatkontext). Es liefert Fundstellen mit Zeile und Kategorie, Kennzahlen (Satzlängen, Gedankenstriche je 1000 Wörter, Einsatz-Absätze) und eine Verdachtsdichte in drei Stufen.
3. **Lesen.** Was das Skript nicht sieht, der Abschnitt „Was nur das Lesen findet“ in `merkmale.md`: Behauptungen ohne Beleg oder Erlebnis, nichts Konkretes (Name, Zahl, Ort, Datum), jeder Absatz mit Pointe, Begriffe ohne Verwendung, keine Reibung, Übergänge, die immer aufgehen, austauschbare Aufzählungen, tragende Metaphern ohne Inhalt. Jede Beobachtung mit Zitat oder Zeile belegen; keine Beobachtung ohne Stelle.
4. **Ausgabe** in dieser Form:
   - **Fundstellen** als Liste: Zeile, Merkmal, kurzes Zitat. Skriptfunde und Lesefunde getrennt.
   - **Kennzahlen** aus dem Skript.
   - **Einschätzung** in einem Absatz: Wie stark ist der Gesamteindruck (gering, mittel, hoch), woran liegt es vor allem, und was davon ist bei diesem Text legitim. Bei einem eigenen Text zusätzlich: welche Stellen Verdacht auslösen, obwohl sie sachlich oder typografisch richtig sind, damit die Autorin oder der Autor bewusst entscheidet.
   - Bei Texten unter 150 Wörtern sagen, dass einzelne Funde mehr zählen als die Stufe.
5. **Nicht tun:** keinen Text umschreiben oder „entschärfen“, keine Formulierungsvorschläge, kein Satz wie „dieser Text wurde von KI geschrieben“. Wer eine Umformulierung will, bekommt sie in einem eigenen Schritt und auf ausdrückliche Bitte.

## Grenzen

- Ein Mensch kann jedes Merkmal treffen, eine KI kann jedes vermeiden. Die Prüfung zeigt Anmutung, nicht Herkunft.
- Formale Dokumente mit Überschriften, Listen und Angaben wie „Stand:“ erzeugen Treffer beim Vorsatz-Muster; das Skript filtert die häufigsten Fälle, nicht alle.
- Die Dichte-Stufen sind grob kalibriert (gering unter 2, mittel bis 6, hoch darüber, gewichtete Indizien je 100 Wörter) und werden mit der Nutzung nachjustiert.

## Neue Merkmale

Fällt beim Prüfen ein Merkmal auf, das in `merkmale.md` fehlt, am Ende als Vorschlag formulieren (Eintrag für den passenden Abschnitt, mit Datum und kurzem Beleg). Es kommt per Pull Request ins Repo; nach dem Merge reicht im Projekt „Jetzt synchronisieren“. Den Skill selbst muss Marco nur neu hochladen, wenn sich dieser Ablauf oder das Skript ändern.
