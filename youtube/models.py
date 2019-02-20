from django.db import models
from youtube.tasks import get_videos


class Channel(models.Model):
    channel_id = models.CharField(max_length=30)

    def clean(self):
        super(Channel, self).clean()

        get_videos.send(self.channel_id)
        return self

