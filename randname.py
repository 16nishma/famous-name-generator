#Name Generator
famous_names= ["Elvis","Beyoncé", "Dolly",
"Shakira","Mariah","Zendaya","Adele","Cher", "Gwen",
"Meghan","Ed","Zayn","Ellen","Rihanna","Kylie"]
from random import *
random_num= randint(0,len(famous_names)-1)
print("Your famous name is...")
print(famous_names[random_num])
