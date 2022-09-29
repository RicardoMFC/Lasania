# Lasania
Proyecto basico de ing mat

https://github.com/RicardoMFC/Lasania.git

Introducción
Python es un lenguaje de programación orientado a objetos dinámico y fuertemente tipado . Emplea tipeo pato y tipeo gradual , a través de sugerencias de tipo . La programación a través de paradigmas es totalmente compatible , pero internamente, todo en Python es un objeto .

Python pone un fuerte énfasis en la legibilidad del código y ( similar a Haskell ) utiliza una sangría significativa para las definiciones de funciones, métodos y clases. El Zen de Python (PEP 20) y ¿Qué es Pythonic? establecer filosofías adicionales.

Los objetos se asignan a nombres a través del operador de asignación , =. Las variables se escriben en snake_case, y las constantes generalmente en SCREAMING_SNAKE_CASE.

Una name( variable o constante ) no se escribe en sí misma y se puede adjuntar o volver a adjuntar a diferentes objetos durante su vida útil. Para convenciones de nomenclatura extendidas y consejos, consulte PEP 8 .

>>> my_first_variable = 1
>>> my_first_variable = "Last one, I promise"
>>> print(my_first_variable)
...
"Last one, I promise"
Las constantes normalmente se definen en un módulo o nivel global , y aunque se pueden cambiar, se pretende que se nombren solo una vez.

Su SCREAMING_SNAKE_CASEes un mensaje a otros desarrolladores de que la asignación no debe modificarse:

# All caps signal that this is intended as a constant.
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but this is VERY strongly discouraged.
# Please don't do: MY_FIRST_CONSTANT = "Some other value"
La palabra clave defcomienza una definición de función . Debe ir seguido del nombre de la función y una lista entre paréntesis de cero o más parámetros formales . Los parámetros pueden ser de varias variedades diferentes, e incluso pueden variar en longitud. La deflínea se termina con dos puntos.

Las instrucciones para el cuerpo de la función comienzan en la siguiente línea defy deben sangrarse en un bloque . No hay una cantidad de sangría estricta ( se aceptan espacios O [tabuladores] ), pero la sangría debe ser consistente para todas las declaraciones sangradas .

Las funciones devuelven explícitamente un valor u objeto a través de la returnpalabra clave.

# Function definition on first line.
def add_two_numbers(number_one, number_two):
  return number_one + number_two  # Returns the sum of the numbers, and is indented by 2 spaces.

>>> add_two_numbers(3, 4)
7
Las funciones que no tienen una returnexpresión explícita devolverán None.

# This function will return None.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two

>>> print(add_two_numbers(5, 7))
None
La sangría inconsistente generará un error:

# The return statement line does not match the first line indent.
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   # Indented by 4 spaces.
...    return result     #this was only indented by 3 spaces
  File "<stdin>", line 3
    return result
                ^
IndentationError: unindent does not match any outer indentation level
Las funciones se llaman usando su nombre seguido de (). El número de argumentos pasados ​​entre paréntesis debe coincidir con el número de parámetros en la definición de función original, a menos que se hayan utilizado argumentos predeterminados :

>>> def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.
        
        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number
        
        Takes number_one and raises it to the power of number_two, returning the result.
        """
        
        return number_one ** number_two
...

>>> number_to_the_power_of(3,3)
27
Una falta de coincidencia entre los parámetros y los argumentos generará un error:

>>> number_to_the_power_of(4,)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'

Agregar un valor predeterminado para un parámetro puede defenderse contra tales errores:

>>> def number_to_the_power_of_default(number_one, number_two=2):
        """Raise a number to an arbitrary power.
        
        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number
        
        Takes number_one and raises it to the power of number_two, returning the result.
        """

        return number_one ** number_two

...
>>> number_to_the_power_of_default(4)
16
Los métodos vinculados a los nombres de clase se invocan a través de la notación de puntos (.), al igual que las funciones, las constantes o los nombres globales importados como parte de un módulo.:


import string

# This is a constant provided by the *string* module.
>>> print(string.ascii_lowercase)
"abcdefghijklmnopqrstuvwxyz"

# This is a method call of the str *class*.
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)
"MY SILLY SENTENCE FOR EXAMPLES."

# This is a method call of an *instance* of the str *class*.
>>> start_text.upper()
"MY SILLY SENTENCE FOR EXAMPLES."
Los comentarios en Python comienzan con un #que no es parte de una cadena y terminan en la terminación de línea. A diferencia de muchos otros lenguajes de programación, Python no admite marcas de comentarios de varias líneas. Cada línea de un bloque de comentarios debe comenzar con el #carácter.

Los comentarios son ignorados por el intérprete:

# This is a single line comment.

x = "foo"  # This is an in-line comment.

# This is a multi-line
# comment block over multiple lines --
# these should be used sparingly.
La primera declaración del cuerpo de una función puede ser opcionalmente una cadena de documentos , que resume de manera concisa el propósito de la función o el objeto. Las cadenas de documentos se leen mediante herramientas de documentación automatizadas y se devuelven llamando .__doc__a la función, el método o el nombre de la clase. También pueden funcionar como pruebas unitarias ligeras , que se tratarán en un ejercicio posterior. Se recomiendan para programas de cualquier tamaño donde se necesita documentación, y sus convenciones se establecen en PEP257 :

# An example on a user-defined function.
>>> def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.
        
        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number
        
        Takes number_one and raises it to the power of number_two, returning the result.
        """

        return number_one ** number_two
...

>>> print(number_to_the_power_of.__doc__)
Raise a number to an arbitrary power.

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.

# __doc__() for the built-in type: str.
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
Instrucciones
Vas a escribir un código que te ayude a cocinar una deliciosa lasaña de tu libro de cocina favorito.

Tienes cinco tareas, todas relacionadas con cocinar tu receta.

Tarea 1
Defina el tiempo de horneado esperado en minutos

Defina una EXPECTED_BAKE_TIMEconstante que devuelva cuántos minutos debe hornearse la lasaña en el horno. Según su libro de cocina, la lasaña debe estar en el horno durante 40 minutos:

>>> import lasagna
>>> lasagna.EXPECTED_BAKE_TIME
40

¿Atascado? Revelar sugerencias
Se abre en un modal
Tarea 2
Calcule el tiempo de horneado restante en minutos

Tarea 3
Calcula el tiempo de preparación en minutos

Tarea 4
Calcule el tiempo total de cocción transcurrido (preparación + horneado) en minutos

Tarea 5
Actualizar la receta con notas.

