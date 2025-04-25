import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Définition des fonctions
x = np.linspace(0, 1000, 500)
F2480 = 2480 + (332 * x) / (332 + x)
F2470 = 2470 + (332 * x) / (332 + x)
F2490 = 2490 + (332 * x) / (332 + x)

# Création du graphique
fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot(x, F2480, label='F2480')
line2, = ax.plot(x, F2470, label='F2470')
line3, = ax.plot(x, F2490, label='F2490')

# Ajout des titres et légendes
ax.set_xlabel('x')
ax.set_ylabel('Valeurs des fonctions')
ax.set_title('Graphique des fonctions F2480, F2470, F2490')
ax.legend()

# Ajout du texte pour afficher les valeurs des fonctions
text = ax.text(0.7, 0.9, '', transform=ax.transAxes)

# Fonction pour mettre à jour les valeurs des fonctions en fonction de la position du curseur
def update_values(event):
    if event.inaxes == ax:
        x_val = event.xdata
        # Trouver l'index le plus proche de la valeur de x
        index = np.argmin(np.abs(x - x_val))
        
        # Mettre à jour le texte avec les valeurs des fonctions
        text.set_text(
            f'x = {x_val:.2f}\n'
            f'F2480 = {F2480[index]:.2f}\n'
            f'F2470 = {F2470[index]:.2f}\n'
            f'F2490 = {F2490[index]:.2f}'
        )
        fig.canvas.draw_idle()

# Connexion de la fonction de mise à jour à l'événement de mouvement de la souris
fig.canvas.mpl_connect('motion_notify_event', update_values)

# Ajout d'un curseur
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='red', linewidth=1)

# Affiche le graphique
plt.show()
