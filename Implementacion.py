import math

# Funciones auxiliares
def distancia(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def costo_triangulo(a, b, c):
    return distancia(a, b) + distancia(b, c) + distancia(c, a)


# Algoritmo de Programación Dinámica
def triangulacion_minima(puntos):
    n = len(puntos)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for longitud in range(2, n):
        for i in range(n - longitud):
            j = i + longitud
            dp[i][j] = float("inf")

            for k in range(i+1, j):
                costo = dp[i][k] + dp[k][j] + costo_triangulo(puntos[i], puntos[k], puntos[j])
                dp[i][j] = min(dp[i][j], costo)

    return dp[0][n-1]

# Interfaz simple de usuario por consola
def pedir_puntos():
    print("=== TRIANGULACIÓN MÍNIMA DE UN POLÍGONO ===")
    print("Ingrese los puntos del polígono en orden (horario o antihorario).")
    print("Ejemplo de formato: 0 0  (x=0, y=0)\n")

    n = int(input("¿Cuántos vértices tiene el polígono?: "))

    puntos = []
    for i in range(n):
        print(f"--- Punto {i+1} ---")
        x = float(input("Ingrese x: "))
        y = float(input("Ingrese y: "))
        puntos.append((x, y))
        print()

    return puntos

# Programa principal
if __name__ == "__main__":
    puntos = pedir_puntos()
    resultado = triangulacion_minima(puntos)
    print("\n===========================================")
    print("Costo mínimo de la triangulación:", resultado)
    print("===========================================\n")
    