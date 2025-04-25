import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Définition des fonctions
x = np.linspace(0, 1000, 500)
F2480 = 2480 + (332 * x) / (332 + x)
F2470 = 2470 + (332 * x) / (332 + x)
F2490 = 2490 + (332 * x) / (332 + x)

fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot(x, F2480, label='F2480')
line2, = ax.plot(x, F2470, label='F2470')
line3, = ax.plot(x, F2490, label='F2490')

ax.set_xlabel('x')
ax.set_ylabel('Valeurs des fonctions')
ax.set_title('Graphique des fonctions F2480, F2470, F2490')
ax.legend()

cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='red', linewidth=1)

# Création de l'annotation (texte dynamique)
annotation = ax.annotate(
    "",
    xy=(0,0), 
    xytext=(20,20), 
    textcoords="offset points",
    bbox=dict(boxstyle="round", fc="w"),
    arrowprops=dict(arrowstyle="->")
)
annotation.set_visible(False)

def on_mouse_move(event):
    if event.inaxes == ax:
        # Trouve l'indice le plus proche de la position x de la souris
        x_mouse = event.xdata
        idx = np.abs(x - x_mouse).argmin()
        x_val = x[idx]
        y1 = F2480[idx]
        y2 = F2470[idx]
        y3 = F2490[idx]
        # Met à jour l'annotation
        annotation.xy = (x_val, y1)
        text = f"x = {x_val:.2f}\nF2480 = {y1:.2f}\nF2470 = {y2:.2f}\nF2490 = {y3:.2f}"
        annotation.set_text(text)
        annotation.set_visible(True)
        fig.canvas.draw_idle()
    else:
        annotation.set_visible(False)
        fig.canvas.draw_idle()

# Connexion de l'événement
fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)

plt.show()
