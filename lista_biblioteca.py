
def add(list):
    novo_contato =[]    
    nome=(input("digite o nome"))
    numero=input("digite o numero")
        
    novo_contato.append(nome)
    novo_contato.append(numero)
        
    list.append(novo_contato)

def ex(list):
    op=int(input("digite qual linha vai excluir:"))
    list.pop(op)

def listar(list):
    if len(list)>1: 
        for i in range(0,len(list)):
          print(i+1,".", list[i][0], list[i][1])
    else: print("Não ha nenhum contato na agenda!")
    
def exlista(list):
    for i in range(0,len(list)): list.pop()

def edit(list):
    op=int(input("Digite numero da coluna"))
    i=int(input("Nome ou numero?"))
    if i==1:
      nome=(input("digite o nome"))
      list[op][0]=nome
    if i==2:
      numero=input("digite o numero")
      list[op][1]=numero
    

