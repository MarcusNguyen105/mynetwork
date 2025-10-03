// Let's implement the exact decoding logic from the original obfuscated code

var _0xa = [0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72];
var _0xb = '3939203733203130362036372038372038342036392038392035332033332031303320353520363520383920393420373620383020313231203337203131343420';

// This is the _0x2468 function from the original code
function _0x2468() {
    var result = '';
    for (var i = 0; i < _0xa.length; i++) {
        result += String.fromCharCode(_0xa[i]);
    }
    return result;
}

// This is the _0x1357 function from the original code
function _0x1357() {
    var result = '';
    for (var i = 0; i < _0xb.length; i += 2) {
        result += String.fromCharCode(parseInt(_0xb.substring(i, 2), 16));
    }
    var parts = result.split(' ');
    var decoded = parts.map(function(part) {
        return String.fromCharCode(parseInt(part));
    }).join('');
    return decoded;
}

console.log("Username:", _0x2468());
console.log("Password:", _0x1357());

// Let's also manually decode the hex string step by step
console.log("\nManual hex decoding:");
var hexStr = '3939203733203130362036372038372038342036392038392035332033332031303320353520363520383920393420373620383020313231203337203131343420';
console.log("Hex string length:", hexStr.length);

var intermediate = '';
for (var i = 0; i < hexStr.length; i += 2) {
    var hex = hexStr.substring(i, i + 2);
    var decimal = parseInt(hex, 16);
    var char = String.fromCharCode(decimal);
    intermediate += char;
    console.log(`${hex} -> ${decimal} -> '${char}'`);
}
console.log("Intermediate result:", JSON.stringify(intermediate));

// Now split by spaces and decode
var numbers = intermediate.split(' ');
console.log("Numbers array:", numbers);

var finalPassword = '';
for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] !== '') {
        var num = parseInt(numbers[i]);
        if (!isNaN(num)) {
            finalPassword += String.fromCharCode(num);
            console.log(`${numbers[i]} -> ${num} -> '${String.fromCharCode(num)}'`);
        }
    }
}
console.log("Final password:", JSON.stringify(finalPassword));