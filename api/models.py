import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    name = models.CharField(max_length=200)

    # A project is done if it has more than one task and all its tasks are done
    def is_done(self):
        done = self.task_set.filter(status=Task.Status.DONE)
        return len(done) == len(self.task_set.all()) > 0

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = 'td', _('To Do')
        DOING = 'dg', _('Doing')
        REVIEW = 'rv', _('Needs Review')
        DONE = 'dn', _('Done')

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    start_date = models.DateField('date started', auto_now_add=True)
    due_date = models.DateTimeField('due date')
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.TODO,
        blank=False,
    )

    def is_done(self):
        return self.status == self.Status.DONE

    def is_past_due(self):
        return self.due_date <= timezone.now()

    def __str__(self):
        return self.text

