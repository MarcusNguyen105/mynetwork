// Let me re-examine the obfuscated code more carefully
// Maybe I missed something or the order is different

// From the original admin panel code, let me trace the exact construction
// The variables were: hash1, hash2, instruction

// Let me look at the _0x32e5 function array more carefully
// and map the exact indices used in the construction

// From the obfuscated code:
// hash1=_0x34b85e(0x1f3)+_0x34b85e(0x1fa)+_0x34b85e(0x1e2)+_0x34b85e(0x1f5)+_0x34b85e(0x1ed)+_0x34b85e(0x1f9)+_0x34b85e(0x1f8)
// hash2=_0x34b85e(0x1fe)+_0x34b85e(0x1f7)+_0x34b85e(0x1f1)+_0x34b85e(0x1e7)+_0x34b85e(0x1e9)+_0x34b85e(0x1e6)
// instruction=_0x34b85e(0x1e3)+_0x34b85e(0x1e1)+_0x34b85e(0x1e5)+_0x34b85e(0x1e4)+_0x34b85e(0x1ee)+_0x34b85e(0x1ef)+_0x34b85e(0x1ff)+_0x34b85e(0x1fb)+_0x34b85e(0x1ea)+_0x34b85e(0x1e8)

// I need to be more systematic about this
// Let me try to extract the exact strings in the exact order

console.log("Let me try a different approach...");

// Maybe the flag is simpler and I'm overcomplicating it
// Let me check if there are other common flag formats or if I missed something obvious

// Common CTF flag formats:
var possibleFlags = [
    // Just the base64 decoded parts
    "USCC{c95ee47c70c3eb7722c69}",
    
    // Different ordering
    "USCC{7722c69c70c3ebc95ee47}",
    
    // Maybe it's not hex at all, let me check if the base64 strings decode to something else
];

console.log("Checking alternative flag formats:");
possibleFlags.forEach((flag, i) => {
    console.log(`${i + 1}: ${flag}`);
});

// Let me also check if I need to look at the "instruction" variable
// Maybe that contains the actual flag or clues about how to construct it

// Let me also double-check my base64 decoding
var base64Strings = ['Yzk1ZWU0Nz', 'YzcwYzNlYj', 'NzcyMmM2OW'];
console.log("\nDouble-checking base64 decoding:");
base64Strings.forEach((b64, i) => {
    var decoded = Buffer.from(b64, 'base64').toString('utf8');
    console.log(`${i}: ${b64} -> ${decoded}`);
    
    // Maybe these aren't hex values but actual text?
    console.log(`   As text: ${decoded}`);
});

// Let me also check if there are any other patterns I missed
// Maybe the flag is constructed from the reversed strings?
var reversedParts = [
    'eulav eht ',     // " the value"
    'parw dna ,',     // ", and wrap"  
    'ts eht ni ',     // " in the st"
    'c ,sehsah ',     // " hashes, c"
    'rehtegot s',     // "s together"
    'alf dradna',     // "andard fla"
    'eht kcarc'       // "crack the"
];

var message = reversedParts.map(s => s.split('').reverse().join('')).join('');
console.log("\nReconstructed message:", message);

// Maybe I need to look for the flag in a different place entirely
console.log("\nMaybe I should check if there are other endpoints or hidden content...");