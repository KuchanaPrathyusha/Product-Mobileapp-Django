# Generated by Django 3.2.7 on 2021-09-30 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('veg', 'Veg'), ('non veg', 'NV')], default='non veg', max_length=8)),
                ('catg', models.CharField(choices=[('dessert', 'Dessert'), ('snack', 'Snack'), ('food', 'Food')], default='food', max_length=8)),
                ('slug', models.SlugField(max_length=30, unique_for_date='publish')),
                ('desc', models.TextField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='cuisine_pic')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuisine_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
