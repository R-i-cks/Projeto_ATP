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

def dictolist(dic):
    L=[]
    for elem in dic.items():
        key,value = elem
        L.append(str(key) + ' :: ' + str(value))
    return L


def guardarficheiro(nome,bd):
    f= open(nome,'w',encoding='utf-8')
    json.dump(bd,f,ensure_ascii=False,indent=2)


#  ------ LISTAR ALFABETICAMENTE ----------------

def chaveOrd(d):
    chave=d['title'].replace("(","")
    chave=chave.replace(")","")
    chave=chave.replace("\'","")
    chave=chave.replace("/'","")
    chave=chave.replace(".'","")
    chave=chave.replace(":'","")
    chave=chave.replace(",","")
    return chave

def listarAlfabeticamente(bd):
    bd.sort(key=chaveOrd)
    return bd        


#  ----- LISTAR POR DETERMINADO GENERO ----------

def listarGenero(bd, genero):
    novaBD=[]
    for filme in bd:
        for elem in filme['genres']:               # Como os elementos da chave 'genres' estao em lista, temos de a percorrer
            if elem==genero:
                novaBD.append(filme)
    return novaBD


#  --------------- CONTA FILMES ------------------

def contaFilmes(bd):
    i=0
    for filme in bd:
        i=i+1
    return ['Há ' +str(i)+ ' filmes na Base de Dados!']

#  ----- CONSULTAR UM FILME -------
def consultarFilme(bd,procura):
    procuraBD=[]
    for filme in bd:
        if procura in filme['title']:
            procuraBD.append(filme)
    
    return procuraBD


#  ----------- DISTRIBUIÇÃO POR GÉNERO -----------

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

#  -------------- ADICIONAR NOVO FILME ---------------

def novofilme(nome,ano,elenco,gen):
    filme={"title":nome,"year":ano,"cast":elenco,"genres":gen}
    return filme

#  ----------- LISTAR FILMES DE DETERMINADO ATOR -----------

def listarFilmeDeAtor(bd, a):
    filmes=[]
    for filme in bd:
        for ator in filme['cast']:
            if ator==a:
                add=[]
                add.append('title: ' + str(filme['title']))
                add.append('year: ' + str(filme['year']))
                add.append('cast: ' + str(filme['cast']))
                add.append('genres: ' + str(filme['genres']))
                filmes.append(add)
    return filmes


def verfilmes(bd):      # Mostra os títulos de todos os filmes na bd
    L=[]
    for elem in bd:
        L.append(elem['title'])  
    return L

def consultarfilme(filmes,nome):
    correspondencia = []
    nome.lower()
    for elem in filmes:
        if nome in elem.lower():
            correspondencia.append(elem)
    return correspondencia

# ------------- DISTRIBUIR FILMES POR ATORES (TOP10) -----------

def distribporAtor(bd):
    dic={}
    for filme in bd:
        for elem in (filme['cast']):
            if elem in dic.keys():
                dic[elem]=dic[elem]+1
            else:
                dic[elem]=1
    return dic

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

    
#-----------(Função extra) Indicam a lista de filmes dos 10 melhores atores respetivamente---------


def consultarFilme(bd,atores):
    procuraBD={}
    for filme in bd:
        for elem in atores:
            if elem in filme['cast']:
                if elem not in procuraBD.keys():
                    lista=[]
                else:
                    lista=procuraBD[elem]
                lista.append(filme['title'])
                procuraBD[elem]=lista
    return procuraBD


def inverEstrAG(bd,chave,pesquisa):
    resultado=[]
    for filme in bd:
        presente = False
        for elem in filme[chave]:
            if pesquisa in elem:
                presente = True
        if presente == True:
            resultado.append(filme['title'])
    return resultado

#  ----- CONSULTAR UM FILME -------
def inverEstF(bd,procura):
    procuraBD=[]
    for filme in bd:
        if procura in filme['title']:
            procuraBD.append(filme['title'])
    return procuraBD


def detNone(lista):   # Verifica a ocorrência de vazios em listas de informação
    detetor = False
    for elem in lista:
        if elem == '':
            detetor = True
    return detetor



    


