#Marcus Krutto 15.11.2024
#Harjutus 12



# def temperatuur(temp,yhik):
#     """
#     See on maailma parim manual 
#     Parameetrid: kui ei tea, siis ei tea
#     Näide: uuri ise
#     """
#     if yhik == "c":
#         v = temp * 5/9 + 32 
#     else:
#         v = (temp - 32) * 5/9
#     return v

# print(temperatuur(3,"c"))
# print(temperatuur(3,"f"))
"""
#kytusekulu
kytuskulu = lambda x, y: (x/100) * y
print(kytuskulu(5, 150))
"""




pangakonto = 15


def konto_haldur(saldo, toiming, summa):
    """
    Eriti oluline dokumentatsioon, et kõik aru saaks
    """
    global pangakonto
    if toiming=="deposiit":
        summa+=saldo
        pangakonto = summa
    else:
        summa = summa - saldo

    pangakonto = summa

    return summa

print(konto_haldur(20,"deposiit", pangakonto))
print(konto_haldur(50,"deposiit", pangakonto))
print(konto_haldur(150,"väljavõte", pangakonto))








