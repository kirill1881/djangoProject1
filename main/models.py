from django.db import models


class Task(models.Model):
    def __init__(self, name, text, time, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name = name
        self.__text = text
        self.__time = time


