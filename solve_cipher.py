import sys, string, math
from collections import Counter
ct = "ZQQCVBFGKFIMJWGTVLSJRIDQYDQNPBZXGFJRPEDYDZYHLLRLSAYXHLGQSZYXHLGEPRGGCLUHJAGWXGIIYNQWYFEQZDHLSFHKLLNGCLUKYNXIUMHTVUIIZUKKJZIHFYQN".strip()
alpha = string.ascii_uppercase
ct = .join([c for c in ct if c in alpha])

# Caesar brute-force
caesar_results = []
for k in range(26):
    pt = .join(alpha[(alpha.index(c)-k)%26] for c in ct)
    caesar_results.append((k, pt))

# Index of coincidence
def ioc(s):
    N = len(s)
    freqs = Counter(s)
    if N <= 1:
        return 0.0
    return sum(f*(f-1) for f in freqs.values())/(N*(N-1))

# Vigenere helpers
def shift_text(s, k):
    return .join(alpha[(alpha.index(c)-k)%26] for c in s)

# Chi-squared for English monoalphabetic
english_freq = {
    A:8.167,B:1.492,C:2.782,D:4.253,E:12.702,F:2.228,G:2.015,H:6.094,
    I:6.966,J:0.153,K:0.772,L:4.025,M:2.406,N:6.749,O:7.507,P:1.929,
    Q:0.095,R:5.987,S:6.327,T:9.056,U:2.758,V:0.978,W:2.360,X:0.150,
    Y:1.974,Z:0.074
}
for k in english_freq:
    english_freq[k] /= 100.0

def chisq(text):
    N = float(len(text))
    if N == 0:
        return float(inf)
    counts = Counter(text)
    chi = 0.0
    for ch in alpha:
        observed = counts.get(ch, 0)
        expected = english_freq[ch]*N
        if expected > 0:
            chi += (observed-expected)**2/expected
    return chi

# Try Vigenere key lengths 1..16 using Friedman/IOC and chi-squared per column
best_vig = []
for key_len in range(1, 17):
    cols = [ for _ in range(key_len)]
    for i, ch in enumerate(ct):
        cols[i % key_len] += ch
    key_shifts = []
    for col in cols:
        best_shift = 0
        best_score = 1e18
        for k in range(26):
            dec = shift_text(col, k)
            score = chisq(dec)
            if score < best_score:
                best_score = score
                best_shift = k
        key_shifts.append(best_shift)
    # Build plaintext
    pt_chars = []
    for i, ch in enumerate(ct):
        k = key_shifts[i % key_len]
        pt_chars.append(alpha[(alpha.index(ch)-k)%26])
    pt = .join(pt_chars)
    score = chisq(pt)
    best_vig.append((score, key_len, key_shifts, pt))

best_vig.sort(key=lambda x: x[0])

print("Top Caesar candidates (first 5):")
for k, pt in caesar_results[:26]:
    # print all with chi
    print("k=%2d chi=%.2f %s" % (k, chisq(pt), pt[:80]))

print("\nTop Vigenere candidates by chi-squared:")
for score, key_len, key_shifts, pt in best_vig[:10]:
    key = .join(alpha[s] for s in key_shifts)
    print("len=%2d chi=%.2f key=%s pt=%s" % (key_len, score, key, pt[:120]))
