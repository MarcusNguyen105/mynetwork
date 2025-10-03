// From the traced arrays, I have these clean values:

// Pure numeric strings (likely hex):
var numeric_parts = [
    '6134353334',  // hash1
    '6161343030',  // hash1
    '6232',        // hash2
    '3463383330',  // instruction
];

// Base64 strings:
var b64_parts = [
    'Yzk1ZWU0Nz',    // instruction, arr[27]
    'NzcyMmM2OW',    // instruction, arr[4]
    'IxZg',          // instruction, arr[8] (without ==)
];

// Let me also check what's in the original _0x4a39 array
var base64_from_4a39 = [
    'Yzk1ZWU0Nz',    // index 8
    'YzcwYzNlYj',    // index 10
    'NzcyMmM2OW',    // index 28
    'Y4OWEwYWFl',    // index 36
    'k1MDI0NDY1',    // index 41
];

console.log('=== Numeric parts as hex ===');
numeric_parts.forEach(hex => {
    var ascii = '';
    for (var i = 0; i < hex.length; i += 2) {
        ascii += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    }
    console.log(`${hex} -> "${ascii}"`);
});

console.log('\n=== Base64 parts decoded ===');
base64_from_4a39.forEach(b64 => {
    try {
        var decoded = Buffer.from(b64, 'base64').toString();
        console.log(`${b64} -> ${decoded}`);
    } catch(e) {
        console.log(`${b64} -> ERROR: ${e.message}`);
    }
});

// Combine base64 parts and decode
console.log('\n=== Trying different combinations ===');

// All base64 from _0x4a39 combined
var full_b64 = base64_from_4a39.join('');
try {
    var decoded = Buffer.from(full_b64, 'base64').toString();
    console.log(`All b64 combined: ${decoded}`);
    
    // This might be a hash - let's see if it's hex
    if (/^[a-f0-9]+$/i.test(decoded)) {
        console.log('  -> This looks like a hex string!');
        console.log(`  -> Length: ${decoded.length} characters`);
    }
} catch(e) {
    console.log('Failed to combine');
}

// Try first 3 base64 parts (these seem cleaner)
var clean_b64 = [base64_from_4a39[0], base64_from_4a39[1], base64_from_4a39[2]].join('');
try {
    var decoded = Buffer.from(clean_b64, 'base64').toString();
    console.log(`\nFirst 3 b64 parts: ${decoded}`);
    if (/^[a-f0-9]+$/i.test(decoded)) {
        console.log('  -> This is a hex string!');
        console.log(`  -> Length: ${decoded.length} characters`);
    }
} catch(e) {}

// The instruction mentions "shift" - maybe I need to unshift/reverse the base64?
console.log('\n=== Trying reversed order ===');
var reversed_b64 = base64_from_4a39.slice().reverse().join('');
try {
    var decoded = Buffer.from(reversed_b64, 'base64').toString();
    console.log(`Reversed b64: ${decoded}`);
} catch(e) {}

// Build complete hash from instruction
// "crack the" suggests this is a hash to crack
// Looking at the format, maybe combine specific parts
var potential_hash_parts = [
    'Yzk1ZWU0Nz',   // c95ee47
    'YzcwYzNlYj',   // c70c3eb  
    'NzcyMmM2OW',   // 7722c69
];

var hash_candidate = '';
potential_hash_parts.forEach(part => {
    hash_candidate += Buffer.from(part, 'base64').toString();
});
console.log(`\n=== Potential hash ===`);
console.log(hash_candidate);
console.log(`Format: Looks like MD5 (hex string, length: ${hash_candidate.length})`);

// Check if we need to add more parts
console.log('\n=== Looking for more hex parts in numeric strings ===');
var all_numeric = ['6134353334', '6161343030', '6232', '3463383330', '863256'];
var combined_hex = '';
all_numeric.forEach(hex => {
    for (var i = 0; i < hex.length; i += 2) {
        combined_hex += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    }
});
console.log(`Numeric parts decoded: ${combined_hex}`);

// Maybe the hash is: base64 decoded parts + numeric decoded parts
var complete_hash = hash_candidate + combined_hex;
console.log(`\nComplete hash candidate: ${complete_hash}`);
console.log(`Length: ${complete_hash.length}`);
