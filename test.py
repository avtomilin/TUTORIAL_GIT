from payment import calculate as cal

def test(a,b):
    c = cal(a,b)

    test_c = a+b

    assert c == test_c


test(100,200)
test(122,150)
test(140,150)