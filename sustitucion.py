from math import gcd
c = 'JFWFG DSWHM HWOCA FRPQG DGWSC AGWGO KGOHK GOGWW FYCOO HZGÑF WZGKG OGWBF MFDKF SCOSC OKFWB CPQGD HGOKG GBFBI FCQOF AHDKC WHFNF OKFDK HSFPQ GZGBG HKGDQ GVCDF ÑGOCD CKFBX GYSWG GWBCP QGOQO SFNQG.'
c1 = c.replace(' ', '')
m = 'PARAESCRIBIRNOHAYQUESERCOHERENTENITENERRAZONNIDEJARDETENERLABASTACONCONTARLOQUESIENTEELALMAOUNAHISTORIAFANTASTICAQUEDELEITESUEÑOSAJENOSOTALVEZCREERLOQUENUNCAFUE'
m1 = m.replace(' ', '')
c = c.upper()
m = m.upper()
word_list = list (c1.upper())
word_list1 = list (m1.upper())
abc = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
primero = []
primos = []
multi = []
palabra_desifrada = []
palabra_encriptada = []
n = 27
descifrar = 1


for i in range(len(abc)):

    if (descifrar == 1):
        primero.append(c.count(abc[i]))
        print(abc [i] + ' = ' + str(c.count(abc[i])))
    else:
        primero.append(m.count(abc[i]))
        print(abc [i] + ' = ' + str(m.count(abc[i])))

for i in range(len(primero)):
    
    if(primero[i] == max(primero)):
        max_prim = i
        print (abc[i] + '=' + str(primero[i]))
    if(primero[i] == sorted(primero)[-2]):
        max_seg = i
        print (abc[i] + '=' + str(primero[max_seg]))

for i in range(n):
    multi.append(n*i)
    
    if (gcd(i,n) == 1):
        primos.append(i)

def hallar_a (b):

    a = (max_prim-b) * 7 %n

    return(a)

def hallar_ainv (a):
    ainv = 0
    for k in range(len(primos)):
        if(a != primos[k]):
            continue
        for i in range(n):
            for j in range(n):
                    if(a*i == multi[j]+1):
                        ainv = i

    return(ainv)


if (descifrar == 1):
    for b in (range(n)):
        a = hallar_a(b)
        ainv1 = hallar_ainv(a)
        for i in range(len(word_list)):
            for j in range(len(abc)):
                if (word_list[i] == abc[j]):
                    letra1 = ((j - b) * ainv1) %n
                    palabra_desifrada.append(abc[letra1])

    palabra_final = "".join(palabra_desifrada)
    print (palabra_final)
        #print(a,b)
    print ('El nuevo diccionario es')
    for i in range(len(abc)):
        letra = ((i - 5) * 4) %n
        print(abc[i] + ' = ' + abc [letra])

else:
    a = 5
    b = 10
    for i in range(len(word_list1)):
        for j in range(len(abc)):
            if (word_list1[i] == abc[j]):
                letra = (a*j + b) %n
                palabra_encriptada.append(abc[letra])
    
    palabra_final = "".join(palabra_encriptada)
    print(palabra_final)
    print(a, b)
    print ('El nuevo abecedario es: ')
    for i in range(len(abc)):
        letra = (a*i + b) %n
        print(abc[i] + ' = ' + abc [letra])

