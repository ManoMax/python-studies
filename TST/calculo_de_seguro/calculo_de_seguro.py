# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Cálculo de Seguro - CC (UFCG)

def calcula_seguro(valor, resposta):
    lista = []
    pts = 0
    # idade
    if resposta[0] <= 21:
        pts += 20
    elif 22 <= resposta[0] <= 30:
        pts += 15
    elif 31 <= resposta[0] <= 40:
        pts += 12
    elif 41 <= resposta[0] <= 60:
        pts += 10
    elif resposta[0] > 60:
        pts += 20

    # casado
    if resposta[1] == True:
        pts += 10
    else:
        pts+= 20

    # Mora em area de risco
    if resposta[2] == True:
        pts += 20
    else:
        pts += 10

    # Possui portão eletronico
    if resposta[3] == True:
        pts += 20
    else:
        pts += 10

    # Mora em casa
    if resposta[4] == True:
        pts += 20
    else:
        pts += 10

    # Casa propria
    if resposta[5] == True:
        pts += 10
    else:
        pts += 20

    #Uso do veiculo
    if resposta[6] == "Lazer":
        pts += 20
    elif resposta[6] == "Trabalho":
        pts += 10
    elif resposta[6] == "Misto":
        pts += 20

    lista.append(pts)

    # Perfil
    if pts <= 80:
        lista.append("Risco Baixo")
    elif 80 < pts <= 100:
        lista.append("Risco Medio")
    elif pts > 100:
        lista.append("Risco Alto")

    # Valor a ser pago
    if pts <= 80:
        seguro = valor * 0.1
        lista.append(seguro)
    elif pts <= 100:
        seguro = valor * 0.2
        lista.append(seguro)
    elif pts > 100:
        seguro = valor * 0.3
        lista.append(seguro)

    return lista

assert calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto']) == [120, "Risco Alto", 600.0]
