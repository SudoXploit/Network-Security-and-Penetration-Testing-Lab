#!/bin/bash
# Auto Nmap scan
# Usage: ./auto_nmap_scan.sh <target-ip>

target=$1

if [ -z "$target" ]; then
  echo "Usage: $0 <target-ip>"
  exit 1
fi

echo "[*] Scanning $target..."
nmap -sS -T4 -A -Pn $target -oN "scan_$target.txt"
