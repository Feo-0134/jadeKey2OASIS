from django.db import models
from django.utils import timezone
import datetime

class Engineer(models.Model):
    ENGINEER_TITLE = [
        ('SE', 'Support Engineer'),
        ('SEE', 'Support Escalation Engineer'),
        ('EE', 'Escalation Engineer'),
    ]
    name = models.CharField(max_length=20)
    # current title
    title = models.CharField(max_length=3, choices=ENGINEER_TITLE)
    # engineer is currently under going a escalation process
    in_a_process = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name


class Process(models.Model):
    PROCESS_TITLE = [
        ('E1', 'Escalation to SEE'),
        ('E2', 'Escalation to EE'),
    ]
    CURRENT_STAGE = [
        ('S1', 'Stage1'),
        ('S2', 'Stage2'),
        ('S3', 'Stage3'),
        ('S4', 'Stage4'),
        ('S5', 'Stage5'),
    ]
    title = models.CharField(max_length=3, choices=PROCESS_TITLE)
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    start_date = models.DateTimeField('date started')
    current_stage = models.CharField(max_length=3, choices=CURRENT_STAGE)
    def __str__(self):
        return self.current_stage + ': ' + self.engineer.name


class Stage(models.Model):
    STAGE_TITLE = [
        ('S1', 'Stage1'),
        ('S2', 'Stage2'),
        ('S3', 'Stage3'),
        ('S4', 'Stage4'),
        ('S5', 'Stage5'),
    ]    
    STATUS = [
        ('alive', 'In Process'),
        ('pass', 'Pass'),
        ('no_pass', 'No Pass')
    ]
    title = models.CharField(max_length=3, choices=STAGE_TITLE )
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    start_date = models.DateTimeField('date started')
    status = models.CharField(max_length=7, choices=STATUS)
    def __str__(self):
        return self.title


class Comment(models.Model):
    RESULT = [
        ('alive', 'In Process'),
        ('pass', 'Pass'),
        ('no_pass', 'No Pass')
    ]
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    author = models.ForeignKey(Engineer, on_delete=models.DO_NOTHING)
    comment_text = models.CharField(max_length=1000)
    result = models.CharField(max_length=7, choices=RESULT)
    def __str__(self):
        return self.author.name

