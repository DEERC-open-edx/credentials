# Generated by Django 1.9.12 on 2017-03-15 18:28
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170215_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='enable_linkedin_sharing',
            field=models.BooleanField(default=True, help_text='Enable sharing via LinkedIn', verbose_name='Enable LinkedIn sharing'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='enable_twitter_sharing',
            field=models.BooleanField(default=True, help_text='Enable sharing via Twitter', verbose_name='Enable Twitter sharing'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter_username',
            field=models.CharField(blank=True, help_text='Twitter username included in tweeted credentials. Do NOT include @.', max_length=15, null=True, verbose_name='Twitter Username'),
        ),
    ]
