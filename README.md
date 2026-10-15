# Phrasenmäher

Der Phrasenmäher markiert zuerst und zeigt jede Fundstelle, dann schlägt er eine gemähte Fassung vor, in der nur die markierten Stellen geändert sind. Übernommen wird sie bewusst, nie automatisch; in der Redaktion ist sie der Text, der zur Freigabe geht. Prüft, ob ein deutscher Text glatt wirkt, nach KI oder nach Phrase, und zeigt, welche Stellen den Eindruck auslösen. Kein Urteil über die Herkunft. Viele der Merkmale sind floskelhaftes Sprechen von Menschen; der Check findet sie unabhängig davon, wer geschrieben hat.

Anlass: „Inside HKomm“, Folge 19 (14.05.2026), Jörg Heeren (Universität Bielefeld) und Stefan Pede (MANDARIN Medien) über Floskeln, den geraden Apostroph und die Frage, wer den Output der KI prüft.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `merkmale.md` | die wachsende Merkmalsliste: Floskeln, Wendungen, Muster, Kennzahlen, Lesemerkmale; wird in Claude-Projekten als Projektwissen eingebunden |
| `skills/phrasenmaeher/` | Quelle des Skills in claude.ai: Ablauf (`SKILL.md`) und Zählskript (`scripts/phrasenmaeher.py`) |

## Nutzen

- **Skill:** Ordner `skills/phrasenmaeher/` als ZIP hochladen (der Ordner ist die Wurzel des ZIPs). Neu hochladen nur, wenn sich Ablauf oder Skript ändern.
- **Merkmalsliste:** in jedem Projekt, in dem geprüft werden soll, unter Wissen „+“ → GitHub → dieses Repo → `merkmale.md`. Nach jedem Merge dort „Jetzt synchronisieren“.
- **Skript allein:** `python3 skills/phrasenmaeher/scripts/phrasenmaeher.py TEXT.txt --merkmale merkmale.md`

## Was hier nicht liegt

Keine Schreibproben, keine Stimme, keine fremden Texte. Die Merkmalsliste beschreibt Formeln, nicht Personen. Die Stimme eines Textes prüft dieses Werkzeug nicht.
