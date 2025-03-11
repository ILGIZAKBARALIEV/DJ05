from django.contrib import admin
from .models import MoviesModel
from .models import DirectorModel
from .models import ReviewModel

admin.site.register(MoviesModel)
admin.site.register(DirectorModel)
admin.site.register(ReviewModel)

