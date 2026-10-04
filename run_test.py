from run import isTriangle

def test_isTriangle():
    assert isTriangle(1,2,3) == False
    assert isTriangle(3,4,5) == True
    assert isTriangle(1.9,2.2,3) == True