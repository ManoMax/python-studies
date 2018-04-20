# coding: utf-8
# Media Mulher

pers = float(raw_input("Personalidade (0 a 10): "))
inte = float(raw_input("Inteligencia (0 a 10): "))
corpo = float(raw_input("Corpo (0 a 10): "))
boca = float(raw_input("Boca/Sorriso (0 a 10): "))
feti = float(raw_input("Fetiche (0 a 10): "))
bran = float(raw_input("Branquice (0 a 10): "))

media = ((pers * 2 + inte * 2 + corpo * 2 + boca * 2
		+ feti + bran) / 10)

print "\nSua mina tem a média: %s" % media
