from django.db import models


class FinancialOrganization(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='name'
    )

    BIN = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='BIN'
    )

    address = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='address'
    )

    phone = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='phone'
    )

    fax = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='fax'
    )

    email = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='email'
    )

    web_site = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='web site'
    )

    class Meta:
        verbose_name = 'finOrganization'
        verbose_name_plural = 'finOrganizations'

    def __str__(self):
        return f'{self.name}'


