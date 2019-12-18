# class teste:




### ARGS


def alteraServidor(*ip):
    for i in range(3):
        print("O IP é ", ip[i])


alteraServidor("192.168.10.1", "10.21.174.23", "10.21.223.26")


#### KWARGS

def classeRede(**ip):
    print('o IP atual é ', ip['ip'])
    print('o novo IP é ', ip['novo'])

classeRede(ip = "10.21.174.23", novo = "10.21.229.13")