#08.11.2024 Marcus Krutto IT-24
#Harjutus 11

# def pikim_sõna(*sonad):
#     pikim = 0
#     for i in sonad:
#         if len(i)>pikim:
#             pikim=len(i)
#     print(f"Pikim sõna on {pikim} märki!")



# pikim_sõna("üks", "kaks", "kolmsada", "INFGAIJFBNNEGUIONWR")

def kolm_pikim_sõnad(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)*3>pikim:
            pikim=len(i)
    print(f"Pikim sõna on {pikim} märki!")


kolm_pikim_sõnad("üks", "kaks", "kolmsada", "INFGAIJFBNNEGUIONWR")




