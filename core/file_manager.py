import csv
import os


class CSVFileManager:
    def __init__(self, filename):
        self.filename = filename


    def writerows(self, data: list[list]) -> None:
        """
        write given list of data to csv
        :param data: list of data
        :return: None
        """
        path = f"../apps/data/{self.filename}.csv"
        with open(file=path, mode="w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)


    def read(self) -> list:
        """
        read csv file as a list
        :return: list of data
        """
        path = f"../apps/data/{self.filename}.csv"
        if os.path.exists(path=path):
            with open(file=path, mode="r", encoding="UTF-8", newline="") as file:
                reader = csv.reader(file)
                return list(reader)
        return list()


    def append(self, data: list) -> None:
        """
        write given list of data to csv
        :param data: list of data
        :return: None
        """
        path = f"../apps/data/{self.filename}.csv"
        with open(file=path, mode="a", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)