# IBSYS I

## 1 ERP - Enterprise Resource Planning

### 1.1 ARIS

#### Welche ARIS-Schichten gibt es? [Cloze]

1. Mengenorientierte Prozesse
2. Wertorientierte Prozesse
3. MIS (Management Information Service) für z.B. Bilanz
4. Analysesysteme (KI, Data Science)
5. Langfristige Planungssysteme (Sukzessive Planung)

#### Was besagt die horizontale Integration?

Beschreibt z.B. komplexen Beschaffungsprozess von Bestellung bis zur Zahlung

#### Was ist die vertikale Integration?

Austausch von Daten zwischen den Ebenen des ARIS, um auf gemeinsames Ziel hinzuarbeiten

#### Welche Sichten haben wir auf Prozesse? [Cloze]

- Funktionssicht (Aufgaben)
- Steuerungssicht (Reihenfolge der Aufgaben)
- Organisationsicht (Aufgabenverteilung)
- Datensicht
- Leistungssicht

### 1.2 Kundenauftragsprozess

#### Welche Prozesse in E1 gibt es beim Kundenauftragsprozess? [Cloze]

- Kundenauftrag (KA)
- Warenlieferung (WL) -> Lieferschein
- Faktura (FA) -> Rechnung
- Zahlung (Z) -> KAZ

#### Wie sieht die Buchungskette beim Kundenauftragsprozess aus?

- BA (Bestandsänderung) -> Bestand
- UE (Umsatzerlöse) -> Ford.
- Ford. -> BBK
- BBK -> Bank

### 1.2 Beschaffungssprozess

#### Welche Prozesse in E1 gibt es beim Beschaffungsprozess? [Cloze]

- Bestellung (B)
- Wareneingang (WE) -> Beschaffungsvolumen Werte
- Rechnungseingang (RE)
- Zahlung (Z)

#### Wie sieht die Buchungskette beim Beschaffungsprozess aus?

Bestand -> WeRe -> Verb. -> BBK -> Bank

### 1.2 Bankbearbeitungskonto

#### Wozu brauchen wir ein Bankbearbeitungskonto?

Überweisungen können oft nicht direkt zugeordnet werden, deshalb werden diese "gelagert" und schließlich über das BBK (durch Buchhaltung oder KI) an Bank gebucht

#### Welche zwei Möglichkeiten gibt es, wenn das BBK eine unzureichende Überweisung findet?

- Offen lassen, Brief/Mahnung schicken
- Als Aufwand buchen (falls z.B. Stammkunde)

#### Was muss für das BBK am Stichtag gelten?

Muss "0"-Saldo haben

#### Was passiert bei einer Belastung der Bank ohne zugehörige Verb. am Stichtag?

Soll-Saldo: Wir erhalten eine Vorabrechnung, läuft über ARAG Konto

#### Was passiert, wenn am Stichtag eine Rechnung gebucht, aber noch nicht bezahlt wurde?

Haben-Saldo: Die Lieferung erfolgt erst in Folgeperiode, läuft über PRAP Konto (wenn Rechnungsbetrag unbekannt über Rückstellung)

#### Wie wird eine Währungsdifferenz gehandhabt?

WeRe-Konto wird über Kursdifferenz-Konto ausgeglichen

### 1.3 Modellbildung

#### Wie wird ein Modell modelliert?

Aus realem System/Prozess wird formales Modell "modelliert", dabei: Abgrenzung, Reduktion, Aggregation, Vereinigung, Dekomposition

#### Was wird im formalen Modell geprüft?

- Validierung (Verifikation, Falsifikation)
- Review/Audit (intern), Evaluation (extern), Akkreditierung (intern/extern)
- Simulation

## 2 Prozesssimulation

### 2.1 Petri-Netze

#### Wozu dienen Petri-Netze?

Petri-Netze dienen der dynamischen Simulation von Netzwerken

#### Welche Sichten werden in Petri-Netzen berücksichtigt?

- Markierung (Position des Auftrags)
- Pfeile (Logische Zusammenhänge)
- Transition (aktive Komponente)
- Stelle (passive Komponente)

### 2.2 Bayes-Netze

#### Formel für bedingte Wahrscheinlichkeit?

P(A|B) = P(A ∩ B) / P(B)

#### Welche Inferenztechniken gibt es? [Cloze]

