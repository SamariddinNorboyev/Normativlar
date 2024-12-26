import logging
from fileinput import filename

logging.basicConfig(
    level=logging.INFO,
    filename="file-operations.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
file_nomi = "doston.txt"
try:
    with open(file_nomi, "r") as file:
        a = file.readline()
except FileNotFoundError:
    logging.error(f"FileNotFoundError {file_nomi} bunday fayl topilmadi!")


with open("file-operations.log", "r") as file:
    content = file.read()
    print(content)