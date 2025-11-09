#!/bin/bash

# Comprehensive Enumeration Scripts
# Run these from your Kali environment

echo "=== System 1: 10.12.0.42 (Linux) ==="
echo ""

echo "[*] Checking FTP (ProFTPD 1.3.5)..."
echo "ftp 10.12.0.42"
echo ""

echo "[*] Checking Web Server..."
echo "curl -v http://10.12.0.42/"
echo "gobuster dir -u http://10.12.0.42/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
echo ""

echo "[*] Checking SSH..."
echo "nc 10.12.0.42 22"
echo ""

echo ""
echo "=== System 2: 10.12.0.111 (Windows) ==="
echo ""

echo "[*] Checking Web Servers..."
echo "curl -v http://10.12.0.111/"
echo "curl -v http://10.12.0.111:8080/"
echo "gobuster dir -u http://10.12.0.111/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
echo "gobuster dir -u http://10.12.0.111:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
echo ""

echo "[*] Checking SMB..."
echo "smbclient -L //10.12.0.111/ -N"
echo "enum4linux -a 10.12.0.111"
echo ""

echo "[*] Checking WinRM..."
echo "crackmapexec winrm 10.12.0.111 -u '' -p ''"
echo ""

echo ""
echo "=== System 3: 10.12.0.136 (Windows) - FLAG 1 FOUND ==="
echo ""

echo "[*] FLAG FOUND: CSEC-3961-QOTD (port 17)"
echo "[*] Checking RDP..."
echo "nc 10.12.0.136 3389"
echo "nmap --script rdp-enum-encryption -p 3389 10.12.0.136"
echo ""

echo "[*] Full port scan for third-party services..."
echo "nmap -p- -sV 10.12.0.136"
echo "nmap -sU --top-ports 1000 10.12.0.136"
echo ""

echo ""
echo "=== System 4: 10.12.0.194 (Linux) ==="
echo ""

echo "[*] Checking Web Server..."
echo "curl -v http://10.12.0.194/"
echo "gobuster dir -u http://10.12.0.194/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt"
echo ""

echo "[*] Checking SSH..."
echo "nc 10.12.0.194 22"
echo ""

echo ""
echo "=== Vulnerability Checks ==="
echo ""
echo "[*] ProFTPD 1.3.5 vulnerabilities:"
echo "searchsploit ProFTPD 1.3.5"
echo ""
echo "[*] Apache 2.4.29 vulnerabilities:"
echo "searchsploit Apache 2.4.29"
echo ""
echo "[*] OpenSSH 7.6 vulnerabilities:"
echo "searchsploit OpenSSH 7.6"
echo ""
