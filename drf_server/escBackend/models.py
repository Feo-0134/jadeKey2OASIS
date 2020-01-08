from django.db import models

class EngineerTitle(models.Model):
    FullName = models.CharField(maxlength=20)
    Abbreviation = models.CharField(maxlength=10)
    def __str__(self):
        return str(self.id) + ': ' + self.FullName

class ProcessKind(models.Model):
    FullName = models.CharField(maxlength=20)
    Abbreviation = models.CharField(maxlength=10)
    def __str__(self):
        return str(self.id) + ': ' + self.FullName

class StageKind(models.Model):
    FullName = models.CharField(maxlength=20)
    Abbreviation = models.CharField(maxlength=10)
    def __str__(self):
        return str(self.id) + ': ' + self.FullName

class Engineer(models.Model):
    Alias = models.CharField(maxlength=10)
    Name = models.CharField(maxlength=20)
    Title = models.ForeignKey(EngineerTitle, ondelete=models.CASCADE)
    EngineerLatestProcess = models.BigIntegerField(default=-1)
    EngineerLatestStage = models.BigIntegerField(default=-1)
    IsReviewer = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + ': ' + self.Name

class Process(models.Model):
    Kind = models.ForeignKey(ProcessKind, ondelete=models.CASCADE)
    ProcessOwner = models.ForeignKey(Engineer, ondelete=CASCADE)
    ProcessReviewer = models.ManyToManyField(
        Engineer,
        through = 'ProcessReview',
        throughfields = ('Process', 'Reviewer')
    )
    ProcessCurrentStage = models.ForeignKey(StageKind, ondelete=CASCADE)
    Stage1TryTimes = models.BigIntegerField(default=-1)
    Stage2TryTimes = models.BigIntegerField(default=-1)
    Stage3TryTimes = models.BigIntegerField(default=-1)
    Stage4TryTimes = models.BigIntegerField(default=-1)
    def __str__(self):
        return str(self.id) + ': ' + self.Owner.Name + ': ' + self.Kind.FullName

class ProcessReview(models.Model):
    Process = models.ForeignKey(Process, ondelete=models.CASCADE)
    Reviewer = models.ForeignKey(Engineer, ondelete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ': ' + self.Process.Owner.Name + ': ' + self.Process.Kind.FullName + ': ' + self.Reviewer.Name

class Comment(models.Model):
    Process = models.ForeignKey(Process, ondelete=models.CASCADE)
    Stage = models.ForeignKey(StageKind, ondelete=models.CASCADE)
    Writer = models.ForeignKey(Engineer, ondelete=models.CASCADE)
    Edited = models.BooleanField(default=False)
    Submited = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + ': ' + self.Process.Owner.Name
         + ': ' + self.Process.Kind.FullName + ': ' + self.Stage.FullName
         + ': ' + self.Writer.Name 
