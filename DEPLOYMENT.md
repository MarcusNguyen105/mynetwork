# Deployment Guide

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start the server
npm start
```

The application will be available at `http://localhost:3004`

## 📋 Files Structure

```
.
├── server.js                   # Express server with endpoints
├── package.json                # Dependencies
├── public/                     # Static files
│   ├── index.html             # Main HTML with obfuscated JS
│   ├── styles.css             # Retro terminal styling
│   └── art.js                 # ASCII art generator
├── CHALLENGE_README.md         # Challenge description
├── SOLUTION.md                # Step-by-step solution
└── DEPLOYMENT.md              # This file
```

## 🔧 Configuration

The server uses the following configuration:
- **Default Port**: 3004
- **Environment Variable**: `PORT` (override default port)

Example:
```bash
PORT=8080 npm start
```

## 🌐 Endpoints

### `GET /`
Serves the main challenge page with obfuscated JavaScript

### `POST /administrator`
The "secret" admin endpoint that validates credentials and returns the flag

**Expected Body:**
```json
{
  "username": "admin1strat0r",
  "password": "Y0uF0und1tN1c3W0rk!",
  "endpoint": "/administrator"
}
```

**Success Response:**
```json
{
  "success": true,
  "message": "Access granted!",
  "flag": "USCC{0b5cur1ty_15_n0t_53cur1ty_ju5t_h1d1ng_th1ng5}"
}
```

### `GET /super_secret_backup_admin_panel_do_not_look`
Easter egg endpoint with hints

## 🐳 Docker Deployment (Optional)

You can create a `Dockerfile`:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3004

CMD ["node", "server.js"]
```

Build and run:
```bash
docker build -t obscurity-challenge .
docker run -p 3004:3004 obscurity-challenge
```

## 🔒 Security Notes

This challenge intentionally demonstrates **BAD** security practices:

❌ **Don't Do This in Real Applications:**
- Storing credentials in client-side code
- Using obfuscation as security
- Exposing admin endpoints without proper authentication
- Trusting client-side validation

✅ **Instead, Use:**
- Server-side authentication (OAuth, JWT, etc.)
- Proper password hashing (bcrypt, argon2)
- HTTPS/TLS encryption
- Rate limiting and CSRF protection
- Environment variables for secrets
- Secure session management

## 📝 Testing

Test the challenge is working:

```bash
# Check server is running
curl http://localhost:3004/

# Test with correct credentials
curl -X POST http://localhost:3004/administrator \
  -H "Content-Type: application/json" \
  -d '{"username":"admin1strat0r","password":"Y0uF0und1tN1c3W0rk!","endpoint":"/administrator"}'

# Should return the flag
```

## 🎯 For CTF Organizers

When deploying for a CTF:

1. Change the flag in `server.js` to your custom flag
2. Consider adding rate limiting to prevent brute force
3. Add logging to track solve attempts
4. Consider using a reverse proxy (nginx) for better performance
5. Monitor resource usage

Example flag customization:
```javascript
// In server.js
flag: 'USCC{your_custom_flag_here}'
```

## 📊 Monitoring

Basic logging is included. For production, consider:
- Adding Morgan or Winston for structured logging
- Setting up metrics (Prometheus)
- Adding health check endpoints
- Implementing request tracing

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Use a different port
PORT=3005 npm start
```

**Dependencies not installing:**
```bash
# Clear npm cache
npm cache clean --force
npm install
```

**Server not accessible:**
- Check firewall rules
- Verify port forwarding if behind NAT
- Check server logs for errors

## 📞 Support

For issues or questions about this challenge:
- Check the SOLUTION.md for detailed walkthrough
- Review the CHALLENGE_README.md for hints
- Examine the obfuscated code in public/index.html
