# Passo 1: Abrir o sistema da empresa  
#         Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login  
# Passo 2: Fazer login  
# Passo 3: Importar a base de dados dos produtos  
# Passo 4: Cadastrar 1 produto  
# Passo 5: Repetir o passo 4 até acabar todos os produtos 

# importando as bibliotecas
import pyautogui
import time
import pandas

#  Passo 1

# deixa o comando mais lento
pyautogui.PAUSE = 0.5

# entrando no navegador 
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrando no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# tempo de espera
time.sleep(3)

# Passo 2

# clicar no campo de email
pyautogui.click(x=595, y=366)

# escrever o email
pyautogui.write("math2306.r@gmail.com")

# passa para o botao de senha
pyautogui.press("tab")

# escrever a senha
pyautogui.write("123456")
pyautogui.press("enter")
# Passo 3:

#ler a base de dados
tabela = pandas.read_csv("dia_1-13.1-Aula1/produtos.csv")
print(tabela)

# Passo 4:

time.sleep(2)


for linha in tabela.index:
    pyautogui.click(x=623, y=257)
    # str--> string
    # pegando o codigo
    cod=tabela.loc[linha, "codigo"]
    pyautogui.write(str(cod))
    pyautogui.press("tab")

    # pegando a marca
    marca=tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # pegando o tipo
    tipo=tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # pegando a categoria
    categoria=tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # pegando o preco unitario
    preco=tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # pegando o custo
    custo=tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # pegando o obs
    obs=str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") 

    pyautogui.scroll(1000) 