# Generated by Django 4.2 on 2023-04-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('qid', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=50)),
                ('similar_answer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('appearance_date', models.DateField()),
                ('small_category', models.CharField(max_length=50)),
                ('big_category', models.CharField(max_length=50)),
                ('note', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
