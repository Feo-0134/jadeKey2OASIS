from django.db import models
from django.contrib.auth.models import User

class Engineer(models.Model):
    ENGINEER_TITLE = [
        ('SE', 'Support Engineer'),
        ('SEE', 'Support Escalation Engineer'),
        ('EE', 'Escalation Engineer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=3, choices=ENGINEER_TITLE)

    def escalation(self, new_title):
        self.title = new_title
        return self.name + ':' + self.title
    
    def __str__(self):
        return str(self.id) + ': ' + self.name

class Comment(models.Model):
    STAGE_TITLE = [
        ('E0S1', 'E0Stage1'),
        ('E0S2', 'E0Stage2'),
        ('E0S3', 'E0Stage3'),
        ('E0S4', 'E0Stage4'),

        ('E1S1', 'E1Stage1'),
        ('E1S2', 'E1Stage2'),
        ('E1S3', 'E1Stage3'),
        ('E1S4', 'E1Stage4'),
        ('E1S0', 'BackUp'),
    ]
    RESULT = [
        ('OG', 'On-going'),
        ('PS', 'Pass'),
        ('NP', 'No Pass')
    ]
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    stageTitle = models.CharField(max_length=4, choices=STAGE_TITLE)
    result = models.CharField(max_length=2, choices=RESULT)  
    comment_text = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.id) + ': ' + self.engineer.name + ': ' + self.stageTitle

class HighLvl(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    related_comment = models.ManyToManyField(
        Comment,
        through='MakeCommentOn',
        through_fields=('highlvl','comment')
    )
    def __str__(self):
        return str(self.id) + ': ' + self.name

class Stage(models.Model):
    STAGE_TITLE = [
        ('E0S1', 'E0Stage1'),
        ('E0S2', 'E0Stage2'),
        ('E0S3', 'E0Stage3'),
        ('E0S4', 'E0Stage4'),

        ('E1S1', 'E1Stage1'),
        ('E1S2', 'E1Stage2'),
        ('E1S3', 'E1Stage3'),
        ('E1S4', 'E1Stage4'),
        ('E1S0', 'BackUp'),
    ]
    STATUS = [
        ('OG', 'On-going'),
        ('PS', 'Pass'),
        ('NP', 'No Pass')
    ]
    
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    title = models.CharField(max_length=4, choices=STAGE_TITLE)
    status = models.CharField(max_length=2, choices=STATUS)
    commitee_num = models.IntegerField()
    related_comment = models.ManyToManyField(
        Comment,
        through='StageLinkComment',
        through_fields=('stage','comment')
    )

    def __str__(self):
        return str(self.id) + ': ' + self.engineer.name + ': ' + self.title

    class Meta:
        ordering = ['status']

class Process(models.Model):
    PROCESS_TITLE = [
        ('E0', 'Escalation to SEE'),
        ('E1', 'Escalation to EE'),
    ]
    STATUS = [
        ('S1', 'Stage1'),
        ('S2', 'Stage2'),
        ('S3', 'Stage3'),
        ('S4', 'Stage4'),
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
        return str(self.id) + ': ' + self.title + ': ' + self.engineer.name

    class Meta:
        ordering = ['engineer']

class ProcessLinkStage(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    def __str__(self):
        return self.process.title + ': ' + self.process.engineer.name + ': ' + self.stage.title

class StageLinkComment(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    def __str__(self):
        return self.stage.engineer.name + ': ' + self.stage.title

class MakeCommentOn(models.Model):
    highlvl = models.ForeignKey(HighLvl, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    def __str__(self):
        return self.highlvl.name + ': ' + self.comment.stageTitle