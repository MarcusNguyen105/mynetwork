#!/bin/bash
# SMB Enumeration Commands for 10.12.0.111

echo "=== SMB Enumeration - 10.12.0.111 ==="
echo ""

echo "[*] Trying anonymous SMB access..."
echo "smbclient -L //10.12.0.111/ -N"
echo ""

echo "[*] Trying to access IPC$ share..."
echo "smbclient //10.12.0.111/IPC$ -N"
echo ""

echo "[*] Enum4linux comprehensive scan..."
echo "enum4linux -a 10.12.0.111"
echo ""

echo "[*] Enum4linux with verbose output..."
echo "enum4linux -v 10.12.0.111"
echo ""

echo "[*] Nmap SMB scripts..."
echo "nmap --script smb-enum-shares,smb-enum-users,smb-os-discovery,smb-security-mode,smb2-security-mode -p 139,445 10.12.0.111"
echo ""

echo "[*] Check SMB version..."
echo "nmap --script smb-protocols -p 139,445 10.12.0.111"
echo ""

echo "[*] Try common usernames..."
echo "crackmapexec smb 10.12.0.111 -u 'guest' -p ''"
echo "crackmapexec smb 10.12.0.111 -u 'anonymous' -p ''"
echo "crackmapexec smb 10.12.0.111 -u '' -p ''"
