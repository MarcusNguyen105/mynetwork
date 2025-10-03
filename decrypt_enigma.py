from enigma.machine import EnigmaMachine
import math


DAY_KEYS = [
    # (day, rotors, rings, plugs)
    (1,  "VIII II III",  "24 09 04",  "CY DQ EP FH GW JL NV OU RX SZ"),
    (2,  "V IV II",      "18 25 15",  "AW CI DY EF GV HT JL KO NS UZ"),
    (3,  "VII IV I",     "03 18 09",  "AJ CZ DL EO FK GS HW NU PR VX"),
    (4,  "VIII VII VI",  "08 21 12",  "AU BW DX EI FJ HS KP MQ NV RT"),
    (5,  "IV VII II",    "01 26 09",  "AG BM CW ER FJ IT KO PS UY VX"),
    (6,  "V VI VII",     "18 01 24",  "AN CK DX FQ GL HY IU JR OZ PV"),
    (7,  "II VI III",    "05 13 20",  "AQ CU DN ES GO IL JV MZ RX WY"),
    (8,  "VIII II VI",   "12 02 23",  "AD BN CP EG HO JW KQ LX TY VZ"),
    (9,  "IV III VI",    "15 08 13",  "AQ BI CL DM EV FK JP NS OZ TU"),
    (10, "VII VIII II",  "14 20 06",  "AR BO CF EK GM HZ JN PX QV WY"),
    (11, "II VI VIII",   "23 19 15",  "CQ DS EZ FL GJ HK MX NY OT PR"),
    (12, "II VI I",      "25 23 20",  "AG EM FY IX JO KR LU NW QS TZ"),
    (13, "VI I II",      "19 15 01",  "AN BL DR EO FQ GS HP IJ TY VW"),
    (14, "III VII IV",   "15 17 04",  "AD BO FK GI HW LY MP NS RX TZ"),
    (15, "III IV I",     "07 19 08",  "AN CS DY FT HZ IM JL OX QW RU"),
    (16, "II IV VII",    "09 02 19",  "AE BS CQ FU GX IT JV KL MW OR"),
    (17, "VI II IV",     "05 13 26",  "AO BS CQ DP EF GN JL KW TY UZ"),
    (18, "VIII VI VII",  "13 02 15",  "AT BV CJ DO EP FY GZ LW MQ NU"),
    (19, "II VII I",     "01 21 24",  "BH CM DU FP GL IO KT QY RW VX"),
    (20, "VIII IV VI",   "10 22 06",  "AR BN DI GP HQ KZ LU MS TX WY"),
    (21, "I VI II",      "13 06 10",  "AX BU CK EL GN HP IO JY MR QV"),
    (22, "VIII III VI",  "20 03 17",  "BD CP EH FO JW KX LU NQ RZ SV"),
    (23, "VII II I",     "19 23 08",  "AX BH CM DY FZ IJ KW LP QV RU"),
    (24, "IV III II",    "11 03 22",  "CH DU EX FZ JT KP LY MR OW QS"),
    (25, "IV V I",       "12 16 08",  "AL DV EX FP HN JU KS MR QY WZ"),
    (26, "VIII II IV",   "24 10 23",  "AX BZ CI DU FY GH KO LP MW NR"),
    (27, "VII IV VI",    "13 17 01",  "AB CJ DZ EL FM GY HX IK RU VW"),
    (28, "VII VI IV",    "13 21 12",  "AU CP DK HY IW JX MQ OZ RS TV"),
    (29, "V IV VIII",    "08 23 20",  "AS BW CF DT EM IZ JQ LV PY RU"),
    (30, "II VI VIII",   "20 12 15",  "AE BX CU DF HZ JO LS MN QY VW"),
]

