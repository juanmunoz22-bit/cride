# Generated by Django 2.0.10 on 2021-12-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Datetime when object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Datetime when object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=140, verbose_name='circle name')),
                ('slug_name', models.SlugField(max_length=40, unique=True)),
                ('about', models.CharField(max_length=255, verbose_name='circle description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='circles/pictures/')),
                ('rides_offered', models.PositiveIntegerField(default=0)),
                ('rides_taken', models.PositiveIntegerField(default=0)),
                ('verified', models.BooleanField(default=False, help_text='Verified circles are also known as official communities', verbose_name='verified circle')),
                ('is_public', models.BooleanField(default=True, help_text='To concrete if a circle is public and everyone can see it and to ask for join', verbose_name='public cicle')),
                ('is_limited', models.BooleanField(default=False, help_text='Limited circles can grow up to a fixed number of members', verbose_name='limited')),
                ('members_limit', models.PositiveIntegerField(default=0, help_text='If circle is limited. This number will be the fixed limit the users select')),
            ],
            options={
                'ordering': ['-rides_taken', '-rides_offered'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]