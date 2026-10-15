# Phrasenmäher

Der Phrasenmäher prüft, ob ein deutscher Text glatt wirkt, nach KI oder nach Phrase, und zeigt die Stellen, die den Eindruck auslösen. Er arbeitet in drei Teilen. Der **Zähler** ist ein Skript und findet Wörter, Wendungen, Muster und Satzformen. Der **Leser** ist ein Sprachmodell mit leerem Kontext, das nur den Text und fünf Fragen bekommt und je Satz urteilt, ob er etwas sagt, ob es belegt ist und ob es jemanden angeht. Der **Mäher** schlägt eine Fassung vor, in der nur die markierten Stellen geändert sind; übernommen wird sie bewusst, nie automatisch. Das Ergebnis sagt nichts darüber, wer geschrieben hat; viele der Merkmale sind floskelhaftes Sprechen von Menschen.

Der Zähler allein genügt nicht. Am 15.10.2026 kam der Text der Demonstrationsseite ohne eine Fundstelle durch das Skript und war trotzdem glatt, weil der Verfasser die Liste kannte und um sie herum schrieb. Seither prüft das Skript auch Satzformen, und zu jeder Prüfung gehört ein Leser, der den Text nicht geschrieben hat.

Anlass: „Inside HKomm“, Folge 19 (14.05.2026), Jörg Heeren (Referent für Wissenschaftskommunikation, Universität Bielefeld) und Stefan Pede (Projekt- und Accountmanager, MANDARIN Medien) über Floskeln, den geraden Apostroph und die Frage, wer den Output der KI prüft.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `merkmale.md` | die wachsende Merkmalsliste: Floskeln, Wendungen, Muster, Kennzahlen, Satzformen, Lesemerkmale; wird in Claude-Projekten als Projektwissen eingebunden |
| `skills/phrasenmaeher/` | Quelle des Skills `phrasenmaeher` in claude.ai: Ablauf Zähler, Leser, Mäher (`SKILL.md`) und Zählskript (`scripts/phrasenmaeher.py`) |
| `skills/leser/` | Quelle des Skills `leser`: Kontextregel (`SKILL.md`) und der Auftrag mit den fünf Fragen (`auftrag.md`), einzige Quelle des Auftrags |

## Nutzen

- **Skills:** `skills/phrasenmaeher/` und `skills/leser/` je als ZIP hochladen (der Ordner ist die Wurzel des ZIPs); beide gelten in allen Chats und Projekten. Neu hochladen nur, wenn sich Ablauf, Skript oder Auftrag ändern.
- **Merkmalsliste:** in jedem Projekt, in dem geprüft werden soll, unter Wissen „+“ → GitHub → dieses Repo → `merkmale.md`. Nach jedem Merge dort „Jetzt synchronisieren“.
- **Skript allein:** `python3 skills/phrasenmaeher/scripts/phrasenmaeher.py TEXT.txt --merkmale merkmale.md`
- **Leser allein:** Skill `leser` in einem neuen Chat ohne Projekt mit dem Text aufrufen; das ist der leere Kontext. Ohne Skill: den Abschnitt unter dem Trennstrich in `skills/leser/auftrag.md` mit dem Text an ein Sprachmodell geben, das sonst nichts über den Text weiß.
- **Browser:** eine Fassung des Zählers läuft auf [marcokoerner.com/phrasenmaeher](https://marcokoerner.com/phrasenmaeher/); der Text verlässt den Browser nicht. Der Leser läuft dort nicht.

## Was hier nicht liegt

Hier liegen keine Schreibproben, keine Stimme und keine fremden Texte. Die Merkmalsliste beschreibt Formeln, nicht Personen. Die Stimme eines Textes prüft dieses Werkzeug nicht.
