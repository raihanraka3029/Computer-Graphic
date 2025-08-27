import matplotlib.pyplot as plt
import numpy as np

rowmax = 1000
colmax = 1000

Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)

# Titik tengah lingkaran
center_x, center_y = rowmax // 2, colmax // 2

# Radius lingkaran
radius = 200

# Warna
yellow = [255, 255, 0]
black = [0, 0, 0]

# Membuat setengah lingkaran kuning di kiri dan setengah lingkaran hitam di kanan
for i in range(rowmax + 1):
    for j in range(colmax + 1):
        # Menghitung jarak dari titik (i, j) ke pusat lingkaran
        distance = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)

        # Jika jarak kurang dari radius dan di sebelah kiri
        if distance <= radius and j <= center_y:
            Gambar[i, j] = yellow
        # Jika jarak kurang dari radius dan di sebelah kanan
        elif distance <= radius and j > center_y:
            Gambar[i, j] = black

print(type(Gambar))

plt.figure()
plt.imshow(Gambar)
plt.show()