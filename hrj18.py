#Python hrj18 Marcus Krutto
#07.01.2025

#Import

import csv

#Faili töötlus
meeskonnad = {}

faili_nimi = "EstonianBasketballGames.csv"

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    dict_rreader = csv.DictReader(fail)

    for rida in dict_rreader:
        if rida["Team 1"] not in meeskonnad:
            mk1 = rida["Team 1"]
            meeskonnad[mk1] = 0
        if rida["Team 1"] in meeskonnad:
            mk1 = rida["Team 1"]
            meeskonnad[mk1] += 1
        
        if rida["Team 2"] not in meeskonnad:
            mk2 = rida["Team 2"]
            meeskonnad[mk2] = 0
        if rida["Team 2"] in meeskonnad:
            mk2 = rida["Team 2"]
            meeskonnad[mk2] += 1

#Mitu osales

print(f"Osales: {len(meeskonnad)} meeskonda")

#Salvestan csv faili

with open('meeskonnad.csv', 'w', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file, lineterminator='\n')
    for key, value in meeskonnad.items():
       writer.writerow([key, value])