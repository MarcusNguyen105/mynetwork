#!/bin/bash
# Echo Service CTF Challenge - Quick Runner Script

echo "=========================================="
echo "   Echo Service CTF Challenge Runner"
echo "=========================================="
echo ""

show_menu() {
    echo "Select an option:"
    echo ""
    echo "  1) Automated Brute Force (Recommended)"
    echo "  2) Test Service Connection"
    echo "  3) Manual Exploit (requires offset and address)"
    echo "  4) View Binary Analysis"
    echo "  5) Brute Force Offset Only"
    echo "  6) Brute Force Address Only"
    echo "  7) Test Specific Configuration"
    echo "  8) View Documentation"
    echo "  9) Exit"
    echo ""
    read -p "Choice [1-9]: " choice
    echo ""
}

while true; do
    show_menu
    
    case $choice in
        1)
            echo "[*] Running automated brute force..."
            echo "[*] This will try common offset and address combinations"
            echo "[*] Press Ctrl+C to stop"
            echo ""
            python3 bruteforce.py
            ;;
        2)
            echo "[*] Testing service connection..."
            python3 exploit.py test
            ;;
        3)
            read -p "Enter offset (e.g., 40): " offset
            read -p "Enter address (e.g., 0x080486a7): " addr
            echo "[*] Running exploit with offset=$offset, address=$addr"
            python3 exploit.py $offset $addr
            ;;
        4)
            echo "[*] Analyzing binary dump..."
            python3 analyze_dump.py
            ;;
        5)
            read -p "Enter known address (e.g., 0x080486a7): " addr
            echo "[*] Brute forcing offset with address=$addr"
            python3 bruteforce.py offset $addr
            ;;
        6)
            read -p "Enter known offset (e.g., 40): " offset
            echo "[*] Brute forcing address with offset=$offset"
            python3 bruteforce.py address $offset
            ;;
        7)
            read -p "Enter offset (e.g., 40): " offset
            read -p "Enter address (e.g., 0x080486a7): " addr
            echo "[*] Testing offset=$offset, address=$addr"
            python3 bruteforce.py test $offset $addr
            ;;
        8)
            echo "Available documentation files:"
            echo ""
            echo "  • INDEX.md        - Main overview (START HERE)"
            echo "  • QUICKSTART.md   - Quick reference guide"
            echo "  • SOLUTION.md     - Detailed solution"
            echo "  • README.md       - Challenge analysis"
            echo "  • COMPLETE_TOOLKIT_SUMMARY.txt - Full summary"
            echo ""
            read -p "Which file to view? (or press Enter to skip): " docfile
            if [ -n "$docfile" ]; then
                if [ -f "$docfile" ]; then
                    less "$docfile" || cat "$docfile"
                else
                    echo "File not found: $docfile"
                fi
            fi
            ;;
        9)
            echo "Goodbye! Good luck with the challenge!"
            exit 0
            ;;
        *)
            echo "[!] Invalid choice. Please select 1-9."
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
    clear
done
