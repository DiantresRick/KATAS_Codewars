# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.


def summation(num):
    acumulador = 0
    for i in range(1,num + 1):
        acumulador = acumulador + i   
    return acumulador


def summation2(num):
    return sum(range(1,num+1))

if __name__ == "__main__":

    ## Test summation
    assert(summation(1), 1)
    assert(summation(8), 36)

    ## Test summation2
    assert(summation2(1), 1)
    assert(summation2(8), 36)

