def add(x, y):
    t = x+y   # Logic
    return t


def test_add():
    for i in range(-50, 50):
        for j in range (-50, 50):
            assert add(i, j) == i+j

def abcd():
    while True:
        for i in x:
            if i.on():
                return i

def get_car():
    while True:
        for car in pool:
            if not car.in_use():
                return car
        print ("Cars not available. Sleeping")
        time.sleep(5)
    
