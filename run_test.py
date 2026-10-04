from run import isTriangle,ThirdAngle

def test_isTriangle():
    assert isTriangle(1,2,3) == False
    assert isTriangle(3,4,5) == True
    assert isTriangle(1.9,2.2,3) == True

def test_ThirdAngle():
    assert ThirdAngle(60,60) == 60
    assert ThirdAngle(90,45) == 45