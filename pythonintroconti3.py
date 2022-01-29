# Simple function
def name():
    print("Jahanzeb Naeem")
name()
print('-------------------')
# Parametrised function
def add(n1,n2):
    print(n1+n2)
add(4,5)
print('-------------------')
# Returning value function
def cal(n3,n4):
    return n3+n4
print(cal(3,4))
print('-------------------')
# Default values function
def add(n1,n2=4):
    print(n1+n2)
add(3,7)
print('-------------------')
cars = ['Honda', 'MG', 'Toyota']
print(cars[1])
cars.insert(1, 'Suzuki')
print(cars)
# cars.remove('Suzuki')
# print(cars)
cars.sort()
print(cars)
