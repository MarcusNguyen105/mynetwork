// Deobfuscate the credentials from the JavaScript

// Username array
var _0xa = [0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72];

// Password string
var _0xb = '99 73 106 67 87 84 69 89 53 33 103 55 65 89 94 76 80 121 37 134';

// Decode username (_0x2468 function)
function getUsername() {
    var result = '';
    for (var i = 0; i < _0xa.length; i++) {
        result += String.fromCharCode(_0xa[i]);
    }
    return result;
}

// Decode password (_0x1357 function)
function getPassword() {
    // First: convert hex pairs to characters
    var temp = '';
    for (var i = 0; i < _0xb.length; i += 2) {
        temp += String.fromCharCode(parseInt(_0xb.substring(i, 2), 16));
    }
    
    // Split by space and map each number to a character
    var parts = _0xb.split(' ');
    var result = parts.map(function(num) {
        return String.fromCharCode(parseInt(num));
    }).join('');
    
    return result;
}

var username = getUsername();
var password = getPassword();

console.log('Username:', username);
console.log('Password:', password);
console.log('\nBasic Auth:', btoa(username + ':' + password));
console.log('\nEndpoint: /administrator');
