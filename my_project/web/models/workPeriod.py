from django.db import models
from datetime import datetime


class WorkPeriod(models.Model):
    start_date = models.DateTimeField("Created on", null=False)

    end_date = models.DateTimeField("Created on", blank=True, null=True)

    executive = models.ForeignKey(
        'web.Executive',
        on_delete=models.CASCADE,
        related_name='working_periods',
        verbose_name='executive'
    )

    class Meta:
        verbose_name = 'work period'
        verbose_name_plural = 'work periods'

    def __str__(self):
        return f'{self.executive} | {self.start_date} | {self.end_date}'


