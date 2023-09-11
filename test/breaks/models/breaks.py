from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'breaks',
        verbose_name="Смена",
    )
    employee = models.ForeignKey(
        User, models.CASCADE, 'breaks', verbose_name="Сотрудник",
        blank=True,
    )
    break_start = models.TimeField('Начало обеда', null=True, blank=True, )
    break_end = models.TimeField('Конец обеда', null=True, blank=True, )
    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT, 'breaks', verbose_name='Статус',
        blank=True,
    )

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ('-replacement__date', 'break_start', )

    def __str__(self):
        return f'Обед пользователя  {self.employee} - {self.pk}'
