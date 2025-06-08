from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Board, Task,LUCIDE_ICON_CHOICES,STATUS_CHOICES

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_board_for_new_user(sender, instance, created, **kwargs):
    """
    When a new User is created, automatically create an associated Board.
    """
    if created:
        board = Board.objects.create(
            user=instance,
            name=f"{instance.username}'s Board"
        )

        tasks_to_create = [
            Task(
                title="Buy groceries",
                description="Milk, eggs, bread",
                icon_name=LUCIDE_ICON_CHOICES[0][0],    
                status=STATUS_CHOICES[0][0], 
                user=instance, 
                board=board,   
            ),
            Task(
                title="Write report",
                description="Send draft to team",
                icon_name=LUCIDE_ICON_CHOICES[1][0],
                status=STATUS_CHOICES[1][0],
                user=instance,  
                board=board,
            ),
            Task(
                title="Plan meetup",
                description="Book venue and send invites",
                icon_name=LUCIDE_ICON_CHOICES[2][0],    
                status=STATUS_CHOICES[2][0], 
                user=instance,
                board=board,
            ),
            Task(
                title="Review PRs",
                description="Look over open GitHub pull requests",
                icon_name=LUCIDE_ICON_CHOICES[3][0],    
                status=STATUS_CHOICES[1][0], 
                user=instance, 
                board=board,
            ),
        ]

        Task.objects.bulk_create(tasks_to_create)