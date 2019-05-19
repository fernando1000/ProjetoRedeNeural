class RNA:

    def funcao_soma(entradas_x1_x2, pesos_x1_x2):
        soma = 0
        for i in range(len(entradas_x1_x2)):
            soma = soma + (entradas_x1_x2[i] * pesos_x1_x2[i])

        return soma

    def funcao_degrau(resultado_funcao_soma):
        if(resultado_funcao_soma >= 1):
            return 1
        else:
            return 0

    def calcula_saida(registro_x1_x2, pesos):
        resultado_funcao_soma = RNA.funcao_soma(registro_x1_x2, pesos)
        # print('result_funcao_soma: {}'.format(resultado_funcao_soma))
        resposta_obtida_funcao_degrau = RNA.funcao_degrau(resultado_funcao_soma)
        # print('result_funcao_degrau: {}'.format(resposta_obtida_funcao_degrau))
        return resposta_obtida_funcao_degrau

    def calcula_erro(resposta_correta, resposta_obtida):
        erro = abs(resposta_correta - resposta_obtida)
        return erro

    def treinar(entradas, respostas_corretas, pesos, taxa_aprendizagem):
        erro_total = 1
        while (erro_total != 0):
            erro_total = 0
            for i in range(len(respostas_corretas)):
                saida_calculada = RNA.calcula_saida(entradas[i], pesos)
                erro = RNA.calcula_erro(respostas_corretas[i], saida_calculada)
                # print('result_calcula_erro: {}'.format(erro))
                erro_total = erro_total + erro
                for j in range(len(pesos)):
                    pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
                    print('peso atualizado: {}'.format(pesos[j]))

            print('total de erros: {}'.format(erro_total))
