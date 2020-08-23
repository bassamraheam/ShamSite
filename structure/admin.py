from django.contrib import admin
from .models import Question, News, MotionImage, Adds, Contact, Success, Others, NavBar


admin.site.register(News)
admin.site.register(NavBar)
admin.site.register(Question)
admin.site.register(MotionImage)
admin.site.register(Adds)
admin.site.register(Contact)
admin.site.register(Success)
admin.site.register(Others)

