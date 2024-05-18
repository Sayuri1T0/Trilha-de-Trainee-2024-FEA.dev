#!/usr/bin/env python
# coding: utf-8

# ![WhatsApp%20Image%202023-09-10%20at%2011.20.28.jpeg](attachment:WhatsApp%20Image%202023-09-10%20at%2011.20.28.jpeg)
# 

# ### Fala devs, blz?? 
# 
# Esta será nossa primeira lista de exercícios para você testar seu conhecimento acerca do conteúdo do MÓDULO 2:
# 
# -Meu Primeiro Programa em Python
# 
# 
# -Estrutura de Dados

# ## INSTRUÇÕES:
# 
# A lista deve ser realizada pelo Jupyter Notebook.
# 
# Nâo é necessário entregar a lista para afins de certificado dentro da plataforma, entretanto para alunos da USP que queiram participar do processo seletivo ou conseguir créditos AAC (apenas FEANOS) é necessária a entrega de TODAS as listas.
# 
# A entrega das listas ou pelo menos sua excecução é recomendada a fim de exercitar todo o conhecimento adquirido do curso.
# 
# O DESAFIO é para realmente te desafiar, por isso não desista de tentar e de continuar com o curso, ao longo das listas você verá que cada vez mais você terá ferramentas para completá-lo.
# 
# Caso haja alguma dúvida acerca da lista participe das monitorias que serão oferecidas as quintas e sábados das 17h as 18h pelo DISCORD. Caso seu problema não seje resolvido envie uma mensagem para contato.feadev@gmail.com
# 
# O gabarito será disponibilizado na plataforma após o término de periodo de envio
# 
# 

# In[ ]:


## vamos começar??


# ## QUESTÃO 0

# Todo programador deve saber apenas uma coisa: Pedir para o Python escrever "Hello, Word"
# Vamos testar se você já pode ser nomeado como um programador???

# In[1]:


FEADEV = "Hello, Word"
print(FEADEV)


# E se eu te pedir para criar um código que tenha como OUTPUT  (termo comumente usado na programação e na computação em geral para se referir à saída de um programa ou processo) o seu número favorito? Como seria?

# In[18]:


#seu código começa aqui

fav = 37//2
print(fav)


# ## QUESTÃO 1
# 

# 
# Você foi contratado por um restaurante na cidade de São Paulo. Seu trabalho é criar um sistema de reservas online que proporcionará uma experiência mais eficiente e rápida ao
# cliente. No sistema, os clientes serão solicitados a inserir o seu nome e o sobrenome ao fazer uma reserva.
# 
# Agora, sua tarefa é criar um código em Python no Jupyter Notebook para combinar o seu primeiro nome e seu sobrenome e exibir o nome completo que o atendente usará para chamar você quando a mesa estiver pronta.
# 
# Seu código deve fazer o seguinte:
# 
# Declare duas variáveis: primeiro_nome e sobrenome.
# Atribua um valor ao primeiro_nome representando o primeiro nome que a atendente anotou.
# Atribua um valor ao sobrenome representando o sobrenome que o atendente solicitou posteriormente.
# Use sua habilidade em Python para combinar essas duas partes e criar o nome completo.
# Exiba o nome completo no Jupyter Notebook.
# 
# Desafio aceito? Agora, você está pronto para criar o código que garantirá que o recepcionista chame você corretamente quando a mesa estiver pronta!

# ![Captura%20de%20tela%202023-09-24%20140330.png](attachment:Captura%20de%20tela%202023-09-24%20140330.png)

# In[11]:


primeiro_nome = input("Qual é seu nome?\n")

sobrenome = input("Que nome legal! Para finalizar, qual seu sobrenome?\n")

nome_completo = f"Obrigada! Quando seu pedido ficar pronto, chameremos por {primeiro_nome} {sobrenome}"

print(nome_completo)


# ## QUESTÃO 2
# 
# 

# Imagine que você é um aluno do Ensino Fundamental e acabou de fazer uma prova de matemática. Em uma questão, o professor pediu o resultado de 10 + 5 x 2. A expressão criou uma forte discussão entre os estudantes da classe, uma parte defendia que a resposta correta era 20; a outra, 30.
# 
# Então, você recorreu ao Python para descobrir a resposta correta.
# 
# Como deve ser o código para chegar ao resultado?

