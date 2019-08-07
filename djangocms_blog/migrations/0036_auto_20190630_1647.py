# Generated by Django 2.1.9 on 2019-06-30 14:47

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('djangocms_blog', '0035_posttranslation_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', slotname='media', to='cms.Placeholder'),
        ),
        migrations.AlterField(
            model_name='authorentriesplugin',
            name='authors',
            field=models.ManyToManyField(limit_choices_to={'djangocms_blog_post_author__publish': True}, to=settings.AUTH_USER_MODEL, verbose_name='authors'),
        ),
        migrations.AlterField(
            model_name='latestpostsplugin',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Show only the blog articles tagged with chosen tags.', related_name='djangocms_blog_latest_post', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='filter by tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='djangocms_blog_tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]