from django.db import models

class DirectorModel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'





class MoviesModel(models.Model):
    title = models.CharField(max_length=100)
    movies_count = models.IntegerField(default=5, null=True , blank=True )
    description = models.TextField()
    reviews_count = models.IntegerField(default=5)
    duration = models.IntegerField(null=True , blank=True)
    rating = models.FloatField(null=True , blank=True)
    director = models.ForeignKey(DirectorModel, on_delete=models.CASCADE,related_name='movies',null=True,blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

STARS = (
    (star,'*'*star) for star in range(1,6)
)


class ReviewModel(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, default=5, null=True , blank=True)
    movies = models.ForeignKey(MoviesModel, on_delete=models.CASCADE,related_name='reviews')
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
