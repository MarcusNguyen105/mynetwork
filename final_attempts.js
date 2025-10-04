// Let me try all the possible flag combinations I can think of

console.log("All possible flag attempts:");

// From the base64 decoding
console.log("1. USCC{7722c69c95ee47}");
console.log("2. USCC{c95ee477722c69}");

// With separators
console.log("3. USCC{7722c69-c95ee47}");
console.log("4. USCC{7722c69_c95ee47}");

// From hex patterns in hash1 and hash2
console.log("5. USCC{736888613435333445}");
console.log("6. USCC{17884262326589810}");

// Combining hex from hash1 and hash2
console.log("7. USCC{736888178842}");
console.log("8. USCC{613435333445}");

// Maybe it's the hex string from instruction
console.log("9. USCC{4c830}");

// Maybe it's a combination of the decoded hex
console.log("10. USCC{4c8307722c69c95ee47}");

// Maybe the format is different - let me try without USCC
console.log("11. 7722c69c95ee47");
console.log("12. USCC{7722c69c95ee47}");

// Maybe it's the full instruction decoded
var instruction = ") tamrof g3463383330863256EtMoYkNzcyMmM2OWeulav eht shift1392482zqhnOIYzk1ZWU0Nzeht kcarcIxZg==";

// Let me try to extract just the meaningful parts
// The base64 strings: NzcyMmM2OW (7722c69), Yzk1ZWU0Nz (c95ee47)
// The hex string: 3463383330 (4c830)

console.log("13. USCC{7722c69}");
console.log("14. USCC{c95ee47}");

// Maybe I need to look at this differently
// The challenge is about "security through obscurity"
// Maybe the flag is hidden in plain sight somewhere else

console.log("\nMaybe I should check if there are other clues I missed...");

// Let me also try the combinations in different orders
console.log("15. USCC{c95ee477722c69}");
console.log("16. USCC{47c95ee69c2277}");

// Maybe it's a hash format
console.log("17. USCC{c95ee47c70c3eb7722c69}");  // This was my original attempt

// Let me also check if it could be a different format entirely
console.log("18. uscc{7722c69c95ee47}");  // lowercase
console.log("19. {7722c69c95ee47}");      // no prefix