# Map of day to kenngruppen from the table
KENNGRUPPEN = {
    1: ["LQC", "ZRR", "NOW", "AIO"],
    2: ["PDG", "VMK", "UBM", "FMX"],
    3: ["POQ", "EPJ", "LLZ", "FYL"],
    4: ["ABF", "QON", "QDK", "CBR"],
    5: ["YFS", "ZDZ", "QAW", "VZM"],
    6: ["IGG", "CRF", "BIL", "HHF"],
    7: ["EZU", "YZQ", "RTP", "ENI"],
    8: ["ZAS", "UDW", "EDA", "FDZ"],
    9: ["CXZ", "ORI", "ISE", "IFC"],
    10: ["TFZ", "UQH", "UMO", "MPA"],
    11: ["DUQ", "ONH", "VWG", "BRY"],
    12: ["HNR", "PQV", "HMN", "GLW"],
    13: ["KHL", "MLP", "LIB", "QAV"],
    14: ["CMV", "XSW", "XDS", "VQO"],
    15: ["XMO", "EBZ", "SLT", "TML"],
    16: ["OKU", "GAE", "JDZ", "TJQ"],
    17: ["BWW", "HZE", "QQZ", "CFK"],
    18: ["LCE", "VZK", "WPV", "EVM"],
    19: ["GPP", "SHJ", "OQW", "ETU"],
    20: ["YGC", "WHF", "YDK", "UML"],
    21: ["BCI", "VKY", "FIH", "FAC"],
    22: ["QME", "ARA", "PRP", "BRA"],
    23: ["ANG", "IRG", "HLO", "UHZ"],
    24: ["OVE", "FSQ", "WDQ", "CGQ"],
    25: ["HIP", "UMA", "PBQ", "MJE"],
    26: ["QRN", "TOX", "GRT", "BNQ"],
    27: ["IND", "PNB", "EPL", "CFH"],
    28: ["VQF", "TKL", "BQV", "DJU"],
    29: ["PDZ", "DJE", "AFY", "ABJ"],
    30: ["AZG", "IGN", "UKY", "YPL"],
}


INDICATOR = "GZVDBR"
CIPHERTEXT_GROUPS = [
    "XLWHF", "DJKUC", "ZONWZ", "UFDGB", "SIILK",
    "GSOBR", "NPPMF", "BWFTU", "CHPCO", "UUBMB",
    "NUUMW", "HMPJG", "JGJPM", "AXKPY", "FENEP",
    "LKHGM", "LUPUJ", "WWCZO", "YATTS", "CBSKI",
    "QFKSG", "ADRPZ", "J",
]


def strip_kenngruppen(groups: list[str], kenngruppen: list[str]) -> list[str]:
    return [g for g in groups if g not in kenngruppen]


def build_machine(reflector: str, rotors: str, rings: str, plugs: str) -> EnigmaMachine:
    return EnigmaMachine.from_key_sheet(
        rotors=rotors,
        reflector=reflector,
        ring_settings=rings,
        plugboard_settings=plugs,
    )


def find_message_key(reflector: str, rotors: str, rings: str, plugs: str) -> tuple[str, str] | tuple[None, None]:
    machine = build_machine(reflector, rotors, rings, plugs)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                grund = f"{a}{b}{c}"
                machine.set_display(grund)
                decoded = machine.process_text(INDICATOR)
                if decoded[:3] == decoded[3:6]:
                    return grund, decoded[:3]
    return None, None


def decrypt_body(reflector: str, rotors: str, rings: str, plugs: str, msg_key: str, skip_groups: int) -> str:
    machine = build_machine(reflector, rotors, rings, plugs)
    machine.set_display(msg_key)
    body_ct = "".join(CIPHERTEXT_GROUPS[skip_groups:])
    return machine.process_text(body_ct)


