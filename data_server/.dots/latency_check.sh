#!/bin/bash

# Variablen für den Host und den Dateinamen
LATENCY_FILE="/home/ubuntu/.dots/data/latency_data.txt" # Dateiname für die Latenzdaten
LATENCY_LOG="/home/ubuntu/.dots/data/latency_check.log"
if [[ -z $1 ]]
then
	echo "Using default Ping-Host: CCC.de" >> $LATENCY_LOG
	HOST="ccc.de" # Standard-Host, kann überschrieben werden
else
	HOST=$1
	echo "Using custom Host $HOST" >> $LATENCY_LOG
fi


# Funktion, um die erreichbarkeit des Hosts festzustellen
check_host() {
	local test=($ping -c 1 $HOST)
	if [[ test -eq 0 ]]
	then
		write_latency_to_file
	else
		echo "Host $1 not reachable, relaying to default Ping-Host: CCC.de" >> $LATENCY_LOG
		HOST="ccc.de" # Standard-Host, kann überschrieben werden
		write_latency_to_file
	fi
}

# Funktion, um die durchschnittliche Latenz zu messen
measure_latency() {
    # Führt den Ping-Befehl aus und extrahiert die durchschnittliche Latenz
    local latency=$(ping -c 5 $HOST | tail -1 | awk '{print $4}' | cut -d '/' -f 2)
    echo $latency
}

# Funktion, um die gemessene Latenz in eine Datei zu schreiben
write_latency_to_file() {
    # Ruft die Funktion measure_latency auf und leitet das Ergebnis in eine Datei um
    local latency=$(measure_latency)
    echo $latency > $LATENCY_FILE
}

# Hauptfunktion
main() {
	check_host
}

# Ausführung der Hauptfunktion
main
