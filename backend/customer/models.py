from django.db import models



# Create your models here.

class Customer(models.Model):
    CHOICES = (('FP', 'Физлицо'),
               ('JP', 'Юрлицо'))

    name = models.CharField(verbose_name='Наименование',
                            max_length=35, default='')
    email = models.EmailField()
    jp = models.CharField(verbose_name='Тип юрлица',
                          choices=(('FP', 'Физлицо'), ('JP', 'ООО')),
                          max_length=3)
    inn = models.CharField(verbose_name='ИНН',
                           max_length=10, blank=True, default='')
    kpp = models.CharField(verbose_name='КПП',
                           max_length=25, blank=True, default='')
    okpo = models.CharField(verbose_name='ОКПО',
                            max_length=20, blank=True, default='')
    address = models.TextField(verbose_name='Фактический адрес',
                               max_length=15, blank=True, default='')

    def __str__(self):
        return f'{self.name}|{self.inn}'

    class Meta:
        verbose_name = 'Заказчик',
        verbose_name_plural = 'Заказчики'


class BankDetail(models.Model):
    name = models.CharField(verbose_name='Банк',
                            max_length=35, default='')
    bic = models.CharField(verbose_name='БИК',
                           max_length=32, default='')
    account = models.CharField(verbose_name='р/с',
                               max_length=30, default='')
    c_account = models.CharField(verbose_name='к/c',
                                 max_length=28, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='customer_bank')

    def __str__(self):
        return f'Реквизиты {self.customer}'

    class Meta:
        verbose_name = 'Реквизиты',
        verbose_name_plural = 'Перечень реквизитов'


class Contracts(models.Model):
    name = models.CharField(max_length=33, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='customer_contracts')

    def __str__(self):
        return f'{self.name} | {self.customer.name}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
