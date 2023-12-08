import pygame
import sys
from pygame.locals import *
import os

pygame.init()

# Khai báo cửa sổ game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chụp màn hình")

# Khai báo màu sắc
white = (255, 255, 255)

# Khai báo font
font = pygame.font.Font(None, 36)

# Load hình ảnh button và thiết lập kích thước mong muốn
button_image = pygame.image.load("button.png")  # Thay "button.png" bằng đường dẫn đến hình ảnh của nút
button_size = (150, 50)
button_image = pygame.transform.scale(button_image, button_size)

# Lấy kích thước hình ảnh button
button_rect = button_image.get_rect()

# Đặt vị trí của button
button_rect.topleft = (200, 300)

# Thư mục để lưu ảnh
screenshot_folder = "screenshots"

# Đảm bảo thư mục tồn tại
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Đường dẫn và biến đếm để lưu ảnh
screenshot_base_name = "screenshot"
screenshot_extension = ".png"
screenshot_path = os.path.join(screenshot_folder, screenshot_base_name)
screenshot_count = 0


# Hàm kiểm tra xem tên file đã tồn tại chưa
def is_file_exist(path):
    return os.path.exists(path)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Kiểm tra xem chuột có được nhấn vào button không
            if button_rect.collidepoint(event.pos):
                # Tạo tên mới cho ảnh và lưu ảnh
                while is_file_exist(f"{screenshot_path}_{screenshot_count}{screenshot_extension}"):
                    screenshot_count += 1

                new_screenshot_path = f"{screenshot_path}_{screenshot_count}{screenshot_extension}"
                pygame.image.save(screen, new_screenshot_path)
                print("Chụp màn hình và lưu ảnh tại:", new_screenshot_path)

    # Vẽ nền trắng
    screen.fill(white)

    # Hiển thị button
    screen.blit(button_image, button_rect.topleft)

    # Cập nhật cửa sổ
    pygame.display.flip()
