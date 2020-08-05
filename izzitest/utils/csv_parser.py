"""
CSV parser
"""
import csv

class CsvParser():
    """
    Class for work with csv files
    """
    @staticmethod
    def parse(file):
        """
        Parse csv file and return list with its rows

        :param file: str | path to the file
        :return: list
        """
        with open(file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            data = list(reader)
        return data

    @staticmethod
    def is_heading(row):
        """
        Check if this row is heading
        :param row: list | csv row
        :return: bool
        """
        heading = ['FirstName', 'LastName', 'BirthDate', 'RegistrationDate']
        return row == heading
