// I found `({...}CCSU` which reverses to `USCC}...{(`
// This looks like it could be the flag format with something in the middle

// Let me look for what might go in the `...` part
// Maybe it's constructed from other strings in the array

var flagStart = 'USCC{';
var flagEnd = '}';

// The string `({...}CCSU` suggests the flag format is USCC{...}
// Let me look for what might fill the middle part

// Let me check all the potential hash parts I found
var hashParts = [
    '6631656436',  // f1ed6
    '3961373433',  // 9a743
    '3361326434',  // 3a2d4
    '3463383330',  // 4c830
    '6134353334',  // a4534
    '6161343030'   // aa400
];

console.log("Decoding potential hash parts:");
var decodedParts = [];
hashParts.forEach((hex, index) => {
    var decoded = '';
    for (var i = 0; i < hex.length; i += 2) {
        decoded += String.fromCharCode(parseInt(hex.substring(i, i + 2), 16));
    }
    console.log(`${hex} -> ${decoded}`);
    decodedParts.push(decoded);
});

// Try different combinations
console.log("\nTrying different flag combinations:");
console.log("All parts: USCC{" + decodedParts.join('') + "}");

// Maybe it's just some of them
console.log("First 3: USCC{" + decodedParts.slice(0, 3).join('') + "}");
console.log("Last 3: USCC{" + decodedParts.slice(-3).join('') + "}");

// Maybe the order is different
console.log("Reversed: USCC{" + decodedParts.reverse().join('') + "}");

// Let me also check if there are any other clues in the obfuscated code
// Maybe I need to look at what the hash1, hash2, instruction variables actually contain

// Let me also check if there's a simpler pattern
// Maybe the flag is just hidden in plain sight somewhere

console.log("\nLet me also check if the flag might be constructed differently...");

// Maybe I need to look at the console output when the JavaScript actually runs
// Or maybe there's a hidden element or comment I missed

// Let me check if any of the base64 strings decode to something useful
var base64Strings = ['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW', 'IxZg=='];
console.log("\nChecking base64 strings again:");
base64Strings.forEach(b64 => {
    try {
        var decoded = Buffer.from(b64, 'base64').toString('utf8');
        console.log(`${b64} -> ${decoded}`);
    } catch (e) {
        console.log(`${b64} -> Error: ${e.message}`);
    }
});

// Maybe the flag is the combination of these decoded values in the USCC{} format
var base64Decoded = ['c95ee47', 'c70c3eb', '7722c69'];
console.log("\nBase64 decoded flag attempts:");
console.log("USCC{" + base64Decoded.join('') + "}");
console.log("USCC{" + base64Decoded.join('-') + "}");
console.log("USCC{" + base64Decoded.join('_') + "}");