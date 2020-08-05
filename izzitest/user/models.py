from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models, IntegrityError
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from order.models import Order


class User(AbstractBaseUser):
    """
    Represent User in database and has its CRUD methods
    """
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthday = models.DateField()
    registration_date = models.DateField()
    order_id = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE, null=True)

    objects = BaseUserManager()

    class Meta:
        db_table = 'Users'

    def __repr__(self):
        return f'{self.name=}, {self.surname=}, {self.birthday=}, {self.registration_date=},' \
               f' {self.order_id=}'

    @staticmethod
    def create(name, surname, birthday, registration_date, order_id=None):
        """
        Create new user in database

        :param name: str
        :param surname: str
        :param birthday: str | date format YYYY-MM-DD
        :param registration_date: str | date format YYYY-MM-DD
        :param order_id: int
        :return: User object
        """
        user = User(
            name=name,
            surname=surname,
            birthday=birthday,
            registration_date=registration_date,
            order_id=order_id
        )

        try:
            user.save()
            return user
        except (IntegrityError, ValidationError):
            return None

    @staticmethod
    def filter(name=None, surname=None, birthday=None, registration_date=None, order_id=None):
        """
        Get users from database by parameters

        :param name: str
        :param surname: str
        :param birthday: str | date format YYYY-MM-DD
        :param registration_date: str | date format YYYY-MM-DD
        :param order_id: int
        :return: list
        """
        data = {}

        if name is not None:
            data['name'] = name
        if surname is not None:
            data['surname'] = surname
        if birthday is not None:
            data['birthday'] = birthday
        if registration_date is not None:
            data['registration_date'] = registration_date
        if order_id is not None:
            data['order_id'] = order_id

        try:
            users = User.objects.filter(**data)
            return list(users)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all():
        """
        Get list of all user objects in database

        :return: list
        """
        return list(User.objects.all())
