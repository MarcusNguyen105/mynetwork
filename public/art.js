// ASCII art for the computer
const computerArt = `
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║           SECURE SYSTEM ACCESS PORTAL v2.7.3             ║
    ║                                                           ║
    ║            [████████████████████████████████]             ║
    ║                                                           ║
    ║        ⚠️  AUTHORIZED PERSONNEL ONLY  ⚠️                   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝

       _____                           _             
      / ____|                         (_)            
     | (___   ___  ___ _   _ _ __ ___ _ _ __   __ _ 
      \\___ \\ / _ \\/ __| | | | '__/ _ \\ | '_ \\ / _\` |
      ____) |  __/ (__| |_| | | |  __/ | | | | (_| |
     |_____/ \\___|\\___|\\__,_|_|  \\___|_|_| |_|\\__, |
                                               __/ |
                                              |___/ 
    
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║  📡 System Status: OPERATIONAL                            ║
    ║  🔐 Security Level: MAXIMUM                               ║
    ║  🛡️  Encryption: ADVANCED OBFUSCATION™                    ║
    ║  🔒 Authentication: TOTALLY SECURE                        ║
    ║                                                           ║
    ║  💡 Hint: Try opening your browser's developer console    ║
    ║      and see what the system is doing...                  ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝

    [>] Initializing secure connection...
    [>] Loading encryption modules...
    [>] Validating certificates... 
    [>] System ready for authentication...

    ⚡ Fun fact: Security through obscurity is like hiding your
       house key under the doormat and calling it "security"!
`;

document.getElementById('computer-art').textContent = computerArt;

// Add some "hacker" typing effect
let lines = computerArt.split('\n');
let currentLine = 0;

function typeEffect() {
    if (currentLine < lines.length) {
        document.getElementById('computer-art').textContent = 
            lines.slice(0, currentLine + 1).join('\n');
        currentLine++;
        setTimeout(typeEffect, 50);
    }
}

// Uncomment for typing effect (disabled by default for better UX)
// document.getElementById('computer-art').textContent = '';
// typeEffect();
