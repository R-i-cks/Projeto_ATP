import json

def lerficheiro(nome):
    ficheiro = open(nome, encoding="utf-8")
    bd=[]
    dicJSON = json.load(ficheiro)
    return dicJSON

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
    return i

#  ----------- DISTRIBUIÇÃO POR GÉNERO -----------

def distribPorGenero(bd):
    dic={}
    for filme in bd:
        for elem in (filme['genres']):
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


def novofilme():       
    nome=input("Title: ")
    ano= input("Year: ")
    nelenc=int(input("Cast lenght: "))
    elenco=[]
    for i in range(nelenc):
        elenco.append(input("Cast: "))
    ngen= int(input("Genres lenght"))
    gen=[]
    for j in range(ngen):
        gen.append(input("Genres: "))
    filme={"title":nome,"year":ano,"cast":elenco,"genres":gen}
    return filme