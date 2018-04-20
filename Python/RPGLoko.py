# coding: utf-8
#RPG muito Louco

#(import os) - Para limpar: system('clear')

Nome = raw_input("Digite seu Nome Guerreiro: ")
pontuacao = 0
HP = 10
Inventario = []


def Inventario():
    print
    print "Inventário:"
    for i in range(len(Inventario)):
        print "%d.", Inventario[i]
        

print
print " Era uma vez, um nobre guerreiro chamado %s, no qual se aventurou numa incrivel jornada." % Nome
print "Ao chegar lá, não importa aonde, encontrou um Velho."
print

fase1 = int(raw_input("•Matar o velho, digite 1.\n•Chingar o velho, digite 2."))

if fase1 == 1:
    print
    print "HP(Velho): 0"
    print "Pontuação: +5"
    print "Conquista: Assassino Sangue Frio."
    print
    print "Parabéns, você matou o velho, e recebeu uma Recompensa."
    pontuacao = pontuacao + 5
    print
    print "•Espada de Esmaralda Adquirida."
    print
    print "(Reza a lenda, que tal Espada era de um dragão, e sua lâmina deve ser guardada para o final do jogo.)"
    print
    print "%s: O sangue desse Velho parece ser bem Louco, algo me diz que vem Treta pela frente." % Nome
    print
    fase2 = int(raw_input("•Continuar jornada, digite 1.\n•Treinar movimentos com o Novo Item, digite 2."))
    if fase2 == 1:
        print
        print '"Chinga todo mundo, menos a poha da minha mãe!" ... Voz ao fundo.'
        print "%s: Que poha é essa?" % Nome
        print
        print "Muleque Invocado vem lhe atacar."
        print
        fase3 = int(raw_input("•Desviar do Golpe, digite 1.\n•Defender Golpe, digite 2."))
        if fase3 == 2:
            print
            print "Tentativa de Defesa Fail."
            print
            print "Hit: 2 HP"
            HP = HP - 2
            print "HP(%s): %d" % (Nome, HP)
            print
            print "%s: Os golpes desse Muleque, apesar de no ar, me acertam com muita voracidade!" % Nome
            print "Muleque Invocado: Seu imbecil!"
            print
            fase4 = int(raw_input("•Atacar com Estilingue, principal arma do Nobre Guerreiro %s, digite 1.\n•Usar Espada de Esmeralda, digite 2." % Nome))
            if fase4 == 1:
                print
                print "Hit: 2 HP"
                pontuacao = pontuacao + 2
                print 
                print pontuacao
            print
            if fase4 == 2:
                 print
                 print "Você utilizou a Espada de Esmeralda de maneira tola."
                 print 
                 print "Hit: 1"
                 print "Espada de Esmeralda: Efeito Reverso."
                 print
                 HP = HP - 1
                 print "HP(%s): %d" % (Nome, HP)
                 print "HP(Muleque Invocado): 1"
                 print
                 fase5 = int(raw_input("%s: Quem é você? Eu não chinguei tua mãe!, Digite 1.\n•%s: Maldito Muleque Invocado dos golpes Fail, Segura teu óculos!, Digite 2." % (Nome, Nome)))
    if fase2 == 2:
        print 
        print "O Nobre Guerreiro %s puxa a 'Espada de Esmeralda' e sente em tuas mãos um poder jamais sentido. Percebe que aquela não é uma simples espada e que não pode ser usada de qualquer maneira." % Nome
        print
        fase3 = int(raw_input("•Deseja continuar com o Treinamento?, digite 1.\n•Não utilizar a Espada(Indicação do Jogo), digite 2."))
        if fase3 == 1:
            print
            print "Jogo: Tu é um corno viu bicho?, se ferra ai."
            HP -= 1
            print
            print "Hit: 1"
            print "HP: %d" % HP
            pontuacao += 2
            print "Pontuação: +2"
            print "Conquista: Analista de Itens."
            print
            print "%s: A espada aparenta surtir um Efeito Reverso." % Nome
            print
            fase4 = int(raw_input("•Dropar a 'Espada de Esmeralda, digite 1.\n•Guardar Item(Limite de 3 Itens no Inventário), digite 2."))
            if fase4 == 1:
                print
                print 
