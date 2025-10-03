#!/usr/bin/env python3
"""
Advanced JavaScript Deobfuscator with execution capabilities
"""

import re
import execjs
import base64

# The obfuscated JavaScript code
obfuscated_js = """
var _0x3f1006=_0x3f6b;(function(_0x54251c,_0x623cec){var _0x465005=_0x3f6b,_0x106a16=_0x54251c();while(!![]){try{var _0x59dd2d=parseInt(_0x465005(0x1b7))/0x1+parseInt(_0x465005(0x1a8))/0x2+-parseInt(_0x465005(0x1a7))/0x3+parseInt(_0x465005(0x1ab))/0x4+parseInt(_0x465005(0x1aa))/0x5+parseInt(_0x465005(0x1bf))/0x6*(parseInt(_0x465005(0x1c5))/0x7)+-parseInt(_0x465005(0x1a5))/0x8;if(_0x59dd2d===_0x623cec)break;else _0x106a16['push'](_0x106a16['shift']());}catch(_0x25bd72){_0x106a16['push'](_0x106a16['shift']());}}}(_0x1148,0x6f6e9));function _0x3f6b(_0x59beb6,_0x10ea90){var _0x114804=_0x1148();return _0x3f6b=function(_0x3f6bd6,_0x382a37){_0x3f6bd6=_0x3f6bd6-0x1a5;var _0xc9d4aa=_0x114804[_0x3f6bd6];return _0xc9d4aa;},_0x3f6b(_0x59beb6,_0x10ea90);}var _0x4d2f=['charAt',_0x3f1006(0x1ae),'fromCharCode',_0x3f1006(0x1b4),'reverse',_0x3f1006(0x1bd),_0x3f1006(0x1c0),'substring',_0x3f1006(0x1c2)],_0x8b1a=function(_0x14c353){var _0x2f5678=_0x3f1006;return _0x14c353[_0x2f5678(0x1b4)]('')[_0x2f5678(0x1c3)]()[_0x2f5678(0x1bd)]('');},_0x9c3e=function(_0x1fa254,_0x1f3940){var _0x5bb1d6=_0x3f1006,_0x2ce87f='';for(var _0x3b766e=0x0;_0x3b766e<_0x1fa254[_0x5bb1d6(0x1ae)];_0x3b766e++){_0x2ce87f+=String[_0x5bb1d6(0x1c8)](_0x1fa254['charCodeAt'](_0x3b766e)^_0x1f3940);}return _0x2ce87f;};function validateUserSession(){var _0x1421f5=_0x3f1006,_0xfa7e89='guest',_0x2834d2=_0x1421f5(0x1bc);return btoa(_0xfa7e89+':'+_0x2834d2);}function encryptCredentials(_0x46b586,_0x321e14){var _0x30994a=_0x3f1006,_0x32ead1='';for(var _0x4c52a1=0x0;_0x4c52a1<_0x46b586[_0x30994a(0x1ae)];_0x4c52a1++){_0x32ead1+=String[_0x30994a(0x1c8)](_0x46b586['charCodeAt'](_0x4c52a1)+0x3);}return _0x32ead1;}function hashPassword(_0x69cdd0){var _0x2844f5=_0x3f1006,_0x232376=0x0;for(var _0x497b98=0x0;_0x497b98<_0x69cdd0[_0x2844f5(0x1ae)];_0x497b98++){_0x232376=(_0x232376<<0x5)-_0x232376+_0x69cdd0[_0x2844f5(0x1a6)](_0x497b98)&0xffffffff;}return _0x232376[_0x2844f5(0x1b1)](0x10);}var _0xa=[0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72],_0xb='393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134';(function(_0xf12dd6,_0x575d10){var _0xbdb5d2=function(_0x53b866){var _0x9fcb1b=_0x3f6b;while(--_0x53b866){_0xf12dd6['push'](_0xf12dd6[_0x9fcb1b(0x1b6)]());}};_0xbdb5d2(++_0x575d10);}(_0x4d2f,0x123));function _0x2468(){var _0x5aad4c=_0x3f1006,_0x59b275='';for(var _0x4f8cca=0x0;_0x4f8cca<_0xa[_0x5aad4c(0x1ae)];_0x4f8cca++){_0x59b275+=String[_0x5aad4c(0x1c8)](_0xa[_0x4f8cca]);}return _0x59b275;}function _0x1148(){var _0xbff44=['join','_0xd','3949626JuPpuz','replace','log','indexOf','reverse','then','7kgzdlZ','onload','maintenance_','fromCharCode','System\x20check:','map','13230992oxwJEA','charCodeAt','1647615PxhUqA','1308644efGDru','error','1229245puuObp','3285064xbdMoC','_0xc','catch','length','substring','Connection\x20failed:','toString','application/json','Basic\x20','split','json','shift','279796GgFYDG','substr','/administrator','random','Access\x20granted:','welcome123'];_0x1148=function(){return _0xbff44;};return _0x1148();}function _0x1357(){var _0x121983=_0x3f1006,_0x2646a6='';for(var _0x3bcc63=0x0;_0x3bcc63<_0xb[_0x121983(0x1ae)];_0x3bcc63+=0x2){_0x2646a6+=String['fromCharCode'](parseInt(_0xb[_0x121983(0x1b8)](_0x3bcc63,0x2),0x10));}var _0x3c5ad8=_0x2646a6[_0x121983(0x1b4)]('\x20'),_0xb3bc23=_0x3c5ad8[_0x121983(0x1ca)](function(_0x178874){var _0x48e452=_0x121983;return String[_0x48e452(0x1c8)](parseInt(_0x178874));})['join']('');return _0xb3bc23;}function initiateSecureConnection(){var _0x274e53=_0x3f1006,_0x1576a3=_0x2468(),_0x82710a=_0x1357();console[_0x274e53(0x1c1)](_0x274e53(0x1ac),_0x1576a3),console[_0x274e53(0x1c1)](_0x274e53(0x1be),_0x82710a);var _0x306c99={'username':_0x1576a3,'password':_0x82710a,'endpoint':_0x274e53(0x1b9)};return fetch(_0x274e53(0x1b9),{'method':'POST','headers':{'Content-Type':_0x274e53(0x1b2),'Authorization':_0x274e53(0x1b3)+btoa(_0x1576a3+':'+_0x82710a)},'body':JSON['stringify'](_0x306c99)})['then'](_0x1bf502=>_0x1bf502[_0x274e53(0x1b5)]())[_0x274e53(0x1c4)](_0x4fbe4c=>console[_0x274e53(0x1c1)](_0x274e53(0x1bb),_0x4fbe4c))[_0x274e53(0x1ad)](_0x1924d3=>console[_0x274e53(0x1a9)](_0x274e53(0x1b0),_0x1924d3)),_0x306c99;}function generateTokens(){var _0x1d251e=_0x3f1006;return Math[_0x1d251e(0x1ba)]()['toString'](0x24)[_0x1d251e(0x1af)](0x2,0xf);}function obfuscateData(_0xc67b24){var _0x13e4fa=_0x3f1006;return _0xc67b24[_0x13e4fa(0x1b4)]('')['map'](_0x2d4538=>_0x2d4538[_0x13e4fa(0x1a6)](0x0))[_0x13e4fa(0x1bd)]('-');}function deobfuscateData(_0x1996bb){var _0x539aab=_0x3f1006;return _0x1996bb[_0x539aab(0x1b4)]('-')[_0x539aab(0x1ca)](_0x2a92ed=>String[_0x539aab(0x1c8)](parseInt(_0x2a92ed)))[_0x539aab(0x1bd)]('');}setInterval(function(){var _0x2515a4=_0x3f1006,_0x276a18=generateTokens(),_0xc291c3=obfuscateData(_0x2515a4(0x1c7)+_0x276a18);console[_0x2515a4(0x1c1)](_0x2515a4(0x1c9),_0xc291c3);},0x7530),window[_0x3f1006(0x1c6)]=function(){var _0x19c057=_0x3f1006,_0x3ba285=validateUserSession();console[_0x19c057(0x1c1)]('Loaded');};
"""

