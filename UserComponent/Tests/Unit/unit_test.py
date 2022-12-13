from LogicLayer.Security.InputSanitizer import InputSanitizer


#CLEAN NAME
def test_clean_name():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_name("Albus")
    assert value == True

def test_clean_name_false_positive():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_name("Albus>><<<!!!!````")
    assert value == False


#CLEAN EMAIL
def test_clean_email():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_email("test@gmail.com")
    assert value == True


def test_clean_email_false_postive():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_email("test@gmai>>>l.com")
    assert value == False


#CLEAN AGE
def test_clean_age():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_age("16")
    assert value == True


def test_clean_age_false_postive():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_age("1611")
    assert value == False


#CLEAN PHONENUMBER
def test_clean_phonenumber():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_phonenumber("12345678")
    assert value == True


def test_clean_phonenumber_false_positive():
    sanitizer = InputSanitizer()
    value = sanitizer.clean_phonenumber("1wefwef")
    assert value == False



#CLEAN INPUT
def test_clean_input():
    sanitizer = InputSanitizer()
    data = {"email":"test@gmail.com", "age":"15", "first_name":"test", "last_name":"test", "phone_number":"12345678"}
    value = sanitizer.clean_input(data)
    assert value == True


def test_clean_input_false_positive():
    sanitizer = InputSanitizer()
    data = {"email":"test>>>>>@gmail.com", "age":"15111", "first_name":"tes****t", "last_name":"test", "phone_number":"12345678"}
    value = sanitizer.clean_input(data)
    assert value == False