elif fase1 == 2:
    print
    print "-%s: Velho!" % Nome
    print
    print "-Velho: Você é foda cara! Ninguem nunca me chamou assim."
    print
    print "-Velho: Sou o Mestre dos Manos, conhecido como 'Mano Vô' e comando um Exercito... mas ele se perdeu."
    print
    fase2 = int(raw_input("•Juntar-se ao Exercito dos Manos, digite 1.\n•Odiar o Exercito dos Manos e se filiar aos Bolsominions que vem se aproximando, digite 2."))
    if fase2 == 1:
        print
        print "%s: Fala Catxorro, cualé do bagulho doido? Posso colar nessa quebrada?" % Nome
        print
        print "Velho: Ta Pegando Fogo, Bixo!"
        print
        fase3 = int(raw_input("•%s: Chama os Bombeiros!, digite 1.\n•%s: Quê?, digite 2.\n•Correr para apagar fogo imaginário, digite 3." % (Nome, Nome)))
        if fase3 == 2:
            print
            print "Velho: Pois é mano, é Caixa Baixa vagabundo! Tu não deveria ficar por aqui."
            print 
            print "Nesse momento vem se aproximando um bando de Bolsominions em sua direção."
        if fase3 == 1:
            print
            print "Velho: Você respondeu meu meme corretamente, irei me juntar a você em sua jornada."
            print
            print "•Velho Adquirido."
        if fase3 == 3:
            print
            print "Velho: Tu esta me chamando de Louco? Saiba bem que eu carrego uma cha..."
            print
            print "Chega um bando de Bolsominions, gritando e cortando a fala do Velho."
            print
        
    if fase2 == 2:
        print
        print "Ao se posicionar contra o 'Mano Vô', o exército de Bolsominions aparenta estar farto de tanta Corrupção, e não se coloca contra ninguem."
        print
        fase3 = int(raw_input("•Atacar Mano Vô, digite 1.\n•Gritar: DILMÃE!, digite 2."))
        print
        if fase3 == 1:
            print "Mano Vô exibe uma Espada com aspecto brilhante e, em frações de segundo, faz um giro no ar, no qual corta as pernas de cerca de 3 Manifestantes."
            print
            print "Mano Vô: Corra!"
            fase4 = int(raw_input("•Correr, digite 1.\n•Ficar e Lutar!, digite 2."))
            if fase4 == 2:
                print
                print "Dois dos Bolsominions (2/10), um com um Consolo na mão vem em sua direção"
                print
                print "%s: Oh não! Um consolo." % Nome
                print
                fase5 = int(raw_input("•Equipar-se com 'Estilingue', principal arma do Nobre Guerreiro %s, digite 1.\n•Equipar câmera de celular, digite 2." % Nome))
                if fase5 == 1:
                    print "Rode o dado-20"
                    print
                if fase5 == 2:
                    print "Cuidado: Uma imagem vale mais que mil palavras."
                    print
                    print "Mano Vô: Não quero ter que machucar ninguem, essa Manifestação não possui propostas econômicas, mas respeito quem possui baixo intelecto."
                    print
                    print "%s: Você é Louco?" % Nome
                    print
                    fase6 = int(raw_input("•Filmar mano Vô, digite 1.\n•Filmar Bolsominions, digite 2."))
                    if fase6 == 1:
                        print
                        print "Nesse momentos, Mano Vô efetua golpes tão rápidos que a câmera mal conseguiu gravas seus movimentos."
                        print
                        print "Noticiário: Manifestantes usam suas pernas para atacar idoso, e por propostas de projetod aprovados do atual Presidente 'Globinho TV', o senhor consegue ter segurança e sai ileso."
                        print
                        fase7 = int(raw_input("•Continuar filmando o massacre, digite 1.\n•Tentar conter o confronto publicando o vídeo na Internet, digite 2."))
                        if fase7 == 1:
                            print
                            print "Helicópteros da TV Roubo se posicinam para fazer filmagens aéreas da Movimentação Policial."
                            print
                            print "Noticiário: Segundo postagens da Internet, cerca 2000 manifestantes estão de movimentando até o Local."
        if fase3 == 2:
            print "Um bando de Bolsominions se viram pra ti e se posicionam em Modo de Ataque."
            print
            fase4 = int(raw_input("•Atacar com Estilingue, principal arma do Nobre Guerreiro %s, digite 1.\n•Se preparar pra se defender de ataques de raiva e chingamentos na Internet, digite 2." % Nome))