- Deduktion: Theorie -> Empirie (Simulation)
- Induktion: Empirie -> Theorie (Data Mining)
- Abduktion: Gesetz + Wirkung -> Ursache

### 2.3 Markow-Ketten

#### Welche Erkenntnis gewinnen wir aus Markow-Ketten?

Kapazitätsbedarf je Schritt der Kette

#### Wann werden Markow-Ketten insbesondere benutzt?

Bei zyklischen Prozessen (also Schleifen), können aber auch für azyklische Prozesse verwendet werden

#### Welche Annahmen treffen wir bei Markow-Ketten? [Cloze]

- Markow-Ketten 1. Ordnung mit Markow-Demenz (=ohne Gedächtnis)
- Wahrscheinlichkeiten und Zeiten sind stationär (zeitdiskret)

#### Was ist die Markow-Bedingung?

Nächster Schritt ist nicht abhängig von vorherigen Schritten

#### Wie kann man Leerzeiten vermeiden?

- Ressourcen oder Kapazitäten erhöhen
- Splitting
- Überlappende Fertigung mit Losgrößen

#### Wann ist eine Markow-Kette homogen?

Zeitdiskret (=Zeitschritte sind konstant und stationär)

## 3 Anwendungsorientierte Aspekte der vertikalen und horizontalen Integration

### 3.2 Systemübergreifende Prozesse

#### Wofür braucht man Transferkonten?

Mit Transferkonten können systemübergreifende Belegprozesse zw. E2 und E3 realisiert werden, ohne in Bilanz berücksichtigt zu werden

#### In welchem System muss das WeRe Konto beim BP sein, um Rückwärtsverweise zu vermeiden?

Im ERP-System (meist System 2), so werden rückverweisende Schnittstellen vermieden

#### Operative vs. periodische Schnittstellen?

Operative Schnittstellen laufen ständig, periodische SST bspw. nur bei Konsolidierungen

#### Was ist Netting?

Verrechnung gegenläufiger Zahlungsansprüche, z.B. bei Forderungen und Verbindlichkeiten

#### Nenne die Schritte der Konsolidierung

1. Salden der operativen Systeme ausgleichen
2. Konsolidieren (TK -> TK-operativ und TK-kon -> TK-kon)
3. Rest-Positionen in TK-kon an Konten aus operativen Systemen buchen

### 3.3 Internal Accounts

#### Was ist die Besonderheit von Prozesskonten?

Prozesskonten sind Bearbeitungskonten (wie WeRe, BBK) oder Transferkonten und tauchen nicht in der Bilanz auf, deshalb müssen ihre Salden am Stichtag "0" sein

#### Was ist Cash-Concentration?

Übertragen von Geldern von verschiedenen Konten an zentrales Konto, um Effizienz des Cash-Managements zu erhöhen

### 3.4 MIS-Paradigmen

#### Welche Art von Datenbanken gibt es bei E1, E2 und E3? [Cloze]

- E1, E2: OLTP (Online transaction processing)
- E3: OLAP (Onlinen analytical processing)

#### Was enthält das MIS?

- Bilanz und G+V
- Kennzahlensysteme (z.B. Kosten-/Leistungsrechnung)

#### Welche Verfügbarkeiten von Informationen gibt es?

- Periodisch/nach Bedarf
- Standardisiert/flexibel
- Erstellung automatisch/manuell
- persistente Daten/"gehen verloren"

#### Nenne die 3 MIS-Paradigmen [Cloze]

- Programme/Routine: Bei OLTP, für Berichterstellung (nicht persistent)
- Berichtsdatenbanken: OLAP, für Speichern von Berichtsdaten
- In-Memory Computing

#### Charakterisiere das MIS-Paradigma "Programm/Routine"

- Aktuell
- Hoher Kapazitätsbedarf
- Weniger performant

#### Charakterisiere das MIS-Paradigma "Berichtsdatenbank"

- Performant
- Aktualität abhängig von ETL-Prozess (OLTP)

#### Charakterisiere das MIS-Paradigma "In-Memory Computing"

- Hochperformant
- Aktuell

#### Was ist die Mitbuchkontentechnik?

Datenobjekt im MIS, dass Buchungen im E2 "mitschreibt"

## 4 Referenzmodell der Integration auf der Abrechnungsebene

### 4.1 Kreissysteme

#### Was ist ein Einkreissystem?

