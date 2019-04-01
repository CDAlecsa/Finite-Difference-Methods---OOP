#%%%%
'''
                                Python Packages 
'''


from scipy.optimize import fsolve
from matplotlib.pyplot import figure, plot, grid, xlabel, ylabel, title, show, ticklabel_format, legend
from numpy import exp, negative

from MeshClass import Mesh


#%%%%
'''
                                The function from the RHS 
'''

f = lambda T,X : negative(X)


#%%%%
'''
                                Numerical and exact solutions
'''

def FNewton(x,hh,tt,A):                            
    return x - A - hh * f(tt,x)    


MeshGrid_BackEuler = Mesh()
MeshGrid_BackEuler = Mesh._CreateMeshInput()

ExactSol = lambda C, T : C * exp(negative(T)) 

N = MeshGrid_BackEuler.returnTimeLength()
t = MeshGrid_BackEuler.returnTimeMesh()
h = MeshGrid_BackEuler.returnTimeStepSize()
x0 = MeshGrid_BackEuler.returnInitialValue()
x = [x0]


for n in range(0,N-1):
    guess = x[n]
    args = ( h,t[n+1],x[n] )
    x.append(fsolve(FNewton, guess, args, xtol = 1e-10))



#%%%%
'''
                                Plots 
'''

figure(1)     
plot(t,abs(x-ExactSol(x0,t)),'bo-')
xlabel('Time',fontweight = 'bold')
ylabel('Error',fontweight = 'bold')
grid()
title('Absolute error : 1st order IVP')
ticklabel_format(axis='y', style='sci', scilimits=(-2,2))


figure(2)     
plot(t,x,'bo-')
plot(t,ExactSol(x0,t),'ro-')
xlabel('Time',fontweight = 'bold')
ylabel('Num. and Exact Sol.',fontweight = 'bold')
grid()
title('Solutions : 1st order IVP')
ticklabel_format(axis='y', style='sci', scilimits=(-2,2))  
legend(['Numerical sol.', 'Exact sol.'])
show()



