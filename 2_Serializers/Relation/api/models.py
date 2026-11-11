from django.db import models

# many (songs) to one (singer)
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song') # related name is useful when accessing fk column directly in parent model
    duration = models.IntegerField()
    

    def __str__(self):
        return self.title