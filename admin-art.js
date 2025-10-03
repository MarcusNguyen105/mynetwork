const adminFrames = [
    `
┌──────────────────────────────┐
│     ADMINISTRATOR PANEL      │
├──────────────────────────────┤
│                              │
│  STATUS: LOGGED IN           │
│  USER: admin1strat0r         │
│  ACCESS: FULL PRIVILEGES     │
│                              │
│  [●] SYSTEM ONLINE           │
│  [●] SECURITY ENABLED        │
│  [○] MAINTENANCE MODE        │
│                              │
└──────────────────────────────┘
        `,

    `
┌──────────────────────────────┐
│       SERVER STATUS          │
├──────────────────────────────┤
│                              │
│  WEB-01    [ONLINE]          │
│  DB-01     [ONLINE]          │
│  AUTH-01   [SECURE]          │
│                              │
│  LOAD: ████░░░░ 45%          │
│  CPU:  ██████░░ 72%          │
│  MEM:  ███░░░░░ 34%          │
│                              │
└──────────────────────────────┘
        `,

    `
┌──────────────────────────────┐
│      SECURITY MONITOR        │
├──────────────────────────────┤
│                              │
│  FIREWALL:     [ACTIVE]      │
│  ENCRYPTION:   [ENABLED]     │
│  INTRUSION:    [BLOCKED]     │
│                              │
│  CONNECTIONS:  247           │
│  BLOCKED IPS:  12            │
│  ALERTS:       0             │
│                              │
└──────────────────────────────┘
        `
];

let currentFrame = 0;
const adminArt = document.getElementById('admin-art');

function updateAdminFrame() {
    adminArt.textContent = adminFrames[currentFrame];
    currentFrame = (currentFrame + 1) % adminFrames.length;
}

updateAdminFrame();
setInterval(updateAdminFrame, 2500);

setInterval(() => {
    const colors = ['#ff0000', '#ffff00', '#ff6600'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.querySelector('.terminal-container').style.borderColor = randomColor;
    document.querySelector('.terminal-container').style.color = randomColor;

    setTimeout(() => {
        document.querySelector('.terminal-container').style.borderColor = '#ff6600';
        document.querySelector('.terminal-container').style.color = '#ff6600';
    }, 200);
}, 7000);

setInterval(() => {
    const chars = ['▓', '▒', '░', '█'];
    const randomChar = chars[Math.floor(Math.random() * chars.length)];
    const blinkElement = document.createElement('span');
    blinkElement.textContent = randomChar;
    blinkElement.style.position = 'absolute';
    blinkElement.style.opacity = '0.3';
    blinkElement.style.animation = 'fadeOut 0.5s ease-out forwards';

    document.body.appendChild(blinkElement);
    setTimeout(() => blinkElement.remove(), 500);
}, 100);

const style = document.createElement('style');
style.textContent = `
        @keyframes fadeOut {
            from { opacity: 0.3; }
            to { opacity: 0; }
        }
    `;
document.head.appendChild(style);