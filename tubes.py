import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Rekursif berbasis Segitiga Pascal
def kombinasi_recursive_pascal(n, r, memo=None):
    if memo is None:
        memo = {}
    if (n, r) in memo:
        return memo[(n, r)]
    if r == 0 or r == n:
        return 1
    memo[(n, r)] = kombinasi_recursive_pascal(n - 1, r - 1, memo) + kombinasi_recursive_pascal(n - 1, r, memo)
    return memo[(n, r)]

# Iteratif
def kombinasi_iterative(n, r):
    if r > n:
        return 0
    r = min(r, n - r)  # Gunakan simetri kombinasi
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

# Grafik untuk menyimpan data
n_values = []
r_values = []
recursive_times = []
iterative_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Recursive Pascal', marker='o', linestyle='-')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive Pascal vs Iterative (Kombinasi)')
    plt.xlabel('Input (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "r", "Recursive Pascal Time (s)", "Iterative Time (s)"]
    # Gunakan panjang minimum dari semua list untuk menghindari IndexError
    min_len = min(len(n_values), len(r_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([n_values[i], r_values[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
while True:
    try:
        n = int(input("Masukkan nilai n (atau ketik -1 untuk keluar): "))
        if n == -1:
            print("Program selesai. Terima kasih!")
            break
        if n < 0:
            print("Masukkan nilai n yang positif!")
            continue

        r = int(input("Masukkan nilai r: "))
        if r < 0 or r > n:
            print("Masukkan nilai r yang valid (0 <= r <= n)!")
            continue

        n_values.append(n)
        r_values.append(r)

        # Ukur waktu eksekusi algoritma rekursif berbasis Segitiga Pascal
        start_time = time.time()
        kombinasi_recursive_pascal(n, r)
        recursive_times.append(time.time() - start_time)

        # Ukur waktu eksekusi algoritma iteratif
        start_time = time.time()
        kombinasi_iterative(n, r)
        iterative_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan nilai n dan r yang valid!")
