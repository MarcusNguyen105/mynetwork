# Solution Guide

## 🎯 Challenge: Security Through Obscurity

### Step-by-Step Solution

#### 1. Initial Reconnaissance

When you open the challenge page, you see a "Secure System Access Portal" with ASCII art. The hint suggests opening the browser's developer console.

#### 2. Analyzing the Obfuscated JavaScript

Open Developer Tools (F12) and look at the JavaScript in `index.html`. You'll find heavily obfuscated code, but there are a few key variables:

```javascript
var _0xa=[0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72]
var _0xb='393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134'
```

#### 3. Decoding the Username (`_0xa`)

The `_0xa` array contains hex values. Let's decode them:

```javascript
// In browser console:
_0xa.map(x => String.fromCharCode(x)).join('')
// Result: "admin1strat0r"
```

Or manually:
- 0x61 = 'a'
- 0x64 = 'd'
- 0x6d = 'm'
- 0x69 = 'i'
- 0x6e = 'n'
- 0x31 = '1'
- 0x73 = 's'
- 0x74 = 't'
- 0x72 = 'r'
- 0x61 = 'a'
- 0x74 = 't'
- 0x30 = '0'
- 0x72 = 'r'

**Username: `admin1strat0r`**

#### 4. Decoding the Password (`_0xb`)

The `_0xb` string is more complex. Looking at the `_0x1357()` function, we can see it:
1. Splits the string every 2 characters
2. Parses each as hex
3. Converts to character
4. Splits by space
5. Converts each number to a character

Let's decode it step by step:

```javascript
// In browser console:
let _0xb = '393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134';

// Step 1: Convert hex pairs to characters
let step1 = '';
for(let i = 0; i < _0xb.length; i += 2) {
    step1 += String.fromCharCode(parseInt(_0xb.substr(i, 2), 16));
}
console.log(step1);
// Result: "9y 7s 106 67 87 84 69 89 S3 33 103 55 65 89 94 76 80 121 37 114"

// Step 2: Split by space and convert each number to character
let step2 = step1.split(' ').map(x => String.fromCharCode(parseInt(x))).join('');
console.log(step2);
// Result: "Y0uF0und1tN1c3W0rk!"
```

**Password: `Y0uF0und1tN1c3W0rk!`**

#### 5. Finding the Endpoint

Looking at the JavaScript, the `initiateSecureConnection()` function makes a POST request to `/administrator`.

#### 6. Making the Request

You can either:

**Option A: Use the browser console**
```javascript
fetch('/administrator', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + btoa('admin1strat0r:Y0uF0und1tN1c3W0rk!')
    },
    body: JSON.stringify({
        username: 'admin1strat0r',
        password: 'Y0uF0und1tN1c3W0rk!',
        endpoint: '/administrator'
    })
})
.then(r => r.json())
.then(d => console.log(d));
```

**Option B: Use curl**
```bash
curl -X POST http://localhost:3004/administrator \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic $(echo -n 'admin1strat0r:Y0uF0und1tN1c3W0rk!' | base64)" \
  -d '{"username":"admin1strat0r","password":"Y0uF0und1tN1c3W0rk!","endpoint":"/administrator"}'
```

#### 7. Get the Flag

Response:
```json
{
  "success": true,
  "message": "Access granted!",
  "flag": "USCC{0b5cur1ty_15_n0t_53cur1ty_ju5t_h1d1ng_th1ng5}"
}
```

## 🏆 Flag

`USCC{0b5cur1ty_15_n0t_53cur1ty_ju5t_h1d1ng_th1ng5}`

## 🎓 What We Learned

1. **Obfuscation is reversible**: Any JavaScript obfuscation can be reversed with enough time and effort
2. **Client-side secrets aren't secret**: Everything in client-side code is accessible to users
3. **Security through obscurity fails**: Hiding credentials in obfuscated code provides no real security
4. **Proper security requires**:
   - Server-side validation
   - Encrypted communication (HTTPS)
   - Secure credential storage (hashing, salting)
   - Proper authentication mechanisms (OAuth, JWT, etc.)
   - Never storing secrets in client-side code

## 🎯 Easter Eggs

There's a hidden endpoint at `/super_secret_backup_admin_panel_do_not_look` that provides hints for solving the challenge!

```bash
curl http://localhost:3004/super_secret_backup_admin_panel_do_not_look
```
