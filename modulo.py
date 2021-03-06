import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

#  ------------- PROCURA DE IDS -------------

def procuraID(id,bd):
    for elem in bd:
        if id == elem['id']:
            return elem

def eliminaent(bd,id):
    for elem in bd:
        if id == elem['id']:
            bd.remove(elem)
            return elem


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


def formatL(bd):
    i=0
    form=[]
    while i<len(bd):
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


# ------------- DISTRIBUIÇAO DE FILMES POR ATORES E POR GENERO (TOP10) -----------

def distribuicao(bd,obj):           
    dic={}
    for filme in bd:
        for elem in filme[obj]:
            if elem in dic.keys():
                dic[elem]=dic[elem]+1
            else:
                dic[elem]=1
    return dic

def top10Genero(d):
    L=[]
    i=0
    totaloutros=0
    orderGenres = sorted(d.items(), key=lambda item: item[1], reverse=True) #. items() trandorma o dicionário em tuplos
    for elem in orderGenres:
        if(i<10):
            (objet, vezes)=elem
            if objet !='and' and objet!= "(voice)":
                L.append(elem)
                i=i+1
        else:
            (objet, vezes)=elem
            totaloutros=totaloutros+int(vezes)
            
    L.append(("Outros",totaloutros))
    return L

def top10Atores(d):
    L=[]
    i=0
    orderActors = sorted(d.items(), key=lambda item: item[1], reverse=True) #. items() trandorma o dicionário em tuplos
    for elem in orderActors:
        if(i<10):
            (objet, vezes)=elem
            if objet !='and' and objet!= "(voice)":
                L.append(elem)
                i=i+1
    return L

def plot(L, tipo):
    x=[]
    y=[]
    for recorrencia in L:
        ( x1, y1 ) = recorrencia
        x.append(x1)
        y.append(y1)

    fig = plt.figure(figsize=(13, 8))     # aumento da largura e altura do gráfico para que os nomes não se sobreponham
    plt.xlabel(tipo)
    plt.ylabel("Quantidade")
    plt.title("Distribuição por " + tipo)
    plt.margins(x=0.005)                   # diminuição das margens
    plt.bar(x,y,width=0.9)
    plt.savefig('grafico.png', format='png')
    return 'grafico.png'

# ------------- DETETAR LISTA VAZIA --------------

def detNone(lista):   # Verifica a ocorrência de vazios em listas de informação
    detetor = False
    for elem in lista:
        if elem == None or elem =='':
            detetor = True
    return detetor


# ------------- ORDENA GENEROS E ATORES (EXTRA) -------------

def ordenaGenerosAtores(bd,tipo):
    generos={}
    for filme in bd:
        for gen in filme[tipo]:
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
