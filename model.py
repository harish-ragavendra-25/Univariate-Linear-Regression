import numpy as np
import matplotlib.pyplot as plt
X=np.array(eval(input()))
Y=np.array(eval(input()))
Xmean = np.mean(X)
Ymean = np.mean(Y)
num,den = 0,0
for i in range (len(X)):
    num += (X[i]-Xmean)*(Y[i]-Ymean)
    den += (X[i]-Xmean)**2
m = num/den
c = Ymean-m*Xmean
print (m,c)
Y_pred=m*X+c
print(Y_pred)
plt.scatter(X,Y)
plt.plot(X,Y_pred, color="orange")
plt.show()