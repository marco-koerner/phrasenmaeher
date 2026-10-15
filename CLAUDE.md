# Arbeitsregeln für Claude in diesem Repo

Werkzeug zur Prüfung, ob Texte glatt wirken (KI-Anmutung, Phrasensprache). Lies zuerst `README.md`.

- Änderungen auf eigenem Branch als Pull Request; Marcos Merge ist die Übernahme.
- `merkmale.md` ist die Quelle der Merkmale und wird in Projekten über GitHub eingebunden. Neue Merkmale dort eintragen, mit Datum und kurzem Beleg (ein Zitat von wenigen Wörtern reicht). Format einhalten, weil das Skript die Abschnitte „Floskeln“, „Wendungen“ und „Muster“ liest.
- Zwei Skills: `skills/phrasenmaeher/` enthält nur Ablauf und Skript, `skills/leser/` nur Kontextregel und den Auftrag an den Leser (`auftrag.md`, einzige Quelle des Auftrags; nirgends kopieren, nur verweisen). Regeln und Wortlisten gehören in keinen der beiden.
- Nach einer Änderung am Skript die drei Prüffälle gedanklich durchgehen: ein KI-typischer LinkedIn-Post muss „hoch“ ergeben, ein formales Dokument und ein sachlicher Fließtext „gering“.
- Keine fremden Texte im Repo ablegen (Urheberrecht), keine Schreibproben, keine Bezüge zu Identitäten, Pseudonymen oder Projekten; das Repo ist öffentlich und bleibt frei von allem, was auf Personen, Pseudonyme oder laufende Projekte zurückführt.
- Deutsch. Deutsche Anführungszeichen „ “, nie gerade Anführungszeichen im Fließtext (im Skript sind sie Code).
