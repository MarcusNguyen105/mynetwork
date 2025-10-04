// Let's deobfuscate the JavaScript step by step

// First, let's extract the key arrays and functions
var _0xa = [0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72];
var _0xb = '3939203733203130362036372038372038342036392038392035332033332031303320353520363520383920393420373620383020313231203337203131343420';

// Function to decode _0xa array (this gives us the username)
function decode_a() {
    var result = '';
    for (var i = 0; i < _0xa.length; i++) {
        result += String.fromCharCode(_0xa[i]);
    }
    return result;
}

// Function to decode _0xb string (this should give us the password)
// Looking at the original code, it seems to split by spaces and convert each number to char
function decode_b() {
    var result = '';
    // First convert hex pairs to get space-separated numbers
    for (var i = 0; i < _0xb.length; i += 2) {
        result += String.fromCharCode(parseInt(_0xb.substring(i, i + 2), 16));
    }
    console.log("Hex decoded result:", result);
    
    // Then split by spaces and convert each number to character
    var parts = result.split(' ');
    var decoded = parts.map(function(part) {
        return String.fromCharCode(parseInt(part));
    }).join('');
    return decoded;
}

console.log("Decoded _0xa:", decode_a());
console.log("Decoded _0xb:", decode_b());

// Let's also check the individual character codes
console.log("Password char codes:");
var password = decode_b();
for (var i = 0; i < password.length; i++) {
    console.log(i, password.charCodeAt(i), password.charAt(i));
}

// Let's also try to decode the hex string differently
console.log("\nTrying different decoding approach:");
var hexString = '3939203733203130362036372038372038342036392038392035332033332031303320353520363520383920393420373620383020313231203337203131343420';
var parts = [];
for (var i = 0; i < hexString.length; i += 3) {
    var hex = hexString.substring(i, i + 2);
    parts.push(parseInt(hex, 16));
}
console.log("Decimal values:", parts);

var decoded2 = parts.map(function(val) {
    return String.fromCharCode(val);
}).join('');
console.log("Alternative decode:", decoded2);
// The code seems to be making a POST request to /administrator endpoint