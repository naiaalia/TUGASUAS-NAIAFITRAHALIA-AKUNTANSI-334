import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data baru
data_baru = pd.read_csv('NaiaII.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data_baru.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data_baru.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data_baru.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data_baru.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data_baru.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data_baru.dtypes)

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(data_baru['umur'], data_baru['pendapatan'], color='green', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Umur')
plt.ylabel('Pendapatan')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(data_baru['pendapatan'].dropna(), bins=20, color='lightgreen', edgecolor='black')
plt.title('Histogram of Pendapatan')
plt.xlabel('Pendapatan')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(data_baru['umur'].dropna())
plt.title('Box Plot of Umur')
plt.ylabel('Umur')

# Membuat data untuk barplot kategori pekerjaan
job_categories = data_baru['pekerjaan'].value_counts().index.tolist()
job_counts = data_baru['pekerjaan'].value_counts().tolist()

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(job_categories, job_counts, color='lightblue')
plt.title('Barplot Kategori Pekerjaan')
plt.xlabel('Kategori Pekerjaan')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
