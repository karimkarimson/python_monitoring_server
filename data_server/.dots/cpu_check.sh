#!/bin/bash
CPU_FILE="/home/ubuntu/.dots/data/cpu_data.txt"
get_cpu() {
	local cpu=$(mpstat | grep -A 5 '%idle' | tail -n 1 | awk -F " " '{print 100 - $ 12}'a)
	echo $cpu > $CPU_FILE
}
get_cpu
