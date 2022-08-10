import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def expo(ctx,   keko):
    await ctx.message.delete()
    await ctx.send("Generando expositor de habbo...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   
    
    habbo = response.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=4&gesture=std&size=m&headonly=1"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((54,62), Image.Resampling.LANCZOS)#tamaño del keko 1
    
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    ###

    
    expositorhabbos = Image.open(r"imagenes/expositorHabbos.png").convert("RGBA") #imagen
    img1 = expositorhabbos.resize((60,92), Image.Resampling.LANCZOS)#tamaño de la expositorhabbos

    cristal = Image.open(r"imagenes/cristal.png").convert("RGBA") #imagen
    img1 = cristal.resize((60,92), Image.Resampling.LANCZOS)#tamaño de la cristal


    ###
    trozo = Image.open(r"imagenes/trozo.png").convert("RGBA") #imagen
    img1 = trozo.resize((60,92), Image.Resampling.LANCZOS)#tamaño de la cristal
    ###
    expo = Image.open(r"imagenes/arribaexpo.png").convert("RGBA") #imagen
    img1 = expo.resize((60,92), Image.Resampling.LANCZOS)#tamaño de la arribaexpo

    
    

 
   
    img1.paste(expositorhabbos,(0,0), mask = expositorhabbos) #Posicion de la gafas
    
    img1.paste(img2,(0,20), mask = img2) #Posicion del keko 1
    


    
    img1.paste(cristal,(0,0), mask = cristal) #Posicion de la cristal
    img1.paste(expo,(0,0), mask = expo) #Posicion de la expo

    img1.paste(trozo,(0,0), mask = trozo) #Posicion de la trozo

    
    ### 

    
    
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   