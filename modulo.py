import json

def lerficheiro(nome):
    if '.json' in nome:
        ficheiro = open(nome, encoding="utf-8")
        bd=[]
        dicJSON = json.load(ficheiro)
        return dicJSON
    else:
        return 


def tiraext(nome):     
    if '.' in nome:
        n = nome.split('.')
        nome = n[0]
    return(nome)

#  ------------- DICIONARIO PARA LISTA ----------------

def dictolist(dic):
    L=[]
    for elem in dic.items():
        key,value = elem
        L.append(str(key) + ' :: ' + str(value))
    return L

#  -------------- GUARDAR FICHEIRO ----------------

def guardarficheiro(nome,bd):
    f= open(nome,'w',encoding='utf-8')
    json.dump(bd,f,ensure_ascii=False,indent=2)

#  ------------- CONSTRUÇAO DE IDS ----------------
    
def id(bd):
    i=1
    listaID = []
    for filme in bd:
        if filme.get('id') != None:
            listaID.append(filme.get('id'))
    for filme in bd:
        if filme.get('id') == None: 
            while str(i) in listaID:
                i=i+1
            filme['id']=(str(i))
            listaID.append(str(i))
            i=i+1

#  ------ LISTAR ALFABETICAMENTE ----------------

def chaveOrd(d):
    chave=d['title'].replace("(","")
    chave=chave.replace(")","")
    chave=chave.replace("/","")
    chave=chave.replace("\'","")
    chave=chave.replace(".","")
    chave=chave.replace(":","")
    chave=chave.replace(",","")
    chave=chave.replace("\"","")
    return chave

def listarAlfabeticamente(bd):
    bd.sort(key=chaveOrd)
    return bd        

# ------------- FORMATACAO ----------------

def formatacao(bd):
    i=0
    form=[]
    while i<len(bd):
        if i==0:
            form.append('Title |  Year  |  Cast  |   Genres  |  ID  ')
        c = str(bd[i]['cast']).strip('[') 
        d =str(bd[i]['genres']).strip('[')
        form.append(bd[i]['title'] +' | ' +  str(bd[i]['year']) + ' | ' + c.strip(']') + ' | ' + d.strip(']') + ' | ' + bd[i]['id'] )
        i=i+1
    return form

#  --------------- CONTA FILMES ------------------

def contaFilmes(bd):
    i=0
    for filme in bd:
        i=i+1
    return ['Há ' +str(i)+ ' filmes na Base de Dados!']


#  ----------- DISTRIBUIÇÃO POR GÉNERO e ATORES -----------

def distribuicao(bd,obj):           
    dic={}
    for filme in bd:
        for elem in filme[obj]:
            if elem in dic.keys():
                dic[elem]=dic[elem]+1
            else:
                dic[elem]=1
    return dic



def plotGenero(d):
    x=d.keys()
    y=[]
    for i in d.keys():
        y.append(d[i])

    fig = plt.figure(figsize=(45, 10))     # aumento da largura e altura do gráfico para que os nomes não se sobreponham
    plt.xlabel("Género")
    plt.ylabel("Quantidade")
    plt.title("Distribuição por Género")
    plt.margins(x=0.005)                   # diminuição das margens
    plt.bar(x,y,width=0.9)
    plt.show()

#  ----------------------- ADICIONAR NOVO FILME ----------------------

def novofilme(lista):
    filme={"title":lista[0],"year":lista[1],"cast":lista[2],"genres":lista[3]}
    return filme

#  ----------- LISTAR FILMES DE DETERMINADO ATOR OU GÉNERO -----------

def listarAG(bd,a,tipo):
    filmes=[]
    for filme in bd:
        for ator in filme[tipo]:
            if a.lower() in ator.lower():
                filmes.append(filme)
    return filmes

#  ----------------------- CONSULTAR FILME ----------------------

def consultarfilme(bd,nome):
    correspondencia = []
    nome=nome.lower()
    for elem in bd:
        if nome in elem['title'].lower():
            correspondencia.append(elem)
    return correspondencia


# ------------- DISTRIBUIR FILMES POR ATORES (TOP10) -----------



def top10Atores(d):
    L=[]
    i=0
    orderActors = sorted(d.items(), key=lambda item: item[1], reverse=True) #. items() trandorma o dicionário em tuplos
    for elem in orderActors:
        if(i<10):
            L.append(elem)
            i=i+1
        else:
            break
    return L


def plotAtor(d):
    x=[]
    y=[]
    
    for f in d:
        x.append(f[0])
        y.append(f[1])
    fig = plt.figure(figsize=(45, 10))     # aumento da largura e altura do gráfico para que os nomes não se sobreponham
    plt.xlabel("Ator")
    plt.ylabel("Quantidade")
    plt.title("Distribuição por Filme")
    plt.margins(x=0.005)                   # diminuição das margens
    plt.bar(x,y,width=0.9)
    plt.show()

# ------------- DETETAR LISTA VAZIA --------------

def detNone(lista):   # Verifica a ocorrência de vazios em listas de informação
    detetor = False
    for elem in lista:
        if elem == None or elem =='':
            detetor = True
    return detetor


# ------------- ORDENA GENEROS (EXTRA) -------------

def ordenaGeneros(bd):
    generos={}
    for filme in bd:
        for gen in filme['genres']:
            gen=gen.replace("/","")
            gen=gen.replace("\"","")
            gen=gen.replace("/","")
            gen=gen.replace("(","")
            gen=gen.replace(")","")
            gen=gen.replace(".","")
            gen=gen.replace("\'","")
            if gen!="":
                if gen in generos.keys():
                    generos[gen]=generos[gen]+', ' + filme['title'] + ': ' + filme['id']
                else:
                    generos[gen]=filme['title']+ ': ' + filme['id']
    generos=sorted(generos.items())
    return generos

# ------------- ORDENA ATORES (EXTRA) --------------

def ordenaAtores(bd):
    atores={}
    for filme in bd:
        for ator in filme['cast']:
            ator=ator.replace("/","")
            ator=ator.replace("\"","")
            ator=ator.replace("/","")
            ator=ator.replace("(","")
            ator=ator.replace(")","")
            ator=ator.replace(".","")
            ator=ator.replace("\'","")
            if ator!="":
                if ator in atores.keys():
                    atores[ator]=atores[ator]+', ' + filme['title'] + ': ' + filme['id']
                else:
                    atores[ator]=filme['title']+ ': ' + filme['id']
    atores=sorted(atores.items())
    return atores
