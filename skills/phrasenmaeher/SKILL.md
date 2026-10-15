---
name: phrasenmaeher
description: Prüft, ob ein deutscher Text glatt wirkt, nach KI oder nach Phrase, in drei Teilen. Ein Skript zählt Floskeln, Wendungen, Muster, Satzformen (Doppelpunkt-Aufzählung, Schlagwortsatz ohne Verb, Definitionssatz, Pointe am Absatzende) und Kennzahlen; ein Leser mit leerem Kontext stellt jedem Satz fünf Fragen (Aussage, Beleg, Nutzen für die Leserin, Neues, Austauschbarkeit); der Mäher schlägt eine Fassung vor, in der nur die markierten Stellen geändert sind. Nutze diesen Skill, wenn jemand fragt, ob ein Text „nach KI klingt“, „KI-ig“ oder „glatt“ wirkt, floskelhaft ist oder vor dem Absenden geprüft werden soll, bei eigenen wie fremden Texten (etwa LinkedIn-Posts). Das Ergebnis sagt nichts über die Herkunft.
---

# Phrasenmäher

Prüft einen Text auf das, was Leserinnen und Leser an KI oder an Phrasen denken lässt. Drei Teile, in dieser Reihenfolge:

- **Zähler**: ein Skript, deterministisch. Es findet Wörter, Wendungen, Muster und Satzformen. Es findet keine Aussagen.
- **Leser**: jemand, der den Text nicht geschrieben hat, mit leerem Kontext. Er bekommt nur den Text und die fünf Fragen in `leser.md` und urteilt je Satz. Er findet, was kein Skript findet: Behauptungen ohne Beleg, Sätze, die niemanden angehen, Wiederholungen, Austauschbares.
- **Mäher**: schlägt eine Fassung vor, in der ausschließlich die Stellen geändert sind, die Zähler oder Leser markiert haben.

Der Zähler allein reicht nicht. Das hat sich am 15.10.2026 am Text der Demonstrationsseite gezeigt: ohne eine einzige Fundstelle durch das Skript und trotzdem glatt, weil der Verfasser die Liste kannte und um sie herum schrieb. Wer den Satz geschrieben hat, hat auch die Rechtfertigung dafür im Kopf; deshalb liest ein anderer. Jedes Merkmal kommt auch in menschlichen Texten vor, der Gedankenstrich ist korrekte Typografie; ob eine Stelle stehen bleibt, entscheidet die Autorin oder der Autor. In der Redaktion ist die gemähte Fassung der Text, der zur Freigabe geht.

## Merkmalsliste

Die Liste der Floskeln, Wendungen und Muster liegt als `merkmale.md` im Repo `marco-koerner/phrasenmaeher` und wird in Projekten als **Projektwissen über GitHub** eingebunden. Sie wächst mit jedem Fund; das Skript hat nur eine eingebaute Kurzfassung, die Satzformen stecken im Skript selbst.

- Liegt `merkmale.md` im Projektwissen (oder wurde sie in den Chat gegeben): Inhalt unverändert als Datei `merkmale.md` ablegen und dem Skript mit `--merkmale` übergeben.
- Liegt sie nicht vor: Skript ohne `--merkmale` laufen lassen und in der Ausgabe sagen, dass nur die eingebaute Kurzliste galt.

## Ablauf

1. **Text als Datei ablegen** (.txt, .md oder .docx). Eingefügten Text unverändert speichern, Absätze erhalten; die Zeilennummern der Ausgabe beziehen sich auf diese Datei.
2. **Zähler:** `python3 scripts/phrasenmaeher.py TEXT --merkmale merkmale.md` (`--kurz` ohne Zitatkontext). Er liefert Fundstellen mit Zeile und Kategorie (Floskel, Wendung, Muster, Satzbau, Typografie, Absatzbau, Rhythmus), Kennzahlen (Satzlängen, Gedankenstriche je 1000 Wörter, Einsatz-Absätze, Flesch-Index) und eine Verdachtsdichte in drei Stufen.
3. **Leser.** Den Text mit dem Auftrag aus `leser.md` an jemanden geben, der ihn nicht geschrieben hat:
   - Steht ein Werkzeug für einen eigenen Agenten zur Verfügung (in Claude Code das Agent-Werkzeug, Typ general-purpose): einen Agenten starten, dessen Prompt nur aus dem Abschnitt unter dem Trennstrich in `leser.md` und dem Text besteht. Keine Merkmalsliste, keine Textproben, keine Vorgeschichte, kein Hinweis auf Verfasser oder Zweck. Das Ergebnis unverändert übernehmen.
   - Gibt es kein solches Werkzeug (etwa im Chat): die fünf Fragen selbst Satz für Satz schriftlich beantworten, bevor irgendetwas anderes geschieht, und in der Ausgabe sagen, dass der Leser im selben Kontext lief und deshalb milder urteilt als ein fremder.
   - Jede Beobachtung des Lesers trägt den zitierten Satz. Sätze mit „fällt durch“ gelten als markiert; Sätze mit „schwach“ werden in der Einschätzung genannt und bleiben Entscheidung der Autorin oder des Autors.
