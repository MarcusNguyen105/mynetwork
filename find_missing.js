// Looking at the original _0x4a39 array for ALL numeric strings

var all_from_4a39 = [
    '70390zHMDsK',
    '966028jCWdrH',
    '6631656436',    // This one!
    '863256EtMoYk',
    '6589810GTlrab',
    '882245NXpbDV',
    '43312yxCGot',
    '4373736qzQvCI',
    '6232',
    '8796768UCpcfR',
    '3961373433',
    '3361326434',
    '11CsMkkl',
    '3463383330',
    '31508QVFcbD',
    '40556232pbALNU',
    '736888mBECaR',
    '29ekpzDq',
    '854YoyEjg',
    '66nVBDrR',
    '6134353334',
];

console.log('=== Checking ALL strings from _0x4a39 for pure hex numbers ===');
var pure_numbers = [];

all_from_4a39.forEach(str => {
    // Extract only the parts that are all digits
    var match = str.match(/^\d+$/);
    if (match) {
        var hex = match[0];
        if (hex.length % 2 === 0) {
            var decoded = '';
            for (var i = 0; i < hex.length; i += 2) {
                decoded += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
            }
            var is_hex = /^[a-f0-9]+$/i.test(decoded);
            console.log(`${hex} -> "${decoded}" (is hex: ${is_hex})`);
            if (is_hex) {
                pure_numbers.push({original: hex, decoded: decoded});
            }
        }
    }
});

console.log('\n=== All hex parts in order ===');

// Build in the correct order based on what we know
var parts_in_order = [
    {b64: 'Yzk1ZWU0Nz', decoded: 'c95ee47'},
    {b64: 'YzcwYzNlYj', decoded: 'c70c3eb'},
    {b64: 'NzcyMmM2OW', decoded: '7722c69'},
];

console.log('Base64 parts:');
parts_in_order.forEach(p => {
    console.log(`  ${p.b64} -> ${p.decoded}`);
});

console.log('\nNumeric parts (in array order):');
// 6631656436 appears at index 11 in _0x4a39
// Let me decode it
var hex_candidates = [
    '6631656436',  // index 11
    '6232',        // index 20
    '3961373433',  // index 24
    '3361326434',  // index 25
    '3463383330',  // index 29
    '6134353334',  // index 48
];

hex_candidates.forEach(hex => {
    var decoded = '';
    for (var i = 0; i < hex.length; i += 2) {
        decoded += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    }
    var is_hex = /^[a-f0-9]+$/i.test(decoded);
    console.log(`  ${hex} -> "${decoded}" (is hex: ${is_hex}, len: ${decoded.length})`);
});

// Let me try: c95ee47 + c70c3eb + 7722c69 + f1ed6 + 4c830 + a4534
var attempt1 = 'c95ee47' + 'c70c3eb' + '7722c69' + 'f1ed6' + '4c830' + 'a4534';
console.log(`\n=== Attempt with f1ed6 ===`);
console.log(`Hash: ${attempt1}`);
console.log(`Length: ${attempt1.length}`);

// Or maybe: c95ee47 + c70c3eb + 7722c69 + 4c830 + a4534 + b2
var attempt2 = 'c95ee47' + 'c70c3eb' + '7722c69' + '4c830' + 'a4534' + 'b2';
console.log(`\n=== Attempt with b2 ===`);
console.log(`Hash: ${attempt2}`);
console.log(`Length: ${attempt2.length}`);

// Check which arrays are being used in hash1
// hash1 uses: arr[19], arr[26], arr[2], arr[21], arr[13], arr[25], arr[24]
// arr[26] = 6134353334
// arr[21] = 6161343030

// Let me try with aa400
var attempt3 = 'c95ee47' + 'c70c3eb' + '7722c69' + '4c830' + 'a' + 'a4534';
console.log(`\n=== Attempt with single 'a' ===`);
console.log(`Hash: ${attempt3}`);
console.log(`Length: ${attempt3.length}`);

// Or just add the missing 'a' at the right spot
var attempt4 = 'c95ee47c70c3eb7722c694c830aa4534';
console.log(`\n=== Attempt 4 (added 'a') ===`);
console.log(`Hash: ${attempt4}`);
console.log(`Length: ${attempt4.length}`);
console.log(`Flag: USCC{${attempt4}}`);
