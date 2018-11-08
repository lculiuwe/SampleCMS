from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# 文章类型类
class Category(models.Model):
    name = models.CharField(verbose_name='文章类型',max_length=200)
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField(verbose_name='最后修改时间',auto_now=True)

    # 用于后台显示中文标签
    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    # 用于后台显示中文标签
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs={'pk':self.pk})

# 标签类
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名称',max_length=100)

    # 用于后台显示中文标签
    class Meta:
        verbose_name = '标签名称'
        verbose_name_plural = verbose_name

    # 用于后台显示中文标签
    def __str__(self):
        return self.name


# 文章类
class Article(models.Model):

    STATUS_CHOICES=(
        ('d','Draft'),
        ('p','Published'),
    )

    title = models.CharField(verbose_name='文章标题',max_length=80)
    content = RichTextUploadingField(verbose_name='文章内容')
    author = models.ForeignKey(User,verbose_name='作者',on_delete=models.SET_NULL,null=True)
    abstract = models.CharField(verbose_name='文章摘要',max_length=60,blank=True,null=True,help_text='可选,如果为空则选取文章内容的前60个字符！')
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    views = models.PositiveIntegerField(verbose_name='浏览量',default=0)
    likes = models.PositiveIntegerField(verbose_name='点赞数',default=0)
    topped = models.BooleanField(verbose_name='是否置顶',default=False)
    status = models.CharField(verbose_name='文章状态',max_length=1,choices=STATUS_CHOICES)
    category = models.ForeignKey(Category,verbose_name='文章分类',on_delete=models.SET_NULL,null=True,default='无分类')
    tags = models.ManyToManyField(Tag,verbose_name='文章标签',blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


    def __unicode__(self):
        return self.title

    # 显示中文名称
    def __str__(self):
        return self.title

    # 生成详情页链接
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    # 记录访问量
    def views_add(self):
        self.views += 1
        self.save(update_fields=['views'])  #只更新views的值，以提高效率

    # 定义颜色显示，用于Admin后台管理，显示发布状态
    # def colored_name(self,color_code):
    #     return format_html(
    #         '<span style="color: #{};">{}</span>',
    #         self.status,
    #         color_code,
    #
    #     )

# 广告图片/轮播图
class AdImages(models.Model):
    title = models.CharField(verbose_name = '广告标题',max_length = 100)
    image = models.ImageField(verbose_name='广告图片',upload_to ='ad_images',null = True,blank = True,max_length = 100)
    url = models.URLField(verbose_name='链接地址',max_length=200,help_text='可以为本站URL地址或者外部网站地址！')
    index = models.IntegerField(verbose_name='顺序',default=1)
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)

    class Meta:
        verbose_name = '广告轮播图'
        verbose_name_plural = verbose_name
