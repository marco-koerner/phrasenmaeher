# Merkmale, die einen Text glatt wirken lassen

Stand: 15.10.2026, erste Fassung. Grundlage: eigene Beobachtung, „Inside HKomm“ Folge 19 (Jörg Heeren, Universität Bielefeld, zu Floskeln wie „innovativ“ und „bahnbrechend“ und zum geraden Apostroph), die Leitplanken aus Marcos Redaktion (keine Hook-Zeilen, keine Dreierlisten mit Pointe, keine Vorsätze mit Doppelpunkt).

Glätte ist der Eindruck, dass ein Text aus Formeln besteht statt aus Gedanken. Viele Leserinnen und Leser halten ihn dann für KI-geschrieben; genauso gut ist es PR-Sprech, Beratersprache oder LinkedIn-Routine von Menschen. Die Liste unterscheidet das nicht, sie findet die Formeln. Kein Merkmal beweist etwas, der Gedankenstrich ist korrekte deutsche Typografie. Es zählt die Häufung. Diese Datei beschreibt, was den **Verdacht** auslöst, damit man es findet und bewusst entscheidet, ob es stehen bleibt.

Das Skript `phrasenmaeher.py` liest diese Datei: Einträge unter „Floskeln“ und „Wendungen“ sucht es wörtlich (Groß- und Kleinschreibung egal, nur ganze Wörter), Einträge unter „Muster“ als regulären Ausdruck in Backticks. Alles nach „ – “ hinter einem Eintrag ist Erläuterung und wird nicht gesucht.

## Floskeln

Wörter, die KI-Texte und Phrasendrescherei überdurchschnittlich oft verwenden. Einzeln harmlos, gehäuft verdächtig.

- innovativ
- bahnbrechend
- wegweisend
- revolutionär
- revolutionieren
- nahtlos
- ganzheitlich
- entscheidend
- essenziell
- spannend
- faszinierend
- beeindruckend
- robust
- dynamisch
- vielfältig
- effizient
- optimieren
- Synergien
- Mehrwert
- Game-Changer
- Gamechanger
- Meilenstein
- Reise – im Sinne von „Lernreise“, „auf dieser Reise“
- Landschaft – im Sinne von „Medienlandschaft“, „Bildungslandschaft“
- entfesseln
- freischalten
- Potenzial entfalten
- auf das nächste Level
- tief eintauchen
- eintauchen
- beleuchten
- navigieren – im Sinne von „durch Herausforderungen navigieren“
- Herausforderungen meistern
- Schlüssel – „der Schlüssel zum Erfolg“
- letztendlich
- letztlich
- zweifellos
- unbestreitbar
- bemerkenswert

## Wendungen

Feste Formeln, die Struktur vortäuschen oder den Leser an die Hand nehmen.

- in einer Welt, in der
- in der heutigen
- in Zeiten von
- es ist wichtig zu beachten
- es ist wichtig, zu beachten
- es ist erwähnenswert
- es lohnt sich
- lassen Sie uns
- lasst uns
- tauchen wir ein
- werfen wir einen Blick
- zusammenfassend lässt sich sagen
- abschließend lässt sich
- kurz gesagt
- mit anderen Worten
- nicht nur, sondern auch
- es geht nicht darum
- es geht nicht um
- ich freue mich, mitteilen zu können
- ich bin begeistert
- ich bin stolz
- was denkt ihr
- was meint ihr – Schlussfrage als Köder, 15.10.2026, fiel in Redaktionsentwürfen auf
- wie seht ihr das
- wie handhabt ihr das
- wie sind eure Erfahrungen
- eure Erfahrungen
- lasst es mich wissen
- teilt es gern
- gerne teilen
- Spoiler:
- Fazit:
- Mein Learning:
- Die Wahrheit ist:
- Das Ergebnis?
- Das Problem?
- Der Grund?

## Muster

Reguläre Ausdrücke in Backticks, dahinter die Erläuterung. Flags: Groß- und Kleinschreibung egal, zeilenweise.

- `\bnicht (?:nur )?\w+(?:\s\w+){0,3}, sondern\b` – Kontrast „nicht X, sondern Y“
- `\bweniger \w+, mehr \w+` – Kontrastpaar „weniger X, mehr Y“
- `\?\s+(?:\S+\s){0,4}\S+[.!]` – rhetorische Frage mit Kurzantwort („Das Ergebnis? Mehr Reichweite.“)
- `^\s*[\U0001F300-\U0001FAFF☀-➿✅✔➡]` – Emoji als Aufzählungszeichen am Zeilenanfang
- `(?:#\w+\s*){3,}$` – Hashtag-Block am Ende
- `\bwir alle\b` – Vereinnahmung („wir alle kennen das“)

## Was das Skript zählt, ohne Liste

Diese Merkmale stecken im Skript selbst, weil sie Rechnen statt Wortsuche brauchen:

- gerade Apostrophe (') und gerade Anführungszeichen (") statt typografischer; englische Anführungszeichen (“ ”) in deutschem Text
- Gedankenstriche: Anzahl je 1000 Wörter; verdächtig ab etwa 5 je 1000 Wörter oder zwei im selben Satz
- Vorsatz mit Doppelpunkt („Die Wahrheit ist: …“, „Mein Fazit: …“), den man streichen könnte; Beschriftungen vor Listen und Angaben wie „Stand:“ zählen nicht
- Übergangswörter in Serie (Doch, Dabei, Gleichzeitig, Dennoch …): einzeln normal, drei in fünf Sätzen verdächtig
- Einsatz-Absätze: Anteil der Absätze, die nur aus einem Satz bestehen (LinkedIn-Muster)
- Hook-Zeile: sehr kurze erste Zeile, dann Leerzeile
- Dreier-Stakkato: drei sehr kurze Sätze nacheinander
- Anapher: drei Sätze nacheinander mit demselben ersten Wort
- gleichmäßiger Rhythmus: Satzlängen streuen kaum (Streuung geteilt durch Mittelwert unter 0,35)
- Schlussfrage: letzter Absatz endet mit einer Frage an die Leserschaft

## Was nur das Lesen findet

Das Skript zählt Oberfläche. Beim Lesen zusätzlich prüfen:

- Behauptungen ohne Beleg, Beispiel oder Erlebnis; nichts Konkretes (kein Name, keine Zahl, kein Ort, kein Datum)
- jeder Absatz endet auf eine Pointe; jeder Absatz gleich lang
- Begriffe, die eingeführt werden, ohne gebraucht zu werden
- keine Reibung: nichts, dem jemand widersprechen würde, keine Position mit Risiko
- Übergänge, die immer aufgehen („Doch … Dabei … Gleichzeitig …“)
- Aufzählungen, deren Punkte austauschbar sind
- Metaphern, die nichts tragen („Werkzeugkasten“, „Brücke bauen“)

## Pflege

Neue Merkmale hier eintragen, mit Datum in der Erläuterung, wenn sie aus einem konkreten Fund stammen. Keine fremden Texte im Repo ablegen; ein kurzes Zitat als Beleg reicht.
