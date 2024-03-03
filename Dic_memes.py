import random

meme_dict = {
    "CRINGE": "algo excepcionalmente raro o embarazoso",
    "LOL": "una respuesta común a algo gracioso",
    "XD": "una risa o simbolismo de la misma",
    "MELO": "genial o bueno",
    "PARCERO": "amigo o conocido"
}

print("¿Qué palabra no entiendes? ")
palabra = input("=  ").upper()

if palabra in meme_dict: 
    print(palabra, "significa", meme_dict[palabra])
    
else: 
    print("Esa palabra no se encuentra, pero te puedo dar otra: ")
    clave = random.choice(list(meme_dict.keys()))

    print(clave+" significa",meme_dict[clave])
