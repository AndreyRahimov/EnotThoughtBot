import os
import sys

BOOK_PATH = "book/book.txt"
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation_marks = ",.!:;?"
    finish = start + size

    if len(text) > finish:
        while text[finish] in punctuation_marks:
            finish -= 1

    text = text[start:finish]

    for char in text[::-1]:
        if char in punctuation_marks:
            break
        finish -= 1

    text = text[:finish]

    return text, finish


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    page_num = 1
    position = 0
    while len(text) > position:
        page, page_len = _get_part_text(text, position, PAGE_SIZE)
        page = page.lstrip()
        book[page_num] = page
        page_num += 1
        position += page_len


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
