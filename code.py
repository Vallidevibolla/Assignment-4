import numpy as np
import matplotlib.pyplot as plt



#if using termux
import subprocess
import shlex
#end if



#Inputs
n = np.array([1,-2]) 
c = 4
e1 = np.array([0,2]) 
e2 = np.array([4,0]) 
e3 = np.array([2,0]) 
e4 = np.array([0,1]) 
e5 = np.array([1,1]) 

A = c*e1/(n@e1)
B = c*e2/(n@e2)
C = c*e3/(n@e3)
D = c*e4/(n@e4)
E = c*e5/(n@e5)


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
