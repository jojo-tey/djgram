import os
import uuid

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# 메타 = 클래스의 클래스 같은 개념 / 모델 객체의 이름 / 관리자화면 등에 표시됨
    class Meta:
        abstract = True


class Content(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')

    # 최신 포스팅 먼저 가져오기
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "contents"


def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(instance.UPLOAD_PATH, "%s.%s" % (uuid.uuid4(), ext))
    # uuid.uuid4() : 파일의 16자리 고유한 아이디 생성


class Image(BaseModel):
    UPLOAD_PATH = 'user-upload'

    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)
    order = models.SmallIntegerField()  # image numbering

    class Meta:
        unique_together = ['content', 'order']
        ordering = ['order']


class FollowRelation(BaseModel):
    follower = models.OneToOneField(User, on_delete=models.CASCADE)
    # 팔로우는 여러사람이 서로 팔로우 할수 있으므로 manytomany
    followee = models.ManyToManyField(User, related_name='followee')
