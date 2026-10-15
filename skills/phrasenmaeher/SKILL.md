---
name: phrasenmaeher
description: Prüft, ob ein deutscher Text glatt wirkt, nach KI oder nach Phrase, und zeigt die Stellen, die den Eindruck auslösen (Floskeln, Wendungen, Schlussfragen als Köder, Gedankenstriche, Apostrophe, Vorsätze mit Doppelpunkt, Dreier-Stakkato, Hook-Zeile, gleichförmiger Rhythmus). Nutze diesen Skill, wenn jemand fragt, ob ein Text „nach KI klingt“, „KI-ig“ oder „glatt“ wirkt, floskelhaft ist oder vor dem Absenden geprüft werden soll, bei eigenen wie fremden Texten (etwa LinkedIn-Posts). Liefert Indizien mit Fundstelle, eine Einschätzung und eine gemähte Fassung, in der nur die markierten Stellen geändert sind; kein Urteil über die Herkunft.
---

# Phrasenmäher

Prüft die Oberfläche eines Textes auf Merkmale, die Leserinnen und Leser an KI denken lassen. Drei Teile: ein Skript zählt, was sich zählen lässt; danach liest Claude, was sich nur lesend finden lässt; zuletzt mäht Claude, also schlägt eine Fassung vor, in der ausschließlich die markierten Stellen geändert sind. Ergebnis sind Fundstellen, eine Einschätzung und die gemähte Fassung. **Kein Urteil über die Herkunft.** Übernommen wird die gemähte Fassung nur bewusst; in der Redaktion ist sie der Text, der zur Freigabe geht. Jedes Merkmal kommt auch in menschlichen Texten vor, der Gedankenstrich ist korrekte Typografie; es zählt die Häufung, und ob eine Stelle stehen bleibt, entscheidet die Autorin oder der Autor.

## Merkmalsliste

Die Liste der Floskeln, Wendungen und Muster liegt als `merkmale.md` im Repo `marco-koerner/phrasenmaeher` und wird in Projekten als **Projektwissen über GitHub** eingebunden. Sie wächst mit jedem Fund; das Skript hat nur eine eingebaute Kurzfassung.

- Liegt `merkmale.md` im Projektwissen (oder wurde sie in den Chat gegeben): Inhalt unverändert als Datei `merkmale.md` ablegen und dem Skript mit `--merkmale` übergeben.
- Liegt sie nicht vor: Skript ohne `--merkmale` laufen lassen und in der Ausgabe sagen, dass nur die eingebaute Kurzliste galt.

## Ablauf

1. **Text als Datei ablegen** (.txt, .md oder .docx). Eingefügten Text unverändert speichern, Absätze erhalten; die Zeilennummern der Ausgabe beziehen sich auf diese Datei.
2. **Skript:** `python3 scripts/phrasenmaeher.py TEXT --merkmale merkmale.md` (`--kurz` ohne Zitatkontext). Es liefert Fundstellen mit Zeile und Kategorie, Kennzahlen (Satzlängen, Gedankenstriche je 1000 Wörter, Einsatz-Absätze) und eine Verdachtsdichte in drei Stufen.
3. **Lesen.** Was das Skript nicht sieht, der Abschnitt „Was nur das Lesen findet“ in `merkmale.md`: Behauptungen ohne Beleg oder Erlebnis, nichts Konkretes (Name, Zahl, Ort, Datum), jeder Absatz mit Pointe, Begriffe ohne Verwendung, keine Reibung, Übergänge, die immer aufgehen, austauschbare Aufzählungen, tragende Metaphern ohne Inhalt. Jede Beobachtung mit Zitat oder Zeile belegen; keine Beobachtung ohne Stelle.
4. **Mähen.** Eine gemähte Fassung des ganzen Textes erstellen, nach diesen Regeln:
   - Nur markierte Stellen ändern. Jeder nicht markierte Satz bleibt wortgleich, auch wenn er sich besser formulieren ließe.
   - Streichen vor Ersetzen. Eine Floskel fällt meist ersatzlos weg; ein Vorsatz mit Doppelpunkt wird gestrichen, die Pointe bleibt; eine Schlussfrage als Köder fällt weg. Ist Ersatz nötig, dann konkret statt allgemein (eine Zahl, ein Name, ein Beispiel aus dem Text selbst), nie eine andere Formel.
   - Markierungen, die sachlich oder typografisch berechtigt sind (ein Gedankenstrich, der inhaltlich trägt, ein Zitat mit geraden Anführungszeichen in Code), stehen lassen und in der Änderungsliste als „bewusst belassen“ führen.
   - Die gemähte Fassung erneut durch das Skript laufen lassen. Bleiben neue Funde, einmal nachbessern; danach aufhören, damit nicht eine Formel die nächste ersetzt.
   - Stimme und Inhalt sind nicht Gegenstand des Mähens. Fehlt dem Text nach dem Mähen ein Gedanke, das in der Einschätzung sagen, nicht einen erfinden.
