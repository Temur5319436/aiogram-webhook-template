from django.db import models


class Conversation(models.Model):
    chat_id = models.CharField(max_length=25)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        db_table = "conversations"
