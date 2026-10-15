---
name: leser
description: Liest einen deutschen Text als strenge Leserin, Satz für Satz, und urteilt je Satz („trägt“, „schwach“, „fällt durch“), ob er eine Aussage hat, ob die Behauptung belegt ist und ob er die Leserin etwas angeht, dazu ob er Neues sagt und ob er austauschbar ist. Nutze diesen Skill, wenn jemand einen Text streng gegenlesen, Satz für Satz prüfen oder vom „Leser“ lesen lassen will, fragen will, welche Sätze nicht tragen oder welche Behauptungen ohne Beleg sind, bei eigenen wie fremden Texten (Posts, Webseiten, Pressemitteilungen, Kapitel, Profile). Schreibt nichts um; wer eine gemähte Fassung will, nimmt den Skill phrasenmaeher.
---

# Leser

Der Leser ist ein Auftrag, kein Werkzeug mit Gedächtnis: Er bekommt einen Text und fünf Fragen je Satz und sonst nichts. Der Auftrag steht vollständig in `auftrag.md` (alles unter dem Trennstrich). Er findet, was kein Skript findet, etwa eine Behauptung ohne Beleg, einen Satz, der niemanden angeht, eine Wiederholung oder einen Satz, der in jedem Text stehen könnte.

Seine Stärke hängt am leeren Kontext. Wer einen Satz geschrieben hat, hat die Rechtfertigung dafür schon im Kopf und urteilt milder. Deshalb zuerst klären, woher der Text kommt.

## Woher kommt der Text

1. **Der Text kommt von außen** (eingefügt, hochgeladen, aus einem anderen Gespräch), und dieses Gespräch hat ihn weder geschrieben noch besprochen: Das ist der leere Kontext. Auftrag aus `auftrag.md` anwenden, Text anhängen, Ausgabe wie dort beschrieben. Projektwissen, Textproben und Vorwissen über die Verfasserin nicht heranziehen; der Leser kennt nur den Text.
2. **Der Text ist in diesem Gespräch entstanden** (Claude hat ihn geschrieben, überarbeitet oder lange besprochen):
   - Gibt es ein Werkzeug für einen eigenen Agenten (in Claude Code das Agent-Werkzeug, Typ general-purpose): einen Agenten starten, dessen Prompt nur aus dem Abschnitt unter dem Trennstrich in `auftrag.md` und dem Text besteht. Keine Merkmalsliste, keine Textproben, keine Vorgeschichte, kein Hinweis auf Verfasser oder Zweck. Das Ergebnis unverändert wiedergeben.
   - Gibt es kein solches Werkzeug (etwa im Chat): sagen, dass der Leser im selben Kontext milder urteilt, und die Alternative nennen: den Text in einem neuen Chat ohne Projekt mit diesem Skill lesen lassen. Auf Wunsch trotzdem den Auftrag hier abarbeiten, Satz für Satz schriftlich, bevor irgendetwas anderes geschieht, und die Ausgabe mit „Leser im selben Kontext“ kennzeichnen.

## Ausgabe

Wie in `auftrag.md`: nummerierte Liste in Satzreihenfolge, jeder Satz zitiert, Urteil und Begründung; dann die drei belastendsten Sätze; dann, was der Text nicht sagt, obwohl die Leserin es bräuchte. Keine Zusammenfassung davor, kein Lob, keine Vorschläge zur Umformulierung.

Bei Listen, Überschriften und Beschriftungen (etwa „Stand: …“) das Urteil nicht erzwingen: Ein Listenpunkt ist kein Satz, das sagt der Leser und geht weiter.

## Was der Leser nicht tut

- Er schreibt nichts um und schlägt keine Formulierung vor. Streichen und Ersetzen ist Sache des Mähers im Skill `phrasenmaeher`, und das entscheidet die Autorin oder der Autor.
- Er zählt keine Floskeln und urteilt nicht über Ton, Rhythmus oder Wortwahl; dafür ist der Zähler im Skill `phrasenmaeher` da.
- Er urteilt nicht über die Herkunft des Textes (Mensch oder Modell).
- Er läuft je Text einmal. Nach der Überarbeitung nicht erneut lesen lassen, sonst ersetzt eine Rechtfertigung die nächste; was er gefunden hat, ist behoben oder als offene Frage ausgewiesen.

## Grenzen

- Der Leser ist hart gebaut. Er lässt auch Sätze durchfallen, die aus gutem Grund stehen (eine Anleitung, ein Zitat, eine bewusste Allgemeinheit). Sein Urteil ist ein Befund, keine Anweisung; wer den Text verantwortet, entscheidet je Satz und schreibt auf, was nicht übernommen wurde und warum.
- Wo Regeln einer Auftraggeberin den KI-Einsatz einschränken, ist der Leser eine Beurteilung, kein Textentwurf, und wird wie jede KI-Hilfe dokumentiert.
- Der Auftrag liegt im Repo `marco-koerner/phrasenmaeher` unter `skills/leser/auftrag.md`. Ändert er sich, lädt Marco diesen Skill neu hoch.
