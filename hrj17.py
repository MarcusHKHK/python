#Marcus Krutto 29.11.2024
#Haarjutus 17

"""
fail = open("pangakonto.txt")
loend = (fail.readlines())

print(f"Tehinguid kokku {len(loend)}")

positiivne = []

for i in loend:
    if float(i)>0:
        positiivne.append(float(i))     
        positiivne.count()

print(f"Nii palju positiivseid tehinguid: {}")

"""







fail = open("palgad.txt")
andmed = (fail.readlines())

mehed = []
naised = []

for i in andmed:
    x = (str(i.split(",")[3]))
    y = (str(i.split(",")[6]))
    if x =='Mees':
        mehed.append(float(y))
    else:
        naised.append(float(y))


print("Meeste keskmine palk:",sum(mehed)/len(mehed))
print("Naiste keskmine palk:",sum(naised)/len(naised))



