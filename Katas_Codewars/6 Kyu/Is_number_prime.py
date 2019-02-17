# Define a function isPrime/is_prime() that takes one integer argument and returns 
# true/True or false/False depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 
# that has no positive divisors other than 1 and itself.


def is_prime(number):
    position = 2
    while position < number:
        if number % position == 0:
            return False
        position = position + 1
    if position == number:
        return True
    else:
        return False


if __name__ == __main__:

	assert is_prime(0)== False
	assert is_prime(1)== False
	assert is_prime(2)== True

### Historia de usuario
## Numero primo == Solo divisible entre si o la unidad
## Dividir por todos los numeros hasta la unidad
## Detener el recorrido si antes encontramos divisores