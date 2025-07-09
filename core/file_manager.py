import csv
import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.path = f"core/data/{self.filename}.csv"

    def writerows(self, data: list[list]) -> None:
        with open(self.path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def read(self) -> list:
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8", newline="") as file:
                reader = csv.reader(file)
                return list(reader)
        return []

    def append(self, row: list) -> None:
        with open(self.path, mode="a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)
