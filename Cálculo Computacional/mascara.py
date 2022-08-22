
def getNumero(numeroInteiro):
        a = str(numeroInteiro) #recebe o número
        z = a[::-1] #faz a inversão
        b = ''   #guarda o resultado da inversão
        cnt = 0 #conta os números para colocar o ponto(de trás para frente)

        for i in z:

                if cnt == 3: #a cada três coloca um ponto
                        b += '.'
                        cnt = 0 #retorna o contador a zero
                        b+=i # adiciona o próximo número e conta em "cnt"
                        cnt +=1

                else: #caso contador não seja três não adiciona ponto
                        b+=i
                        cnt += 1

        d  = b[::-1] # faz a reinversão e coloca em d
        return d