def main() -> None:
    # Auto-detect day by finding a Kenngruppe embedded in the first few groups
    joined_groups = CIPHERTEXT_GROUPS[:4]
    candidate_days = []
    for day, groups in KENNGRUPPEN.items():
        for g in joined_groups:
            for k in groups:
                if k in g:
                    candidate_days.append((day, k, g))
    if candidate_days:
        # De-duplicate days
        days = sorted(set(d for d, _, _ in candidate_days))
        print(f"Kenngruppe suggests days: {days} -> details: {candidate_days}")
    else:
        print("No Kenngruppe match found in first groups")
    # Focused decode: Day 20 using header Grundstellung GZV and doubled indicator starting after first group
    rotors20, rings20, plugs20 = "VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY"
    machine20 = build_machine("B", rotors20, rings20, plugs20)
    try:
        machine20.set_display("GZV")
        after_first = "".join(CIPHERTEXT_GROUPS[1:])
        indicator_ct = after_first[:6]
        decoded = machine20.process_text(indicator_ct)
        if decoded[:3] == decoded[3:6]:
            msg_key = decoded[:3]
            machine20 = build_machine("B", rotors20, rings20, plugs20)
            machine20.set_display(msg_key)
            body_pt = machine20.process_text(after_first[6:])
            print(f"Day20 direct: Grund GZV -> msg_key {msg_key}")
            print(body_pt)
            if "USCC{" in body_pt:
                print("Flag found in day20 direct.")
                return
    except Exception as e:
        pass
    # Use detected day(s) and try classic doubled-indicator recovery after the Kenngruppe-bearing group
    ct_groups = CIPHERTEXT_GROUPS
    for day in sorted(set(d for d, _, _ in candidate_days)):
        rotors, rings, plugs = next((r, ri, p) for d, r, ri, p in DAY_KEYS if d == day)
        # Find index of embedded kenngruppe group
        kgroups = KENNGRUPPEN[day]
        kg_index = None
        for idx, grp in enumerate(ct_groups[:5]):
            if any(k in grp for k in kgroups):
                kg_index = idx
                break
        if kg_index is None or kg_index + 2 >= len(ct_groups):
            continue
        indicator_ct = (ct_groups[kg_index + 1] + ct_groups[kg_index + 2])[:6]
        print(f"Day {day}: trying indicator {indicator_ct} after group {kg_index}")
        for reflector in ("B", "C"):
            machine = build_machine(reflector, rotors, rings, plugs)
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            found = False
            for a in alphabet:
                for b in alphabet:
                    for c in alphabet:
                        grund = f"{a}{b}{c}"
                        machine.set_display(grund)
                        decoded = machine.process_text(indicator_ct)
                        if decoded[:3] == decoded[3:6]:
                            msg_key = decoded[:3]
                            # Decrypt remainder after the 6 letters
                            body = "".join(ct_groups[kg_index + 1:])
                            body = body[6:]
                            m2 = build_machine(reflector, rotors, rings, plugs)
                            m2.set_display(msg_key)
                            pt = m2.process_text(body)
                            print(f"SUCCESS day {day} UKW {reflector} Grund={grund} Key={msg_key}")
                            if "USCC{" in pt:
                                print(pt)
                                return
                            # Show a snippet to inspect
                            print(pt[:220])
                            found = True
                            break
                    if found:
                        break
                if found:
                    break

    # Direct attempt using provided header for day 20: Grundstellung GZV, message key DBR
    rotors20, rings20, plugs20 = "VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY"
    for reflector in ("B", "C"):
        machine = build_machine(reflector, rotors20, rings20, plugs20)
        machine.set_display("DBR")
        for num_skip in range(0, 4):
            pt = machine.process_text("".join(CIPHERTEXT_GROUPS[num_skip:]))
            if "USCC{" in pt:
                print(f"Flag found with Day20 UKW {reflector} skip={num_skip}:")
                print(pt)
                return
        # reset machine between different skip tests

    for day, rotors, rings, plugs in DAY_KEYS:
        for reflector in ("B", "C"):
            # Try both given and reversed rotor order (with rings reversed to match rotors)
            rotor_variants = [
                (rotors, rings, "as-is"),
                (" ".join(reversed(rotors.split())), " ".join(reversed(rings.split())), "reversed"),
            ]
            for rotors_v, rings_v, tag in rotor_variants:
                grund, msg_key = find_message_key(reflector, rotors_v, rings_v, plugs)
                if not msg_key:
                    continue
                print(f"Day {day} ({tag}): UKW {reflector}, Grund {grund}, Key {msg_key}")
                for num_skip in range(0, 11):
                    pt = decrypt_body(reflector, rotors_v, rings_v, plugs, msg_key, num_skip)
                    if "USCC{" in pt:
                        print("Flag found:")
                        print(pt)
                        return
                    if any(token in pt for token in ("USCC", "FLAG", "DER", "UND", "DIE", "EIN", "IST")):
                        print(f"Candidate day={day} ukw={reflector} order={tag} skip={num_skip}: {pt[:220]}")

    # Remove day 20 Kenngruppen groups from body and decrypt with solved key BLC
    kenngruppen20 = ["YGC", "WHF", "YDK", "UML"]
    filtered = strip_kenngruppen(CIPHERTEXT_GROUPS, kenngruppen20)
    m = build_machine("B", "VIII IV VI", "10 22 06", "AR BN DI GP HQ KZ LU MS TX WY")
    m.set_display("BLC")
    pt = m.process_text("".join(filtered))
    print("After removing Kenngruppen (day20) and decrypting with BLC:")
    print(pt)
    if "USCC{" in pt:
        print("Flag found after Kenngruppe filtering")
        return

    # Brute-force day 20 initial rotor display over all 26^3 for both reflectors
    # searching for USCC in plaintext, ignoring indicator conventions
    print("Brute-forcing day 20 rotor starts for USCC pattern...")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ct_full = "".join(CIPHERTEXT_GROUPS)
    for reflector in ("B", "C"):
        for rotors, rings, tag in [
            ("VIII IV VI", "10 22 06", "as-is"),
            ("VI IV VIII", "06 22 10", "reversed"),
        ]:
            count = 0
            for a in alphabet:
                for b in alphabet:
                    for c in alphabet:
                        count += 1
                        m = build_machine(reflector, rotors, rings, "AR BN DI GP HQ KZ LU MS TX WY")
                        m.set_display(f"{a}{b}{c}")
                        pt = m.process_text(ct_full)
                        if "USCC{" in pt:
                            print(f"Found flag under day20 ukw={reflector} order={tag} display={a}{b}{c}")
                            print(pt)
                            return
            print(f"Completed brute-force for UKW {reflector} {tag}: {count} starts tested")

    # If not found, brute-force day 20 message key and score German likelihood
    def german_score(text: str) -> float:
        # Rough log-score based on common bigrams/trigrams; not precise but helps
        common = [
            "DER", "DIE", "UND", "EIN", "ICH", "NICHT", "DAS", "IST", "SIE", "MIT",
            "DEN", "HAB", "AUF", "FUR", "VON", "WIE", "WER", "WIR", "ZU", "ZUR",
        ]
        score = 0.0
        up = text
        for token in common:
            score += math.log(1 + up.count(token))
        # penalize too many rare letters
        penalty = sum(up.count(ch) for ch in "QXJ") * 0.2
        return score - penalty

    day, rotors, rings, plugs = next(x for x in DAY_KEYS if x[0] == 20)
    best = []  # list of tuples (score, key, pt_snippet)
    for reflector in ("B",):  # UKW B is historically correct for 1939 Army/Airforce
        machine = build_machine(reflector, rotors, rings, plugs)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # decrypt body given key
        def decrypt_with_key(k: str) -> str:
            m = build_machine(reflector, rotors, rings, plugs)
            m.set_display(k)
            return m.process_text("".join(CIPHERTEXT_GROUPS))

        # full brute force
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    key = f"{a}{b}{c}"
                    pt = decrypt_with_key(key)
                    sc = german_score(pt)
                    if len(best) < 10 or sc > best[0][0]:
                        best.append((sc, key, pt[:220]))
                        best.sort(key=lambda t: t[0])
                        if len(best) > 10:
                            best.pop(0)
        print("Top candidates for day 20 (UKW B) by score:")
        for sc, key, snip in sorted(best, key=lambda t: -t[0])[:10]:
            print(f"Key {key} score {sc:.2f}: {snip}")

    print("Failed to recover plaintext with day 20 settings.")


if __name__ == "__main__":
    main()

