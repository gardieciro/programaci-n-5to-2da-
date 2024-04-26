nota1=int(input("ingrese laprimera nota:"))
nota2=int(input("ingrese la segunda nota:"))
nota3=int(input("ingrese la tercer nota:"))

prom=(nota1+nota2+nota3)/3

if prom>=7:
     print("usted esta promocionada,su nota es:",prom)

elif prom>=4:
     print("usted esta regular,su nota es: ",prom)

else :
     print("usted esta reprobado,su nota es:",prom)
