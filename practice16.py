#Write a Python script to merge two Python dictionaries

d1 = { 'a':9,'b':8}
d2 = { 'c':7,'d':6}

d = d1.copy()

d.update(d2)

print(d)
