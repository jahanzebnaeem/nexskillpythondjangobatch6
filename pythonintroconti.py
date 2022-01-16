xyz = [1,2,3,5,7,9,11]
print(xyz)
print(xyz[2])
print(xyz[1:4])
print(xyz[-2:])
print(xyz[:])
xyz.append(13)
xyz.append(6**4)
print(xyz)
print(len(xyz))
x = int(input("Please enter a number: "))
if x<0:
    x=0
    print("Neg val changed")
elif x==0:
    print("zero")
else:
    print("More than zero")
for p in xyz:
    print(p)
cars = {'honda1':['city', 'civic'],'honda':'civic','toyota':'gli','mg':'hs'}
for car, model in cars.items():
    print(model)
