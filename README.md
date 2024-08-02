# Analisis Penolakan Pelanggan

## Latar Belakang

Dalam industri perbankan, memahami profil dan perilaku pelanggan merupakan kunci untuk mengelola risiko kredit dan mengembangkan strategi pemasaran yang efektif. Perusahaan kartu kredit sering kali menghadapi tantangan dalam menyetujui aplikasi kartu kredit dari pelanggan. Tingginya tingkat penolakan dapat menyebabkan ketidakpuasan pelanggan dan kehilangan potensi pendapatan. Untuk mengatasi masalah ini, project ini dibuat dengan tujuan untuk mengurangi jumlah aplikasi yang ditolak dan meningkatkan persetujuan kartu kredit.

## Objektivitas Data

Objektivitas utama dari proyek ini adalah menganalisa faktor-faktor yang mempengaruhi keputusan disetujuinya pengajuan kartu kredit. Dengan mengidentifikasi pola atau kriteria yang sering menyebabkan penolakan, kita dapat mengembangkan wawasan dan strategi untuk meningkatkan proses persetujuan.

## Dataset

kaggle = ('https://www.kaggle.com/datasets/rohitudageri/credit-card-details/data')

## File-File dalam Proyek

- `cleaned_credit_card.csv`: Dataset yang telah dibersihkan untuk analisis
- `model_of_credit_card.py`: Skrip untuk model prediksi kartu kredit
- `model_pca.pkl`: Model PCA untuk pengurangan dimensi
- `scaler_cluster.pkl`: Scaler untuk clustering
- `eda.py`: Skrip untuk analisis data eksploratif (EDA)
- `encoder.pkl`: Encoder untuk variabel kategorikal
- `model.pkl`: Model prediksi utama
- `prediction.py`: Skrip untuk membuat prediksi
- `scaler.pkl`: Scaler untuk pemrosesan data
- `adaboost_logreg_best.pkl`: Model Adaboost dengan Logistic Regression terbaik

## Kesimpulan

Melalui analisis ini, kami bertujuan untuk mendapatkan pemahaman yang lebih dalam tentang faktor-faktor kunci yang mempengaruhi persetujuan aplikasi kartu kredit. Dengan memanfaatkan pengetahuan ini, kami dapat mengoptimalkan proses persetujuan, mengurangi tingkat penolakan, dan meningkatkan kepuasan pelanggan. Pada akhirnya, ini akan membantu perusahaan kartu kredit untuk meningkatkan pendapatan dan mengelola risiko kredit dengan lebih baik

## Penulis

- Clara H.
- Dendi A.
- Thariq A.

### Kesimpulan

Analisis penolakan pelanggan untuk aplikasi kartu kredit telah mengungkapkan beberapa wawasan penting:

1. **Tingkat Pendapatan**: Pelamar dengan tingkat pendapatan yang lebih tinggi memiliki probabilitas persetujuan yang lebih tinggi. Hal ini kemungkinan karena kemampuan mereka yang dianggap lebih baik dalam mengelola kredit.
2. **Riwayat Kredit**: Riwayat kredit yang bersih tanpa default atau keterlambatan pembayaran secara signifikan meningkatkan peluang persetujuan.
3. **Status Pekerjaan**: Karyawan penuh waktu lebih mungkin disetujui dibandingkan dengan karyawan paruh waktu atau pelamar yang tidak bekerja.
4. **Rasio Utang terhadap Pendapatan**: Rasio utang terhadap pendapatan yang lebih rendah dikaitkan dengan tingkat persetujuan yang lebih tinggi, menunjukkan pentingnya stabilitas keuangan.
5. **Usia**: Pelamar berusia menengah cenderung memiliki tingkat persetujuan yang lebih tinggi dibandingkan dengan pelamar yang lebih muda, kemungkinan karena stabilitas keuangan yang lebih besar dan riwayat kredit yang lebih lama.

Dengan berfokus pada faktor-faktor ini, perusahaan kartu kredit dapat memperbaiki kriteria persetujuannya, menyesuaikan strategi pemasarannya, dan menawarkan produk keuangan yang ditargetkan untuk segmen pelanggan yang berbeda. Pendekatan ini tidak hanya akan mengurangi tingkat penolakan tetapi juga meningkatkan kepuasan dan loyalitas pelanggan