// Looking at the _0x4a39 array, I see these numeric strings that look like hex:
var hex_strings = [
    '6631656436',  // from _0x4a39
    '6232',        // from _0x4a39
    '3961373433',  // from _0x4a39
    '3361326434',  // from _0x4a39
    '3463383330',  // from _0x4a39
    '6134353334',  // from console
];

// Also from _0x32e5 build, there are these values that look like base64:
var base64_parts = [
    'Yzk1ZWU0Nz',
    'YzcwYzNlYj',
    'NzcyMmM2OW',
    'Y4OWEwYWFl',
    'k1MDI0NDY1',
];

console.log('=== Hex strings decoded ===');
hex_strings.forEach(hex => {
    var result = '';
    for (var i = 0; i < hex.length; i += 2) {
        result += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    }
    console.log(`${hex} -> ${result}`);
});

console.log('\n=== Base64 parts decoded ===');
base64_parts.forEach(b64 => {
    try {
        var decoded = Buffer.from(b64, 'base64').toString();
        console.log(`${b64} -> ${decoded}`);
    } catch(e) {
        console.log(`${b64} -> ERROR`);
    }
});

// Try combining base64 parts
console.log('\n=== Combined base64 ===');
var combined_b64 = base64_parts.join('');
try {
    var decoded = Buffer.from(combined_b64, 'base64').toString();
    console.log(`Combined: ${decoded}`);
} catch(e) {
    console.log('Failed to decode combined');
}

// From the instruction, I saw these parts when reversed
var instruction_parts = [
    'IxZg',  // This was "==gZxI" reversed, missing ==
    'zN0UWZ1kzY',
    'WO2MmMyczN',
    'kYoMtE'
];

console.log('\n=== Instruction parts with padding ===');
instruction_parts.forEach(part => {
    // Try with different padding
    for (var padding of ['', '=', '==', '===']) {
        try {
            var decoded = Buffer.from(part + padding, 'base64').toString();
            if (decoded.length > 0 && /^[\x20-\x7E]*$/.test(decoded)) {
                console.log(`${part}${padding} -> ${decoded}`);
            }
        } catch(e) {}
    }
});

// Try the full base64 string I saw in the original 
var full_parts = ['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW'];
var fullb64 = full_parts.join('');
console.log('\n=== Full b64 parts ===');
console.log(fullb64);
try {
    console.log('Decoded:', Buffer.from(fullb64, 'base64').toString());
} catch(e) {
    console.log('Error:', e.message);
}
