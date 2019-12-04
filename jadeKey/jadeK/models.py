from django.db import models
from django.utils import timezone
import datetime

class Engineer(models.Model):
    # current title
    ENGINEER_TITLE = (
        ('SE', 'Support Engineer'),
        ('SEE', 'Support Escalation Engineer'),
        ('EE', 'Escalation Engineer'),
    )
    # engineer is currently under going a escalation process
    in_a_process = models.BooleanField(Field.default = False)

class Process(models.Model):
    PROCESS_TITLE = (
        ('E1', 'Escalation to SEE'),
        ('E2', 'Escalation to EE'),
    )
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    start_date = models.DateTimeField('date started')
    CURRENT_STAGE = (
        ('S1', 'Stage1'),
        ('S2', 'Stage2'),
        ('S3', 'Stage3'),
        ('S4', 'Stage4'),
        ('S5', 'Stage5'),
    )
    end_date = models.DateTimeField('date ended')

class Stage(models.Model):
    STAGE_TITLE = (
        ('S1', 'Stage1'),
        ('S2', 'Stage2'),
        ('S3', 'Stage3'),
        ('S4', 'Stage4'),
        ('S5', 'Stage5'),
    )
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    start_date = models.DateTimeField('date started')
    STATUS = (
        ('alive', 'In Process'),
        ('pass', 'Pass'),
        ('no_pass', 'No Pass')
    )
    end_date = models.DateTimeField('date ended')

class Comment(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    author = models.ForeignKey(Engineer, on_delete=models.DO_NOTHING)
    comment_text = models.CharField(max_length=1000)
    RESULT = (
        ('alive', 'In Process'),
        ('pass', 'Pass'),
        ('no_pass', 'No Pass')
    )
