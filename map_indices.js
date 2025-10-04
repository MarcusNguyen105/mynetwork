// Now I have the actual indices, let me map them to the strings
// The _0x32e5 array is built from _0x3476 calls, which access the _0x4a39 array

// From the code, I can see the _0x32e5 array construction:
var _0x32e5Array = [
    // These are built from _0x5a1ae8 calls (which is _0x3476) to _0x4a39 array
    // Plus some literal strings
    
    // Let me reconstruct this array based on the pattern I see
    // Index 0: _0x5a1ae8(0x16c)
    // Index 1: _0x5a1ae8(0x164) 
    // etc.
    
    // But this is getting very complex. Let me try a different approach.
    // Maybe I should just try to execute the JavaScript and see what gets logged
];

// Let me try the indices I calculated and see what they might map to
var hash1Indices = [19, 26, 2, 21, 13, 25, 24];
var hash2Indices = [30, 23, 17, 7, 9, 6];
var instructionIndices = [3, 1, 5, 4, 14, 15, 31, 27, 10, 8];

console.log("Hash1 indices:", hash1Indices);
console.log("Hash2 indices:", hash2Indices);
console.log("Instruction indices:", instructionIndices);

// Let me try to map these to the known strings from the _0x4a39 array
var _0x4a39Array = [
    'eulav\x20eht\x20',      // 0
    'table',                 // 1
    '70390zHMDsK',           // 2
    'object',                // 3
    '966028jCWdrH',          // 4
    'function',              // 5
    'log',                   // 6
    '5YARiXg',               // 7
    'Yzk1ZWU0Nz',            // 8
    '45JEiLUC',              // 9
    'YzcwYzNlYj',            // 10
    '6631656436',            // 11
    '863256EtMoYk',          // 12
    'push',                  // 13
    '6589810GTlrab',         // 14
    'apply',                 // 15
    '882245NXpbDV',          // 16
    '43312yxCGot',           // 17
    '4373736qzQvCI',         // 18
    'toString',              // 19
    'warn',                  // 20
    '6232',                  // 21
    '8796768UCpcfR',         // 22
    'length',                // 23
    'parw\x20dna\x20,',      // 24
    '3961373433',            // 25
    '3361326434',            // 26
    '11CsMkkl',              // 27
    'exception',             // 28
    'NzcyMmM2OW',            // 29
    '3463383330',            // 30
    '31508QVFcbD',           // 31
    'error',                 // 32
    'undefined',             // 33
    '({...}CCSU',            // 34
    'alf\x20dradna',         // 35
    'ts\x20eht\x20ni\x20',   // 36
    'Y4OWEwYWFl',            // 37
    'c\x20,sehsah\x20',      // 38
    '40556232pbALNU',        // 39
    '736888mBECaR',          // 40
    'shift',                 // 41
    'bind',                  // 42
    'k1MDI0NDY1',            // 43
    '__proto__',             // 44
    'rehtegot\x20s',         // 45
    '29ekpzDq',              // 46
    'info',                  // 47
    '854YoyEjg',             // 48
    '66nVBDrR',              // 49
    'console',               // 50
    '6134353334'             // 51
];

console.log("\nMapping hash1 indices to strings:");
var hash1Parts = hash1Indices.map(i => {
    if (i < _0x4a39Array.length) {
        console.log(`Index ${i}: ${_0x4a39Array[i]}`);
        return _0x4a39Array[i];
    }
    return '';
});

console.log("\nMapping hash2 indices to strings:");
var hash2Parts = hash2Indices.map(i => {
    if (i < _0x4a39Array.length) {
        console.log(`Index ${i}: ${_0x4a39Array[i]}`);
        return _0x4a39Array[i];
    }
    return '';
});

console.log("\nMapping instruction indices to strings:");
var instructionParts = instructionIndices.map(i => {
    if (i < _0x4a39Array.length) {
        console.log(`Index ${i}: ${_0x4a39Array[i]}`);
        return _0x4a39Array[i];
    }
    return '';
});

console.log("\nReconstructed values:");
console.log("hash1:", hash1Parts.join(''));
console.log("hash2:", hash2Parts.join(''));
console.log("instruction:", instructionParts.join(''));

// Maybe the flag is the combination of these
console.log("\nPossible flags:");
console.log("USCC{" + hash1Parts.join('') + hash2Parts.join('') + "}");
console.log("USCC{" + hash1Parts.join('') + "}");
console.log("USCC{" + hash2Parts.join('') + "}");