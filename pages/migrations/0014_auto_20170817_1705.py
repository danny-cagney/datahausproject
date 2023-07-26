# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('pages', '0013_videopage_videopagecarouselitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGalleryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='VideoPageCarouselItem',
            new_name='VideoGalleryPageCarouselItem',
        ),
        migrations.RemoveField(
            model_name='videopage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='videopage',
            name='page_ptr',
        ),
        migrations.AlterField(
            model_name='videogallerypagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_items', to='pages.VideoGalleryPage'),
        ),
        migrations.DeleteModel(
            name='VideoPage',
        ),
    ]
