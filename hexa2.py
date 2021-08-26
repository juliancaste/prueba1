
def digito(hexa):
    bina = "{0:04b}".format(int(hexa, 16))
    return (bina)

def list_str(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def interprete(trama):

    for bloque in trama:
        bin =[]
        for dig in bloque:
            res= digito(dig)
            for bi in res:
                bin.append(bi)
        act=bin[0]
        leds=bin[1:8]
        valor=bin[8:16]

        print(bin)
        if int(act) == 0:
            print("No activos")
        else:
            print("Activos ! ")

        print(list_str(leds))
        num_leds=int(list_str(leds), 2)
        print("numero de leds = ",num_leds)

        print(list_str(valor))
        num_valor=int(list_str(valor), 2)
        print("Valor del pulso = ", num_valor)


trama=['58A6', 'FC89', 'BD1A', '4313' ,'1250', '0F21', 'C89B', 'D1A4' ]
interprete(trama)