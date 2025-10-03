// Let me trace which exact values are used from the arrays

// From trace_indices.js, I know:
// hash1 uses indices: 0x1f3, 0x1fa, 0x1e2, 0x1f5, 0x1ed, 0x1f9, 0x1f8
// which map to arr[19], arr[26], arr[2], arr[21], arr[13], arr[25], arr[24]

// arr[19] = 736888mBECaR
// arr[26] = 6134353334  -> a4534
// arr[2] = 45JEiLUC  
// arr[21] = 6161343030  -> aa400
// arr[13] = 9VFwNrg
// arr[25] = apply
// arr[24] = __proto__

// hash2 uses: arr[30], arr[23], arr[17], arr[7], arr[9], arr[6]
// arr[30] = 178842lPRJmm
// arr[23] = object
// arr[17] = length
// arr[7] = push
// arr[9] = 6232  -> b2
// arr[6] = 6589810GTlrab

console.log('=== Values actually used in hash1 and hash2 ===');
console.log('Hash1 numeric parts:');
console.log('  arr[26] = 6134353334 -> a4534');
console.log('  arr[21] = 6161343030 -> aa400');

console.log('\nHash2 numeric parts:');
console.log('  arr[9] = 6232 -> b2');

// So from hash1 and hash2, I get: a4534, aa400, b2
// From base64 in _0x4a39, I get: c95ee47, c70c3eb, 7722c69
// From instruction, I get: 3463383330 -> 4c830

// Total:
// c95ee47 (7) + c70c3eb (7) + 7722c69 (7) + 4c830 (5) + a4534 (5) + aa400 (5) + b2 (2)
// = 38 characters, too long

// Maybe the hash is ONLY from the base64 + specific numeric?
// Let me check what numeric strings appear in which concatenated string

console.log('\n=== Extracting ONLY clean numeric strings from hash1 ===');
var hash1 = '736888mBECaR613435333445JEiLUC61613430309VFwNrgapply__proto__';
var nums_hash1 = hash1.match(/\d+/g);
console.log('Numbers from hash1:', nums_hash1);

nums_hash1.forEach(num => {
    if (num.length % 2 === 0 && num.length >= 4) {
        var decoded = '';
        for (var i = 0; i < num.length; i += 2) {
            decoded += String.fromCharCode(parseInt(num.substr(i, 2), 16));
        }
        if (/^[a-f0-9]+$/i.test(decoded)) {
            console.log(`  ${num} -> ${decoded}`);
        }
    }
});

console.log('\n=== Full reconstruction attempt ===');
// Maybe the pattern is:
// Base64 parts: c95ee47 + c70c3eb + 7722c69 = 21 chars
// Numeric from instruction: 4c830 = 5 chars
// Numeric from hash1: ???

// Looking at the numbers in hash1:
// 613435333445 -> could this be one number?
var large_num = '613435333445';
console.log(`Decoding ${large_num}:`);
var decoded = '';
for (var i = 0; i < large_num.length; i += 2) {
    decoded += String.fromCharCode(parseInt(large_num.substr(i, 2), 16));
}
console.log(`  -> "${decoded}"`);

// Or split as 6134353334 + 45
// 45 in hex is 'E'
console.log('\n6134353334 -> a4534');
console.log('45 -> E');

// So maybe: c95ee47 + c70c3eb + 7722c69 + 4c830 + a4534 + E
var attempt = 'c95ee47c70c3eb7722c694c830a4534' + 'E';
console.log(`\nAttempt with E: ${attempt}`);
console.log(`Length: ${attempt.length}`);

// Or maybe the last digit is from 6161343030
// 61613430 + 30
// 30 in hex is '0'
console.log('\n30 in hex = 0');
var attempt2 = 'c95ee47c70c3eb7722c694c830a4534' + '0';
console.log(`Attempt with 0: ${attempt2}`);
console.log(`Length: ${attempt2.length}`);

// Or look at 61613430309
// The last part is 09 which is a tab character, probably not it
// But wait, maybe it's 61613430 + 309
// Or 6161343030 + 9

console.log('\n=== Most likely hash ===');
var final_hash = 'c95ee47c70c3eb7722c694c830aa4534';
console.log(`Hash: ${final_hash}`);
console.log(`Length: ${final_hash.length}`);
console.log(`\nFlag: USCC{${final_hash}}`);
