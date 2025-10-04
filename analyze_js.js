// Let's analyze the original JavaScript more carefully
// Looking for any other transformations or functions

// From the original code, I see these functions:
// validateUserSession() - returns btoa('guest:welcome123')
// encryptCredentials() - adds 3 to each character code
// hashPassword() - creates a hash
// obfuscateData() and deobfuscateData() - character code transformations

// Let me check if there are other credential combinations

console.log("Testing guest credentials:");
const guestCreds = btoa('guest:welcome123');
console.log("Guest base64:", guestCreds);

// Let's also check if the password needs some transformation
// Maybe the character 1144 is wrong, let me check the hex decoding again

var hexString = '3939203733203130362036372038372038342036392038392035332033332031303320353520363520383920393420373620383020313231203337203131343420';

// Let's be very careful with the hex decoding
console.log("\nCareful hex analysis:");
var chars = [];
for (var i = 0; i < hexString.length; i += 2) {
    var hex = hexString.substring(i, i + 2);
    var decimal = parseInt(hex, 16);
    chars.push({hex: hex, decimal: decimal, char: String.fromCharCode(decimal)});
}

var intermediate = chars.map(c => c.char).join('');
console.log("Intermediate string:", JSON.stringify(intermediate));

// Split by spaces and convert to characters
var numbers = intermediate.split(' ').filter(n => n !== '');
console.log("Numbers:", numbers);

var password = '';
for (var i = 0; i < numbers.length; i++) {
    var num = parseInt(numbers[i]);
    if (!isNaN(num) && num > 0 && num < 65536) { // Valid Unicode range
        password += String.fromCharCode(num);
    }
}

console.log("Reconstructed password:", JSON.stringify(password));
console.log("Password length:", password.length);

// Let's also try the btoa function like in validateUserSession
const adminCreds = btoa('admin1strat0r:' + password);
console.log("Admin base64:", adminCreds);