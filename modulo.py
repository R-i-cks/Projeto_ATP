import json

def lerficheiro(nome):
    ficheiro = open(nome, encoding="utf-8")
    bd=[]
    dicJSON = json.load(ficheiro)
    return dicJSON

