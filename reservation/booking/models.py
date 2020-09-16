from django.db import models

# Create your models here.

class Salon(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Time(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    salon = models.ForeignKey(Salon ,on_delete=models.DO_NOTHING)

    def __str__(self):
        self.start_time+'-'+self.end_time
class Slot(models.Model):
    user_list = [('1', "1"), ('2', "2"), ('3', '3'), ('4', '4'), ('5', '5')]
    slot_input = models.CharField(max_length=5)
    time_for_book = models.ForeignKey(Time,on_delete=models.DO_NOTHING)

