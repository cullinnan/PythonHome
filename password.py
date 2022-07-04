import random
chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!@#()$%^&* '
s = ''
user = ''
count = 0
with open('password.txt', 'rt') as file:
    res = file.read()
while len(s) <= len(res):
    s += random.choice(chars)
    if s == res[0]:
        count += 1
        res = res[1:]
        user += s
    else:
        count += 1
        s = ''
        continue
print(f'Password - {user}\ncount - {count}')