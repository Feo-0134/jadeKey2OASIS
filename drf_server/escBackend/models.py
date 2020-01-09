from django.db import models

class EngineerTitle(models.Model):
    FullName = models.CharField(max_length=20)
    Abbreviation = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id) + ': ' + self.FullName

class ProcessKind(models.Model):
    FullName = models.CharField(max_length=20)
    Abbreviation = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id) + ': ' + self.FullName

class StageKind(models.Model):
    FullName = models.CharField(max_length=20)
    Abbreviation = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id) + ': ' + self.FullName

class Engineer(models.Model):
    Alias = models.CharField(max_length=10)
    Name = models.CharField(max_length=20)
    Title = models.ForeignKey(EngineerTitle, on_delete=models.CASCADE)
    EngineerLatestProcess = models.BigIntegerField(default=-1)
    EngineerLatestStage = models.BigIntegerField(default=-1)
    IsReviewer = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + ': ' + self.Name

class Process(models.Model):
    Kind = models.ForeignKey(ProcessKind, on_delete=models.CASCADE)
    ProcessOwner = models.ForeignKey(Engineer, on_delete=CASCADE)
    ProcessReviewer = models.ManyToManyField(
        Engineer,
        through = 'ProcessReview',
        throughfields = ('Process', 'Reviewer')
    )
    ProcessCurrentStage = models.ForeignKey(StageKind, on_delete=CASCADE)
    Stage1TryTimes = models.BigIntegerField(default=-1)
    Stage2TryTimes = models.BigIntegerField(default=-1)
    Stage3TryTimes = models.BigIntegerField(default=-1)
    Stage4TryTimes = models.BigIntegerField(default=-1)
    def __str__(self):
        return str(self.id) + ': ' + self.Owner.Name + ': ' + self.Kind.FullName

class ProcessReview(models.Model):
    Process = models.ForeignKey(Process, on_delete=models.CASCADE)
    Reviewer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ': ' + self.Process.Owner.Name + ': ' + self.Process.Kind.FullName + ': ' + self.Reviewer.Name

class Comment(models.Model):
    Process = models.ForeignKey(Process, on_delete=models.CASCADE)
    Stage = models.ForeignKey(StageKind, on_delete=models.CASCADE)
    Writer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    Edited = models.BooleanField(default=False)
    Submited = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + ': ' + self.Process.Owner.Name + ': ' + self.Process.Kind.FullName + ': ' + self.Stage.FullName + ': ' + self.Writer.Name 
