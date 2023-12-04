import pytesseract
from PIL import Image

import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog as fd

import argparse
import cv2
import os


def read_image():
    # Mở hộp thoại để chọn tệp ảnh
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if file_path:
        # Đọc ảnh và chuyển nó sang văn bản bằng Tesseract OCR
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang='vie')

        # Hiển thị nội dung văn bản trong một cửa sổ mới`
        text_window = tk.Toplevel(root)
        text_window.title("Nội dung đọc từ ảnh")

        with open("text.txt", "w", encoding="utf-8") as file:
            file.write(text)

        text_widget = tk.Text(text_window, wrap=tk.WORD)
        text_widget.insert(tk.END, text)
        text_widget.pack(expand=True, fill='both')

# Tạo một cửa sổ chương trình
root = tk.Tk()
root.title("Ứng dụng OCR")

# Tạo một nút để chọn và đọc ảnh
read_button = tk.Button(root, text="Chọn ảnh và đọc", command=read_image)
read_button.pack(pady=10)

# Bắt đầu vòng lặp sự kiện để hiển thị cửa sổ
root.mainloop()


# def tesseract_OCR():
#     # Chỉ định đường dẫn tới tesseract executable
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Điều chỉnh đường dẫn tùy theo cài đặt của bạn
#
#     # Đường dẫn đến ảnh
#     image_path = 'test.png'
#
#     # Đọc ảnh
#     image = Image.open(image_path)
#
#     # Nhận diện văn bản
#     text = pytesseract.image_to_string(image, lang='vie')
#
#     # Hiển thị văn bản
#     print(text)
#
#     # Ghi văn bản vào file
#     output_file_path = 'test.txt'
#     with open(output_file_path, 'w', encoding='utf-8') as file:
#         file.write(text)
#
#     print(f'Văn bản đã được ghi vào file {output_file_path}')