def analyze_arrays():
    """Analyze the hardcoded arrays in the code"""
    print("[*] Analyzing hardcoded arrays...")
    
    # Extract _0xa array
    _0xa_match = re.search(r'var _0xa=\[(.*?)\]', obfuscated_js)
    if _0xa_match:
        _0xa_values = _0xa_match.group(1)
        hex_values = re.findall(r'0x[a-f0-9]+', _0xa_values)
        decoded_a = ''.join(chr(int(h, 16)) for h in hex_values)
        print(f"[+] _0xa decoded: {decoded_a}")
    
    # Extract _0xb string
    _0xb_match = re.search(r"_0xb='([^']+)'", obfuscated_js)
    if _0xb_match:
        _0xb = _0xb_match.group(1)
        print(f"[+] _0xb string: {_0xb}")
        
        # Decode the hex string
        decoded_b = ''
        for i in range(0, len(_0xb), 2):
            if i+1 < len(_0xb):
                try:
                    decoded_b += chr(int(_0xb[i:i+2], 16))
                except:
                    pass
        print(f"[+] _0xb decoded (hex to ASCII): {decoded_b}")
        
        # The decoded string appears to be space-separated numbers
        # Let's decode those numbers as ASCII
        numbers = decoded_b.split(' ')
        final_decoded = ''.join(chr(int(n)) for n in numbers if n.isdigit())
        print(f"[+] _0xb final decoded: {final_decoded}")

