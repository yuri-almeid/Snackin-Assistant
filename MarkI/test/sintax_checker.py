# -*- coding: UTF-8 -*-

# Este código visa verificar a combinação todas as possíveis frases de bem vindo

# Contextos
contexto1 = ["Bom dia, ", "Boa tarde, ", "Boa noite, "]

contexto2 = ['como vai?', 'como tem passado?', 'que bom te ver aqui!', 'fico feliz em te ver aqui',
                'desejo boas compras!', 'te desejo uma boa experiência Snackin']

contexto3 = ['',', que tal uma bebida gelada para aproveitar o seu final de semana?',
          ', desejamos um excelente final de semana!']

for c1 in range(len(contexto1)):
  for c2 in range(len(contexto2)):
    for c3 in range(len(contexto3)):
      print(contexto1[c1] + 'Fulano' + ' ' + contexto2[c2] + contexto3[c3])