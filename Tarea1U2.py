import random

def centros_al_cuadrado(semilla, n_digitos, cantidad):
    resultados = []
    for _ in range(cantidad):
     
        cuadrado = str(semilla ** 2).zfill(2 * n_digitos) 
        
    
        inicio = (len(cuadrado) - n_digitos) // 2
        semilla = int(cuadrado[inicio:inicio + n_digitos])
       
        resultado = semilla / (10 ** n_digitos)
        resultados.append(resultado)
    
    return resultados

def medios_cuadrados(semilla, n_digitos, cantidad):
    resultados = []
    for _ in range(cantidad):
       
        cuadrado = str(semilla ** 2).zfill(2 * n_digitos)  
        

        inicio = (len(cuadrado) - n_digitos) // 2
        semilla = int(cuadrado[inicio:inicio + n_digitos])
        
  
        resultado = semilla / (10 ** n_digitos)
        resultados.append(resultado)
    
    return resultados

# Parámetros
semilla_cuadrados = random.randint(1000, 9999)  # Semilla de 4 dígitos
n_digitos = 4  # Número de dígitos a tomar en los métodos
cantidad = 100  # Cantidad de números aleatorios a generar

# Generar números aleatorios por el método de centros al cuadrado
resultados_centros = centros_al_cuadrado(semilla_cuadrados, n_digitos, cantidad)
print("Números aleatorios por el método de Centros al Cuadrado:")
print(resultados_centros)

# Generar números aleatorios por el método de medios cuadrados
resultados_medios = medios_cuadrados(semilla_cuadrados, n_digitos, cantidad)
print("\nNúmeros aleatorios por el método de Medios Cuadrados:")
print(resultados_medios)
