// Let me try to execute the obfuscated JavaScript to see what the actual values are
// I'll recreate the deobfuscation functions based on the pattern I see

// From the obfuscated code, I can see the pattern of the deobfuscation
// Let me try to manually trace through it

// The _0x4a39 array contains the strings, and the functions use indices to access them
// Let me extract the key strings and try to map them correctly

var obfuscatedArray = [
    'eulav\x20eht\x20',  // 0
    'table',             // 1
    '70390zHMDsK',       // 2
    'object',            // 3
    '966028jCWdrH',      // 4
    'function',          // 5
    'log',               // 6
    '5YARiXg',           // 7
    'Yzk1ZWU0Nz',        // 8
    '45JEiLUC',          // 9
    'YzcwYzNlYj',        // 10
    '6631656436',        // 11
    '863256EtMoYk',      // 12
    'push',              // 13
    '6589810GTlrab',     // 14
    'apply',             // 15
    '882245NXpbDV',      // 16
    '43312yxCGot',       // 17
    '4373736qzQvCI',     // 18
    'toString',          // 19
    'warn',              // 20
    '6232',              // 21
    '8796768UCpcfR',     // 22
    'length',            // 23
    'parw\x20dna\x20,',  // 24
    '3961373433',        // 25
    '3361326434',        // 26
    '11CsMkkl',          // 27
    'exception',         // 28
    'NzcyMmM2OW',        // 29
    '3463383330',        // 30
    '31508QVFcbD',       // 31
    'error',             // 32
    'undefined',         // 33
    '({...}CCSU',        // 34
    'alf\x20dradna',     // 35
    'ts\x20eht\x20ni\x20', // 36
    'Y4OWEwYWFl',        // 37
    'c\x20,sehsah\x20',  // 38
    '40556232pbALNU',    // 39
    '736888mBECaR',      // 40
    'shift',             // 41
    'bind',              // 42
    'k1MDI0NDY1',        // 43
    '__proto__',         // 44
    'rehtegot\x20s',     // 45
    '29ekpzDq',          // 46
    'info',              // 47
    '854YoyEjg',         // 48
    '66nVBDrR',          // 49
    'console',           // 50
    '6134353334'         // 51
];

// Now let me try to figure out what indices are used for hash1, hash2, instruction
// From the pattern, it looks like the function subtracts some offset from the index

console.log("Trying to decode the actual hash values...");

// Let me check what the base64 and hex strings actually contain
console.log("\nBase64 strings:");
['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW', 'Y4OWEwYWFl', 'k1MDI0NDY1'].forEach((b64, i) => {
    try {
        var decoded = Buffer.from(b64, 'base64').toString('utf8');
        console.log(`${b64} -> ${decoded}`);
    } catch (e) {
        console.log(`${b64} -> Error: ${e.message}`);
    }
});

console.log("\nHex strings:");
['6631656436', '6232', '3961373433', '3361326434', '3463383330', '40556232', '6134353334'].forEach((hex, i) => {
    try {
        var decoded = '';
        for (var j = 0; j < hex.length; j += 2) {
            decoded += String.fromCharCode(parseInt(hex.substring(j, j + 2), 16));
        }
        console.log(`${hex} -> ${decoded}`);
    } catch (e) {
        console.log(`${hex} -> Error: ${e.message}`);
    }
});

// Maybe the flag is actually in the console output when the page loads?
// Or maybe I need to look at the instruction variable more carefully

console.log("\nLet me try the simpler flag formats:");
console.log("USCC{c95ee47c70c3eb7722c69}");
console.log("USCC{7722c69c70c3ebc95ee47}");

// Maybe the flag is just the concatenation of the three base64-decoded values
var flag = "c95ee47" + "c70c3eb" + "7722c69";
console.log("Simple concatenation: USCC{" + flag + "}");

// Or maybe in reverse order
var flagReverse = "7722c69" + "c70c3eb" + "c95ee47";
console.log("Reverse order: USCC{" + flagReverse + "}");