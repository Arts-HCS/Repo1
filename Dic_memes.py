import random

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "XD": "Una risa o simbolismo de la misma",
    "MELO": "Genial o bueno",
    "PARCERO": "Amigo o conocido"
}

print("¿Qué palabra no entiendes? ")
palabra = input("=  ").upper()

if palabra in meme_dict: 
    print(palabra, "significa", meme_dict[palabra])
    
else: 
    print("Esa palabra no se encuentra, pero te puedo dar otra: ")
    clave = random.choice(meme_dict.keys())
    print(clave+" significa",meme_dict[clave])
