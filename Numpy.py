import numpy as np;

a = np.array([1,2,3]);#Cria uma matriz de apenas uma dimensão

b = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)]);#cria uma matriz;

c = np.zeros((3,3));

d = np.ones((3,3));

e = np.eye(3);

maxnp = np.max(b)
minnp = np.min(b)

sumnp = np.sum(b)

meannp = np.mean(b)

stdnp = np.std(b)
print(stdnp)