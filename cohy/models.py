from django.db import models

# Create your models here.
class Station(models.Model):
    code = models.CharField(max_length=15)

    def load_to_object(self, file_content):
        pass
