"""
Module for Order model
"""
from django.db import models, IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class Order(models.Model):
    """
    Represent Order in database and has its CRUD methods
    """
    product = models.CharField(max_length=255)  # product name
    date = models.DateField()  # date of creation

    class Meta:
        db_table = 'Orders'  # table name

    def __repr__(self):
        return f'(product = {self.product}, date = {self.date})'

    @staticmethod
    def create(product, date):
        """
        Create new order in database

        :param product: str | product name
        :param date: str | date form YYYY-MM-DD
        :return: Order object
        """
        # check if this order already exist in database
        order = Order.filter(product=product, date=date)

        # if exists return that object
        if order:
            return order[0]

        order = Order(product=product, date=date)

        try:
            order.save()
            return order
        except IntegrityError:
            return None

    @staticmethod
    def filter(product=None, date=None):
        """
        Get orders from database by parameters

        :param product: str | product name
        :param date: str | date form YYYY-MM-DD
        :return: list
        """
        data = {}
        if product is not None:
            data['product'] = product
        if date is not None:
            data['date'] = date

        try:
            orders = Order.objects.filter(**data)
            return list(orders)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all():
        """
        Get list of all order objects in database

        :return: list
        """
        return list(Order.objects.all())
