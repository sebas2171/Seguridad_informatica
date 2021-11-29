c = 'ÑDVHJXULGDGLPIRUODWLFDRVHJXULGDGGHWHFPRÑRJLDVGHÑDLP IRUODFLRPHVHÑDUHDGHÑDLPIRUODWLFDTXHVHHPIRFDHPÑDSURWHFFL RPGHÑDLPIUDHVWUXFWX U'
c1 = c.replace(' ', '')
m = 'Los hombres jovenes quieren ser fieles y no lo consiguen los hombres viejos quieren ser infieles y no lo logran'
m1 = m.replace(' ', '')
c = c.upper()
m = m.upper()
print(m)
word_list = list (c1.upper())
word_list1 = list (m1.upper())
abc = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
primero = []
segundo = []
palabra = []
n = 27
decifrar = 1
# b es cero para poder usar el metodo de los dos primeros numeros que mas se repite por si no se conoce la b
# si se tiene b se opta por poner su valor y asi cifrar y desifrar con dicho desplazamiento
b= 0

for i in range(len(abc)):
    if (decifrar == 1):
        primero.append(c.count(abc[i]))
        segundo.append(c.count(abc[i]))
        print(abc [i] + ' ' + str(c.count(abc[i])))
    else:
        primero.append(m.count(abc[i]))
        segundo.append(m.count(abc[i]))
        print(abc [i] + ' ' + str(m.count(abc[i])))

segundo.remove(max(segundo))

for i in range(len(primero)):
    if(primero[i] == max(primero)):
        max_prim = i
        print ('primero: ' + abc[i] + '=' + str(primero[i]))
    if (len(segundo) > i):
        if(segundo[i] == max(segundo)):
            max_seg = i
            print ('segundo: ' + abc[i] + '=' + str(segundo[i]))


if (b == 0):
    b = max_prim %n
    b1 = max_seg %n
else:
    b1 = b

if (decifrar == 1):
    for i in range(len(word_list)):
        for j in range(len(abc)):
            if (word_list[i] == abc[j]):
                # si por alguna razon b no desifra el mensaje se debe cambiar por b1 dentro de la ecuacion
                # de la siguiente manera (j+(n-b)) %n por (j+(n-b1)) %n
                letra_desifrada = (j + (n-b)) %n
                palabra.append(abc[letra_desifrada])

else:
    for i in range(len(word_list1)):
        for j in range(len(abc)):
            if (word_list1[i] == abc[j]): 
                letra_cifrada = (j+b) %n
                palabra.append(abc[letra_cifrada])


palabra_final = "".join(palabra)

print (palabra_final)