#Marcus Krutto 15.01.25
#Harjutus 22

from datetime import datetime, timedelta
import dateparser

# Kuva praegune päev, kuu, aasta, tund, minut
# Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S
# Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled
# Kuva vanus aastates
# Kuva, kas tegemist on juubeliaastaga

sp = datetime(2010, 1, 14)
now = datetime.now()
print(now)
print(now.strftime("%d.%m.%Y %H:%M:%S"))

#Vanus

vanus = now - sp
print("Minu vanus: ", vanus.days)
print("Minu vanus: ", now.year-sp.year)

#Juubel
if int(vanus.days/365)%5==0:
    print("See on juubeli aasta.")
else:
    print("See ei ole juubeli aasta.")