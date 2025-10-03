import string
from collections import Counter


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENGLISH_FREQ = {
    c: f for c, f in zip(
        ALPHABET,
        [
            8.167,
            1.492,
            2.782,
            4.253,
            12.702,
            2.228,
            2.015,
            6.094,
            6.966,
            0.153,
            0.772,
            4.025,
            2.406,
            6.749,
            7.507,
            1.929,
            0.095,
            5.987,
            6.327,
            9.056,
            2.758,
            0.978,
            2.360,
            0.150,
            1.974,
            0.074,
        ],
    )
}


def chi_square_score(text: str) -> float:
    n = len(text)
    if n == 0:
        return float("inf")
    counts = Counter(text)
    score = 0.0
    for c in ALPHABET:
        expected = ENGLISH_FREQ[c] * n / 100.0
        observed = counts.get(c, 0)
        if expected > 0:
            score += (observed - expected) ** 2 / expected
    return score


def decode_with_shift(text: str, shift: int) -> str:
    idx = {c: i for i, c in enumerate(ALPHABET)}
    return "".join(ALPHABET[(idx[c] - shift) % 26] for c in text)


def best_shift_for_column(column_text: str) -> int:
    best_shift = 0
    best_score = float("inf")
    for shift in range(26):
        decoded = decode_with_shift(column_text, shift)
        score = chi_square_score(decoded)
        if score < best_score:
            best_score = score
            best_shift = shift
    return best_shift


def solve_vigenere(ciphertext: str, max_key_len: int = 24):
    ciphertext = "".join(c for c in ciphertext.upper() if c in ALPHABET)
    candidates = []
    for klen in range(1, max_key_len + 1):
        shifts = []
        for i in range(klen):
            column = ciphertext[i::klen]
            shift = best_shift_for_column(column)
            shifts.append(shift)
        key = "".join(ALPHABET[s] for s in shifts)
        # Decode full plaintext with found shifts
        plain_chars = []
        for i, c in enumerate(ciphertext):
            s = shifts[i % klen]
            plain_chars.append(ALPHABET[(ord(c) - ord('A') - s) % 26])
        pt = "".join(plain_chars)

        common_words = [
            "THE",
            "AND",
            "THIS",
            "THAT",
            "YOU",
            "FOR",
            "WITH",
            "HAVE",
            "NOT",
            "ARE",
            "ION",
            "ING",
            "ED ",
            " TO ",
            " OF ",
        ]
        word_score = sum(pt.count(w) for w in common_words)
        cs = chi_square_score(pt)
        candidates.append((word_score, -cs, klen, key, pt))

    candidates.sort(reverse=True)
    return candidates


if __name__ == "__main__":
    ct = (
        "ZQQCVBFGKFIMJWGTVLSJRIDQYDQNPBZXGFJRPEDYDZYHLLRLSAYXHLGQSZYXHLGEPRGGCLU"
        "HJAGWXGIIYNQWYFEQZDHLSFHKLLNGCLUKYNXIUMHTVUIIZUKKJZIHFYQN"
    )
    results = solve_vigenere(ct, max_key_len=24)
    for i, (w, negcs, k, key, pt) in enumerate(results[:10], start=1):
        print(f"{i}. k={k} key={key} word_score={w} chi2={-negcs:.2f}")
        print(pt)
        print()