# Generated by Django 2.0.6 on 2018-06-10 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_main', '0003_auto_20180610_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签名称', 'verbose_name_plural': '标签名称'},
        ),
    ]
