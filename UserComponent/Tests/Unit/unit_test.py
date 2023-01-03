from LogicLayer.Security.InputSanitizer import InputSanitizer


#CLEAN NAME
def test_clean_name():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_name("Albus")
    # Assert
    assert value == True

def test_clean_name_false_positive():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_name("Albus>><<<!!!!````")
    # Assert
    assert value == False


#CLEAN EMAIL
def test_clean_email():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_email("test@gmail.com")
    # Assert
    assert value == True


def test_clean_email_false_postive():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_email("test@gmai>>>l.com")
    # Assert
    assert value == False


#CLEAN AGE
def test_clean_age():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_age("16")
    # Assert
    assert value == True


def test_clean_age_false_postive():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_age("1611")
    # Assert
    assert value == False


#CLEAN PHONENUMBER
def test_clean_phonenumber():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_phonenumber("12345678")
    # Assert
    assert value == True


def test_clean_phonenumber_false_positive():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_phonenumber("1wefwef")
    # Assert
    assert value == False



#CLEAN INPUT
def test_clean_input():
    # Arrange
    sanitizer = InputSanitizer()
    data = {"email":"test@gmail.com", "age":"15", "first_name":"test", "last_name":"test", "phone_number":"12345678"}
    # Act
    value = sanitizer.clean_input(data)
    # Assert
    assert value == True


def test_clean_input_false_positive():
    # Arrange
    sanitizer = InputSanitizer()
    data = {"email":"test>>>>>@gmail.com", "age":"15111", "first_name":"tes****t", "last_name":"test", "phone_number":"12345678"}
    # Act
    value = sanitizer.clean_input(data)
    # Assert
    assert value == False