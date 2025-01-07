#Marcus Krutto 12.18.2024
#Marcus Krutto  10 7 8 12 17

import random

# 7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# 	küsitakse valuuta kogust ja tehakse arvutused - 2p
# 	kood kommenteeritud - 1p

#Euro kalkulaator
"""
eur = 15.64
eek = 0.06

a = int(input("Vali millist valuutat (1: EUR->EEK; 2: EEK->EUR): "))

#Valuuta arvutamine

if a==1:
    b = int(input("Palju sul on Eurosi: "))
    c = b*eur
    print(f"Sul on nii palju EEK: {c}")
elif a==2:
    d = int(input("Palju sul on Eesti kroone: "))
    e = d*eek
    print(f"Sul on nii palju EUR: {e}")
else:
    print("Tegid vale valiku.")
"""

# 8. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p
"""
#Täringu Casino
loop = 1
while loop==1:
     #Konto
     print("Arvuti ei panusta üle 100!!!!")
     konto = int(input("Kui palju teie kontol raha on: "))
     kontoarvuti = 100
     kontoinimene = [] 
     if konto >= 0:
         kontoinimene.append(konto)
     else:
         print("Vabandan, kontol ei ole piisavalt raha!")
     panus = int(input("Kui palju te panustate: "))
     arvpanus = random.randrange(1,kontoarvuti)
     for i in range(len(kontoinimene)):
         kontoinimene[i] -= panus
     panusk = panus + arvpanus
     print(f"Panused on: Arvuti: {arvpanus}; Inimene: {panus}; Panuseid kokku: {panusk}")
     #Arvuti täringud
     arvt1 = random.randrange(1,7)
     arvt2 = random.randrange(1,7)
     #Inimese täringud
     inmt1 = random.randrange(1,7)
     inmt2 = random.randrange(1,7)
     #Tärinug võrdlus
     arvts = arvt1+arvt2
     inmts = inmt1+inmt2
     print(f"Arvuti täringu summa: {arvts}")
     print(f"Inimese täringu summa: {inmts}")
     if arvts <= inmts:
         for i in range(len(kontoinimene)):
             kontoinimene[i] += panusk
         print(f"Inimene võitis selle summa {panusk}")
         print(f"Kontol on {kontoinimene}€")
     else:
         print(f"Inimene kaotas :(")
"""
#  10. Kaugushüpe
#  kasutaja sisestab 3 kaugushüppe tulemust - 1p
#  sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
#  programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
#  kood kommenteeritud - 1p        
"""

#Kaugushüpe
kaugus = []
a = 1
for i in range(3):
    kysi = int(input(f"{a}.Esimene kaugushüpe kaugus: "))
    a = a+1
    kaugus.append(kysi)
#Vastused
print(f"Kõige pikkem hüpe oli {max(kaugus)}")
print(f"Keskmine hüpe kaugus oli {sum(kaugus)/len(kaugus)}")
"""


# 17. Email
# 	Kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	Programm kontrollib kas email on sisestatud õigesti
# 	Programm tükeldab selle ja väljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com

email = "marcus.krutto@gmail.com"
if "@" not in email:
    print("Sisestasite emaili valesti!")
a = email.split(".")

print(f"Tere {a[0]}, sinu email on server serveris ja domeeniks on sul com")











