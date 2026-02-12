# EJERCICIO 1 - Create entry file
app.py

# EJERCICIO 2 - Import NumPy
import numpy as np

# EJERCICIO 3 - NumPy version
import numpy as np
print(np.__version__)
print(np.show_config())

# EJERCICIO 4 - Your first vector
import numpy as np
vector = np.zeros(10)
print(vector)

# EJERCICIO 5 - Array memory size
import numpy as np
vector = np.zeros(10)
print(vector.size)
memory_size = vector.size * vector.itemsize
print(memory_size)

# EJERCICIO 6 - NumPy documentation
import numpy as np
print(np.info(np.add))

# EJERCICIO 7 - Change vector values
import numpy as np
vector_nulo = np.zeros(10)
vector_nulo[4] = 1
print(vector_nulo)

# EJERCICIO 8 - Vector ranging values
import numpy as np
vector = np.arange(10, 50, dtype=int)
print(vector)

# EJERCICIO 9 - Reverse vector
import numpy as np
vector = np.arange(0, 10, dtype=int)
reverse_vector = vector[::-1]
print(reverse_vector)

# EJERCICIO 10 - Matrix with ranging values
import numpy as np
vector = np.arange(0, 9, dtype=int)
matrix = vector.reshape(3, 3)
print(matrix)

# EJERCICIO 11 - Find indices of non-zero elements
import numpy as np
mi_lista = [1, 2, 0, 0, 4, 0]
x = np.array(mi_lista)
indices = np.nonzero(x)
print(indices)

# EJERCICIO 12 - Identity matrix
import numpy as np
matrix = np.eye(3)
print(matrix)

# EJERCICIO 13 - Random values array
import numpy as np
arr = np.random.random(3)
print(arr)

# EJERCICIO 14 - Minimum and maximum
import numpy as np
arr = np.random.random(10)
print(arr)
max_value = np.max(arr)
print(max_value)

# EJERCICIO 15 - Mean value
import numpy as np
arr = np.random.random(10)
mean_value = np.mean(arr)
print(mean_value)

# EJERCICIO 16 - Array border
import numpy as np
matrix = np.ones((5, 5))
matrix[1:-1, 1:-1] = 0
print(matrix)

# EJERCICIO 17 - Add border to array
import numpy as np
matrix = np.ones((3, 3))
matrix_with_border = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
print(matrix_with_border)

# EJERCICIO 18 - Result of expressions
import numpy as np
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

# EJERCICIO 19 - Diagonal
import numpy as np
vector = np.arange(0, 9, dtype=int)
matrix = vector.reshape(3, 3)
diagonal = np.diag(matrix)
print(diagonal)

# EJERCICIO 20 - Checkboard pattern
import numpy as np
board = np.zeros((8, 8))
board[::2, 1::2] = 1
board[1::2, ::2] = 1
print(board)
