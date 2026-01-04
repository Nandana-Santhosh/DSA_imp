import math
n=(int(input("enter the value of h")))
t=(int(input("enter the angle")))
new={30,45,60}
if n<=100 and t in new:
    if t==30:
        x=(n*math.tan(0.166*math.pi))
    if t==45:
        x=(n*math.tan(0.25*math.pi))
    if t==60:
        x=(n*math.tan(0.333*math.pi))
        
    area=math.ceil(math.pi*x*x)
    print(area)
else:
    print("Invalid input")

