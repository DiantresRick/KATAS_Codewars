# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.


    #Replace sustituye todos los caracteres objetivo, por el que caracter que decides
def remove_exclamation_marks(s):
       
    s = s.replace("!", "")
    return s


    # Inicializar un  string vacio
    # Recorrer el string, y guardar todo lo que no sea !
def remove_exclamation_marks2(s):
    
    result_string=""

    for items in s:
        if(items!="!"):
            result_string+=items
    
    return result_string


if __name__ == "__main__":
    
   
    assert(remove_exclamation_marks("Hello World!")== "Hello World")
    assert(remove_exclamation_marks("Hello World!!!")== "Hello World")
    assert(remove_exclamation_marks("Hi! Hello!")== "Hi Hello")
    assert(remove_exclamation_marks("")== "")
    assert(remove_exclamation_marks("Oh, no!!!")== "Oh, no")