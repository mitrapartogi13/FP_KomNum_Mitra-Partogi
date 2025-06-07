def f(x):
    return 3 * x**5 - 8 * x**4

def riemann_integral(a, b, n):
    delta_x = (b - a) / n
    total = 0
    for i in range(n):
        x_riemann = a + i * delta_x 
        total += f(x_riemann)
    luas = total * delta_x
    return round(luas, 2)

def nilai_sebenarnya(a, b):
    def F(x):
        return 0.5 * x**6 - (8/5) * x**5
    hasil = F(b) - F(a)
    return round(hasil, 2)

def riemann_error(a, b, n):
    approx = riemann_integral(a, b, n)
    val_sebenarnya = nilai_sebenarnya(a, b)
    error = abs((val_sebenarnya - approx)/val_sebenarnya) * 100
    return round(approx, 2), round(val_sebenarnya, 2), round(error, 2)

# param
a = 4 # batas bawah
b = 16 # batas atas
n = 4 # jumlah partisi

# hitung
approx, val_sebenarnya, error = riemann_error(a, b, n)

# output ketelitian 2 angka di belakang koma
print(f"Luas dengan Riemann (n=4): {approx:.2f}")
print(f"Luas sebenarnya: {val_sebenarnya:.2f}")
print(f"Error true: {error:.2f}")
