from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    YEAR_CHOICES = [
        ('B1', 'Bachelor Year 1'),
        ('B2', 'Bachelor Year 2'),
        ('B3', 'Bachelor Year 3'),
        ('M1', 'Master Year 1'),
        ('M2', 'Master Year 2'),
    ]
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_year_display()})"

class Summary(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='summaries/')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='summaries')

    def __str__(self):
        return self.name

    @property
    def rating(self):
        votes = self.votes.aggregate(upvotes=Count('id', filter=models.Q(upvoted=True)),
                                     downvotes=Count('id', filter=models.Q(upvoted=False)))
        return votes['upvotes'] - votes['downvotes']
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE, related_name='votes')
    upvoted = models.BooleanField(default=True)  # True for upvote, False for downvote

    class Meta:
        unique_together = ('user', 'summary')  # Ensures one vote per user per summary

    def __str__(self):
        vote_type = "Upvote" if self.upvoted else "Downvote"
        return f"{vote_type} by {self.user.username} on {self.summary.name}"


# Extending User model
User.add_to_class('faculty', models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True))
