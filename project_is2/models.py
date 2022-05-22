from django.db import models

# Create your models here.
class Topic(models.Model):
    """Пользователь изучает определенные темы. Данный класс описывает ее."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает представление модели в виде строки"""
        return self.text

class Entry(models.Model):
    """Информация, которую изучил пользователь по определенной теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Возвращает представление модели в виде строки"""
        return f"{self.text[:50]}..."
        