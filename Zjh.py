import numpy as np
def cin_matrix():
    s=[]
    while(1):
        line=input()
        if(line=='\n'or not line): break
        s.append(list(map(int, line.split(' '))))
    #s=np.array(s)
    return s
a=cin_matrix()
b=cin_matrix()
print('max position for the first matrix:',end=' ')
for i in np.argmax(a,axis=1):
    print(i+1,end=' ')
print("")
print('max position for the second matrix:',end=' ')
for i in np.argmax(b,axis=1):
    print(i+1,end=' ')
print("")
print("Multiplication result:")
for i in list(np.matmul(a,b)):
    for j in i: print(j,end=' ')
    print()
