// Let's deobfuscate the admin panel JavaScript

// I need to extract the obfuscated arrays and decode them
// From the code, I can see there are multiple layers of obfuscation

// Let me try to understand the structure first
// There are functions _0x4a39, _0x32e5, _0x4deb, _0x3476 that seem to be deobfuscation functions

// Let me extract the key strings and try to decode them manually
// From the code, I can see these base64-like strings:
var strings = [
    'Yzk1ZWU0Nz',
    'YzcwYzNlYj',
    'NzcyMmM2OW',
    'Y4OWEwYWFl',
    'k1MDI0NDY1'
];

console.log("Decoding base64 strings:");
strings.forEach((str, index) => {
    try {
        var decoded = Buffer.from(str, 'base64').toString('utf8');
        console.log(`${index}: ${str} -> ${decoded}`);
    } catch (e) {
        console.log(`${index}: ${str} -> Error: ${e.message}`);
    }
});

// I also see hex-like strings:
var hexStrings = [
    '6631656436',
    '6232',
    '3961373433',
    '3361326434',
    '3463383330',
    '40556232',
    '6134353334'
];

console.log("\nDecoding hex strings:");
hexStrings.forEach((str, index) => {
    try {
        var decoded = '';
        for (var i = 0; i < str.length; i += 2) {
            decoded += String.fromCharCode(parseInt(str.substring(i, i + 2), 16));
        }
        console.log(`${index}: ${str} -> ${decoded}`);
    } catch (e) {
        console.log(`${index}: ${str} -> Error: ${e.message}`);
    }
});

// I also see some reversed strings in the obfuscated array:
var reversedStrings = [
    'eulav eht ',
    'parw dna ,',
    'ts eht ni ',
    'c ,sehsah ',
    'rehtegot s',
    'alf dradna',
    'eht kcarc'
];

console.log("\nReversing strings:");
reversedStrings.forEach((str, index) => {
    var reversed = str.split('').reverse().join('');
    console.log(`${index}: "${str}" -> "${reversed}"`);
});

// Let me try to piece together what looks like a flag format
console.log("\nLooking for flag patterns...");
// The challenge mentioned "security through obscurity", so the flag might be hidden in these strings