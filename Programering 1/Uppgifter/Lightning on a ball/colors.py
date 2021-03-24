import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
 
 
X = np.linspace(0, 10, 101)
Y = 10*np.sin(X)
 
cmap = cm.get_cmap('Blues', len(Y))
norm = Normalize(vmin=np.min(Y),vmax=np.max(Y))
 
for i in range(len(X)-1):
    plt.plot(X[i:i+2], Y[i:i+2], color=cmap(norm(Y[i])))
 
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

plt.show()