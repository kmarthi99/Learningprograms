def frgjmp(X,Y,D):
    #coun=0
    TD = Y - X
    if TD % D == 0:
        jump = TD // D
    else:
        jump = (TD // D) + 1
    return jump

x=10
y=105
z=30
print(frgjmp(x,y,z))