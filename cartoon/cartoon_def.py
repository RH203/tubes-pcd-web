# cartoon/cartoon_def.py

from PIL import Image
import cv2
import numpy as np
import os
import io
import base64

def cartoonize_image(image_path, save_directory, title):
    # Baca gambar menggunakan OpenCV
    img = cv2.imread(image_path)

    # Convert gambar ke ruang warna abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Terapkan Gaussian Blur untuk meratakan citra
    gray_blur = cv2.medianBlur(gray, 7)

    # Deteksi tepi menggunakan algoritma Canny
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Mengaburkan tepi untuk membuat efek sketsa
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Menggabungkan tepi dan gambar berwarna menggunakan mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Menyimpan hasil cartoonizing ke file
    cartoon_path = os.path.join(save_directory, f"{title}_cartoon.jpg")
    cv2.imwrite(cartoon_path, cartoon)

    return cartoon_path

def cartoonize_image_base64(image_path):
    # Baca gambar menggunakan OpenCV
    img = cv2.imread(image_path)

    # Convert gambar ke ruang warna abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Terapkan Gaussian Blur untuk meratakan citra
    gray_blur = cv2.medianBlur(gray, 7)

    # Deteksi tepi menggunakan algoritma Canny
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Mengaburkan tepi untuk membuat efek sketsa
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Menggabungkan tepi dan gambar berwarna menggunakan mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Konversi gambar ke format PIL (Pillow)
    cartoon_pil = Image.fromarray(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))

    # Simpan gambar dalam bentuk BytesIO
    image_stream = io.BytesIO()
    cartoon_pil.save(image_stream, format='JPEG')
    image_stream.seek(0)

    # Encode gambar dalam base64
    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

    return image_base64
