import numpy as np
import matplotlib.pyplot as plt

def buat_titik(radius, y, x, r, g, b, Gambar):
    for i in range(y - radius, y + radius):
        for j in range(x - radius, x + radius):
            if ((i - y) ** 2 + (j - x) ** 2) < radius ** 2:
                Gambar[i, j, 0] = int(r)
                Gambar[i, j, 1] = int(g)
                Gambar[i, j, 2] = int(b)

def buat_garis(x1, y1, x2, y2, radius, r, g, b, Gambar):
    # Calculate the gradient m
    dy = y2 - y1
    dx = x2 - x1
    if dx == 0:
        # Handle case when line is vertical
        for j in range(min(y1, y2), max(y1, y2)):
            buat_titik(radius, j, x1, r, g, b, Gambar)
    elif dy == 0:
        # Handle case when line is horizontal
        for i in range(min(x1, x2), max(x1, x2)):
            buat_titik(radius, y1, i, r, g, b, Gambar)
    else:
        my = dy / dx
        mx = dx / dy
        if abs(my) <= 1:
            for i in range(min(x1, x2), max(x1, x2)):
                j = int(my * (i - x1) + y1)
                buat_titik(radius, j, i, r, g, b, Gambar)
        else:
            for j in range(min(y1, y2), max(y1, y2)):
                i = int((j - y1) / my) + x1
                buat_titik(radius, j, i, r, g, b, Gambar)

# User input
x1, y1 = 300, 400
x2, y2 = 700, 600
pd = 20
lw = 10
dist = 1

# Preparations
hd = int(pd / 2)
hw = int(lw / 2)
col = 1000
row = 1000
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)

# Draw the lines
buat_garis(x1, y1, x2, y1, hw, 0, 0, 255, Gambar)
buat_garis(x1, y1, x1, y2, hw, 0, 0, 255, Gambar)
buat_garis(x1, y2, x2, y2, hw, 0, 0, 255, Gambar)
buat_garis(x2, y1, x2, y2, hw, 0, 0, 255, Gambar)

# Draw the points
buat_titik(12, y1, x1, 255, 255, 255, Gambar)
buat_titik(12, y1, x2, 255, 255, 255, Gambar)
buat_titik(12, y2, x1, 255, 255, 255, Gambar)
buat_titik(12, y2, x2, 255, 255, 255, Gambar)

# Show the plot
plt.imshow(Gambar)
plt.show()
