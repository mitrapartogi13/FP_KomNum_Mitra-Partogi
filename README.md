# FINAL PROJECT KOMPUTASI NUMERIK (A) 2025 / Kelompok A13
Program Python Final Project Komputasi Numerik

Anggota Kelompok A13 :
|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241017 | Mitra Partogi |
| 5025241026 | Very Ardiansyah |
| 5025241054 | Andie Azril Alfrianto |
| 5025241066 | Naufal Daffa Alfa Zain |
| 5025241067 | Bagus Cahya Saputra |

<h4>Penulis README = Mitra Partogi</h4>
Tujuan : Pemenuhan Tugas Final Project Komputasi Numerik. <br>
Soal : 
<div align="left">
  <img src="https://github.com/user-attachments/assets/acbaa9b3-92c0-42bc-b9fd-0bec5c7b1d2d" width="600" />
</div>

Kode :
```py
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

```

Penjelasan kode :
- ```py
  def f(x):
    return 3 * x**5 - 8 * x**4
  ```
  Fungsi f(x) asli seperti yang ada di soal.
- ```py
  def riemann_integral(a, b, n):
    delta_x = (b - a) / n
    total = 0
    for i in range(n):
        x_riemann = a + i * delta_x 
        total += f(x_riemann)
    luas = total * delta_x
    return round(luas, 2)
  ```
  Fungsi ini untuk menjalankan fungsi integral Riemann
  - a untuk batas bawah, b untuk batas atas, n untuk jumlah partisi
  - delta_x = (b-a)/n
  - x_riemann: titik awal setiap partisi
  - total: menjumlahkan tinggi tiap * lebar
  - Akhirnya dikalikan dengan delta_x untuk mendapatkan estimasi luas
  - return round(luas, 2) membulatkan hasil ke 2 angka di belakang koma
- ```py
  def nilai_sebenarnya(a, b):
    def F(x):
        return 0.5 * x**6 - (8/5) * x**5
    hasil = F(b) - F(a)
    return round(hasil, 2)

  ```
  Fungsi ini untuk kalkulasi nilai luas sebenarnya. Luas sebenarnya juga dikenal sebagai Luas analitik.
- ```py
  def riemann_error(a, b, n):
    approx = riemann_integral(a, b, n)
    val_sebenarnya = nilai_sebenarnya(a, b)
    error = abs((val_sebenarnya - approx)/val_sebenarnya) * 100
    return round(approx, 2), round(val_sebenarnya, 2), round(error, 2)

  ```
  Fungsi ini sederhananya adalah menghitung Error True dari hasil kalkulasi.
  Et = abs((nilai_sebenarnya-nilai_hasil)/nilai_sebenarnya)
  di fungsi ini terpanggil fungsi integral Riemann dan integral analitik supaya bisa dihitung Et nya
- ```py
  # param
  a = 4 # batas bawah
  b = 16 # batas atas
  n = 4 # jumlah partisi

  ```
  Kumpulan parameternya.
- ```py
  approx, val_sebenarnya, error = riemann_error(a, b, n)
  ```
  - Memanggil fungsi riemann_error() dengan parameter yang sudah ditentukan.
  - Menyimpan hasil luas aproksimasi (approx), nilai eksak (val_sebenarnya), dan error-nya (error).
- ```py
  print(f"Luas dengan Riemann (n=4): {approx:.2f}")
  print(f"Luas sebenarnya: {val_sebenarnya:.2f}")
  print(f"Error true: {error:.2f}")
  ```
  Mencetak hasil akhir dengan format dua angka di belakang koma (:.2f)

<h2>OUTPUT PROGRAM</h2>

```py
Luas dengan Riemann (n=4): 3412884.00
Luas sebenarnya: 6710476.80
Error true: 49.14
```
<div align="left">
  <img src="https://github.com/user-attachments/assets/1a430c20-c6c2-416e-855e-48f67fda3ccf" width="300" height="500" />
</div>
Sekian dan Terima Kasih!
   

