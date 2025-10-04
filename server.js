const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3004;

app.use(express.json());
app.use(express.static('public'));

// Super "secure" endpoint with flag
app.post('/administrator', (req, res) => {
    const { username, password } = req.body;
    
    // Check for the "secret" credentials hidden in the obfuscated JavaScript
    if (username === 'admin1strat0r' && password === 'Y0uF0und1tN1c3W0rk!') {
        res.json({
            success: true,
            message: 'Access granted!',
            flag: 'USCC{0b5cur1ty_15_n0t_53cur1ty_ju5t_h1d1ng_th1ng5}'
        });
    } else {
        res.status(401).json({
            success: false,
            message: 'Invalid credentials'
        });
    }
});

// Easter egg endpoint that's "hidden"
app.get('/super_secret_backup_admin_panel_do_not_look', (req, res) => {
    res.json({
        hint: 'The password is hiding in plain sight... well, obfuscated sight.',
        username_hint: 'Look at the _0xa array',
        password_hint: 'Look at the _0xb string and decode it'
    });
});

app.listen(PORT, () => {
    console.log(`🔒 "Secure" Portal running on http://localhost:${PORT}`);
    console.log(`⚠️  Warning: This uses security through obscurity (which is NOT security!)`);
});
