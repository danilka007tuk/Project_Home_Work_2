import os

from src.reading import read_csv, read_excel

if __name__ == "__main__":
    file_path_1 = os.path.join("data_2", "transactions.csv")
    operations = read_csv(file_path_1)
    for operation in operations:
        print(operation)

if __name__ == "__main__":
    file_path_2 = os.path.join("data_2", "transactions_excel.xlsx")
    print(read_excel(file_path_2))
