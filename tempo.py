numero = input("Coloque o tempo em segundos:")
segundo = int(numero)
minuto = 0
hora = 0

if segundo >= 60:
    minuto = segundo//60
    segundo = segundo%60
        
if minuto >= 60:
    hora = minuto//60
    minuto = minuto%60

print(hora, ":", minuto, ":", segundo)