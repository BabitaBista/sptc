# Generated by Django 4.1.4 on 2023-01-11 11:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0006_homepage_testimonial_homepage_testimonial_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner', wagtail.fields.StreamField([('banner', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock(help_text='maximum charachter limit is 400.', max_length=400, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button', wagtail.blocks.PageChooserBlock(required=False))]))], blank=True, null=True, use_json_field=None)),
                ('about_company', wagtail.fields.StreamField([('about_company', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock())]))], blank=True, null=True, use_json_field=None)),
                ('mission_vision', wagtail.fields.StreamField([('mission_vision', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('description', wagtail.blocks.RichTextBlock())]))], blank=True, null=True, use_json_field=None)),
                ('chairman_message', wagtail.fields.StreamField([('chairman_message', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('name', wagtail.blocks.CharBlock(required=True)), ('position', wagtail.blocks.CharBlock(required=False)), ('qualification', wagtail.blocks.CharBlock(required=False)), ('message', wagtail.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True, use_json_field=None)),
                ('team_text', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
