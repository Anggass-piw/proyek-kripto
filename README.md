# Latihan Kriptografi

Kumpulan skrip belajar kriptografi dari Cryptopals, eksperimen RSA, dan demo pustaka `cryptography`.

> **Peringatan keamanan:** kode di `rsa/` dibuat untuk edukasi dan eksperimen serangan, bukan untuk melindungi data nyata. Khususnya, `rsa/rsa_basic.py` menerapkan textbook RSA secara langsung **tanpa padding**; cara ini tidak aman untuk penggunaan produksi. Ukuran kunci kecil dan kondisi khusus pada contoh lain juga disengaja agar konsepnya mudah dipelajari. Jangan gunakan contoh-contoh ini untuk mengenkripsi rahasia atau membuat kunci produksi. `pyca/demo.py` memperlihatkan primitive yang lebih tepat—RSA-OAEP dan AES-GCM—tetapi tetap hanya demo, bukan sistem produksi lengkap.

## Isi

- `cryptopals/`: latihan hex ke Base64, XOR, dan deteksi single-byte XOR.
- `rsa/`: RSA dasar, generator parameter lemah, serta demonstrasi serangan small-n, low-exponent, dan common-modulus.
- `pyca/demo.py`: demo AES-GCM dan RSA-OAEP menggunakan pustaka `cryptography`.

## Dependensi dan instalasi

Diperlukan Python 3. Gunakan lingkungan virtual agar dependensi proyek terisolasi:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

`cryptopals/` menggunakan pustaka standar Python. Skrip di `rsa/` memerlukan `sympy`, sedangkan `pyca/demo.py` memerlukan `cryptography`. Kedua dependensi eksternal tersebut tercantum di `requirements.txt`.

## Menjalankan contoh

```bash
python rsa/rsa_basic.py
python rsa/attack_low_e.py
python pyca/demo.py
```

Skrip `cryptopals/c04_detect_single_xor.py` mengharapkan berkas `cryptopals/data/4.txt`; berkas input tersebut belum disertakan di repositori ini.

## RsaCtfTool (opsional, Termux)

RsaCtfTool adalah perangkat terpisah dan tidak termasuk dependensi Python proyek ini. Setelah memasangnya sendiri, contoh pemanggilannya:

```bash
PYTHONPATH=~/RsaCtfTool/src python -m RsaCtfTool.main -n N -e E --decrypt C
```
