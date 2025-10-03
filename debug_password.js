// Let's debug the password decoding more carefully

var hexString = '3939203733203130362036372038372038342036392038392035332033332031303320353520363520383920393420373620383020313231203337203131343420';

console.log("Hex string analysis:");
console.log("Length:", hexString.length);

// Convert hex to intermediate string
var intermediate = '';
for (var i = 0; i < hexString.length; i += 2) {
    var hex = hexString.substring(i, i + 2);
    var decimal = parseInt(hex, 16);
    var char = String.fromCharCode(decimal);
    intermediate += char;
    console.log(`Position ${i/2}: ${hex} -> ${decimal} -> '${char}'`);
}

console.log("\nIntermediate result:", JSON.stringify(intermediate));

// Split by spaces
var parts = intermediate.split(' ');
console.log("\nParts after splitting by space:");
parts.forEach((part, index) => {
    console.log(`${index}: "${part}"`);
});

// Convert each part to character
console.log("\nConverting parts to characters:");
var password = '';
parts.forEach((part, index) => {
    if (part !== '') {
        var num = parseInt(part);
        if (!isNaN(num)) {
            var char = String.fromCharCode(num);
            password += char;
            console.log(`${index}: "${part}" -> ${num} -> '${char}' (code: ${char.charCodeAt(0)})`);
        }
    }
});

console.log("\nFinal password:", JSON.stringify(password));
console.log("Password length:", password.length);

// Let's also check if the last "1144" might be two separate numbers
console.log("\nChecking if 1144 should be split:");
var lastPart = "1144";
// Maybe it's "114" and "4"?
console.log("114 ->", String.fromCharCode(114));
console.log("4 ->", String.fromCharCode(4));
// Or maybe it's "11" and "44"?
console.log("11 ->", String.fromCharCode(11));
console.log("44 ->", String.fromCharCode(44));

// Let's try without the problematic last character
var passwordWithoutLast = password.substring(0, password.length - 1);
console.log("Password without last char:", JSON.stringify(passwordWithoutLast));