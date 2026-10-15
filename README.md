# KI-Check

Privat. Prüft, ob ein deutscher Text nach KI aussieht, und zeigt, welche Stellen den Verdacht auslösen. Kein Urteil über die Herkunft, keine Umformulierung.

Anlass: „Inside HKomm“, Folge 19 (14.05.2026), Jörg Heeren (Universität Bielefeld) und Stefan Pede (MANDARIN Medien) über Floskeln, den geraden Apostroph und die Frage, wer den Output der KI prüft.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `merkmale.md` | die wachsende Merkmalsliste: Floskeln, Wendungen, Muster, Kennzahlen, Lesemerkmale; wird in Claude-Projekten als Projektwissen eingebunden |
| `skills/ki-check/` | Quelle des Skills in claude.ai: Ablauf (`SKILL.md`) und Zählskript (`scripts/ki_check.py`) |

## Nutzen

- **Skill:** Ordner `skills/ki-check/` als ZIP hochladen (der Ordner ist die Wurzel des ZIPs). Neu hochladen nur, wenn sich Ablauf oder Skript ändern.
- **Merkmalsliste:** in jedem Projekt, in dem geprüft werden soll, unter Wissen „+“ → GitHub → dieses Repo → `merkmale.md`. Nach jedem Merge dort „Jetzt synchronisieren“.
- **Skript allein:** `python3 skills/ki-check/scripts/ki_check.py TEXT.txt --merkmale merkmale.md`

## Identitäten

Die Merkmalsliste ist identitätsneutral: keine Schreibproben, keine Stimme, nichts, was auf eine bestimmte Person oder ein Pseudonym zurückführt. Deshalb kann dieselbe Datei in jedem Projekt hängen. Die Stimme eines Textes prüft dieser Skill nicht.
