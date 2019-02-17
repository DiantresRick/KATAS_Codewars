# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.


def parse(data):
    array = []
    valor = 0
    
    for item in data:
        if item == "i":
            valor += 1 
        if item == "d":
            valor -= 1
        if item == "s":
            valor = valor**2
        if item == "o":
            array.append(valor)

    return array




if __name__ == "__main__":

## Test 1
    assert(parse("ooo")== [0,0,0])
## Test 2
    assert(parse("ioioio")== [1,2,3])
## Test 3
    assert(parse("idoiido")== [0,1])
## Test 4
    assert(parse("isoisoiso")== [1,4,25])
## Test 5   
    assert(parse("codewars")== [0])
