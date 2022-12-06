import re


def is_valid(d):
    return (
        d["byr"]
        and d["iyr"]
        and d["eyr"]
        and d["hgt"]
        and d["hcl"]
        and d["ecl"]
        and d["pid"]
    )


def check_yr(val, start, stop):
    p = re.compile("^[0-9]{4}$")
    if not p.match(val):
        return False
    return start <= int(val) <= stop


def check_hgt(val):
    p = re.compile("([0-9]*)(cm|in)$")
    a = p.match(val)
    if not a:
        return False
    if a.group(2) == "cm":
        return 150 <= int(a.group(1)) <= 193
    elif a.group(2) == "in":
        return 59 <= int(a.group(1)) <= 76
    return False


def check_hcl(val):
    p = re.compile("^#[0-9a-f]{6}$")
    return bool(p.match(val))


def check_ecl(val):
    if val in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    return False


def check_pid(val):
    p = re.compile("^[0-9]{9}$")
    return bool(p.match(val))


with open("input04.txt", "r") as f:
    lines = f.readlines()

p = re.compile("([0-9A-Za-z]*):([#0-9A-Za-z]*)")

for part1 in (True, False):
    valid = 0
    fields = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": False,
    }
    for line in lines:
        if line == "\n":
            if is_valid(fields):
                valid += 1
            fields = {
                "byr": False,
                "iyr": False,
                "eyr": False,
                "hgt": False,
                "hcl": False,
                "ecl": False,
                "pid": False,
                "cid": False,
            }
            continue
        for key, val in p.findall(line):
            if part1:
                if key in fields.keys():
                    fields[key] = True
            else:
                # Part 2
                if key == "byr":
                    fields[key] = check_yr(val, 1920, 2002)
                elif key == "iyr":
                    fields[key] = check_yr(val, 2010, 2020)
                elif key == "eyr":
                    fields[key] = check_yr(val, 2020, 2030)
                elif key == "hgt":
                    fields[key] = check_hgt(val)
                elif key == "hcl":
                    fields[key] = check_hcl(val)
                elif key == "ecl":
                    fields[key] = check_ecl(val)
                elif key == "pid":
                    fields[key] = check_pid(val)
                elif key == "cid":
                    fields[key] = True

    if is_valid(fields):
        valid += 1
    print(valid)
