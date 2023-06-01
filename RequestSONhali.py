
from asyncio.windows_events import NULL
from tarfile import NUL
from telnetlib import DO
from urllib import request, response
import requests

url = requests.get("https://pokeapi.co/api/v2/pokemon")
data = url.json()


pokemons = data['results']
pokDict1 = {}

adet = 0
for names in pokemons:
    adet+=1
    pokDict1[adet] = f"{names['name']}"

def girdiAl():
    global kullaniciGirdisi 
    for pok in pokDict1:  
        print(f"{pok}: {pokDict1[pok]}") 
    kullaniciGirdisi = int(input(f"Lutfen  1- {len(pokDict1)} arasinda secim yapiniz\n"))  
    kontrolMechanism()                    
    
def kontrolMechanism():
    global pokName
    if kullaniciGirdisi in pokDict1:          
        pokName = pokDict1[kullaniciGirdisi]  
        poks() 
    else: 
        print("Girdiginiz veriye ait bilgi bulunamadi") 


def poks():
    for element in pokemons: 
        if element['name'] == pokName:
            print("Name : ", element['name'])  
            poksURL = requests.get(f"{element['url']}") 
            poksDATA = poksURL.json() 
            break
    count = 0 
    for prop in poksDATA['abilities']:
        count = count +1   

        print(f"Ability {count}:", prop['ability']['name'])  
 
    print("Weight: ", poksDATA['weight']) 
  
    totalMoves = 0
    for move in poksDATA['moves']:
        totalMoves +=1
    print(f"Total Moves :{totalMoves} \n Moves: ", end = " ")
    
    for move in poksDATA['moves']:
        totalMoves +=1
        print(move['move']['name'],", ", end =" ")





girdiAl()

