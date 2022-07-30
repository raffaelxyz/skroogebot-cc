import random
import os
os.system("clear")
print("███████▀▀▀░░░░░░░▀▀▀███████")
print("████▀░░░░░░░░░░░░░░░░░▀████")
print("███│░░░░░░░░░░░░░░░░░░░│███")
print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
print("██▌░│██████▌░░░▐██████│░▐██")
print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
print("████▄─┘██▌░░░░░░░▐██└─▄████")
print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
print("███████▄░░░░░░░░░░░▄███████")
print("██████████▄▄▄▄▄▄▄██████████")
print("╔═╗╔╗────────────────╔╗────╔╗─")
print("║═╣║╠╗╔╦╗╔═╗╔═╗╔═╗╔═╗║╚╗╔═╗║╚╗")
print("╠═║║═╣║╔╝║╬║║╬║║╬║║╩╣║╬║║╬║║╔╣~ig: @raffaelxy_z")
print("╚═╝╚╩╝╚╝─╚═╝╚═╝╠╗║╚═╝╚═╝╚═╝╚═╝")
print("───────────────╚═╝────────────")
print("GERADOR DE CC FULL INTER")
print("dc: rafaellindao#0001")
print("Escolha uma bin:")
print("[1]VISA TRADITIONAL")
print("[2]MASTERCARD STANTARD")
print("[3]MASTERCARD CORPORATE")
print("[4]MASTERCARD GOLD")
print("[5]VISA PLATINUM")
print("[6]MASTERCARD BLACK")
print("[7]VISA INFINITE")
esc_bin = int(input())
esc_quantia = int(input("Digite uma quantia (VALOR MAXIMO \"1M\"):\n"))
local = input("Informe o local que esta o txt que deseja salvar tudo(NAO PRECISA POR O \".txt\"):\n")
local = local + ".txt"
co = 0


#SE ISSO FAÇA ISSO...
if(esc_bin<=0 or esc_bin>7):
    print("DIGITE UMA OPÇAO QUE EXISTA!!")

elif(esc_quantia<=0 or esc_quantia>1000000):
    print("DIGITE UMA QUANTIA VALIDA NÃO MENOR QUE 0 E NÃO MAIOR QUE 1M!!")

while(co<esc_quantia):
    if(esc_bin==1):
        bin = 439160
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|VISA|TRADITIONAL")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1

    elif(esc_bin==2):
        bin = 527498
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|MASTERCARD|STANDARD")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1

    elif(esc_bin==3):
        bin = 556614
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|MASTERCARD|CORPORATE")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1

    elif(esc_bin==4):
        bin = 530701
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|MASTERCARD|GOLD")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1

    elif(esc_bin==5):
        bin = 402381
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|VISA|PLATINUM")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1

    elif(esc_bin==6):
        bin = 553660
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|MASTERCARD|BLACK")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1

    elif(esc_bin==7):
        bin = 439474
        segundo = (random.randrange(1000000000,9999999999))
        data_mes = (random.randrange(1,12))
        if(data_mes<10):
            data_mes = "0" + str(data_mes)
        data_ano = (random.randrange(2023,2027))
        cvv = (random.randrange(100,999))
        gerar = (str(bin) + str(segundo) + "|" + str(data_mes) + "|" + str(data_ano) + "|" + str(cvv) + "|BANCO INTER, S.A.|VISA|INFINITE")
        abrirArquivo = open(r"" + local, "a")
        abrirArquivo.write(str(gerar) + "\n")
        abrirArquivo.close()
        co = co + 1
print("APROVEITE AS CCS!!")
