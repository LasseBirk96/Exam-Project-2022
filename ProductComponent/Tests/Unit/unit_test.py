from LogicLayer.Security.InputSanitizer import InputSanitizer


# CLEAN TEXT
def test_clean_text():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_text("Orange Juice")
    # Assert
    assert value == True


def test_clean_text_false_positive():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_text("***234DGR")
    # Assert
    assert value == False


# CLEAN NUMBER
def test_clean_number():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_number("123")
    # Assert
    assert value == True


def test_clean_number_false_positive():
    # Arrange
    sanitizer = InputSanitizer()
    # Act
    value = sanitizer.clean_number("11111123")
    # Assert
    assert value == False

  

# CLEAN INPUT
def test_clean_input():
  # Arrange
  sanitizer = InputSanitizer()
  data = {"product_name":"Pizza med dress", "description":"lækker pizza", "price":"123"}
  # Act
  value = sanitizer.clean_input(data)
  # Assert
  assert value == True


def test_clean_input_false_positive():
  # Arrange
  sanitizer = InputSanitizer()
  data = {"product_name":"Pizza med dr!!!11111!ess", "description":"lækker pizza", "price":"121113"}
  # Act
  value = sanitizer.clean_input(data)
  # Assert
  assert value == False