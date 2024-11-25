from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.text} (Valor: {self.value})"

class QuestionnaireResponse(models.Model):
    id = models.AutoField(primary_key=True)  
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)  
    class_group = models.ForeignKey('users.Class', on_delete=models.CASCADE)  
    answers  = models.JSONField()  
    feedback = models.TextField(blank=True, null=True)  
    total_score = models.DecimalField(max_digits=5, decimal_places=2)  

    class Meta:
        unique_together  = ('student', 'class_group')  

    def __str__(self):
        return f"Resposta {self.id} - Aluno: {self.student}, Turma: {self.class_group.id}"

