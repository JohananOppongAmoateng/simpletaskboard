from django.db import models
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()

STATUS_CHOICES = [
    ('wont_do',     "Won't do"),
    ('in_progress', "In progress"),
    ('completed',   "Completed"),
]
    
LUCIDE_ICON_CHOICES = [
    ('Activity',      'Activity'),
    ('Airplay',       'Airplay'),
    ('CheckCircle',   'Check Circle'),
    ('Star',          'Star'),
]

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Board(TimeStamp):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='boards', blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Task(TimeStamp):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,choices=STATUS_CHOICES,default=STATUS_CHOICES[1][0]
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True
    )
    icon_name   = models.CharField(
        max_length=50,
        choices=LUCIDE_ICON_CHOICES,
        default='Activity',
        help_text="Select one of the Lucide icon names"
    )
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True
    )


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  

