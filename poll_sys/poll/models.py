from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Poll {self.title}"

class Question(models.Model):
    label = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question {self.label} - {self.poll} "


class Option(models.Model):
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Option {self.label}"


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.question.label} - {self.option.label}"


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Participant " + self.name + " - " + self.email


class PollParticipant(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="participants")
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="polls")
    has_submitted = models.BooleanField(default=False)
    is_emailed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.participant.name} - {self.poll.title}"


class Vote(models.Model):
    poll_participant = models.ForeignKey(PollParticipant, on_delete=models.CASCADE, related_name="votes") 
    question_option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE, related_name="votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('question_option', 'poll_participant')
        

    def __str__(self):
        return f"{self.participant.name} voted for {self.question_option.option.label}"
