import discord
import random
from funcs import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

ultima_accion = None

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)



def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS" 

@client.event
async def on_message(message):
    global ultima_accion
    if message.author == client.user:
        return
    new = message.content.lower()
    if new.startswith('hola'):
        ultima_accion = ("hola", )
        await message.channel.send('¡Hola! Soy un bot')
    elif new.startswith('sonrie'):
        ultima_accion = ("sonrie",)
        await message.channel.send(gen_emodji())
    elif new.startswith('volado'):
        ultima_accion = ("volado", )
        await message.channel.send(flip_coin())
    elif new.startswith('password'):
        ultima_accion = ("password", )
        await message.channel.send("Tu contraseña es: "+ gen(10))
    elif new.startswith('adios'):
        ultima_accion = ("adios", )
        await message.channel.send("¡Adios!")
    elif new.startswith("otra vez"):
        if ultima_accion:
            if ultima_accion[0] == "hola":
                await message.channel.send('¡Hola! Soy un bot')
            elif ultima_accion[0] == "sonrie":
                await message.channel.send(gen_emodji())
            elif ultima_accion[0] == "volado":
                await message.channel.send(flip_coin())
            elif ultima_accion[0] == "password":
                await message.channel.send("Tu contraseña es: "+ gen(10))
            elif ultima_accion[0] == "adios":
                await message.channel.send("¡Adios!")
        else:
            await message.channel.send("No hay una acción anterior para repetir.")
    else:
        await message.channel.send("No te entiendo, prueba con otro comando")



client.run("Token")
