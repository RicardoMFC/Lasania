EXPECTED_BAKE_TIME=40 
#Creo una constante que define cuantos minutos tiene que estar en el horno la lasaña
x = int (input("Introduzca cuantos minutos lleva en el horno\n"))
#Creo una variable y a través de la función input leo por teclado cuantos minutos lleva la lasaña en el horno

def bake_time_remaining(num1):
    print ("Quedan",EXPECTED_BAKE_TIME-x)
#Defino una función que me devuleve cuantos minutos más debo dejar la lasaña en el horno, para ello leo por teclado el tiempo que lleva en el horno y se lo resto a mi constante EXPECTED_BAKE_TIME
bake_time_remaining (x)

y=int(input("Cuantas capas quiere agregar a la lasania\n"))
#Leo por taclado cuantas capas se quieren agregar a la lasaña

def preparation_time_in_minutes(num2):
  val=y*2
  print ("Tardará", val ,"minutos")
#Defino otra funcion que me dice cuantos minutos tardare en preparar las capas de la lasaña, teniendo en cuenta que se tarda en preparar cada capa dos minutos
preparation_time_in_minutes(y)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  res=x+y*2
  print ("Minutos trabajados", res)
#Por ultimo, hago otra funcion que devuelve el tiempo que se ha invertido en hacer la lasaña, a partir de sumar los minutos que lleva en el horno la lasaña y el tiempo que se tarda en hacer cada capa. 
elapsed_time_in_minutes(y,x)