# ![Captura%20de%20tela%202023-09-24%20140141.png](attachment:Captura%20de%20tela%202023-09-24%20140141.png)

# In[12]:


# seu código começa aqui 

# Defina os números

a = 10
b = 5
c = 2

# Calcule o resultado

resultado = a + (b*c)

# Exiba o resultado

print(resultado)


# In[13]:


# seu código começa aqui

# Calcule o resultado diretamente

resultado = 10 + (5*2)

# Exiba o resultado

print(resultado)


# ## QUESTÃO 3

# Você e o seu melhor amigo são interessados por desafios de criptografia. Certo dia, vocês recebem uma carta com uma mensagem secreta. Para decifrá-la, é necessário utilizar as técnicas de operações de texto em Python.
# 
# Mistério da Mensagem Secreta:
# 
# A mensagem é dada por:

# In[17]:


#Mistério: @lg0 3$c0nd3 3$t@ m3n$@g3m. P0d3r1@$ d3c1fr@-l@??


# A mensagem parece confusa, mas você sabe que ela contém informações importantes. Aqui estão as etapas que você deve seguir para decifrar a mensagem:
# 
# Crie uma variável chamada mensagem e atribua a ela a mensagem secreta fornecida acima.
# Use operações de texto em Python para limpar a mensagem, removendo todos os caracteres especiais, números e espaços em branco.
# 
# Converta a mensagem resultante para letras minúsculas.
# 
# Agora que a mensagem está limpa, vocês podem decifrá-la? A mensagem secreta pode conter uma pista importante!
# 
# Crie um código em Python no Jupyter Notebook para realizar essas etapas e revelar o que está por trás desse mistério! 🕵️‍♂️🔍

# In[31]:


#seu código começa aqui

import re

mensagem = '@lg0 3$c0nd3 3$t@ m3n$@g3m. P0d3r1@$ d3c1fr@-l@??'

mensagem = re.sub(r'[@_!#$%^&()<>?/\|}{~:.,-]+', '', mensagem)
print(mensagem)

mensagem = re.sub(r'[0-9]','',mensagem)
print(mensagem)

mensagem = re.sub(r' ','',mensagem)
print(mensagem)

mensagem = mensagem.lower()
print(mensagem)


# ## QUESTÃO 4

# 
# Você acaba de ingressar no curso de Python do FEA.dev e decide iniciar sua própria consultoria. Parabéns!!! Você logo recebe seu primeiro cliente, a confeitaria e panificadora Confeitos no Forno. Ela tem um grande objetivo em mente: desbancar os concorrentes. Para isso, vai recorrer à tecnologia em seus processos. 
# 
# Sua primeira função é criar um sistema que recebe o valor de cada venda de doce e de salgado e imprima o valor final.

# In[1]:


#seu código começa aqui

Receita = []
algo_mais = ("Sim")

card_doce = ("Bolo - R$5,00\nTorta - R$4,50\nBombom - R$3,00")
card_salgado = ("Pão de queijo - R$8,00\nSalgado - R$9,00\nLanche natural - 12,00")

resposta = input("Olá, bem vindo à Confeitos no forno. Gostaria de fazer um pedido?\n")

if resposta in ("sim", "SIM", "Sim", "yes", "Yes", "YES"):
        
    while algo_mais in ("sim", "SIM", "Sim", "yes", "Yes", "YES"):
        Hello = input("Legal! Gostaria de pedir um doce ou salgado?\n")

        if Hello in ["Doce", "doce", "DOCE"]:
            print(f"Certo! Esse é o cardápio:\n{card_doce}")
            pedido_doce = input("Qual gostaria?\n")
            if pedido_doce in ("bolo", "Bolo", "BOLO"):
                Receita.append(5.00)
            if pedido_doce in ("torta", "Torta", "TORTA"):
                Receita.append(4.50)
            if pedido_doce in ("bombom", "Bombom", "BOMBOM"):
                Receita.append(3.30)
        else:
            print(f"Certo! Esse é o cardápio:\n{card_salgado}")
            pedido_doce = input("Qual gostaria?\n")
            if pedido_doce in ("Pão de queijo", "PAO DE QUEIJO", "pao de queijo", "pão de queijo"):
                Receita.append(8.00)
            if pedido_doce in ("salgado", "Salgado", "SALGADO"):
                Receita.append(9.00)
            if pedido_doce in ("lanche natural", "Lanche natural", "LANCHE NATURAL"):
                Receita.append(12.00)

        algo_mais = input("Gostaria de algo mais?\n")

    else:
        print("Ok, obrigada pela visita! Até a próxima!")

