#Write a Python script to concatenate the following dictionaries to create a new one

d1 = {0:10,1:20}
d2 = {2:30,3:40}
d3 = {4:50,5:60}

d4 = {}

for d in (d1,d2,d3):
    d4.update(d)

print(d4)
