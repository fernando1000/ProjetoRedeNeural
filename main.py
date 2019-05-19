from rna import RNA

entradas = [[0,0],[0,1],[1,0],[1,1]]
respostas_corretas = [0,0,0,1]
pesos = [0.0, 0.0]
taxa_aprendizagem = 0.1

RNA.treinar(entradas, respostas_corretas, pesos, taxa_aprendizagem)
