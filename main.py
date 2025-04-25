import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Définition de l'axe des x et calcul des fonctions
x = np.linspace(0, 1000, 500)
F2480 = 2480 + (332 * x) / (332 + x)
F2470 = 2470 + (332 * x) / (332 + x)
F2490 = 2490 + (332 * x) / (332 + x)

# Création du graphique
fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot(x, F2480, label='F2480')
line2, = ax.plot(x, F2470, label='F2470')
line3, = ax.plot(x, F2490, label='F2490')

ax.set_xlabel('x')
ax.set_ylabel('Valeurs des fonctions')
ax.set_title('Graphique des fonctions F2480, F2470, F2490')
ax.legend()

# Curseur interactif
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='red', linewidth=1)

# Annotation pour afficher les valeurs au vol
annot = ax.annotate(
    "", xy=(0,0), xytext=(15,15), textcoords="offset points",
    bbox=dict(boxstyle="round", fc="w"),
    arrowprops=dict(arrowstyle="->")
)
annot.set_visible(False)

def on_mouse_move(event):
    if not event.inaxes:
        annot.set_visible(False)
        fig.canvas.draw_idle()
        return
    x_val = event.xdata
    y1 = 2480 + (332 * x_val) / (332 + x_val)
    y2 = 2470 + (332 * x_val) / (332 + x_val)
    y3 = 2490 + (332 * x_val) / (332 + x_val)
    text = f"x = {x_val:.2f}\nF2480 = {y1:.2f}\nF2470 = {y2:.2f}\nF2490 = {y3:.2f}"
    annot.xy = (x_val, y1)
    annot.set_text(text)
    annot.set_visible(True)
    fig.canvas.draw_idle()

# Liaison de l'événement de mouvement de souris
fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)

plt.show()
