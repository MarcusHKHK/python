#22.10.24 Marcus Krutto
#ülesanded 7 Loendid

import datetime

"""
#jukebox

muusika = ['ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"','Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"']

for i in range(len(muusika)):
    print(str(i+1)+". " +muusika[i])


try:
    valik = int(input("Vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    print("Midagi läks katki. Teavita adminni!")
"""

#Tänane kuu number
x = datetime.datetime.now()
tana = int(x.strftime("%m")) - 1 # -1 et loendiga ühildada


#12 Kuud

kuud = [["jaanuar",-13,5,28,-1,-19,-13,25,-3,11,16,-10,-9,-8,20,3,22,-20,-15,13,20,23,3,23,13,-14,-20,-7,1,-1,-8,18],
["veebruar",-1,21,-6,-14,-4,-12,23,27,-19,-18,7,5,22,-5,-9,16,16,23,17,21,0,-19,-3,28,20,-12,17,-7],
["märts",13,15,0,-10,16,-5,-10,-11,28,-9,20,9,20,-5,-16,25,-12,-1,-12,-16,24,4,-14,18,20,0,-17,-8,15,7,-16],
["aprill",19,28,16,8,28,24,22,16,26,28,9,-5,-8,28,13,-9,-9,11,-8,5,-8,-1,-3,11,-13,-5,23,-8,20,22],
["mai",13,23,-2,2,17,10,-3,-5,13,22,22,-6,25,17,6,-6,-14,-14,2,-17,-1,1,8,28,4,23,-15,4,24,-13,-18],
["juuni",-2,-7,7,25,29,-11,19,-8,11,-16,-12,5,-10,-16,15,11,11,29,-18,-8,-14,-13,11,18,19,14,26,1,11,16],
["juuli",8,-18,15,-8,26,21,17,6,26,4,18,18,-10,2,-18,-16,-7,25,-8,-7,-17,-15,6,-5,17,12,24,18,30,5,13],
["august",-16,17,20,21,16,13,19,-2,3,24,-14,-18,23,-17,-15,3,-11,0,-2,0,11,3,27,-5,6,3,-11,-4,-13,7,-8],
["september",-11,28,17,6,-12,30,-12,23,-7,25,26,8,17,-20,8,21,1,14,18,9,21,12,-7,-11,-19,-19,27,10,15,26],
["oktoober",30,24,29,27,25,-16,15,-3,1,-5,-15,13,-17,22,12,16,1,-14,20,24,0,-3,11,-7,-2,26,-19,2,10,6,18],
["november",20,28,5,-16,2,-12,-15,-5,7,25,30,-14,27,1,6,5,11,4,-2,19,10,-17,6,1,23,14,2,8,3,19],
["detsember",9,2,-19,30,26,21,6,-16,2,-17,-6,-2,-15,-1,21,27,30,-16,20,11,-12,10,-8,-18,19,14,-6,-8,1,26,13]]

#Ülesanded
print(kuud[tana][0])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine = []
for i in range(1,len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end=", ")

print()
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {sum(ajutine)/len(ajutine)}")

print(f"-20 esineb {ajutine.count(-20)} korda")

ajutine.pop(5)
print(ajutine)


