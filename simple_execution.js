// Let me try to execute just the key parts manually
// I'll recreate the deobfuscation functions step by step

// First, let me create the _0x4a39 function
function _0x4a39() {
    var _0x3b4f7a = [
        'eulav\x20eht\x20','table','70390zHMDsK','object','966028jCWdrH','function','log','5YARiXg',
        'Yzk1ZWU0Nz','45JEiLUC','YzcwYzNlYj','6631656436','863256EtMoYk','push','6589810GTlrab',
        'apply','882245NXpbDV','43312yxCGot','4373736qzQvCI','toString','warn','6232',
        '8796768UCpcfR','length','parw\x20dna\x20,','3961373433','3361326434','11CsMkkl',
        'exception','NzcyMmM2OW','3463383330','31508QVFcbD','error','undefined','({...}CCSU',
        'alf\x20dradna','ts\x20eht\x20ni\x20','Y4OWEwYWFl','c\x20,sehsah\x20','40556232pbALNU',
        '736888mBECaR','shift','bind','k1MDI0NDY1','__proto__','rehtegot\x20s','29ekpzDq',
        'info','854YoyEjg','66nVBDrR','console','6134353334'
    ];
    return _0x3b4f7a;
}

// Create the _0x3476 function
function _0x3476(_0x24cc5b, _0x2b4f98) {
    var _0x2da9db = _0x4a39();
    return function(_0x224fec, _0x1e2820) {
        _0x224fec = _0x224fec - 0x146;
        var _0x4a390d = _0x2da9db[_0x224fec];
        return _0x4a390d;
    }(_0x24cc5b, _0x2b4f98);
}

// Create the _0x32e5 function
function _0x32e5() {
    var _0x5a1ae8 = _0x3476;
    var _0x5b28f4 = [
        _0x5a1ae8(0x16c), _0x5a1ae8(0x164), _0x5a1ae8(0x14f), ')\x20tamrof\x20g',
        _0x5a1ae8(0x163), _0x5a1ae8(0x152), _0x5a1ae8(0x154), _0x5a1ae8(0x153),
        'IxZg==', _0x5a1ae8(0x15b), 'eht\x20kcarc', _0x5a1ae8(0x14d),
        _0x5a1ae8(0x156), '9VFwNrg', _0x5a1ae8(0x146), _0x5a1ae8(0x16f),
        _0x5a1ae8(0x148), _0x5a1ae8(0x15d), _0x5a1ae8(0x168), _0x5a1ae8(0x16e),
        '287AWNVHd', '6161343030', _0x5a1ae8(0x157), _0x5a1ae8(0x149),
        _0x5a1ae8(0x172), _0x5a1ae8(0x155), _0x5a1ae8(0x179), _0x5a1ae8(0x14e),
        _0x5a1ae8(0x14a), 'etanetacno', '178842lPRJmm', '1392482zqhnOI'
    ];
    return _0x5b28f4;
}

// Create the _0x4deb function
function _0x4deb(_0x5de5a9, _0xabcebe) {
    var _0x224507 = _0x32e5();
    return function(_0x11db13, _0x3f63a1) {
        _0x11db13 = _0x11db13 - (0x9b * 0x15 + -0x17a6 + 0xccf);
        var _0x400144 = _0x224507[_0x11db13];
        return _0x400144;
    }(_0x5de5a9, _0xabcebe);
}

var _0x34b85e = _0x4deb;

// Now let's construct the variables
try {
    var hash1 = _0x34b85e(0x1f3) + _0x34b85e(0x1fa) + _0x34b85e(0x1e2) + _0x34b85e(0x1f5) + _0x34b85e(0x1ed) + _0x34b85e(0x1f9) + _0x34b85e(0x1f8);
    var hash2 = _0x34b85e(0x1fe) + _0x34b85e(0x1f7) + _0x34b85e(0x1f1) + _0x34b85e(0x1e7) + _0x34b85e(0x1e9) + _0x34b85e(0x1e6);
    var instruction = _0x34b85e(0x1e3) + _0x34b85e(0x1e1) + _0x34b85e(0x1e5) + _0x34b85e(0x1e4) + _0x34b85e(0x1ee) + _0x34b85e(0x1ef) + _0x34b85e(0x1ff) + _0x34b85e(0x1fb) + _0x34b85e(0x1ea) + _0x34b85e(0x1e8);

    console.log("hash1:", hash1);
    console.log("hash2:", hash2);
    console.log("instruction:", instruction);
    
    // Try different flag combinations
    console.log("\nPossible flags:");
    console.log("USCC{" + hash1 + "}");
    console.log("USCC{" + hash2 + "}");
    console.log("USCC{" + instruction + "}");
    console.log("USCC{" + hash1 + hash2 + "}");
    
} catch (error) {
    console.log("Error executing:", error.message);
    
    // Let me try to debug by checking individual function calls
    console.log("Debugging individual calls:");
    try {
        console.log("_0x34b85e(0x1f3):", _0x34b85e(0x1f3));
        console.log("_0x34b85e(0x1fa):", _0x34b85e(0x1fa));
    } catch (e) {
        console.log("Error in individual calls:", e.message);
    }
}