resp = input ("Cal é o primeiro cateto?    ") 
resp2 = input ("Cal é o segundo cateto?    ")
numero = int(resp)
numero2 = int(resp2)
import math
cua1 =  (numero * numero)
cua2 = (numero2 * numero2)
hipo = math.sqrt(cua1 + cua2)
print ("esta é a tua hipotenusa ",    hipo)


