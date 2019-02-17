# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything 
# but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.



def validate_pin(pin):
    
    if len(pin) != 4 and len(pin) != 6:
        return False
    else: 
        if pin.isdigit(): 
            return True
        else:
            return False

if __name__ == "__main__":
    
    ## TEST CASES 1
    assert validate_pin("1")==False
    assert validate_pin("12")==False
    assert validate_pin("123")==False
    assert validate_pin("12345")==False
    assert validate_pin("1234567")==False
    assert validate_pin("-1234")==False
    assert validate_pin("1.234")==False
    assert validate_pin("-1.234")==False 
    assert validate_pin("00000000")==False 

    ## TEST CASES 2
    ## Should return False for pins which contain characters other than digits
    assert validate_pin("a234")==False
    assert validate_pin(".234")==False
    assert validate_pin("-123")==False
    assert validate_pin("-1.234")==False 

    ## TEST CASES 3
    ## Should return True for valid pins
    assert validate_pin("1234")==True
    assert validate_pin("0000")==True
    assert validate_pin("1111")==True
    assert validate_pin("123456")==True
    assert validate_pin("098765")==True
    assert validate_pin("000000")==True
    assert validate_pin("123456")==True
    assert validate_pin("090909")==True
