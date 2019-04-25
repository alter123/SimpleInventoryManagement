import uuid

from django.db import models


class Item(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.item_id