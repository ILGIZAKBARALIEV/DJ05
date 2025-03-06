from django.db import models

class DirectorModel(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'


class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(DirectorModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'




class ReviewModel(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'