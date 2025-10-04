#!/usr/bin/env python3

def try_decode_final_section():
    # The final section parts
    parts = ['vbR^w8|=^(}^<Q;;)g5BRR%', ':%:_', 'ZEo|gBoRoJogE', 'g5oEJgs']

    print("Testing substitution hypothesis based on flag format USCC{}")
    print("Hypothesis: g5 = 'US', oEJ = 'CC', gs = '{}', and other patterns")

    # Test the hypothesis on the parts
    for i, part in enumerate(parts):
        print(f"\nPart {i}: '{part}'")

        # Try the substitution pattern
        # g5 -> US
        # oEJ -> CC
        # gs -> {}

        test_result = part
        test_result = test_result.replace('g5', 'US')
        test_result = test_result.replace('oEJ', 'CC')
        test_result = test_result.replace('gs', '{}')

        print(f"After substitution: '{test_result}'")

        # Check if this looks like a flag
        if 'USCC' in test_result and ('{' in test_result or '}' in test_result):
            print("*** FOUND FLAG CANDIDATE ***")

    # Try more comprehensive substitution
    print("\n" + "="*50)
    print("Trying more systematic substitution:")

    # Let's map individual characters based on the flag assumption
    # From g5oEJgs -> USCC{}
    # So: g->U, 5->S, o->C, E->C, J->C, g->}, s->{, but wait that doesn't work

    # Let's try: g5 = US, oEJ = CC, gs = {}
    # That would mean g->U, 5->S, o->C, E->C, J->C, g->}, s->{, but g is used twice

    # Wait, that doesn't work because g would need to be both U and }
    # So maybe it's not that simple

    # Let's look at it differently
    # g5oEJgs
    # If this is USCC{}, then:
    # g = U, 5 = S, o = C, E = C, J = C, g = }, s = {

    # But g can't be both U and }
    # Unless there's a different mapping

    # Maybe it's g5 = US, oEJgs = CC{}
    # Let's check the length: g5oEJgs is 7 chars, USCC{} is 6 chars, close

    # g5oEJgs -> U S C C { }
    # g  5  o  E  J  g  s
    # U  S  C  C  {  }  - but that's 6 chars, but we have 7 chars

    # Maybe g5oEJgs -> U S C C { }
    # So: g=U, 5=S, o=C, E=C, J=C, g={, s=}

    # But then g would be both U and {

    # This is confusing. Let me try a different approach.

    # Let's assume the entire final section is the encoded flag
    # and try to find a substitution that gives USCC{}

    final_section = 'vbR^w8|=^(}^<Q;;)g5BRR% :%:_ ZEo|gBoRoJogE g5oEJgs'
    print(f"\nFull final section: '{final_section}'")

    # Let's try to find patterns that could correspond to USCC
    # Look for 4 consecutive characters that could map to USCC

    print("\nLooking for 4-char sequences that could map to USCC:")
    for i in range(len(final_section) - 3):
        seq = final_section[i:i+4]
        print(f"  '{seq}' at position {i}")

    # Notice some interesting patterns:
    # g5BRR - if g5=US, then USBRR
    # g5oEJgs - if g5=US, oEJ=CC, gs={}, then USCC{}

    # Wait, that almost works! Let's see:
    # g5oEJgs -> g5 oEJ gs -> US CC {} -> USCC{}

    # Yes! The mapping is:
    # g5 -> US
    # oEJ -> CC
    # gs -> {}

    # And the 'g' in gs is a different character than the 'g' in g5!

    # Let's verify this mapping on the entire text

    print("\nTesting the mapping:")
    print("g5 -> US")
    print("oEJ -> CC")
    print("gs -> {}")

    # Apply to the entire final section
    result = final_section
    result = result.replace('g5', 'US')
    result = result.replace('oEJ', 'CC')
    result = result.replace('gs', '{}')

    print(f"Result: '{result}'")

    # But this doesn't handle all characters. Let's see what else needs mapping
    # The result would be: vbR^w8|=^(}^<Q;;)USBRR% :%:_ ZEo|gBoRoJogE USCC{}

    # This looks promising! Now I need to figure out what the other patterns mean
    # Notice "gBoRoJogE" - this looks like it might be "something"

    # Let's see if there are more patterns
    # g5BRR -> USBRR (but g5->US, so USBRR)
    # gBoR -> ? (if gB = US, then USB oR?)
    # oJogE -> ? (if oJ = CC, then CC ogE?)

    # Hmm, not consistent.

    # Maybe it's a different mapping.
    # Let's look at the structure again.

    # The parts are separated by spaces and symbols
    # Maybe each part represents something

    print("\nAnalyzing parts separately:")
    for i, part in enumerate(parts):
        print(f"Part {i}: '{part}'")

        # Try the same substitution on each part
        part_result = part
        part_result = part_result.replace('g5', 'US')
        part_result = part_result.replace('oEJ', 'CC')
        part_result = part_result.replace('gs', '{}')

        print(f"  -> '{part_result}'")

if __name__ == "__main__":
    try_decode_final_section()