Muy bueno, explica los modelos de concurrencia en Python, y como se implementan en los servidores web.
Explica el bloqueo GIL y por qué es ineficiente para CPU-bound tasks.

https://medium.com/coccoc-engineering-blog/webservers-concurency-models-in-python-529af709b7a


Aquí explica el GIL:
https://realpython.com/python-gil/





Grupo "Avanzado"

- Ejercicio: Pedir la función de Fibonacci. Definición: F(n) = F(n-1) + F(n-2), con F(0) = 0 y F(1) = 1.
- Explicar que se puede memoizar la función para mejorar su rendimiento. Probar n=30, n=35, n=40.
- Ejercicio: Implementar la función de Fibonacci con memoización
- Comentar brevemente programación funcional. Memoizar con lru_cache.

- Pero vamos a usarla para hacer programación en paralelo en python
  -



Más tipos de paralelismo:
To run each call to the fibonacci function in parallel, you can use Python's concurrent.futures module. This module provides a high-level interface for asynchronously executing callables using threads or processes. For CPU-bound tasks like computing Fibonacci numbers, concurrent.futures.ProcessPoolExecutor is usually more appropriate than ThreadPoolExecutor.

