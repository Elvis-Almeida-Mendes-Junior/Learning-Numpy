
# Aprendendo Numpy

Vamos Aprender Numpy Uma Das Bibliotecas mais ultilizadas Em python


## Autores

- [@elvisjunior](https://www.github.com/Elvis-Almeida-Mendes-Junior)



## Instalação

Instale Numpy com pip

```bash
  pip install numpy
```
    
## Uso

```python
import numpy as np;

a = np.array([1,2,3])
#retorna uma lista de uma dimensão
```

## Se Você Quiser Uma Matrix

```python
import numpy as np;

a = np.array([(1,2,3)],(2,3,4),(5,6,7))
#retorna uma matrix com as linhas sendo divididas pelas virgulas
```
## Matrix Apenas de Zeros

```python
import numpy as np;

c = np.zeros((3,3))
#retorna uma matrix apenas com numeros zeros
#tendo 3 linhas e 3 colunas(esse numero pode ser alterado)
```

## Matrix Apenas de Uns

```python
import numpy as np;

c = np.ones((3,3))
#retorna uma matrix apenas com numeros 1
#tendo 3 linhas e 3 colunas(esse numero pode ser alterado)
```
## Matrix Olho

```python
import numpy as np;

c = np.eye((3))
#recebe apenas um parametro e sempre vai ser quadrada
#tendo as diagonais composta por 1 e todo o resto por 0
```
## Maior e Menor Valor

```python
maxnp = np.max(b) # == 12
minnp = np.min(b) # == 1

print(minnp)
```
## Somandos os elementos da matrix

```python
sumnp = np.sum(b)
print(sumnp) # == 78
```
## Media

```python
meannp = np.mean(b)
print(meannp) # == 6.5
```
## Desvio Padrão

```python
stdnp = np.std(b)
print(stdnp)
```


