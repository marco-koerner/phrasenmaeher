# Merkmale, die einen Text glatt wirken lassen

Stand: 15.10.2026, erste Fassung. Grundlage: eigene Beobachtung, „Inside HKomm“ Folge 19 vom 14.05.2026 (Jörg Heeren, Referent für Wissenschaftskommunikation an der Universität Bielefeld, zu Floskeln wie „innovativ“ und „bahnbrechend“ und zum geraden Apostroph), die Leitplanken aus Marcos Redaktion (keine Hook-Zeilen, keine Dreierlisten mit Pointe, keine Vorsätze mit Doppelpunkt).

Diese Datei sammelt Wörter, Wendungen und Formen, die Leserinnen und Leser nach meiner Beobachtung an KI-Text oder an Phrasendrescherei denken lassen; einige davon nennt Heeren in der Podcastfolge. Ob ein Mensch oder ein Modell geschrieben hat, unterscheidet die Liste nicht, und kein Merkmal beweist etwas, der Gedankenstrich ist korrekte deutsche Typografie. Die Liste zeigt, was den **Verdacht** auslöst, damit man die Stelle findet und bewusst entscheidet, ob sie stehen bleibt.

Die Liste hat eine Grenze, die sich am 15.10.2026 am Text der Demonstrationsseite gezeigt hat: Der Text kam ohne eine einzige Fundstelle durch das Skript und war trotzdem glatt (eine Definition ohne Quelle, eine Aufzählung statt eines Satzes, ein Selbstbezug ohne Nutzen für die Leserin). Wer die Liste kennt, schreibt um sie herum; das gilt für ein Sprachmodell wie für einen Menschen. Deshalb prüft das Skript seither auch Satzformen (Abschnitt „Was das Skript zählt, ohne Liste“), und deshalb gehört zu jeder Prüfung ein Leser, der den Text nicht geschrieben hat (`leser.md` im Skill).

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
- Flesch-Index nach Amstad (180 − mittlere Satzlänge − 58,5 × mittlere Silbenzahl je Wort): misst Lesbarkeit, nicht Glätte, und fließt nicht in die Dichte ein. Ein Text kann leicht lesbar sein und trotzdem nichts sagen; der Index allein entscheidet nichts

Satzformen (Kategorie „Satzbau“, seit 15.10.2026, Anlass: der Seitentext, der ohne Fund durchkam):

- Doppelpunkt-Aufzählung: kurzer Satzanfang, Doppelpunkt, dann drei oder mehr kurze Glieder („Markiert, was einen Text glatt wirken lässt: Floskeln, Wendungen, Muster, Rhythmus.“); eine Reihung ersetzt den Satz
- Dreierreihe mit gleichem Auftakt: drei Glieder in einem Satz beginnen mit demselben Wort („Keine Cookies, keine Auswertung, keine Verbindung zu Dritten.“)
- Schlagwortsatz ohne Verb: zwei bis sechs Wörter, Auftakt „Kein“, „Nur“, „Ohne“, „Mehr“, „Nichts“ oder ähnlich, kein finites Verb („Kein Urteil über die Herkunft.“)
- Definitionssatz: ein Begriff ohne Artikel am Satzanfang, dann „ist der“, „sind oft“ und ähnlich („Glätte ist der Eindruck, dass …“, „KI-Texte sind oft sehr lesbar …“); die Form eines Lexikonsatzes, die Behauptung bleibt ohne Beleg
- Pointe am Absatzende: ein Absatz mit mindestens einem Satz ab zwölf Wörtern endet auf einen Satz mit höchstens sechs Wörtern („Er findet die Formeln.“)

## Was nur das Lesen findet

Das Skript zählt Oberfläche und Satzformen. Es findet keine Aussagen, also nicht, ob ein Satz etwas behauptet, das niemand belegt, oder etwas sagt, das niemanden interessiert. Das findet nur, wer liest, und am besten jemand, der den Text nicht geschrieben hat: Wer den Satz geschrieben hat, hat auch die Rechtfertigung dafür im Kopf. Deshalb stellt der Leser (`leser.md` im Skill) jedem Satz fünf Fragen:

1. Ist das ein Satz mit einer Aussage, oder eine Reihung, ein Fragment, ein Schlagwort?
2. Woher stammt die Behauptung? Beleg, Beispiel, Erlebnis, Quelle im Text, oder nirgends nachlesbar?
3. Wen interessiert das? Was weiß die Leserin nach dem Satz, was sie vorher nicht wusste, und braucht sie es?
4. Sagt der Satz etwas Neues, oder wiederholt er einen Satz davor?
5. Könnte der Satz in jedem beliebigen Text zu einem anderen Thema stehen?

Beim Lesen außerdem prüfen:

- nichts Konkretes (kein Name, keine Zahl, kein Ort, kein Datum)
- jeder Absatz endet auf eine Pointe; jeder Absatz gleich lang
- Begriffe, die eingeführt werden, ohne gebraucht zu werden
- Selbstbezug, der der Leserin nichts bringt („Gebaut habe ich das für …“)
- keine Reibung: nichts, dem jemand widersprechen würde, keine Position mit Risiko
- Übergänge, die immer aufgehen („Doch … Dabei … Gleichzeitig …“)
- Aufzählungen, deren Punkte austauschbar sind
- Metaphern, die nichts tragen („Werkzeugkasten“, „Brücke bauen“)

## Pflege

Neue Merkmale hier eintragen, mit Datum in der Erläuterung, wenn sie aus einem konkreten Fund stammen. Keine fremden Texte im Repo ablegen; ein kurzes Zitat als Beleg reicht.
