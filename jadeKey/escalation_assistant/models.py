from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Engineer(models.Model):
    ENGINEER_TITLE = [
        ('SE', 'Support Engineer'),
        ('SEE', 'Support Escalation Engineer'),
        ('EE', 'Escalation Engineer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    title = models.CharField(max_length=3, choices=ENGINEER_TITLE)

    
    def __str__(self):
        return self.name

class Comment(models.Model):
    RESULT = [
        ('OG', 'On-going'),
        ('PS', 'Pass'),
        ('NP', 'No Pass')
    ]
    
    author = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    result = models.CharField(max_length=2, choices=RESULT)  
    comment_text = models.CharField(max_length=1000)

    
    def __str__(self):
        return self.stage.process.engineer + ':' + self.stage.process.title + ': ' + self.stage.title + ': ' + self.stage.status + ':' + self.author.name + ': ' + self.result

class Stage(models.Model):
    STAGE_TITLE = [
        ('S1', 'Stage1'),
        ('S2', 'Stage2'),
        ('S3', 'Stage3'),
        ('S4', 'Stage4'),
        ('S0', 'BackUp'),
    ]    
    STATUS = [
        ('OG', 'On-going'),
        ('PS', 'Pass'),
        ('NP', 'No Pass')
    ]
    
    title = models.CharField(max_length=2, choices=STAGE_TITLE)
    status = models.CharField(max_length=2, choices=STATUS)
    commitee_num = models.IntegerField()
    comment = models.ManyToManyField(
        Comment,
        through='StageLinkComment',
        through_fields=('stage','comment')
    )

    def __str__(self):
        return self.process.engineer + ':' + self.process.title + ': ' + self.title + ': ' + self.status

    class Meta:
        ordering = ['status']

class Process(models.Model):
    PROCESS_TITLE = [
        ('E1', 'Escalation to SEE'),
        ('E2', 'Escalation to EE'),
    ]
    STATUS = [
        ('S0', 'Stage1'),
        ('S1', 'Stage1'),
        ('S2', 'Stage1'),
        ('S3', 'Stage1'),
        ('PS', 'Pass'),
        ('NP', 'No Pass')
    ]

    title = models.CharField(max_length=2, choices=PROCESS_TITLE)
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS)
    stage = models.ManyToManyField(
        Stage,
        through='ProcessLinkStage',
        through_fields=('process','stage')
    )

    def __str__(self):
        return self.title + ': ' + self.status + ': ' + self.engineer.name

    class Meta:
        ordering = ['engineer']
    

class ProcessLinkStage(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

class StageLinkComment(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)