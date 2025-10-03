#!/bin/bash
# Manual interaction script for the CTF challenge

echo "=== Connecting to CTF Challenge ==="
echo "Host: chals.uscc-cyberbowl-2025.ctf.institute"
echo "Port: 3013"
echo ""
echo "Commands to try:"
echo "1. List employees: 4"
echo "2. Create employee with PIN 484: 1, then 'Test', then 484"
echo "3. Access secrets: 3"
echo ""
echo "Press Ctrl+C to exit"
echo ""

# Try to connect with timeout
timeout 10 nc chals.uscc-cyberbowl-2025.ctf.institute 3013
