# Function to compute maximum heart rate
def maxHR(age):
    max=208-0.7*age

    #parte 1 
    print("tu frecuencia cardiaca es ",max)
    
def fre(Rc):
  
    max =208-0.7*age
    if (float(max*0.6))>Rc>=(float(max*0.5)):
       print("Estas en la zona de recuperacion ")
    elif (float(max*0.7))>Rc>=(float(max*0.6)):
       print("estas en la zona de quema de grasa ")
    elif float(max*0.8)>Rc>=(max*0.7):
       print("estas en la zona aerobica ")
    elif (max*0.9)>Rc>=(max*0.8):
       print("estas en la zona de umbral anaerobico ")
    elif Rc>=(max*9):
        print("estas en la zona de esfuerzo maximo ")
        print("Ten cuidado estas al limite ")
    else:
        print("Estas en un estado de reposo ")
  

def entrenamiento(num):
    max =208-0.7*age
    prom=0
    Z1=0
    Z2=0
    Z3=0
    Z4=0
    Z5=0 
    Z6=0
    
    for i in range(num):
        ejercicio=int(input("Ingresa cual es tu frecuencia cardiaca actual: "))
        if (610>=ejercicio>=16):
          prom=prom+ejercicio
          if (max*0.6)>ejercicio>=(max*0.5):
             Z1=Z1+1 
          elif (max*0.7)>ejercicio>=(max*0.6):
            Z2=Z2+1
          elif (max*0.8)>ejercicio>=(max*0.7):
            Z3=Z3+1
          elif (max*0.9)>ejercicio>=(max*0.8):
            Z4=Z4+1
          elif ejercicio>=(max*0.9):
            Z5=Z5+1
          else:
            Z6=Z6+1
        else:
          print("Ingresaste un numero equivocado ")
    promedio=prom/num
    print("Estas fueron tus notas de entrenamiento ")
    print("El promedio de tu frecuencia cardiaca fue de ",promedio)
    print("El numero de veces que estuviste en cada una de ellas fue de ")
    print("1. en la zona de recuperacion ", Z1)
    print("2. en la zona de quema de grasa estuviste ", Z2)
    print("3. en la zona aerobica ", Z3)
    print("4. en la zona del umbral anaerobico ", Z4)
    print("5. en la zona de esfuerzo maximo ", Z5)
    print("6. en la zona de reposo ", Z6)

def entrenamiento2(age):
  if 10>age>=0:
    print("Te recomiendo hacer juegos al aire libre, natacion y bailes ")

  elif 20>age>=10:
     print("Te recomiendo hacer Deportes de equipo, Ciclismo, Entrenamiento de fuerza, Correr o trotar")
  
  elif 30>age>=20:
    print("Te recomiendo hacer entrenamientos de intervalos de alta intensidad, Entrenamiento de fuerza, Clases grupales o deportes individuales ")

  elif 40>age>=30:
    print("Te recomiendo hacer Entrenamiento funcional, Yoga, pilates, Caminatas rápidas, senderismo, Ciclismo indoor o outdoor")

  elif 50>age>=40:
    print("Te recomiendo la Natación, entrenamiento en circuito, Clases de baile, Senderismo")

  elif 130>age>=50:
    print("Te recomiendo hacer Caminatas diarias, ejercicios acuáticos, tai Chi,  yoga, Entrenamiento de resistencia ligera")
 
  else:
    print("Ingresaste una edad inadecuada ")

#menu

if 1==1:
  print("Que quieres hacer?")
  print ("1. saber en que estado estas ")
  print("2. hacer un entrenamiento y ver ")
  print("3. saber que entrenamiento debes realizar para quemar grasa ")
  print("4. Solo tu frecuencia maxima ")
  entre=int(input("Ingresa que configuracion quieres escojer: "))

  if  entre==1:
    age=int(input('Enter your age: '))
    Rc=float(input("Ingresa tu frecuencia actual "))
    if(610>=Rc>=16)and(130>=age>=0):
      maxHR(age)
      fre(Rc)
    else:
      print("Te equivocaste en la frecuencia cardiaca o estas sufriendo algo extraordinario ")

  elif entre==2:
    age=float(input("Ingresa tu edad: "))
    num=int(input("Ingresa el numero de entrenamientos: "))
    if 130>=age>=0: 
      entrenamiento(num)
  elif entre==3:
    age=int(input('Enter your age: '))
    entrenamiento2(age)
  elif entre==4:
    age=int(input('Enter your age: '))
    maxHR(age)
  else:
    print("escojiste una configuracion equivocada ")

 
   