Integrierte Anwendung (wie Personalabrechnung) wird mit Schnittstelle an externes Rechnungswesen angebunden

#### Einkreis- vs. Zweikreissystem?

Ein Zweikreisystem versorgt neben dem externen noch das interne Rechnungswesen (Kostenrechnung)

#### Was enthält ein E-Schein?

- Artefakte (alles, was man sehen kann)
- Propagierte Werte (Grund, warum man Artefakte hat und "Dinge" tut)
- Tieferliegende Annahmen (verwurzelte Werte)

## 5 Prozessqualität

#### Was ist Qualität?

Qualität ist das, wofür der Kunde bereit ist zu zahlen

#### Worauf muss Qualität geprüft werden?

- Überqualität
- Minderqualität

### 5.1 Compliance

#### Was ist Compliance?

Regeltreue (extern, intern)

#### Inwiefern ist Compliance vorgegeben?

- Extern: Gesetze, Verbände
- Intern: Regeln/Richtlinien

### 5.2 Qualitätsmanagement

#### Was ist der KVP und wo hat er seinen Ursprung?

KVP = Kontinuierlicher Verbesserungsprozess, Japan

#### Wozu wird six-sigma verwendet?

Zur Qualitätskontrolle mithilfe von Standardabweichungen

#### Wie groß ist die Wahrscheinlichkeit gemäß six-sigma, dass die Abweichung von der Erwartung größer als die Standardabweichung ist?

P(x > UCL) = P(x > 4,5 sigma) = 3,4 DPMO => beobachtbarer Standardwert

#### Was besagt der Prozessfähigkeitsindex?

- Wie gut ein Prozess ist, innerhalb der Toleranzgrenzen zu produzieren
- Verhältnis aus Standardabweichung und 6

#### Formel für Prozessfähigkeitsindex C?

- Anz. Standardabw (Toleranz) / 6
- oder: Anz. Standardabw (UCL - E(x)) / 3

#### Nach welchen Kriterien wird ein Prozess analysiert?

- Prozessfähigkeit (fähig, nicht fähig)
- Prozessstabilität (stabil, nicht stabil)

#### Was analysiert ein Signifikanztest?

Ist die Varianz der Stichprobe signifikant größer/kleiner als mit Kunde vereinbart? (Gibt es eine Über-/Minderqualität)

#### Welche zwei Arten von Hypothesentests gibt es?

- Stichprobentest
- Parametertest

#### Vorgaben und Formel für Stichprobentest?

- Vorgaben: E(x), n, x, s
- Formel: z = (x - E(x)) / (s / sqrt(n - 1)) -> Ergebnis muss in Quartil sein

#### Vorgaben und Formel für Parametertest?

- Vorgaben: σ, n, s
- Formel: T = s² \* (n - 1) / σ² -> Ergebnis muss in Bereich sein

#### Was ist DMAIC?

Kontinuierlicher Verbesserungsprozess im Qualitätsmanagement

#### Was bedeutet DMAIC?

Define -> Measure -> Analyse -> Improve -> Control

### 5.3 Wissen aus Geschäftsprozessen gewinnen

#### Was sagt die Entropie aus und was ist der gewünschte Wert?

Wie genau Merkmale die Zielvariablen voraussagen, die Entropie soll möglichst klein sein (je weiter von 0,5 entfernt, desto eindeutiger)

#### Nenne die 3 Abbruchkriterien beim maschinellen Lernen

- Eindeutigkeit (bedingte Wahrscheinlichkeit ist 0 oder 1)
- Keine (statistisch relevanten) Daten mehr vorhanden
- Kein weiteres Merkmal verfügbar

#### Wie lautet die Formel für die Entropie?

E = p \* (1 - p)

#### Was tun, wenn man zwei gleiche Entropien hat?

Würfeln

### 5.4 Prozessoptimierung

#### Wie kann man Prozesse optimieren?

- Weglassen (andere Software, Add-Ons)
- Auslagern (shared service kaufen)
- Parallelisieren
- Schleifen entfernen
- Verlagern (innerhalb Geschäftsprozess verschieben)
- Beschleunigen
- Überlappende Fertigung (verringert Durchlaufzeit)

#### Was ist die Transaktionskostentheorie?

Untersucht Entstehung und Minimierung von Kosten bei auffallenden Transaktionen
