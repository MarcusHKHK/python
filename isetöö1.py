#Marcus Krutto 15.5.2024
#Iseseisev töö

import random
import os

# print("Tere, maailm!")

# aasta = 2020
# liblikas = "teelehe-mosaiikliblikas"
# lause_keskosa = "aasta liblikas on"
# lause = aasta, lause_keskosa, liblikas
# print(lause)

#Pilved

# vastus = float(input("Pilvede aluse kõrgus (kilomeetrites): "))
# number = float()
# if number>=6.0:
#     print("Need on ülemised pilved!")
# else:
#     print("Need ei ole ülemised pilved!")


# #bussid
# print("Palun sisestada ainult täisarvud!")
# inimesed = int(input("Mitu inimest on vaja transpordida: "))
# kohtade_arv = int(input("Mitu istekohta on bussis: "))

# a = inimesed//kohtade_arv
# b = inimesed%kohtade_arv
# if inimesed==kohtade_arv:
#     print(f"Selle arvu inimeste transportimiseks on vaja {a} arv busse, viimases bussis istub {a}")
# else:
#     print(f"Selle arvu inimeste transportimiseks on vaja {a} arv busse, viimases bussis istub {b}")


# #Hommik

# a = int(input("Mitu korda on vaja äratada: "))
# for i in range(a):
#     print("On hommik, aeg on üles tõusta")


# #Jänese majustused
# ringide_arv = 4
# i = 1
# porgandite_arv = 0
# while i<=ringide_arv:
#     if i%2==0:
#         porgandite_arv + i
#         print(i)
#     i =+ 1
# print(f"Porgandite koguarv on: {porgandite_arv}")


#Täringud
# taring = int(input("Mitu täringut on vaja visata: "))
# for i in range(taring):
#      a = random.randrange(1,6)
#      print(a)


#Male
# i = 0

# while i==0:
#     taisarv = int(input("Palun sisesta üks täisarv: "))
#     if taisarv == 1:
#         print(f"Nisuteri {taisarv}. ruudu eest saab: 1")
#         i+1
#     else:
#         a = taisarv-1
#         print(f"Nisuteri {taisarv}. ruudu eest saab: {2**a}")
#         i+1

#Õunad
# poialpoiss = int(input("Mitu pöialpoissi soovib õuna (1-7): "))
# b = []
# for i in range(poialpoiss):
#     a = random.randint(1,2)
#     print(a)
#     b.append(a)
# print(f"Lumivalgekesele jäi {14-sum(b)} arv õuna")



#Vastuvõetud

fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
print(fail)
for rida in fail:
    vastuvõetud.append(int(rida))
    fail.close()

print(vastuvõetud)























