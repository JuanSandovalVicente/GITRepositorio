import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Seno")

# Para mostrar el gráfico en una ventana emergente:
plt.show()

# Para guardar el gráfico en un archivo:
plt.savefig("grafico_seno.png")  # Guarda como PNG
plt.savefig("grafico_seno.pdf")  # Guarda como PDF