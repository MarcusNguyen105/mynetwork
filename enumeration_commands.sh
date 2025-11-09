#!/bin/bash
# Enumeration Command Script for 10.12.0.0/24 Penetration Test
# Run these commands from your Kali box with network access to targets

echo "=========================================="
echo "PENETRATION TEST ENUMERATION SCRIPT"
echo "Target Network: 10.12.0.0/24"
echo "=========================================="
echo ""

# Create output directory
mkdir -p ~/pentest_results_$(date +%Y%m%d)
cd ~/pentest_results_$(date +%Y%m%d)
echo "[+] Results directory: $(pwd)"
echo ""

# ==========================================
# 10.12.0.42 - Linux/Ubuntu
# ==========================================
echo "[*] Starting enumeration of 10.12.0.42 (Linux/Ubuntu)"
echo ""

# Web server enumeration
echo "[+] Running gobuster on 10.12.0.42..."
gobuster dir -u http://10.12.0.42 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,bak -o gobuster_10.12.0.42.txt -q &

# Nikto scan
echo "[+] Running nikto on 10.12.0.42..."
nikto -h 10.12.0.42 -o nikto_10.12.0.42.txt &

# FTP anonymous login test
echo "[+] Testing FTP anonymous access on 10.12.0.42..."
echo -e "user anonymous\npass anonymous@test.com\nls\nbye" | ftp -n 10.12.0.42 > ftp_10.12.0.42.txt 2>&1 &

# Manual web checks
echo "[+] Checking common files on 10.12.0.42 web server..."
curl -s http://10.12.0.42/robots.txt > 10.12.0.42_robots.txt 2>&1
curl -s http://10.12.0.42/flag.txt > 10.12.0.42_flag.txt 2>&1
curl -s http://10.12.0.42/.git/config > 10.12.0.42_git.txt 2>&1

# Search for ProFTPD exploits
echo "[+] Searching for ProFTPD 1.3.5 exploits..."
searchsploit proftpd 1.3.5 | tee proftpd_exploits.txt

echo ""

# ==========================================
# 10.12.0.111 - Windows
# ==========================================
echo "[*] Starting enumeration of 10.12.0.111 (Windows)"
echo ""

# Web server enumeration on both ports
echo "[+] Running gobuster on 10.12.0.111:80..."
gobuster dir -u http://10.12.0.111 -w /usr/share/wordlists/dirb/common.txt -x asp,aspx,txt,bak -o gobuster_10.12.0.111_80.txt -q &

echo "[+] Running gobuster on 10.12.0.111:8080..."
gobuster dir -u http://10.12.0.111:8080 -w /usr/share/wordlists/dirb/common.txt -x asp,aspx,txt,bak -o gobuster_10.12.0.111_8080.txt -q &

# Nikto scans
echo "[+] Running nikto on 10.12.0.111:80..."
nikto -h 10.12.0.111 -o nikto_10.12.0.111_80.txt &

echo "[+] Running nikto on 10.12.0.111:8080..."
nikto -h 10.12.0.111:8080 -o nikto_10.12.0.111_8080.txt &

# SMB enumeration
echo "[+] Enumerating SMB shares on 10.12.0.111..."
smbclient -L //10.12.0.111 -N > smb_shares_10.12.0.111.txt 2>&1 &

echo "[+] Running enum4linux on 10.12.0.111..."
enum4linux -a 10.12.0.111 > enum4linux_10.12.0.111.txt 2>&1 &

# Manual web checks
echo "[+] Checking common files on 10.12.0.111 web servers..."
curl -s http://10.12.0.111/robots.txt > 10.12.0.111_80_robots.txt 2>&1
curl -s http://10.12.0.111/flag.txt > 10.12.0.111_80_flag.txt 2>&1
curl -s http://10.12.0.111:8080/robots.txt > 10.12.0.111_8080_robots.txt 2>&1
curl -s http://10.12.0.111:8080/flag.txt > 10.12.0.111_8080_flag.txt 2>&1

echo ""

# ==========================================
# 10.12.0.136 - Windows (Flag already found)
# ==========================================
echo "[*] Starting enumeration of 10.12.0.136 (Windows)"
echo ""

# Interact with legacy services
echo "[+] Interacting with legacy services on 10.12.0.136..."
echo "HELLO" | nc -w 2 10.12.0.136 7 > 10.12.0.136_echo.txt 2>&1 &    # Echo
echo "TEST" | nc -w 2 10.12.0.136 9 > 10.12.0.136_discard.txt 2>&1 &   # Discard
nc -w 2 10.12.0.136 13 > 10.12.0.136_daytime.txt 2>&1 &                # Daytime
nc -w 2 10.12.0.136 17 > 10.12.0.136_qotd.txt 2>&1 &                   # QOTD (flag found here)
nc -w 2 10.12.0.136 19 > 10.12.0.136_chargen.txt 2>&1 &                # Chargen

# RDP enumeration
echo "[+] Checking for RDP vulnerabilities on 10.12.0.136..."
nmap -p 3389 --script rdp-enum-encryption,rdp-vuln-ms12-020 10.12.0.136 -oN nmap_rdp_10.12.0.136.txt &

# RPC enumeration
echo "[+] Attempting RPC enumeration on 10.12.0.136..."
rpcclient -U "" -N -c "srvinfo;enumdomains;querydominfo" 10.12.0.136 > rpcclient_10.12.0.136.txt 2>&1 &

echo ""

# ==========================================
# 10.12.0.194 - Linux/Ubuntu
# ==========================================
echo "[*] Starting enumeration of 10.12.0.194 (Linux/Ubuntu)"
echo ""

# Web server enumeration
echo "[+] Running gobuster on 10.12.0.194..."
gobuster dir -u http://10.12.0.194 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,bak -o gobuster_10.12.0.194.txt -q &

# Nikto scan
echo "[+] Running nikto on 10.12.0.194..."
nikto -h 10.12.0.194 -o nikto_10.12.0.194.txt &

# Manual web checks
echo "[+] Checking common files on 10.12.0.194 web server..."
curl -s http://10.12.0.194/robots.txt > 10.12.0.194_robots.txt 2>&1
curl -s http://10.12.0.194/flag.txt > 10.12.0.194_flag.txt 2>&1
curl -s http://10.12.0.194/.git/config > 10.12.0.194_git.txt 2>&1

# Search for Apache 2.4.29 vulnerabilities
echo "[+] Searching for Apache 2.4.29 exploits..."
searchsploit apache 2.4.29 | tee apache_exploits.txt

echo ""
echo "[*] Waiting for background jobs to complete..."
wait

echo ""
echo "=========================================="
echo "ENUMERATION COMPLETE"
echo "=========================================="
echo ""
echo "Results saved in: $(pwd)"
echo ""
echo "Next steps:"
echo "1. Review all output files for flags and interesting information"
echo "2. Check gobuster results for hidden directories"
echo "3. Manually browse to any discovered web directories"
echo "4. If FTP anonymous access worked, explore the FTP server"
echo "5. If SMB shares are accessible, investigate them"
echo "6. Research any found vulnerabilities and prepare exploits"
echo ""
echo "Quick checks to run manually:"
echo "  - Browse http://10.12.0.42 in a browser"
echo "  - Browse http://10.12.0.111 and http://10.12.0.111:8080"
echo "  - Browse http://10.12.0.194"
echo "  - Review any interesting directories found by gobuster"
echo ""
