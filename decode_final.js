// Let me extract the strings more systematically
// From the obfuscated code, I can see the string arrays

// Looking at the _0x4a39 function array (reversed and with some processing)
const strings_4a39 = [
    'eulav eht ', 'table', '70390zHMDsK', 'object', '966028jCWdrH', 'function', 'log', '5YARiXg',
    'Yzk1ZWU0Nz', '45JEiLUC', 'YzcwYzNlYj', '6631656436', '863256EtMoYk', 'push', '6589810GTlrab',
    'apply', '882245NXpbDV', '43312yxCGot', '4373736qzQvCI', 'toString', 'warn', '6232',
    '8796768UCpcfR', 'length', 'parw dna ,', '3961373433', '3361326434', '11CsMkkl', 'exception',
    'NzcyMmM2OW', '3463383330', '31508QVFcbD', 'error', 'undefined', '({...}CCSU', 'alf dradna',
    'ts eht ni ', 'Y4OWEwYWFl', 'c ,sehsah ', '40556232pbALNU', '736888mBECaR', 'shift', 'bind',
    'k1MDI0NDY1', '__proto__', 'rehtegot s', '29ekpzDq', 'info', '854YoyEjg', '66nVBDrR', 'console',
    '6134353334'
];

// And the _0x32e5 function array
const strings_32e5 = [
    '6134353334', '40556232', 'Y4OWEwYWFl', ') tamrof g', '6232', 'NzcyMmM2OW', 'k1MDI0NDY1',
    'YzcwYzNlYj', 'IxZg==', '3463383330', 'eht kcarc', 'alf dradna', '3361326434', '9VFwNrg',
    '6631656436', 'ts eht ni ', 'Yzk1ZWU0Nz', '3961373433', 'c ,sehsah ', '287AWNVHd',
    '6161343030', 'rehtegot s', 'parw dna ,', 'eulav eht ', 'etanetacno', '({...}CCSU',
    '178842lPRJmm', '1392482zqhnOI'
];

// The key insight is that these are hex-encoded strings that should be decoded directly
// Let me try to find the pattern for hash1, hash2, and instruction

// From the original code structure, let me map the indices:
// hash1 uses indices: 0x1f3, 0x1fa, 0x1e2, 0x1f5, 0x1ed, 0x1f9, 0x1f8
// hash2 uses indices: 0x1fe, 0x1f7, 0x1f1, 0x1e7, 0x1e9, 0x1e6
// instruction uses indices: 0x1e3, 0x1e1, 0x1e5, 0x1e4, 0x1ee, 0x1ef, 0x1ff, 0x1fb, 0x1ea, 0x1e8

// Converting hex indices to decimal:
console.log("Hash1 indices (decimal):", [0x1f3, 0x1fa, 0x1e2, 0x1f5, 0x1ed, 0x1f9, 0x1f8]);
console.log("Hash2 indices (decimal):", [0x1fe, 0x1f7, 0x1f1, 0x1e7, 0x1e9, 0x1e6]);
console.log("Instruction indices (decimal):", [0x1e3, 0x1e1, 0x1e5, 0x1e4, 0x1ee, 0x1ef, 0x1ff, 0x1fb, 0x1ea, 0x1e8]);

// These indices are way too high for the arrays I extracted. Let me look at this differently.
// The obfuscated code has multiple layers. Let me try to find the actual strings by looking for hex patterns.

// I notice these hex strings that look like they could be parts of a hash:
const potential_hash_parts = [
    '6631656436', '6232', '3961373433', '3361326434', '3463383330', '6134353334', '40556232'
];

console.log("\n=== Decoding potential hash parts ===");
potential_hash_parts.forEach(part => {
    let decoded = '';
    for (let i = 0; i < part.length; i += 2) {
        decoded += String.fromCharCode(parseInt(part.substring(i, i + 2), 16));
    }
    console.log(`${part} -> ${decoded}`);
});

// And these base64-looking strings:
const potential_b64_parts = [
    'Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW', 'k1MDI0NDY1', 'Y4OWEwYWFl'
];

console.log("\n=== Decoding potential base64 parts ===");
potential_b64_parts.forEach(part => {
    try {
        let decoded = Buffer.from(part, 'base64').toString('ascii');
        console.log(`${part} -> ${decoded}`);
    } catch (e) {
        console.log(`${part} -> failed to decode`);
    }
});

// Let me try a different approach - maybe these are MD5 hashes or similar
// Let me concatenate the hex parts in order:
const hex_parts_ordered = ['6631656436', '3361326434', '3961373433', '3463383330', '6232', '40556232', '6134353334'];
const hex_concat = hex_parts_ordered.join('');
console.log(`\nConcatenated hex: ${hex_concat}`);

// And the base64 parts:
const b64_parts_ordered = ['YzcwYzNlYj', 'Yzk1ZWU0Nz', 'NzcyMmM2OW', 'k1MDI0NDY1', 'Y4OWEwYWFl'];
const b64_concat = b64_parts_ordered.map(part => {
    try {
        return Buffer.from(part, 'base64').toString('ascii');
    } catch (e) {
        return part;
    }
}).join('');
console.log(`Concatenated base64 decoded: ${b64_concat}`);

// Try the flag with just hex parts
console.log(`\nPossible flag 1: USCC{${hex_concat}}`);
console.log(`Possible flag 2: USCC{${hex_concat}${b64_concat}}`);
console.log(`Possible flag 3: USCC{${b64_concat}${hex_concat}}`);