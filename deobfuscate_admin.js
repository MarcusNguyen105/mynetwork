// Let's deobfuscate the administrator panel JavaScript
// Looking at the end of the script, there are three variables: hash1, hash2, and instruction

// From the obfuscated code, I can see these are built from function calls to _0x34b85e
// Let me extract the key strings and decode them

// The _0x32e5 function contains the string array, and _0x4a39 contains another array
// Let me manually extract the base64-looking strings and reverse the obfuscation

// From the code, I can see these patterns:
var hash1_parts = [
    '6631656436',  // _0x34b85e(0x1f3)
    'YzcwYzNlYj',  // _0x34b85e(0x1fa) 
    '3361326434',  // _0x34b85e(0x1e2)
    '3961373433',  // _0x34b85e(0x1f5)
    '3463383330',  // _0x34b85e(0x1ed)
    'Yzk1ZWU0Nz',  // _0x34b85e(0x1f9)
    'YzcwYzNlYj'   // _0x34b85e(0x1f8)
];

var hash2_parts = [
    'NzcyMmM2OW',  // _0x34b85e(0x1fe)
    'YzcwYzNlYj',  // _0x34b85e(0x1f7)
    'k1MDI0NDY1',  // _0x34b85e(0x1f1)
    '6232',        // _0x34b85e(0x1e7)
    'Y4OWEwYWFl',  // _0x34b85e(0x1e9)
    '40556232'     // _0x34b85e(0x1e6)
];

// The instruction parts are reversed strings, let me decode them
var instruction_parts = [
    'eulav eht ',   // "the value" reversed
    'parw dna ,',   // ", and wrap" reversed  
    'alf dradna',   // "andard fla" reversed
    'ts eht ni ',   // " in the st" reversed
    'etanetacno',   // "oncatenate" reversed
    'c ,sehsah ',   // " hashes, c" reversed
    'rehtegot s',   // "s together" reversed
    'k crack the',  // seems like "crack the k" or similar
    '({...}CCSU',   // "USCC{...})" reversed or similar
    'g format)'     // "(format g" reversed
];

console.log("Hash1 parts:", hash1_parts);
console.log("Hash2 parts:", hash2_parts);

// Let me try to decode these - some look like hex, some like base64
function tryDecode(str) {
    console.log(`Trying to decode: ${str}`);
    
    // Try hex decode
    try {
        let hexDecoded = '';
        for (let i = 0; i < str.length; i += 2) {
            hexDecoded += String.fromCharCode(parseInt(str.substring(i, i + 2), 16));
        }
        console.log(`  Hex decoded: ${hexDecoded}`);
    } catch (e) {
        console.log(`  Hex decode failed`);
    }
    
    // Try base64 decode
    try {
        let base64Decoded = Buffer.from(str, 'base64').toString('ascii');
        console.log(`  Base64 decoded: ${base64Decoded}`);
    } catch (e) {
        console.log(`  Base64 decode failed`);
    }
}

console.log("\n=== Decoding Hash1 Parts ===");
hash1_parts.forEach(tryDecode);

console.log("\n=== Decoding Hash2 Parts ===");
hash2_parts.forEach(tryDecode);

// Let's also reverse the instruction parts
console.log("\n=== Instruction Parts Reversed ===");
instruction_parts.forEach(part => {
    console.log(`"${part}" reversed: "${part.split('').reverse().join('')}"`);
});

// Now let's construct the full hashes and instruction
console.log("\n=== Constructing Full Values ===");

// Hash1: concatenate the base64 decoded parts
let hash1_decoded = hash1_parts.map(part => {
    try {
        if (/^[0-9a-fA-F]+$/.test(part)) {
            // It's hex
            let result = '';
            for (let i = 0; i < part.length; i += 2) {
                result += String.fromCharCode(parseInt(part.substring(i, i + 2), 16));
            }
            return result;
        } else {
            // It's base64
            return Buffer.from(part, 'base64').toString('ascii');
        }
    } catch (e) {
        return part;
    }
}).join('');

let hash2_decoded = hash2_parts.map(part => {
    try {
        if (/^[0-9a-fA-F]+$/.test(part)) {
            // It's hex
            let result = '';
            for (let i = 0; i < part.length; i += 2) {
                result += String.fromCharCode(parseInt(part.substring(i, i + 2), 16));
            }
            return result;
        } else {
            // It's base64
            return Buffer.from(part, 'base64').toString('ascii');
        }
    } catch (e) {
        return part;
    }
}).join('');

console.log(`Hash1 decoded: ${hash1_decoded}`);
console.log(`Hash2 decoded: ${hash2_decoded}`);

// Construct the instruction
let full_instruction = instruction_parts.map(part => part.split('').reverse().join('')).join('');
console.log(`Full instruction: ${full_instruction}`);

// The instruction seems to be telling us to concatenate the hashes and wrap in USCC{} format
console.log(`\nFinal flag: USCC{${hash1_decoded}${hash2_decoded}}`);