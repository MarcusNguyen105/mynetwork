// Let me try to manually deobfuscate the exact construction of hash1, hash2, instruction
// by tracing through the obfuscation functions

// From the code:
// hash1=_0x34b85e(0x1f3)+_0x34b85e(0x1fa)+_0x34b85e(0x1e2)+_0x34b85e(0x1f5)+_0x34b85e(0x1ed)+_0x34b85e(0x1f9)+_0x34b85e(0x1f8)
// hash2=_0x34b85e(0x1fe)+_0x34b85e(0x1f7)+_0x34b85e(0x1f1)+_0x34b85e(0x1e7)+_0x34b85e(0x1e9)+_0x34b85e(0x1e6)
// instruction=_0x34b85e(0x1e3)+_0x34b85e(0x1e1)+_0x34b85e(0x1e5)+_0x34b85e(0x1e4)+_0x34b85e(0x1ee)+_0x34b85e(0x1ef)+_0x34b85e(0x1ff)+_0x34b85e(0x1fb)+_0x34b85e(0x1ea)+_0x34b85e(0x1e8)

// The _0x34b85e function is _0x4deb, which accesses _0x32e5() array
// _0x32e5 returns _0x5b28f4 array which is built from _0x3476 calls to _0x4a39 array

// Let me try to map this out step by step
// The indices like 0x1f3 are hex numbers that get converted

console.log("Converting hex indices to decimal:");
var indices = [
    0x1f3, 0x1fa, 0x1e2, 0x1f5, 0x1ed, 0x1f9, 0x1f8,  // hash1
    0x1fe, 0x1f7, 0x1f1, 0x1e7, 0x1e9, 0x1e6,         // hash2
    0x1e3, 0x1e1, 0x1e5, 0x1e4, 0x1ee, 0x1ef, 0x1ff, 0x1fb, 0x1ea, 0x1e8  // instruction
];

indices.forEach((hex, i) => {
    console.log(`0x${hex.toString(16)} = ${hex}`);
});

// From the _0x4deb function, I can see it subtracts an offset: _0x11db13-(0x9b*0x15+-0x17a6+0xccf)
// Let me calculate that offset
var offset = (0x9b * 0x15 - 0x17a6 + 0xccf);
console.log("Calculated offset:", offset);

// So the actual indices would be the hex values minus this offset
console.log("\nActual array indices after offset:");
indices.forEach((hex, i) => {
    var actualIndex = hex - offset;
    console.log(`${hex} - ${offset} = ${actualIndex}`);
});

// But this is getting very complex. Let me try a simpler approach.
// Maybe I should look for the flag in the browser's developer console

// Or maybe the flag is actually constructed from simpler patterns
// Let me check if there are any obvious flag patterns I missed

// Maybe the flag is just the concatenation of specific strings
// Let me look at the strings that contain numbers or hex-like patterns

var potentialFlagParts = [
    'c95ee47',    // from base64
    'c70c3eb',    // from base64
    '7722c69',    // from base64
    'f1ed6',      // from hex
    'b2',         // from hex
    '9a743',      // from hex
    '3a2d4',      // from hex
    '4c830',      // from hex
    'a4534',      // from hex
    'aa400'       // from hex
];

console.log("\nTrying more flag combinations:");
// Maybe it's not all of them, but a specific subset
console.log("USCC{" + potentialFlagParts.slice(0, 6).join('') + "}");
console.log("USCC{" + potentialFlagParts.slice(3).join('') + "}");

// Maybe with separators
console.log("USCC{" + potentialFlagParts.slice(0, 3).join('-') + "}");
console.log("USCC{" + potentialFlagParts.slice(0, 3).join('_') + "}");

// Maybe it's a different format entirely
console.log("USCC{" + potentialFlagParts[0] + potentialFlagParts[1] + potentialFlagParts[2] + "}");

console.log("\nMaybe I need to check what actually gets executed when the page loads...");