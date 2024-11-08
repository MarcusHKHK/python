#08.11.2024 Marcus Krutto IT-24

#import
import random

# Arvude keskmine
# Koostage Pythoni programm, mis küsib kasutajalt arve ükshaaval. Programm peaks jätkama arvude küsimist ja nende vastuvõtmist seni, kuni kasutaja jätab sisestuse tühjaks (st vajutab sisestusklahvi ilma midagi kirjutamata).
# Programm peab kasutama while-tsüklit arvude küsimiseks ja nende salvestamiseks.
# Pärast seda, kui kasutaja lõpetab arvude sisestamise peab programm arvutama ja väljastama kõikide sisestatud arvude keskmise väärtuse.

# arvud = []
# loop = 1

# while loop == 1:
#     arv = input("Lisa arv: ")
#     if arv=="":
#         break
#     arvud.append(int(arv))
    
# print(sum(arvud)/len(arvud))



# Arvu äraarvamise mäng
katsed = []
loop = 1
arvamused = 0
suv = random.randint(1,10)
print(suv)


while loop == 1:
    arva = int(input("Arva arv 1-10: "))
    arvamused+=1
    if arva == suv:
        print("Õige!")
        print(f"Proovisid arvata {arvamused} korda!")
        katsed.append(arvamused)
        uuesti = input("Soovid uuesti? (j/e): ")
        if uuesti=="j":
            suv = random.randint(1,10)
            arvamused = 0
        else:
            break
    else:
        print("Vale vastus, proovi uuesti!")
print("GameOver")
print(katsed)








