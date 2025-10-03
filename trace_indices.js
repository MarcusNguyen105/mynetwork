// Manual trace of the obfuscation

// _0x4a39 array (0x146 offset subtracted = 326 decimal)
function _0x4a39(){
    return ['eulav\x20eht\x20','table','70390zHMDsK','object','966028jCWdrH','function','log','5YARiXg','Yzk1ZWU0Nz','45JEiLUC','YzcwYzNlYj','6631656436','863256EtMoYk','push','6589810GTlrab','apply','882245NXpbDV','43312yxCGot','4373736qzQvCI','toString','warn','6232','8796768UCpcfR','length','parw\x20dna\x20,','3961373433','3361326434','11CsMkkl','exception','NzcyMmM2OW','3463383330','31508QVFcbD','error','undefined','({...}CCSU','alf\x20dradna','ts\x20eht\x20ni\x20','Y4OWEwYWFl','c\x20,sehsah\x20','40556232pbALNU','736888mBECaR','shift','bind','k1MDI0NDY1','__proto__','rehtegot\x20s','29ekpzDq','info','854YoyEjg','66nVBDrR','console','6134353334'];
}

// Build _0x32e5 array (uses _0x3476 with 0x146 offset)
function build_32e5() {
    var arr = _0x4a39();
    
    // _0x3476(offset) returns arr[offset - 0x146]
    var resolve = (offset) => arr[offset - 0x146];
    
    return [
        resolve(0x16c), // 0
        resolve(0x164), // 1
        resolve(0x14f), // 2
        ')\x20tamrof\x20g', // 3
        resolve(0x163), // 4
        resolve(0x152), // 5
        resolve(0x154), // 6
        resolve(0x153), // 7
        'IxZg==', // 8
        resolve(0x15b), // 9
        'eht\x20kcarc', // 10
        resolve(0x14d), // 11
        resolve(0x156), // 12
        '9VFwNrg', // 13
        resolve(0x146), // 14
        resolve(0x16f), // 15
        resolve(0x148), // 16
        resolve(0x15d), // 17
        resolve(0x168), // 18
        resolve(0x16e), // 19
        '287AWNVHd', // 20
        '6161343030', // 21
        resolve(0x157), // 22
        resolve(0x149), // 23
        resolve(0x172), // 24
        resolve(0x155), // 25
        resolve(0x179), // 26
        resolve(0x14e), // 27
        resolve(0x14a), // 28
        'etanetacno', // 29
        '178842lPRJmm', // 30
        '1392482zqhnOI' // 31
    ];
}

var arr_32e5 = build_32e5();
console.log('_0x32e5 array built:');
arr_32e5.forEach((val, idx) => {
    console.log(`[${idx}]: ${val}`);
});

// _0x4deb uses _0x32e5 with offset (0x9b*0x15+-0x17a6+0xccf) = 505
var offset_4deb = (0x9b*0x15+-0x17a6+0xccf);
console.log(`\n_0x4deb offset: ${offset_4deb} (0x${offset_4deb.toString(16)})`);

// So _0x34b85e(index) = arr_32e5[index - offset_4deb]
var resolve_34b85e = (idx) => arr_32e5[idx - offset_4deb];

// Build hash1, hash2, instruction
console.log('\n=== Building final values ===');

var hash1_indices = [0x1f3, 0x1fa, 0x1e2, 0x1f5, 0x1ed, 0x1f9, 0x1f8];
var hash2_indices = [0x1fe, 0x1f7, 0x1f1, 0x1e7, 0x1e9, 0x1e6];
var instr_indices = [0x1e3, 0x1e1, 0x1e5, 0x1e4, 0x1ee, 0x1ef, 0x1ff, 0x1fb, 0x1ea, 0x1e8];

console.log('\nHash1 parts:');
var hash1_parts = hash1_indices.map(idx => {
    var val = resolve_34b85e(idx);
    console.log(`  [0x${idx.toString(16)}] (${idx}) -> arr[${idx - offset_4deb}] = ${val}`);
    return val;
});
var hash1 = hash1_parts.join('');
console.log('hash1:', hash1);

console.log('\nHash2 parts:');
var hash2_parts = hash2_indices.map(idx => {
    var val = resolve_34b85e(idx);
    console.log(`  [0x${idx.toString(16)}] (${idx}) -> arr[${idx - offset_4deb}] = ${val}`);
    return val;
});
var hash2 = hash2_parts.join('');
console.log('hash2:', hash2);

console.log('\nInstruction parts:');
var instr_parts = instr_indices.map(idx => {
    var val = resolve_34b85e(idx);
    console.log(`  [0x${idx.toString(16)}] (${idx}) -> arr[${idx - offset_4deb}] = ${val}`);
    return val;
});
var instruction = instr_parts.join('');
console.log('instruction:', instruction);
console.log('instruction reversed:', instruction.split('').reverse().join(''));
