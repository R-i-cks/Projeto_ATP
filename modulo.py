import json

def lerficheiro(nome):
    ficheiro = open(nome, encoding="utf-8")
    dicJSON = json.load(ficheiro)
    return dicJSON

def guardarficheiro(BD,nficheiro):
    ficheiro = open(nficheiro,"w",encoding="utf-8")
    ficheiro = json.dump
    (BD)

BD = ["Bonita vista!"]

guardarficheiro(BD,"cinemaATP.json")