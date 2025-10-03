// Let's create the proper base64 encoding for the credentials

const username = 'admin1strat0r';
const password = 'cIjCWTEY5!g7AY^LPy%Ѹ';

console.log('Username:', username);
console.log('Password:', password);
console.log('Password length:', password.length);

// Create the credentials string
const credentials = username + ':' + password;
console.log('Credentials:', credentials);

// Base64 encode
const base64Creds = Buffer.from(credentials, 'utf8').toString('base64');
console.log('Base64 credentials:', base64Creds);

// Let's also try without the Unicode character
const passwordWithoutUnicode = 'cIjCWTEY5!g7AY^LPy%';
const credentialsWithoutUnicode = username + ':' + passwordWithoutUnicode;
const base64CredsWithoutUnicode = Buffer.from(credentialsWithoutUnicode, 'utf8').toString('base64');
console.log('Base64 without Unicode:', base64CredsWithoutUnicode);

// Let's also check the character codes of the password
console.log('\nPassword character analysis:');
for (let i = 0; i < password.length; i++) {
    console.log(`${i}: ${password.charCodeAt(i)} -> '${password.charAt(i)}'`);
}