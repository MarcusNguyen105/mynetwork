#!/usr/bin/env python3
import struct

# The binary data from the CTF challenge
binary_data = """ELF        4   <       4   4€   4€    T  T T   D  H   è   è   h  h D   D   Påtdl  l‹   l‹   L   L   Qåtd                    Råtd  Ÿ   Ÿ   /lib/ld-linux.so.2  GNU     GNU ‡ÅÞB¶ÎRsyÖ°Ï¬Çü   KãÀ                G           i           N           4           ®               T           x           Š           A           p           [           9           b           %           ¬‰      libc.so.6 _IO_stdin_used exit fopen __isoc99_scanf puts putchar stdin printf fgets strlen memset stdout stderr setvbuf __libc_start_main write GLIBC_2.7 GLIBC_2.1 GLIBC_2.0 __gmon_start__    SƒìèW  Ãg  ‹ƒôÿÿÿ…Àtèâ   ƒÄ[Ã             ÿ5  ÿ%   ÿ%  h    éàÿÿÿÿ%  h   éÐÿÿÿÿ%  h   éÀÿÿÿÿ%  h   é°ÿÿÿÿ%  h    é ÿÿÿÿ%  h(   éÿÿÿÿ%$  h0   é€ÿÿÿÿ%(  h8   épÿÿÿÿ%,  h@   é`ÿÿÿÿ%0  hH   éPÿÿÿÿ%4  hP   é@ÿÿÿÿ%8  hX   é0ÿÿÿÿ%ôŸf        1í^áƒäðPTRè#   ÃP  ƒéÿPƒ0éÿÿPQVÇÀ¸ˆ  PèNÿÿÿô‹$Ãff  fff  fff‹$Ãffffffff‹$Ãfffff¸D  =D  t$¸    …ÀtUåƒìhD  ÿÐƒÄÉÃö¼'    óÃ´&    ¼'    ¸D  -D  Áø‰ÂÁêÐÑøt º    …ÒtUåƒìPhD  ÿÒƒÄÉÃt& óÃ¶    €=D  uUåƒìèlÿÿÿÆD  ÉÃv óÃ´&    ¼'    Uå]ëŠUåSì  è+ÿÿÿÃ;  ƒìh  j …ôþÿÿPèþÿÿƒÄƒìƒ°éÿÿPƒ²éÿÿPèVþÿÿƒÄ‰Eôƒ}ô uƒìƒ¼éÿÿPèÛýÿÿƒÄë[ƒìÿuôh  …ôþÿÿPè¯ýÿÿƒÄƒìj
è2þÿÿƒÄƒì…ôþÿÿPèÀýÿÿƒÄƒìP…ôþÿÿPjèËýÿÿƒÄƒìj
èþýÿÿƒÄƒìj èýÿÿUåSìèeþÿÿÃu  ƒìƒêÿÿPèPýÿÿƒÄƒìƒ5êÿÿPèýÿÿƒÄƒìEôPƒOêÿÿPèýÿÿƒÄ‹Eôƒø~ƒìƒRêÿÿPè
ýÿÿƒÄƒìj èýÿÿ‹Eô˜ƒøteƒøƒøtƒøƒøtƒøƒøtëÅƒøtrƒø|Y=9  tzë²ƒìƒhêÿÿPè¿üÿÿƒÄë|ƒìƒêÿÿPè«üÿÿƒÄëhƒìƒ¬êÿÿPè—üÿÿƒÄëTƒìƒÌêÿÿPèƒüÿÿƒÄë@ƒìƒôêÿÿPèoüÿÿƒÄë,ƒìƒëÿÿPè[üÿÿƒÄëƒìƒ@ëÿÿPèGüÿÿƒÄèþÿÿ‹]üÉÃL$ƒäðÿqüUåSQè$ýÿÿÃ4  ‹ƒøÿÿÿ‹ j jj PèZüÿÿƒÄ‹ƒüÿÿÿ‹ j jj PèCüÿÿƒÄ‹ƒðÿÿÿ‹ j jj Pè,üÿÿƒÄècþÿÿ¸    eøY[]aüÃff UWVSè·üÿÿÃÇ  ƒì‹l$(³ÿÿÿè?ûÿÿƒ ÿÿÿ)ÆÁþ…öt%1ÿ¶    ƒìUÿt$,ÿt$,ÿ"» ÿÿÿƒÇƒÄ9þuãƒÄ[^_]Ãv óÃ  SìèSüÿÿÃc  ƒÄ[Ã   r ./flag    Missing flag file! Please contact support if you see this error on the remote target!   ---
JUNKYARD ACCESS TERMINAL
--- Enter access band (1-6):  %i Access band invalid!  SCAVENGER — Yard floor access HAULER — Broken-but-usable stock  MECHANIC — Engine bays & bins QUARRY FOREMAN — Heavy salvage ops    YARD MANAGER — Central yard systems   BOSS — Secure compound & vaults   RAIDER KING — Override scrapyard locks   """

print("Analyzing binary structure...")
print("This appears to be an ELF binary with the following key information:")
print("1. It's a 32-bit ELF executable")
print("2. It has a 'vuln' function (likely the vulnerable function)")
print("3. It has a 'win' function (likely the target function)")
print("4. It uses standard libc functions like printf, fgets, etc.")
print("5. The access levels are:")
print("   - SCAVENGER (1) - Yard floor access")
print("   - HAULER (2) - Broken-but-usable stock") 
print("   - MECHANIC (3) - Engine bays & bins")
print("   - QUARRY FOREMAN (4) - Heavy salvage ops")
print("   - YARD MANAGER (5) - Central yard systems")
print("   - BOSS (6) - Secure compound & vaults")
print("   - RAIDER KING (7) - Override scrapyard locks")

print("\nThe highest access level appears to be 'RAIDER KING' (7)")
print("However, the prompt only accepts 1-6, so we need to find a way to get level 7")
print("This suggests a buffer overflow or integer overflow vulnerability")