from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# 语法分析器
LEXERS = [item for item in get_all_lexers() if item[1]]
# 语言选择器
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# 风格选择器
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# print(LEXERS)
class Snippet(models.Model):
    class Meta:
        ordering = ('created',)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100, default='python')
    style = models.CharField(choices=STYLE_CHOICES, max_length=100, default='friendly')