else:
     print("Ok, obrigada pela visita! Até a próxima!")

print(f'Agora que acabou o expediente, a receita é {Receita}')


# In[9]:


print(Receita)


# ## QUESTÃO 5

# 
# Excelente! A clientela adorou o programa de fidelidade.
# Feito isto, chegou a hora de olhar para os processos internos. A ideia é automatizar a lista de compra da semana, antes feita no papel. 

# a) Visto que a demanda por salgados diminuiu e a de doces aumentou, o Padeiro Chef resolveu retirar alguns produtos salgados do cardápio. Por isso, ingredientes como Milho, Calabresa e Lombo não serão mais necessários. Em contrapartida, é necessário acrescentar na lista de compras Açúcar e o fermento Levain. Atualize a lista de compras por meio do Python

# In[65]:


compras = ['Farinha de Trigo', 'Ovos', 'Fermento Biológico', 'Leite', 'Calabresa', 'Milho', 
           'Champignon', 'Molho de Tomate', 'Frango', 'Requeijão', 'Lombo']

##### Seu código começa aqui

compras.remove('Milho')
compras.remove('Calabresa')
compras.remove('Lombo')

print(compras)


# In[66]:


compras.append('Açucar')
compras.append('fermento Levain')
print(compras)


# b) Enquanto você estava com o computador ligado, um hacker do concorrente resolveu atacar sua lista de compras invertendo alguns dos itens, como se vê abaixo:

# ![Captura%20de%20tela%202023-09-24%20135736.png](attachment:Captura%20de%20tela%202023-09-24%20135736.png)

# Conserte os valores que foram adulterados e imprima a lista corrigida.

# In[32]:


sarpmoc = ['ogirT ed ahniraF', 'Leite', 'Fermento Biológico', 'Champignon', 'etamoT ed ohloM', 'Frango', 
           'Requeijão', 'Ovo', 'niaveL', 'Açúcar']

a0 = sarpmoc[0]
a0 = a0[::-1]

sarpmoc[0] = a0

a4 = sarpmoc[4]
a4 = a4[::-1]

sarpmoc[4] = a4

a8 = sarpmoc[8]
a8 = a8[::-1]

sarpmoc[8] = a8

print(a0)
print(a4)
print(a8)

print(sarpmoc)

compras = sarpmoc
print(compras)


# c) Após esse duro golpe, você percebe que é necessário guardar as informações importantes em uma estrutura de dados que seja mais segura (isto é, que não seja mutável). Converta a lista de compras para uma estrutura com estas características e imprima o tipo da variável. &nbsp; Dica: Utilize a função type() para obter o tipo da variável

# In[38]:


#seu código começa aqui

compras = tuple(compras)

print(f'Suas compras são: {compras} e, para sua segurança, sua classificação é {type(compras)}')


# ![af5addc01d02cc4bc54fd86a456e3dce90d2e4276b59c876cea22cc84e9a4f07_1.jpg](attachment:af5addc01d02cc4bc54fd86a456e3dce90d2e4276b59c876cea22cc84e9a4f07_1.jpg)

# ## QUESTÃO 6

# Empresas modernas se importam com ESG (Environmental, Social and Governance). A Confeitaria no Forno não seria diferente, e sua missão é auxiliar a empresa a reduzir as emissões de lixo em sua operação. &nbsp; 
# 
# 

# ![ac137a44f5f8cd3c6126fc8ff8c24fff.jpg](attachment:ac137a44f5f8cd3c6126fc8ff8c24fff.jpg)

