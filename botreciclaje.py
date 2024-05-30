import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Cargar las listas desde un archivo JSON
def cargar_listas():
    try:
        with open('listas_desechos.json', 'r') as file:
            data = json.load(file)
            return data['recic'], data['no_recic']
    except FileNotFoundError:
        return ["botella", "revista", "periódico", "caja", "papel", "cuaderno", "plástico", "lata", "madera", "vidrio", "madera", "pila"], ["pasta dental", "envoltorio"]

# Guardar las listas en un archivo JSON
def guardar_listas(recic, no_recic):
    with open('listas_desechos.json', 'w') as file:
        data = {'recic': recic, 'no_recic': no_recic}
        json.dump(data, file)

recic, no_recic = cargar_listas()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------------")

@bot.command()
async def basura(ctx):
    global recic, no_recic
    await ctx.send("Ingresa el desecho por el que quieres preguntar")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        message = await bot.wait_for("message", timeout=20, check=check)
        n1 = str(message.content).lower()
        
        if n1 in recic:
            await ctx.send("Tu desecho es reciclable")
        elif n1 in no_recic:
            await ctx.send("Tu desecho no es reciclable")
        else:
            await ctx.send("No sé nada sobre ese desecho.")
            await ctx.send("¿Podrías decirme si es reciclable o no reciclable?")
            try:
                message2 = await bot.wait_for("message", timeout=30, check=check)
                n2 = str(message2.content).lower()
                if n2 in ["reciclable", "es reciclable", "sí es", "si", "si es", "sí"]:
                    recic.append(n1)
                    await ctx.send("Gracias, lo añadiré a la lista de objetos reciclables")
                else:
                    no_recic.append(n1)
                    await ctx.send("Gracias, lo sumaré a la lista de objetos no reciclables")
                
                # Guardar las listas actualizadas en el archivo JSON
                guardar_listas(recic, no_recic)
                
            except ValueError:
                await ctx.send("Ingresa una cadena de texto")
                return
            except TimeoutError:
                await ctx.send("El tiempo de espera para responder se acabó")
                return
    except ValueError:
        await ctx.send("Ingresa una cadena de texto")
        return
    except TimeoutError:
        await ctx.send("Se acabó el tiempo de espera")
        return

@bot.command()
async def hablar(ctx):
    await ctx.send("¿Cómo consideras que son tus hábitos de reciclaje?")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try: 
        resp = await bot.wait_for("message",timeout=60,check=check)
    except TimeoutError:
        await ctx.send("Se acabó el tiempo")
        return 
    
    await ctx.send("Entiendo ¿Considerarías que puedes mejorar en algo?")
    try: 
        resp2 = await bot.wait_for("message",timeout=60,check=check)

    except TimeoutError:
        await ctx.send("Se acabó el tiempo de espera")
        return 
    

    
    await ctx.send("Me alegro por eso ¡ Parece ser que eres muy buen reciclador!")

@bot.command()
async def contar(ctx):
    await ctx.send("¿Cuántos objetos reciclaste aproximadamente hace dos días?")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try: 
        resp4 = await bot.wait_for("message",timeout=30,check=check)
        n4 = int(resp4.content)
    except ValueError:
        await ctx.send("Ingresa un número")
        return
    except TimeoutError:
        await ctx.send("Se acabó el tiempo de espera")
        return
    await ctx.send("¿Cuántos objetos reciclaste aproximadamente hace un día?")
    try: 
        resp5 = await bot.wait_for("message",timeout=30,check=check)
        n5 = int(resp5.content)
    except ValueError:
        await ctx.send("Ingresa un número")
        return
    except TimeoutError:
        await ctx.send("Se acabó el tiempo de espera")
        return
    await ctx.send("¿Cuántos objetos reciclaste aproximadamente hoy?")
    try:
        resp6 = await bot.wait_for("message",timeout=30,check=check)
        n6 = int(resp6.content)
    except ValueError:
        await ctx.send("Ingresa un número")
        return
    except TimeoutError:
        await ctx.send("Se acabó el tiempo de espera")
        return
    
    prom= ((n4+n5+n6)/3)*7
    await ctx.send(f"¡Si sigues así, podrías reciclar cerca de {int(prom)} objetos al cabo de una semana!")

bot.run("token")
