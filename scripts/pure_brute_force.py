import json

PWS = "data/pw_dicts/processed/unique_pws.json"

pws = []
with open(PWS) as f:
    pws = set(json.load(f))
    print str(len(pws)) + "unique passwords to crack"

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
NUM = '0123456789'

# Print out some states
num_with_upper = 0
num_with_lower = 0
num_with_num = 0

# count lower
for pw in pws:
    for c in pw:
        if c in LOWER:
            num_with_lower += 1
            break
print str(num_with_lower) + " password with lowercase characters found (" + str(100.0*num_with_lower/len(pws)) + "%)"
   
# count lower
for pw in pws:
    for c in pw:
        if c in UPPER:
            num_with_upper += 1
            break
print str(num_with_upper) + " password with uppercase characters found (" + str(100.0*num_with_upper/len(pws)) + "%)"

# count lower
for pw in pws:
    for c in pw:
        if c in NUM:
            num_with_num += 1
            break
print str(num_with_num) + " password with numerical characters found (" + str(100.0*num_with_num/len(pws)) + "%)"



cracked_pws = set()
def attempt_pw(str_so_far, max_depth, char_set):
    if str_so_far in pws:
        # print "Cracked " + str_so_far
        cracked_pws.add(str_so_far)

    if len(str_so_far) >= max_depth:
        return

    for c in char_set:
        attempt_pw(str_so_far + c, max_depth, char_set)

print "Brute forcing all 6 character lowercase passwords"
attempt_pw('', max_depth=6, char_set=LOWER)
print str(len(cracked_pws)) + " passwords were cracked (" + str(100.0*len(cracked_pws)/len(pws)) + "%)"

print "Brute forcing all 5 character lowercase/numerical passwords"
cracked_pws = set()
attempt_pw('', max_depth=5, char_set=LOWER + NUM)
print str(len(cracked_pws)) + " passwords were cracked (" + str(100.0*len(cracked_pws)/len(pws)) + "%)"

print "Brute forcing all 5 character alphanumeric passwords"
cracked_pws = set()
attempt_pw('', max_depth=5, char_set=LOWER + UPPER + NUM)
print str(len(cracked_pws)) + " passwords were cracked (" + str(100.0*len(cracked_pws)/len(pws)) + "%)"
