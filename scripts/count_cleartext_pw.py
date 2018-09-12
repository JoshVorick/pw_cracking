import json

OUTPUT = "data/pw_dicts/processed/unique_pws.json"
PW_DICTIONARIES = [
        "data/pw_dicts/1000000-password-seclists.txt",
        "data/pw_dicts/8-more-passwords.txt",
        "data/pw_dicts/uniqpass-v16-passwords.txt",
        "data/pw_dicts/38650-password-sktorrent.txt",
        "data/pw_dicts/bitcoin-brainwallet.lst.txt"
    ]

pws = []
for file_name in PW_DICTIONARIES:
    with open(file_name) as f:
        pws.extend(f.readlines())

pws = [pw.strip() for pw in pws]
print len(pws)

# Count num occurrences
cnt = {}
for pw in pws:
    if pw in cnt:
        cnt[pw] = cnt[pw] + 1
    else:
        cnt[pw] = 1

print len(cnt.keys())
print len(pws) - len(cnt.keys())

with open(OUTPUT, 'w') as f:
    f.write(json.dumps(cnt.keys()))
