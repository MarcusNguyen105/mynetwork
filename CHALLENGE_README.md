# Security Through Obscurity Challenge

> "You're gonna hate me for this one but hear me out: what if instead of actual security, we just had obscurity instead?"

## 🎯 Challenge Description

This CTF challenge demonstrates why **security through obscurity** is NOT real security. The application uses heavily obfuscated JavaScript to "protect" sensitive credentials and endpoints, but all the information needed to gain access is hiding in plain sight (if you know where to look).

## 🚀 Running the Challenge

```bash
# Install dependencies
npm install

# Start the server
npm start

# Or use nodemon for development
npm run dev
```

The server will run on `http://localhost:3004` by default.

## 🎮 Challenge Goal

Find the flag by:
1. Analyzing the obfuscated JavaScript code
2. Extracting the hidden credentials
3. Authenticating to the admin endpoint

## 💡 Hints

1. Open your browser's Developer Console (F12)
2. Look at what the JavaScript is doing
3. The code contains encoded credentials that are "hidden" through obfuscation
4. Check out what functions are being defined and what data they're processing

## 🔍 Learning Objectives

- Understanding why obfuscation ≠ security
- Learning to reverse engineer obfuscated JavaScript
- Recognizing common obfuscation techniques:
  - Hex encoding
  - Character code manipulation
  - String splitting and joining
  - Variable name mangling
- Understanding that client-side code is always accessible

## ⚠️ Educational Purpose

This challenge is designed to teach why:
- **Storing credentials in client-side code is NEVER secure**
- **Obfuscation only slows down attackers, it doesn't stop them**
- **Real security requires server-side validation, encryption, and proper authentication**

## 🏆 Flag Format

`USCC{...}`

---

**Remember:** In real applications, NEVER store secrets in client-side code, no matter how well obfuscated! Always use proper authentication, authorization, and server-side validation.
