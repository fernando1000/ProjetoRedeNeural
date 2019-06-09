from rna import RNA

#entradas = [[0,0],[0,1],[1,0],[1,1]]
#respostas_corretas = [0,0,0,1]
#pesos = [0.0, 0.0]
#taxa_aprendizagem = 0.1

#RNA.treinar(entradas, respostas_corretas, pesos, taxa_aprendizagem)

porco = 0
cachorro = 1

entradas = [[1,1,0], [1,1,0], [1,1,0], [1,1,1], [0,1,1], [0,1,1]]
respostas_corretas = [porco,porco,porco,cachorro,cachorro,cachorro]
pesos = [0.0, 0.0, 0.0]
taxa_aprendizagem = 0.1

pesos_ideal = RNA.treinar(entradas, respostas_corretas, pesos, taxa_aprendizagem)

misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]

testes = [misterioso1, misterioso2, misterioso3]
marcacoes_teste = [0,1,0]

resultados = RNA.adivinhar(testes, pesos_ideal)

for i in range(len(resultados)):
    if(resultados[i] == cachorro):
        print('estou chutando: cachorro')
    else:
        print('estou chutando: porco')
