
x1 = 4
x2 = 3

w1 = 0.21
w2 = 0.22

#entradas = [[0,0], [0,1], [1,0], [1,1]]

funcao_soma = (x1*w1) + (x2*w2)

print('funcao soma deu: '+str(funcao_soma))

def funcao_ativacao_degrau(funcao_soma):
    if(funcao_soma >= 1):
        return 1
    else:
        return 0

r = funcao_ativacao_degrau(funcao_soma)

print('funcao degrau deu: '+str(r))
