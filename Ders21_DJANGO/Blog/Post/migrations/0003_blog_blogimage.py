# Generated by Django 4.0.3 on 2022-03-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_blog_blogpublishdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='BlogImage',
            field=models.ImageField(blank=True, default='NULL', upload_to="{% static 'images/post/' %}"),
        ),
    ]
