#pessoa = {"nome": "guilherme", "idade": 28, "telefone": "333-1696"}
#ou
#pessoa = dict(nome= "Guilherme", idade=28)

    #acessando aos dados
dados = {"nome": "guilherme", "idade": 28, "telefone": "333-1696"}
print(dados["nome"]) #>>>guilherme
print(dados["idade"]) #>>>28
print(dados["telefone"]) #>>>333-1696

        #substituindo
dados["nome"] = "Maria"
print(dados)

    #dicionario aninhados
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
telefone = contatos["guilherme.afonso@gmail"]["idade"] 
print(telefone) #>>>33301696

extra = contatos["kamila@gmail"]["extra"]
print(extra)  #>>>{"a" : 1}

    #iterar dicionario
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
#>>>guilherme.afonso@gmail {'nome': 'guilherme', 'idade': 29}
#kamila@gmail {'nome': 'kamila', 'idade': 26, 'extra': {'a': 1}}
#guilherme.afonso@gmail {'nome': 'guilherme', 'idade': 29}
#kamila@gmail {'nome': 'kamila', 'idade': 26, 'extra': {'a': 1}}

        ##Métodos da classe dict
    
    #{}.clear
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
contatos.clear()
print(contatos) #>>>{}

    #{}.copy
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29} #CHAVE
}
copia = contatos.copy()
copia["guilherme.afonso@gmail"] = {"nome": "gui"}
print(contatos) #>>>{'guilherme.afonso@gmail': {'nome': 'guilherme', 'idade': 29}}
print(copia) #>>>{'guilherme.afonso@gmail': {'nome': 'gui'}}

    #{}.fromkeys
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29} #CHAVE
}
dict.fromkeys(["nome", "idade"])
print(contatos) #>>>{'guilherme.afonso@gmail': {'nome': 'guilherme', 'idade': 29}}

    #{}.get
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
print(contatos.get("chave")) #>>>None
print(contatos.get("chave", {})) #>>>{}
print(contatos.get("guilherme.afonso@gmail", {})) #>>>{'nome': 'guilherme', 'idade': 29}

    #{.keys}
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
print(contatos.keys()) #>>>dict_keys(['guilherme.afonso@gmail', 'kamila@gmail'])

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys()) #>>>dict_keys(['a', 1, 'b'])

    #{}.pop
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
print(contatos.pop("guilherme.afonso@gmail")) #>>>{'nome': 'guilherme', 'idade': 29}
print(contatos.pop("guilherme.afonso@gmail", {})) #>>>{}

    #{}.popitem
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
print(contatos.popitem()) #>>>('kamila@gmail', {'nome': 'kamila', 'idade': 26, 'extra': {'a': 1}})
print(contatos.popitem()) #>>>('guilherme.afonso@gmail', {'nome': 'guilherme', 'idade': 29})

    #{}.setdefault
contato = {"nome": "guilherme", "telefone": "999081696"}

contato.setdefault("idade", 28)
print(contato) #>>>{'nome': 'guilherme', 'telefone': '999081696', 'idade': 28}

    #{}.update
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
contatos.update({"guilherme.afonso@gmail": {"nome": "gui"}})
print(contatos) #>>>{'guilherme.afonso@gmail': {'nome': 'gui'}, 'kamila@gmail': {'nome': 'kamila', 'idade': 26, 'extra': {'a': 1}}}

    #{}.values
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
print(contato.values()) #>>>dict_values(['guilherme', '999081696', 28])

    #in
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
print("guilherme.afonso@gmail" in contatos) #>>> True

    #del
contatos = {
    "guilherme.afonso@gmail": {"nome": "guilherme", "idade": 29},
    "kamila@gmail": {"nome": "kamila", "idade": 26, "extra": {"a" : 1}}
}
del contatos["guilherme.afonso@gmail"]["idade"]
print(contatos) #>>>{'guilherme.afonso@gmail': {'nome': 'guilherme'}, 'kamila@gmail': {'nome': 'kamila', 'idade': 26, 'extra': {'a': 1}}}