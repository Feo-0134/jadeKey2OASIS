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

class Reviewer(models.Model):
    Alias = models.CharField(max_length=10)
    Name = models.CharField(max_length=20)
    Title = models.ForeignKey(EngineerTitle, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ': ' + self.Name

class Comment(models.Model):
    Stage = models.ForeignKey(StageKind, on_delete=models.CASCADE)
    Writer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    Context = models.TextField()
    Edited = models.BooleanField(default=False)
    Submited = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + ': ' + self.Stage.FullName + ': ' + self.Writer.Name 


class Process(models.Model):
    Kind = models.ForeignKey(ProcessKind, on_delete=models.CASCADE)
    ProcessOwner = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    ProcessReviewer = models.ManyToManyField(
        Reviewer,
        through = 'ProcessReview',
        through_fields = ('Process', 'Reviewer')
    )
    ProcessComments = models.ManyToManyField(
        Comment,
        through = 'ProcessComments',
        through_fields = ('Process', 'Comment')
    )
    ProcessCurrentStage = models.ForeignKey(StageKind, on_delete=models.CASCADE)
    Stage1TryTimes = models.BigIntegerField(default=-1)
    Stage2TryTimes = models.BigIntegerField(default=-1)
    Stage3TryTimes = models.BigIntegerField(default=-1)
    Stage4TryTimes = models.BigIntegerField(default=-1)
    def __str__(self):
        return str(self.id) + ': ' + self.ProcessOwner.Name + ': ' + self.Kind.FullName

class ProcessReview(models.Model):
    Process = models.ForeignKey(Process, on_delete=models.CASCADE)
    Reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ': ' + self.Process.ProcessOwner.Name + ': ' + self.Process.Kind.FullName + ': ' + self.Reviewer.Name

class ProcessComments(models.Model):
    Process = models.ForeignKey(Process, on_delete=models.CASCADE)
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ': ' + self.Process.ProcessOwner.Name + ': ' + self.Process.Kind.FullName + ': ' + self.Comment.Stage.FullName+ ': ' + self.Comment.Writer.Name
