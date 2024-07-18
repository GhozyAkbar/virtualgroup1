# Gunakan image Python resmi sebagai basis
FROM python:3.9-slim

# Setel direktori kerja dalam container
WORKDIR /app

COPY . .
# Salin file requirements.txt ke dalam container

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file dari direktori lokal ke dalam container
COPY . .

EXPOSE 8080

EXPOSE 9000

# Tentukan perintah untuk menjalankan aplikasi
CMD ["./start.sh"]