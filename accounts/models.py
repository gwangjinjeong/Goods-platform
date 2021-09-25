from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def user_path(instance, filename):
    #포토의 이름 파일 이름을 받아온다.
    from random import choice #난수발생기
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)] #대소문자 구분없이 가져오겠다.
    pid = ''.join(arr)
    extension = filename.split('.')[-1] # 사진. jpg라고 하면, .자르고 jpg만 가져옴
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, #장고에서 사용자 정보를 건드릴수잇는함수
                               on_delete=models.CASCADE)  # 1:1로 on_delete를 통해서 지우면 다같이 지워지게
    nickname = models.CharField('별명', max_length=20, unique=True)
    
    picture = ProcessedImageField(upload_to=user_path,
                                  processors = [ResizeToFill(150,150)],
                                  format='JPEG',
                                  options={'qulity': 90},
                                  blank = True # 사진 안넣어도 되니!
                                 )
    
    about = models.CharField(max_length = 300, blank=True) # blank로 비워도 된다.
    
    GENDER = (
        ('선택안함','선택안함'),
        ('남성','남성'),
        ('여성','여성')
    )
    
    gender = models.CharField('성별(선택사항)',
                             max_length = 10,
                             choices = GENDER) # choices 옵션을 통해서 선택