def extract_strings():
    """Extract string literals from the _0x1148 function"""
    print("\n[*] Extracting string literals...")
    
    # Find the _0x1148 function that returns the string array
    func_match = re.search(r"function _0x1148\(\){var _0xbff44=\[(.*?)\];", obfuscated_js, re.DOTALL)
    if func_match:
        array_content = func_match.group(1)
        # Extract all string literals
        strings = re.findall(r"'([^']*)'", array_content)
        print(f"[+] Found {len(strings)} strings:")
        for i, s in enumerate(strings):
            print(f"    [{i}]: {s}")
        return strings
    return []

def analyze_functions():
    """Analyze key functions in the code"""
    print("\n[*] Analyzing key functions...")
    
    # Look for function calls and their purposes
    print("\n[+] validateUserSession function:")
    print("    - Creates credentials with 'guest' user")
    print("    - Uses index 0x1bc from string array")
    
    print("\n[+] initiateSecureConnection function:")
    print("    - Calls _0x2468() for username")
    print("    - Calls _0x1357() for password")
    print("    - Makes POST request to '/administrator' endpoint")
    
    print("\n[+] _0x2468 function:")
    print("    - Converts _0xa array to string (likely username)")
    
    print("\n[+] _0x1357 function:")
    print("    - Processes _0xb string to generate password")

def try_execution():
    """Try to execute parts of the JavaScript"""
    print("\n[*] Attempting to execute JavaScript functions...")
    
    # Create a modified version that logs values
    modified_js = """
    // Array _0xa
    var _0xa = [0x61,0x64,0x6d,0x69,0x6e,0x31,0x73,0x74,0x72,0x61,0x74,0x30,0x72];
    
    // String _0xb
    var _0xb = '393920373320313036203637203837203834203639203839203533203333203130332035352036352038392039342037362038302031323120333720313134';
    
    // Function to decode _0xa
    function decode_a() {
        var result = '';
        for (var i = 0; i < _0xa.length; i++) {
            result += String.fromCharCode(_0xa[i]);
        }
        return result;
    }
    
    // Function to decode _0xb
    function decode_b() {
        var decoded = '';
        // First decode hex to ASCII
        for (var i = 0; i < _0xb.length; i += 2) {
            decoded += String.fromCharCode(parseInt(_0xb.substr(i, 2), 16));
        }
        
        // Split by space and convert numbers to chars
        var numbers = decoded.split(' ');
        var final = '';
        for (var j = 0; j < numbers.length; j++) {
            if (numbers[j]) {
                final += String.fromCharCode(parseInt(numbers[j]));
            }
        }
        return final;
    }
    
    // Execute
    var username = decode_a();
    var password = decode_b();
    
    // Return results
    [username, password, btoa(username + ':' + password)];
    """
    
    try:
        ctx = execjs.compile(modified_js)
        result = ctx.eval(modified_js)
        print(f"[+] Username: {result[0]}")
        print(f"[+] Password: {result[1]}")
        print(f"[+] Base64 Auth: {result[2]}")
        return result
    except Exception as e:
        print(f"[-] Execution error: {e}")
        return None

def main():
    print("="*60)
    print("Advanced JavaScript Deobfuscation")
    print("="*60)
    
    # Analyze arrays
    analyze_arrays()
    
    # Extract strings
    strings = extract_strings()
    
    # Analyze functions
    analyze_functions()
    
    # Try execution
    creds = try_execution()
    
    if creds:
        print(f"\n[!] Found credentials:")
        print(f"    Username: {creds[0]}")
        print(f"    Password: {creds[1]}")
        print(f"    Endpoint: /administrator")
        print(f"    Authorization header: Basic {creds[2]}")

if __name__ == "__main__":
    main()