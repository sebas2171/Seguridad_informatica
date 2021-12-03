c = 'TSPDX TCPHM UZPUR SQNLG HOIMI DRUAA PGBÑZ EPPQL OUBLT DSIKP BIUZV YKOMI KEXEQ AADEE CYPDÑ TIKHT IOGAR IFCDQ VAÑTS KTWGO JQREC LEBEJ EEPBF RZICD YBSDV MPCZQ ZPOWG AQMIN CLFIL EOTEI QQTWE NCQLA TEUAD DÑDEZ MSDSA MLSKZ'
c1 = c.replace(' ', '')
m = 'Miro a mi alrededor veo que la tecnologia ha sobrepasado nuestra humanidad espero que algun dia nuestra humanidad sobrepase la tecnologia'
m1 = m.replace(' ', '')
c1 = c1.upper()
m1 = m1.upper()
word_list = list (c1)
word_list1 = list (m1)
clave = ('tecnologia').upper()
clave = list(clave)
n1 = len(clave)
abc = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
palabra = []
n = 27
decifrar = 0
vignere = 0
autoclave = 1
largo_clave = len(clave)
largo_palabra = len(word_list)
largo_palabra1 = len(word_list1)




if (decifrar == 1):
    for i in range(largo_palabra):
        if (largo_clave < largo_palabra):
            
            if (autoclave == 1):
                clave.append(word_list1[i])
                largo_clave = len(clave)
            
            else:
                j = i % n1
                clave.append(clave[j])
                largo_clave = len(clave)
        
        else :
            break

    for i in range(largo_palabra):
        for j in range(len(abc)):
            if (word_list[i] == abc[j]):
                for k in range(len(abc)):
                    if (clave[i] == abc[k]):
                        if (vignere == 1):  
                            letra_descifrada = (j - k) %n
                        else :
                            letra_descifrada = (k - j) % n

                        palabra.append(abc[letra_descifrada])

else:

    for i in range(largo_palabra1):
        if (largo_clave < largo_palabra1):
            clave.append(word_list1[i])
            largo_clave = len(clave)
        
        else :
            break
    
    print (clave)
    print (largo_clave)
    print (largo_palabra1)

    for i in range(largo_palabra1):
        for j in range(len(abc)):
            if (word_list1[i] == abc[j]):
                for k in range(len(abc)):
                    if (clave[i] == abc[k]):
                        letra_cifrada = (j + k) %n
                        palabra.append(abc[letra_cifrada])


palabra_final = "".join(palabra)

print (palabra_final)