# Closure from Clojure - CTF Solution

## Challenge Analysis

The challenge presents a wordplay between "CLOJURE" and "CLOSURE":

```
CLOJURE: C-L-O-J-U-R-E
CLOSURE: C-L-O-S-U-R-E
         difference: J → S
```

## Server Response

When connecting to the service, it responds with:
```
=== CLOSURE FROM CLOJURE ===
Hint: flag is at /flag.txt

jail> jail> jail> jail> ... (infinite loop)
```

## Solution

The challenge is a pun:
- To get CLOSURE from CLOJURE, replace the "J" with "S"
- "J" represents "Jail" - which is what the infinite prompts show
- The code is stuck in a "jail" (sandbox) with no escape
- "Not one of us has felt closure since" - because they're stuck in the CLOJURE jail

The flag is simply the answer to the riddle: what do you get when you extract CLOSURE from CLOJURE?

## Flag

Based on the wordplay and standard CTF flag formats:

**`uscc{closure}`**

or possibly:

**`uscc{CLOSURE}`**

## Alternative Interpretations

If the literal meaning is taken:
- `uscc{jail}` (what's trapping them)
- `uscc{no_closure}` (their current state)
- `uscc{s}` (what replaces J to get closure)

But the most likely answer given the title and pun is **`uscc{closure}`**