4. **Mähen.** Eine gemähte Fassung des ganzen Textes erstellen, nach diesen Regeln:
   - Nur markierte Stellen ändern (Zähler und Leser). Jeder nicht markierte Satz bleibt wortgleich, auch wenn er sich besser formulieren ließe.
   - Streichen vor Ersetzen. Eine Floskel fällt meist ersatzlos weg; ein Vorsatz mit Doppelpunkt wird gestrichen, die Pointe bleibt; eine Schlussfrage als Köder fällt weg; ein Satz, der laut Leser niemanden angeht oder einen Satz davor wiederholt, fällt weg. Ist Ersatz nötig, dann konkret statt allgemein (eine Zahl, ein Name, ein Beispiel aus dem Text selbst), nie eine andere Formel.
   - Eine Behauptung ohne Beleg bekommt keinen erfundenen Beleg. Entweder der Beleg steht im Material, dann wird er genannt, oder der Satz wird zur Frage an die Autorin oder den Autor.
   - Markierungen, die sachlich oder typografisch berechtigt sind (ein Gedankenstrich, der inhaltlich trägt, ein Zitat mit geraden Anführungszeichen in Code, eine Aufzählung, die wirklich eine Aufzählung ist), stehen lassen und in der Änderungsliste als „bewusst belassen“ führen.
   - Die gemähte Fassung erneut durch den Zähler laufen lassen. Bleiben neue Funde, einmal nachbessern; danach aufhören, damit nicht eine Formel die nächste ersetzt. Der Leser läuft nicht ein zweites Mal; was er gefunden hat, ist entweder behoben oder als offene Frage ausgewiesen.
   - Stimme und Inhalt sind nicht Gegenstand des Mähens. Fehlt dem Text nach dem Mähen ein Gedanke, das in der Einschätzung sagen, nicht einen erfinden.
5. **Ausgabe** in dieser Form:
   - **Fundstellen** als Liste: Zeile, Merkmal, kurzes Zitat. Zählerfunde und Leserfunde getrennt; beim Leser je Satz das Urteil und die Frage, die durchfiel.
   - **Kennzahlen** aus dem Zähler, vor und nach dem Mähen (Wörter, Gedankenstriche je 1000 Wörter, Verdachtsdichte).
   - **Einschätzung** in einem Absatz: Wie stark ist der Gesamteindruck (gering, mittel, hoch), woran liegt es vor allem, und was davon ist bei diesem Text legitim. Die drei belastendsten Sätze des Lesers und seine offenen Fragen gehören hierher. Bei einem eigenen Text zusätzlich: welche Stellen Verdacht auslösen, obwohl sie sachlich oder typografisch richtig sind, damit die Autorin oder der Autor bewusst entscheidet.
   - **Gemähte Fassung** als Ganzes, danach die **Änderungsliste**: je Fundstelle vorher → nachher, „bewusst belassen“ mit Grund oder „offene Frage“ mit dem, was fehlt.
   - Bei Texten unter 150 Wörtern sagen, dass einzelne Funde mehr zählen als die Stufe.
6. **Nicht tun:** keine Änderungen außerhalb der Markierungen, keine Verbesserung von Stimme oder Argument, keine erfundenen Belege, kein Satz wie „dieser Text wurde von KI geschrieben“. Wer nur die Markierungen will, sagt es; dann entfällt Schritt 4. Bei fremden Texten (etwa ein LinkedIn-Post, den jemand prüfen lässt) entfällt das Mähen ebenfalls, es sei denn, es wird ausdrücklich gewünscht; der Leser läuft trotzdem.

## Grenzen

- Ein Mensch kann jedes Merkmal treffen, eine KI kann jedes vermeiden. Die Prüfung zeigt Anmutung, nicht Herkunft.
- Wer die Merkmalsliste kennt, schreibt um sie herum. Der Zähler misst dann nichts mehr; der Leser ist in diesem Fall die eigentliche Prüfung.
- Der Leser im selben Kontext ist milder als ein fremder. Wo es auf die Prüfung ankommt (Redaktion, Veröffentlichung), läuft er als eigener Agent.
- Formale Dokumente mit Überschriften, Listen und Angaben wie „Stand:“ erzeugen Treffer beim Vorsatz-Muster und bei der Doppelpunkt-Aufzählung; das Skript filtert die häufigsten Fälle, nicht alle.
- Die gemähte Fassung ist eine sprachliche Bereinigung, kein neuer Text. Wo Regeln einer Auftraggeberin den KI-Einsatz einschränken, gilt sie als Korrektur und wird wie jede KI-Hilfe dokumentiert.
- Die Dichte-Stufen sind grob kalibriert (gering unter 2, mittel bis 6, hoch darüber, gewichtete Indizien je 100 Wörter) und werden mit der Nutzung nachjustiert. Stand 15.10.2026: ein erfundener LinkedIn-Post im KI-Stil 17,8 (hoch), ein Leitlinienpapier 0,5 (gering), Schreibproben eines Menschen 0,4 (gering), der erste Seitentext der Demonstration 3,5 (mittel, nur Satzformen).

## Neue Merkmale

Fällt beim Prüfen ein Merkmal auf, das in `merkmale.md` fehlt, am Ende als Vorschlag formulieren (Eintrag für den passenden Abschnitt, mit Datum und kurzem Beleg). Es kommt per Pull Request ins Repo; nach dem Merge reicht im Projekt „Jetzt synchronisieren“. Den Skill selbst muss Marco nur neu hochladen, wenn sich dieser Ablauf, `leser.md` oder das Skript ändern.
