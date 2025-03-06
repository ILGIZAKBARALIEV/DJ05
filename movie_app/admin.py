from django.contrib import admin
from .models import MovieModel
from .models import DirectorModel
from .models import ReviewModel

admin.site.register(MovieModel)
admin.site.register(DirectorModel)
admin.site.register(ReviewModel)
