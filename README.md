# Face Recognition REST API

Face Recognition REST API adalah sebuah aplikasi berbasis Flask yang menggunakan DeepFace untuk melakukan deteksi dan pengenalan wajah.

## 🚀 Fitur

- Deteksi wajah
- Pengenalan wajah berdasarkan database gambar
- API berbasis REST untuk kemudahan integrasi

## 🛠 Teknologi yang Digunakan

- Python
- Flask
- DeepFace
- OpenCV

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/sukundev/Face-Recognition-API.git
```

### 2. Masuk ke Direktori Project

```bash
cd Face-Recognition-API
```

### 3. Buat Virtual Environment (Opsional)

Sangat disarankan untuk menjalankan proyek ini dalam virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
```

### 4. Install Dependensi

```bash
pip install -r requirements.txt
```

### 5. Jalankan Aplikasi

```bash
python app.py  # Atau
flask run
```

## 🔥 Penggunaan API

### 1. Endpoint: `/register-face`

**Method:** `POST`

- **Deskripsi:** Menyimpan Wajah
- **Parameter:**
  - `image` (file) - Gambar yang akan diproses
- **Contoh Request:**

```bash
curl -X POST -F "image=@/path/to/image.jpg" http://127.0.0.1:5000/register-face
```

<!-- - **Contoh Response:**
```json
{
  "status": "success",
  "faces": [
    {
      "x": 100,
      "y": 50,
      "width": 150,
      "height": 150
    }
  ]
}
``` -->

### 2. Endpoint: `/validate-face`

**Method:** `POST`

- **Deskripsi:** Memverifikasi apakah wajah ter-registrasi
- **Parameter:**
  - `image1` (file) - Gambar yang akan diproses
- **Contoh Request:**

```bash
curl -X POST -F "image1=@/path/to/image1.jpg" http://127.0.0.1:5000/validate-face
```

<!-- - **Contoh Response:**

```json
{
  "status": "success",
  "verified": true,
  "confidence": 0.89
}
``` -->

## 📜 Lisensi

Proyek ini menggunakan lisensi MIT. Silakan cek file `LICENSE` untuk informasi lebih lanjut.

---

Dikembangkan oleh [sukundev](https://github.com/sukundev) 💻🚀
