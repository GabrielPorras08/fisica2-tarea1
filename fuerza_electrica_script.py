import math
import matplotlib.pyplot as plt

# Constante de Coulomb
K = 9 * (10**9)

def calcular_fuerza(q1, q2, x2, y2):
    dx = x2
    dy = y2
    r = math.sqrt(dx**2 + dy**2)
    if r == 0:
        raise ValueError("Las cargas no pueden estar en la misma posición.")

    fuerza_magnitud = K * q1 * q2 / r**2
    fx = fuerza_magnitud * dx / r
    fy = fuerza_magnitud * dy / r
    return fx, fy

def graficar_fuerza(q1, q2, x2, y2, fx, fy):
    plt.figure(figsize=(6,6))
    plt.quiver(x2, y2, fx, fy, angles='xy', scale_units='xy', scale=1, color='blue', label='Fuerza sobre Q2')
    plt.scatter([0, x2], [0, y2], color=['red', 'green'], label='Q1 (origen) y Q2')
    plt.text(0, 0, 'Q1', fontsize=12, ha='right')
    plt.text(x2, y2, 'Q2', fontsize=12, ha='left')
    plt.xlim(min(0, x2) - 5, max(0, x2) + 5)
    plt.ylim(min(0, y2) - 5, max(0, y2) + 5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Fuerza eléctrica ejercida por Q1 sobre Q2')
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    try:
        q1 = float(input("Ingrese la carga Q1 en nanocoulombs (nC): ")) * 1e-9
        q2 = float(input("Ingrese la carga Q2 en nanocoulombs (nC): ")) * 1e-9
        x2 = float(input("Ingrese la coordenada x de Q2: "))
        y2 = float(input("Ingrese la coordenada y de Q2: "))

        fx, fy = calcular_fuerza(q1, q2, x2, y2)
        print(f"\nVector de fuerza sobre Q2:")
        print(f"Fx = {fx:.4e} N")
        print(f"Fy = {fy:.4e} N")

        graficar_fuerza(q1, q2, x2, y2, fx, fy)

    except Exception as e:
        print(f"Error: {e}")
