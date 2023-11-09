from django.db import models


class Executive(models.Model):
    JOBTITLE = [
        ("Председатель Совета директоров", "Председатель Совета директоров"),
        ("Председатель Правления", "Председатель Правления"),
        ("Совет директоров", "Совет директоров"),
        ("Члены Правления", "Члены Правления"),
        ("Главный бухгалтер", "Главный бухгалтер"),
    ]

    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='full_name'
    )

    IIN = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='IIN'
    )

    job_title = models.CharField(
        max_length=300,
        null=False,
        choices=JOBTITLE,
        default="Главный бухгалтер",
    )

    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='phone'
    )

    email = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='email'
    )

    fin_organization = models.ForeignKey(
        'web.FinancialOrganization',
        on_delete=models.CASCADE,
        related_name='executives',
        verbose_name='fin organization',
        default=1
    )

    class Meta:
        verbose_name = 'executive'
        verbose_name_plural = 'executives'

    def __str__(self):
        return f'{self.full_name}'


