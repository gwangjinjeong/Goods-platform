from django.contrib import admin
from .models import Profile

# Register your models here.
# 위에 어떤 기능 혹은 모델을 불러오고 아래에 작성하는 형식으로 

#데코레이터로 만들기
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user']
    list_display_links = ['nickname', 'user']
    search_fields = ['nickname']