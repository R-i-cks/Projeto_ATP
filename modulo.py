import json

def lerficheiro(nome):
    ficheiro = open(nome, encoding="utf-8")
    bd=[]
    dicJSON = json.load(ficheiro)
    return dicJSON


#  ------ LISTAR ALBAFETICAMENTE ----------------

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


#  ----- LISTAR POR DETERMINHADO GENERO ----------

def listarGenero(bd, genero):
    novaBD=[]
    for filme in bd:
        for elem in filme['genres']:               # Como os elementos da chave 'genres' estao em lista, temos de a percorrer
            if elem==genero:
                novaBD.append(filme)
    return novaBD
