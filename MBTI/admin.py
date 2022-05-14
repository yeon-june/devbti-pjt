from django.contrib import admin
from .models import Question, Mbti, BaseInfo, Howto

# Register your models here.
admin.site.register(Question)
admin.site.register(Mbti)
admin.site.register(BaseInfo)
admin.site.register(Howto)