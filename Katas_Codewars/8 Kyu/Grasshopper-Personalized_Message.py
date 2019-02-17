# Personalized greeting
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
# Use conditionals to return the proper message:
# ======= case | return --- | --- name equals owner | 'Hello boss' otherwise | 'Hello guest'


def greet(name, owner):
    if name == owner :
        return ('Hello boss')
    else:
        return ('Hello guest')
    

def greet2(name, owner):
    return "Hello boss" if name == owner else "Hello guest"



if __name__ == "__main__":
    
    ## Test Greet1
    assert(greet('Daniel', 'Daniel')== 'Hello boss')
    assert(greet('Greg', 'Daniel')== 'Hello guest')

    ## Test Greet2  
    assert(greet2('Daniel', 'Daniel')== 'Hello boss')
    assert(greet2('Greg', 'Daniel')== 'Hello guest')