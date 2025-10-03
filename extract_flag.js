// Extract clean parts from the obfuscated strings

// From the deobfuscation, I have these values
var hash1_parts = [
    '6134353334',  // from hash1
    '6161343030'   // from hash1
];

var hash2_parts = [
    '6232',        // from hash2
    '6589810'      // possibly junk
];

// Extract numeric sequences from hash1 and hash2
var hash1_raw = '736888mBECaR613435333445JEiLUC61613430309VFwNrgapply__proto__';
var hash2_raw = '178842lPRJmmobjectlengthpush62326589810GTlrab';

console.log('Looking for patterns in hash1:', hash1_raw);
console.log('Looking for patterns in hash2:', hash2_raw);

// Extract continuous digit sequences
var digits_hash1 = hash1_raw.match(/\d+/g);
var digits_hash2 = hash2_raw.match(/\d+/g);

console.log('\nDigit sequences in hash1:', digits_hash1);
console.log('Digit sequences in hash2:', digits_hash2);

// Try to decode as hex to ASCII
console.log('\n--- Trying hex to ASCII decoding ---');
digits_hash1.forEach((hex, i) => {
    try {
        var result = '';
        for (var j = 0; j < hex.length; j += 2) {
            result += String.fromCharCode(parseInt(hex.substr(j, 2), 16));
        }
        console.log(`hash1[${i}] (${hex}):`, result);
    } catch(e) {}
});

digits_hash2.forEach((hex, i) => {
    try {
        var result = '';
        for (var j = 0; j < hex.length; j += 2) {
            result += String.fromCharCode(parseInt(hex.substr(j, 2), 16));
        }
        console.log(`hash2[${i}] (${hex}):`, result);
    } catch(e) {}
});

// Combine all digits and try decoding
var all_digits = digits_hash1.join('') + digits_hash2.join('');
console.log('\nAll digits combined:', all_digits);

// Try as hex
var hex_decoded = '';
for (var i = 0; i < all_digits.length; i += 2) {
    hex_decoded += String.fromCharCode(parseInt(all_digits.substr(i, 2), 16));
}
console.log('Hex decoded:', hex_decoded);

// Try base64 decode
try {
    console.log('Base64 decoded:', Buffer.from(hex_decoded, 'base64').toString());
} catch(e) {
    console.log('Base64 failed');
}
