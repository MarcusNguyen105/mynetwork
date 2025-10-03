// Let me manually decode each base64 part and check if it's clean hex

var b64_candidates = [
    'Yzk1ZWU0Nz',    // from arr[27]
    'YzcwYzNlYj',    // from arr[10] in original
    'NzcyMmM2OW',    // from arr[28] in original  
    'Y4OWEwYWFl',    // from arr[36]
    'k1MDI0NDY1',    // from arr[41]
];

console.log('=== Checking each base64 string ===');
var clean_hex_parts = [];

b64_candidates.forEach((b64, idx) => {
    try {
        var decoded = Buffer.from(b64, 'base64').toString('utf8');
        var is_hex = /^[a-f0-9]+$/i.test(decoded);
        console.log(`[${idx}] ${b64}`);
        console.log(`  -> "${decoded}"`);
        console.log(`  -> Is hex: ${is_hex}`);
        
        if (is_hex) {
            clean_hex_parts.push(decoded);
        }
    } catch(e) {
        console.log(`[${idx}] ${b64} -> ERROR`);
    }
});

console.log('\n=== Clean hex parts ===');
clean_hex_parts.forEach((hex, idx) => {
    console.log(`[${idx}] ${hex} (length: ${hex.length})`);
});

var combined = clean_hex_parts.join('');
console.log(`\nCombined: ${combined}`);
console.log(`Length: ${combined.length} (MD5 should be 32)`);

// Check if we need more parts from the numeric strings
// Let me look at "3463383330" which appears in instruction
var extra_candidates = [
    '3463383330',  // 4c830
    '6134353334',  // a4534  
    '6161343030',  // aa400
    '6232',        // b2
    '863256',      // from instruction
];

console.log('\n=== Extra numeric candidates ===');
extra_candidates.forEach(hex => {
    var ascii = '';
    var is_valid = hex.length % 2 === 0;
    if (is_valid) {
        for (var i = 0; i < hex.length; i += 2) {
            ascii += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
        }
        var is_hex = /^[a-f0-9]+$/i.test(ascii);
        console.log(`${hex} -> "${ascii}" (is hex: ${is_hex})`);
        if (is_hex) {
            clean_hex_parts.push(ascii);
        }
    }
});

// Try building a 32-character hash
console.log('\n=== Attempting to build MD5 hash ===');
var all_clean = [];
['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW'].forEach(b64 => {
    all_clean.push(Buffer.from(b64, 'base64').toString());
});

// Add numeric parts that decode to hex
['3463383330', '6134353334'].forEach(hex => {
    var ascii = '';
    for (var i = 0; i < hex.length; i += 2) {
        ascii += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    }
    all_clean.push(ascii);
});

var final_hash = all_clean.join('');
console.log(`Hash: ${final_hash}`);
console.log(`Length: ${final_hash.length}`);

// If it's still not 32, try different combinations
if (final_hash.length !== 32) {
    console.log('\n=== Trying to get exactly 32 characters ===');
    // Maybe I need to add more parts or trim
    var trimmed = final_hash.substring(0, 32);
    console.log(`Trimmed to 32: ${trimmed}`);
    
    // Or maybe combine differently
    var alt = 'c95ee47' + 'c70c3eb' + '7722c69' + '4c830' + 'a4534';
    console.log(`Alternative: ${alt} (length: ${alt.length})`);
}

// The flag format is probably USCC{...}
console.log('\n=== Checking if flag might be USCC{hash} ===');
console.log(`USCC{${final_hash}}`);
