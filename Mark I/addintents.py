import json

text = {"intents": [
    {"tag": "t",
    "patterns": ["a", "b", "c" ],
    "responses": ["a", "b", "c"],
    "context_set": "c"
    }
  ]
}

base = {"tag": "",
    "patterns": [],
    "responses": [],
    "context_set": ""
    }

print(text['intents'])

text['intents'].append(base)

print(text)

# # ler de um arquivo
# with open('intents.json', 'r') as arq:
#     obj = json.load(arq)
#     # manipular o obj ...
# print(obj)
# gravar obj em outro arquivo
# with open('saida.json', 'w') as arq:
#     json.dump(texto, arq, indent=4)
    