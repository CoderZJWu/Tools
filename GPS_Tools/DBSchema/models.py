from django.db import models

# Create your models here.
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=30,unique=True)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=18)
    is_delete = models.BooleanField(default=False)

#
# 数据迁移
# 将模型映射到数据库的过程
# 生成迁移文件: python manage.py makemigration
# 执行迁移: python manage.py migrate
#