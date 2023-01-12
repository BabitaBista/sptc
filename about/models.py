from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField
from wagtail.models import Page

from home.blocks import BannerBlock, TitleAndRichTextBlock, MissionVisionTextBlock, MessageBlock


class AboutPage(Page):
    max_count = 1
    banner = StreamField(StreamBlock([('banner', BannerBlock())], max_num=1, required=False), null=True, blank=True, use_json_field=True,)
    about_company = StreamField(StreamBlock([('about_company', TitleAndRichTextBlock())], max_num=1, required=False, ),
                                null=True, blank=True, use_json_field=True)
    mission_vision = StreamField(StreamBlock([('mission_vision', MissionVisionTextBlock())], max_num=1, required=False),
                                 null=True, blank=True, use_json_field=True)
    chairman_message = StreamField(StreamBlock([('chairman_message', MessageBlock())], max_num=1, required=False),
                                   null=True, blank=True, use_json_field=True)
    team_text = models.CharField(max_length=256, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner'),
        FieldPanel('about_company'),
        FieldPanel('mission_vision'),
        FieldPanel('chairman_message'),
        FieldPanel('team_text')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['teams'] = OurTeam.objects.filter(is_active=True)
        return context


class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linked_in = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('is_active'),
        FieldPanel('priority'),
        FieldPanel('description'),
        FieldPanel('facebook'),
        FieldPanel('instagram'),
        FieldPanel('twitter'),
        FieldPanel('linked_in'),
        FieldPanel('whatsapp'),
        FieldPanel('image'),
    ]

    class Meta:
        ordering = ('priority',)

    def __str__(self):
        return self.name