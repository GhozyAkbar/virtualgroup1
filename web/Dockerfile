# Gunakan image Python sebagai base image
FROM python:3.9

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Buat direktori kerja
WORKDIR /code

# Salin file requirements.txt ke direktori kerja
COPY requirements.txt /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi direktori kerja ke image
COPY . /code/

# Jalankan aplikasi
CMD ["python", "app.py"]
