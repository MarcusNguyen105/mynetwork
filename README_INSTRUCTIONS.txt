FOR LOOP CREDENTIAL TESTING - INSTRUCTIONS
===========================================

STEP 1: Update credentials.txt
-------------------------------
Replace "adminStudent1" with your actual admin username based on your student number.
Example: If you're student 5, use "adminStudent5"

The passwords listed are examples. Update them based on the screenshot in your lab instructions.

STEP 2: Find your domain name
-------------------------------
On Windows 10, run this command to find your domain:
    systeminfo | findstr /C:"Domain"

STEP 3: Update the script
--------------------------
Open credential_test.bat and replace "DOMAIN" with your actual domain name from Step 2.

Example: If your domain is "CYBERLAB", change:
    net use \\10.12.0.10\ipc$ %%B /user:DOMAIN\%%A
to:
    net use \\10.12.0.10\ipc$ %%B /user:CYBERLAB\%%A

STEP 4: Delete existing sessions
---------------------------------
Before running the script, execute:
    net use * /delete

Verify with:
    net use

STEP 5: Run the script
----------------------
Execute the batch file:
    credential_test.bat

The script will:
- Test each username/password combination
- Log all attempts to output.txt
- Display results on screen
- Clean up sessions between attempts

STEP 6: Take screenshots
------------------------
1. Screenshot of the entire script (open credential_test.bat in notepad)
2. Screenshot of the command output
3. Screenshot of output.txt file

TROUBLESHOOTING
---------------
- "The network address is invalid" = typo in IP address
- Only one connection per system allowed = run "net use * /delete" first
- Make sure Wireshark is capturing on the correct interface before running!