#  O primeiro passo será tornar o panfleto digital, de forma que seja enviado pelas redes sociais e não precise ser impresso e consequentemente descartável. Para demonstrar essa funcionalidade ao dono, você deve criar um exemplo de panfleto que contenha os salgados, os doces, os tipos de bebida e  os adicionais, conforme os valores a seguir:
# -  Salgados: Coxinha de Frango, Misto Quente e Ovos Mexidos;
# -  Doces: Bolo de Chocolate, Torta de Limão e Brigadeiro;
# -  Bebidas: Guaraná, Cola, Suco de Laranja e Suco de Uva;
# -  Adicionais: Bacon, Requeijão, Chocolate e Morango
# 
# Imprima o panfleto final

# In[45]:


### Seu código começa aqui

S = ['Coxinha de Frango', 'Misto Quente', 'Ovos Mexidos']
D = ['Bolo', 'Torta de Limão', 'Brigadeiro de Chocolate']
B = ['Guaraná, Cola', 'Suco de Laranja', 'Suco de Uva']
A = ['Bacon', 'Requeijão', 'Chocolate', 'Morango']


# In[78]:


import emoji

s1 = S[0] + emoji.emojize('🍗')
s2 = S[1] + emoji.emojize(':sandwich:')
s3 = S[2] + emoji.emojize(':cooking:')
# print(s1,s2,s3)

d1 = D[0] + emoji.emojize('🎂')
d2 = D[1] + emoji.emojize(':shortcake:')
d3 = D[2] + emoji.emojize('🍫')
print(d1,d2,d3)

b1 = B[0] + emoji.emojize('🥤')
b2 = B[1] + emoji.emojize('🧃')
b3 = B[2] + emoji.emojize('🧃')
# print(b1,b2,b3)

a1 = A[0] + emoji.emojize(':bacon:')
a2 = A[1] + emoji.emojize('🧀')
a3 = A[2] + emoji.emojize('🍫')
a4 = A[3] + emoji.emojize(':strawberry:')

# print(a1,a2,a3,a4)


# In[95]:


P1 = ("Salgados\n\n" + s1 + "\n" + s2 + "\n" + s3 +"\n")

P2 = ("Doces\n\n" + d1 + "\n" + d2 + "\n" + d3 +"\n")

P3 = ("Bebidas\n\n" + b1 + "\n" + b2 + "\n" + b3 +"\n")

P4 = ("Adicionais\n\n" + a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 +"\n")


# In[96]:


Panfleto = print(P1 + "\n" + P2 + "\n" + P3 + "\n" + P4)


# ### DESAFIO

# Sucesso! A Confeitaria no Forno tornou-se uma multinacional que engoliu todas as concorrentes. Querendo crescer ainda mais, o Chef sugeriu um novo recurso: deixar os clientes montar e personalizar os doces. Para isso, foi feito um dicionário com todos os ingredientes e os respectivos preços.
# 
# Temos os seguintes pedidos:
# 
# -  1: Bolo de Baunilha com Ganache de Chocolate e Decoração de Chocolate Belga
# -  2: Bolo de Chocolate com Creme de Baunilha e Confete Colorido
# -  3: Massa Folhada com Merengue de Morango e Frutas Vermelhas
# 
# Imprima uma lista com todos os itens do pedido e seu preço final que será retornado ao cliente. Armazene o valor das vendas de forma que não seja possível alterar seus valores e imprima.

# In[12]:


### Seu código começa aqui 
ingredientes = {
    'massas': {
        'Bolo de Baunilha': 25.00,
        'Bolo de Chocolate': 15.00,
        'Massa Folhada': 30.00,
    },
    'coberturas': {
        'Creme de Baunilha': 12.00,
        'Ganache de Chocolate': 15.00,
        'Merengue de Morango': 20.00,
    },
    'recheios': {
        'Frutas Vermelhas': 22.00,
        'Ganache de Morango': 16.50,
        'Creme de Limão': 14.00,
        'Creme de Coco': 18.00,
    },
    'decorações': {
        'Confete Colorido': 5.00,
        'Chocolate Belga': 20.00,
        'Frutas Secas': 12.00,
    }
}

