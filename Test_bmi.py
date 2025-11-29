import bmi as mybmi

def test_bmi_normal_weight(): 
    # Arrange
    height = 1.73
    weight = 57
     #Act
    result = mybmi.calculate_bmi(height,weight)
    #Assert
    assert result == 0

def test_bmi_over_weight():
    height = 1.73
    weight = 78
    result = mybmi.calculate_bmi(height,weight)
    assert result == 1

def test_bmi_under_weight():
    height = 1.73
    weight = 50
    result = mybmi.calculate_bmi(height,weight)
    assert result == -1

