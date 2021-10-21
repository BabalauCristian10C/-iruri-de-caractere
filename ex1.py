#a
sirul = "ABAZBJDSAISD21MAdsaBBMATO"
count = 0
for a in sirul:
    if a == "A":
        count = count+ 1;

print(count)
#b
dublicate = ""
for a in sirul:
    if a == "A":
        dublicate =dublicate+ "*"
    else:
        dublicate = dublicate+ a
print(dublicate)
#c
dublicate_two = ""
for a in sirul:
    if a != "B":
        dublicate_two = dublicate_two +a;
print(dublicate_two)
#d
print(sirul.count("MA"))
#e
x = sirul.replace("MA","TA")
print(x)
#f
g = sirul.replace("TO","")
print(g)
#g 
dublicate_g=""
for i in range(len(sirul)-1, -1, -1):
    dublicate_g = dublicate_g+sirul[i]
print(dublicate_g)