5. **Ausgabe** in dieser Form:
   - **Fundstellen** als Liste: Zeile, Merkmal, kurzes Zitat. Skriptfunde und Lesefunde getrennt.
   - **Kennzahlen** aus dem Skript, vor und nach dem Mähen (Wörter, Gedankenstriche je 1000 Wörter, Verdachtsdichte).
   - **Einschätzung** in einem Absatz: Wie stark ist der Gesamteindruck (gering, mittel, hoch), woran liegt es vor allem, und was davon ist bei diesem Text legitim. Bei einem eigenen Text zusätzlich: welche Stellen Verdacht auslösen, obwohl sie sachlich oder typografisch richtig sind, damit die Autorin oder der Autor bewusst entscheidet.
   - **Gemähte Fassung** als Ganzes, danach die **Änderungsliste**: je Fundstelle vorher → nachher oder „bewusst belassen“ mit Grund.
   - Bei Texten unter 150 Wörtern sagen, dass einzelne Funde mehr zählen als die Stufe.
6. **Nicht tun:** keine Änderungen außerhalb der Markierungen, keine Verbesserung von Stimme oder Argument, kein Satz wie „dieser Text wurde von KI geschrieben“. Wer nur die Markierungen will, sagt es; dann entfällt Schritt 4. Bei fremden Texten (etwa ein LinkedIn-Post, den jemand prüfen lässt) entfällt das Mähen ebenfalls, es sei denn, es wird ausdrücklich gewünscht.

## Grenzen

- Ein Mensch kann jedes Merkmal treffen, eine KI kann jedes vermeiden. Die Prüfung zeigt Anmutung, nicht Herkunft.
- Formale Dokumente mit Überschriften, Listen und Angaben wie „Stand:“ erzeugen Treffer beim Vorsatz-Muster; das Skript filtert die häufigsten Fälle, nicht alle.
- Die gemähte Fassung ist eine sprachliche Bereinigung, kein neuer Text. Wo Regeln einer Auftraggeberin den KI-Einsatz einschränken, gilt sie als Korrektur und wird wie jede KI-Hilfe dokumentiert.
- Die Dichte-Stufen sind grob kalibriert (gering unter 2, mittel bis 6, hoch darüber, gewichtete Indizien je 100 Wörter) und werden mit der Nutzung nachjustiert.

## Neue Merkmale

Fällt beim Prüfen ein Merkmal auf, das in `merkmale.md` fehlt, am Ende als Vorschlag formulieren (Eintrag für den passenden Abschnitt, mit Datum und kurzem Beleg). Es kommt per Pull Request ins Repo; nach dem Merge reicht im Projekt „Jetzt synchronisieren“. Den Skill selbst muss Marco nur neu hochladen, wenn sich dieser Ablauf oder das Skript ändern.
