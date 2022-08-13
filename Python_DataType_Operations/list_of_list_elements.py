x = 2
y = 2
z = 3

l = [ [i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
print(l)


# in case multiple times input needs to be called

x, y, z, n = (int(input()) for _ in range(4))