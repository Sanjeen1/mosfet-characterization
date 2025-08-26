import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("iv_data.txt", comments=['*'])

Vgs_data = data[:, 0]   # First column = Vgs
Id_data  = data[:, 1]   # Second column = Id

print("Vgs_data =", Vgs_data.tolist()[:10], "...")
print("Id_data  =", Id_data.tolist()[:10], "...")


def plot_on_logarithmic_scale(Vgs, Id):
    # Keep only positive Id values
    mask = Id > 0
    Vgs = Vgs[mask]
    Id = Id[mask]

    plt.figure(figsize=(6,4))
    plt.semilogy(Vgs, Id, 'bo-', label="Id vs Vgs (semilog)")
    plt.xlabel("Vgs (V)")
    plt.ylabel("Id (A, log scale)")
    plt.title("Id-Vgs (semilog)")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()

plot_on_logarithmic_scale(Vgs_data, Id_data)
