# Generated by Django 4.2 on 2023-04-26 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hobt_dict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobtdict',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_hobtdict', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hobtdict',
            name='like',
            field=models.ManyToManyField(related_name='liker_hobtdict', to=settings.AUTH_USER_MODEL),
        ),
    ]