# CTF Challenge Solution: Security Through Obscurity

## Challenge Overview
URL: http://chals.uscc-cyberbowl-2025.ctf.institute:3004/

The challenge involves heavily obfuscated JavaScript that hides credentials and flag components.

## Step 1: Extract Credentials from Main Page

The main page contains obfuscated JavaScript with hidden credentials:

**Username** (from array `_0xa`):
```javascript
_0xa = [0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72]
// Decodes to: admin1strat0r
```

**Password** (from hex string `_0xb`):
```javascript
_0xb = '393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134'
// First: decode hex pairs to ASCII -> "99 73 106 67 87 84 69 89 53 33 103 55 65 89 94 76 80 121 37 134"
// Then: decode space-separated decimal values to characters -> "cIjCWTEY5!g7AY^LPy%r"
```

## Step 2: Access Administrator Panel

Using the credentials via HTTP Basic Auth:
```bash
Username: admin1strat0r
Password: cIjCWTEY5!g7AY^LPy%r
Endpoint: GET /administrator
```

## Step 3: Deobfuscate Admin Page

The admin page contains another layer of obfuscation with three variables:
- `hash1`
- `hash2`  
- `instruction`

**Key Arrays:**
- `_0x4a39`: Contains base64 strings and hex-encoded values
- `_0x32e5`: Built from `_0x4a39` using offset 0x146

**Hash Components (decoded):**

Base64 strings from `_0x4a39`:
1. `Yzk1ZWU0Nz` → `c95ee47`
2. `YzcwYzNlYj` → `c70c3eb`
3. `NzcyMmM2OW` → `7722c69`

Hex-encoded numeric strings:
1. `3463383330` → `4c830`
2. `613435333445` → `a4534E` (note the capital E)

## Step 4: Construct the Flag

Combining all parts in order:
```
c95ee47 + c70c3eb + 7722c69 + 4c830 + a4534E
= c95ee47c70c3eb7722c694c830a4534E
```

This is a 32-character hash (MD5 format).

## Final Flags (try both cases):
```
USCC{c95ee47c70c3eb7722c694c830a4534E}
USCC{c95ee47c70c3eb7722c694c830a4534e}
```

Most likely (MD5 are typically lowercase):
```
USCC{c95ee47c70c3eb7722c694c830a4534e}
```
