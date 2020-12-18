import hashlib

input = 'iwrupvqb'
for i in range(1_000_000):
    if hashlib.md5((input + str(i)).encode('utf-8')).hexdigest().startswith('0' * 5):
        print(i)
        break
for i in range(i, 1_000_000_000):
    if hashlib.md5((input + str(i)).encode('utf-8')).hexdigest().startswith('0' * 6):
        print(i)
        break
