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
    title = models.CharField(max_length=3, choices=ENGINEER_TITLE)
    
    def __str__(self):
        return self.name


class Process(models.Model):
    PROCESS_TITLE = [
        ('E1', 'Escalation to SEE'),
        ('E2', 'Escalation to EE'),
    ]
    STATUS = [
        ('alive', 'In Process'),
        ('pass', 'Pass'),
        ('no_pass', 'No Pass')
    ]

    title = models.CharField(max_length=3, choices=PROCESS_TITLE)
    created = models.DateTimeField(auto_now_add=True)
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS)
    
    # def process_started(self):
    #     return self.stage_set

    def __str__(self):
        return self.title + ': ' + self.engineer.name

    class Meta:
        ordering = ['engineer']


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
    
    title = models.CharField(max_length=3, choices=STAGE_TITLE)
    created = models.DateTimeField(auto_now_add=True)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created']


class Comment(models.Model):
    RESULT = [
        ('alive', 'In Process'),
        ('pass', 'Pass'),
        ('no_pass', 'No Pass')
    ]
    
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    result = models.CharField(max_length=7, choices=RESULT)  
    comment_text = models.CharField(max_length=1000)

    
    def __str__(self):
        return self.author.name
    class Meta:
        ordering = ['created']

