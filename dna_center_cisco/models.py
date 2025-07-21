from django.db import models

class InteractionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100, blank=True)
    result = models.CharField(max_length=50)
    action = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.action} - {self.result}"
