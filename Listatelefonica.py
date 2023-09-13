import os
import app as sistema
os.system("cls")
agenda =[
    
    
]


while (True):
    
    op=int(input("Selecione uma opção"))
    if op==1:
        sistema.add(agenda)
    if op==2:
        sistema.edit(agenda)
    if op==3:
        sistema.listar(agenda)
    if op==4:
        sistema.ex(agenda)
    if op==5:
        sistema.exlista(agenda)
    if op==6:
        print(agenda)