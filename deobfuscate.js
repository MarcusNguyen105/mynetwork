// Let's deobfuscate this step by step
// First, let's extract the key variables and functions

// The obfuscated array _0xa contains character codes:
var _0xa = [0x61, 0x64, 0x6d, 0x69, 0x6e, 0x31, 0x73, 0x74, 0x72, 0x61, 0x74, 0x30, 0x72];

// Convert to string:
function _0x2468() {
    var result = '';
    for (var i = 0; i < _0xa.length; i++) {
        result += String.fromCharCode(_0xa[i]);
    }
    return result;
}

console.log("Username from _0x2468():", _0x2468());

// The hex string _0xb - this appears to be space-separated decimal numbers in hex format:
var _0xb = '393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134';

// Let me decode this step by step
console.log("Original hex string:", _0xb);

// First, convert each hex pair to a character to get space-separated decimal numbers
var step1 = '';
for (var i = 0; i < _0xb.length; i += 2) {
    step1 += String.fromCharCode(parseInt(_0xb.substring(i, i + 2), 16));
}
console.log("Step 1 - hex to chars:", step1);

// Now split by spaces and convert each decimal to a character
function _0x1357() {
    var step1 = '';
    for (var i = 0; i < _0xb.length; i += 2) {
        step1 += String.fromCharCode(parseInt(_0xb.substring(i, i + 2), 16));
    }
    
    var numbers = step1.split(' ');
    var result = numbers.map(function(num) {
        return String.fromCharCode(parseInt(num));
    }).join('');
    return result;
}

console.log("Password from _0x1357():", _0x1357());

// Let's also check what endpoint they're trying to access
console.log("Endpoint: /administrator");