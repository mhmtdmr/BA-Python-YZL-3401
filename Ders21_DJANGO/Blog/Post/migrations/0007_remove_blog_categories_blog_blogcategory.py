# Generated by Django 4.0.3 on 2022-04-02 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_blog_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Categories',
        ),
        migrations.AddField(
            model_name='blog',
            name='BlogCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Post.category'),
        ),
    ]