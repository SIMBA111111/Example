from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='replacements',
        verbose_name="Сотрудник",
    )
    replacement = models.ForeignKey(
        'breaks.Replacement', on_delete=models.CASCADE, related_name='employees',
        verbose_name="Смена",
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', on_delete=models.RESTRICT, related_name='replacement_employees',
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = 'Смена - работник'
        verbose_name_plural = 'Смены - работники'

    def __str__(self):
        return f'Смена {self.replacement} для {self.employee}'


class Replacement(models.Model):
    group = models.ForeignKey(
        'breaks.Group', on_delete=models.CASCADE, related_name='replacements',
        verbose_name="Группа",
    )
    date = models.DateField('Дата смены')
    break_start = models.TimeField('Начало обеда')
    break_end = models.TimeField('Конец обеда')
    break_max_duration = models.PositiveSmallIntegerField(
        'Макс. продолжительность обеда'
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена №{self.pk}'
