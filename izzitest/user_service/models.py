"""
Service for work with user
"""
from user.models import User
from utils.csv_parser import CsvParser


class UserService():
    """
    Class for work with user
    """
    # positions in csv row
    NAME = 0
    SURNAME = 1
    BIRTHDAY = 2
    REGISTRATION_DATE = 3

    @staticmethod
    def add_user(name, surname, birthday, registration_date):
        """
        prepare data and create user

        :param name: str
        :param surname: str
        :param birthday: str | date
        :param registration_date: str | date
        :return: User object or None
        """

        birthday = User.format_date(birthday)
        registration_date = User.format_date(registration_date)
        user = User.create(
            name=name,
            surname=surname,
            birthday=birthday,
            registration_date=registration_date
        )
        return user

    @staticmethod
    def add_users_from_csv(file):
        """
        Add users from csv file

        :param file: str | file path
        :return: bool
        """

        start = 0
        rows = CsvParser.parse(file)

        if CsvParser.is_heading(rows[0]):
            start = 1

        for row in rows[start:]:

            if len(row) < 4: # i could use try except here
                continue

            UserService.add_user(
                name=row[UserService.NAME],
                surname=row[UserService.SURNAME],
                birthday=row[UserService.BIRTHDAY],
                registration_date=row[UserService.REGISTRATION_DATE]
            )

        return True
