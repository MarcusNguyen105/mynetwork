// Let's extract the exact construction of hash1, hash2, and instruction
// From the obfuscated code, I can see they are built using _0x34b85e function calls

// I need to map the obfuscated function calls to the actual strings
// Let me extract the key parts from the obfuscated arrays

// From _0x4a39 array, I can extract these strings (reversed):
var obfuscatedStrings = [
    'eulav eht ',      // " the value"
    'table',
    '70390zHMDsK',
    'object',
    '966028jCWdrH', 
    'function',
    'log',
    '5YARiXg',
    'Yzk1ZWU0Nz',      // base64: c95ee47
    '45JEiLUC',
    'YzcwYzNlYj',      // base64: c70c3eb  
    '6631656436',      // hex: f1ed6
    '863256EtMoYk',
    'push',
    '6589810GTlrab',
    'apply',
    '882245NXpbDV',
    '43312yxCGot',
    '4373736qzQvCI',
    'toString',
    'warn',
    '6232',             // hex: b2
    '8796768UCpcfR',
    'length',
    'parw dna ,',       // ", and wrap"
    '3961373433',       // hex: 9a743
    '3361326434',       // hex: 3a2d4
    '11CsMkkl',
    'exception',
    'NzcyMmM2OW',       // base64: 7722c69
    '3463383330',       // hex: 4c830
    '31508QVFcbD',
    'error',
    'undefined',
    '({...}CCSU',
    'alf dradna',       // "andard fla"
    'ts eht ni ',       // " in the st"
    'Y4OWEwYWFl',       // base64 (corrupted)
    'c ,sehsah ',       // " hashes, c"
    '40556232pbALNU',
    '736888mBECaR',
    'shift',
    'bind',
    'k1MDI0NDY1',       // base64 (corrupted)
    '__proto__',
    'rehtegot s',       // "s together"
    '29ekpzDq',
    'info',
    '854YoyEjg',
    '66nVBDrR',
    'console',
    '6134353334'        // hex: a4534
];

// Now let me try to reconstruct the hash values in the correct order
// Looking at the original code structure, hash1 and hash2 seem to be built from specific indices

console.log("Extracting hash components:");

// Base64 strings that decode to hex:
var base64Hashes = ['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW'];
var hexFromBase64 = base64Hashes.map(b64 => {
    try {
        return Buffer.from(b64, 'base64').toString('utf8');
    } catch (e) {
        return null;
    }
}).filter(x => x);

console.log("Hex from base64:", hexFromBase64);

// Direct hex strings:
var directHex = ['6631656436', '6232', '3961373433', '3361326434', '3463383330', '6134353334'];
var hexFromHex = directHex.map(hex => {
    var result = '';
    for (var i = 0; i < hex.length; i += 2) {
        result += String.fromCharCode(parseInt(hex.substring(i, i + 2), 16));
    }
    return result;
});

console.log("Decoded hex strings:", hexFromHex);

// Let's try to construct the flag by combining these in different orders
console.log("\nTrying different flag constructions:");

// Method 1: All base64-decoded hex values first, then direct hex
var flag1 = hexFromBase64.join('') + hexFromHex.join('');
console.log("Method 1: USCC{" + flag1 + "}");

// Method 2: Interleaved based on appearance order in the array
var allHexValues = [...hexFromBase64, ...hexFromHex];
var flag2 = allHexValues.join('');
console.log("Method 2: USCC{" + flag2 + "}");

// Method 3: Just the base64 decoded values
var flag3 = hexFromBase64.join('');
console.log("Method 3: USCC{" + flag3 + "}");

// Let me also check if any of these look like valid MD5/SHA hashes
console.log("\nHash lengths:");
console.log("Flag1 length:", flag1.length);
console.log("Flag2 length:", flag2.length);
console.log("Flag3 length:", flag3.length);