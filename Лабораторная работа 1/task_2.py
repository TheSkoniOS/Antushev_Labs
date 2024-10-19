# TODO Найдите количество книг, которое можно разместить на дискете
import math

info_volume_disk_Mb = 1.44  # Объём диска в Мб
count_pages_in_book = 100   # Количество страниц в книге
count_rows_in_page = 50     # Число строк на странице
count_chars_in_row = 25     # Количество символов в строке


info_volume_disk_b = info_volume_disk_Mb * (1024 ** 2)                      # Объём диска в байтах

volume_row = 4 * count_chars_in_row                                         # Объём строки
volume_page = volume_row * count_rows_in_page                               # Объём страницы
volume_book = volume_page * count_pages_in_book                             # Объём книги

count_books_in_disk = int(math.floor(info_volume_disk_b // volume_book))    # Количество книг на дискете

print("Количество книг, помещающихся на дискету:", count_books_in_disk)
