from django.db import models
from wagtail.blocks import StreamBlock

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel

from home.blocks import BannerBlock, TestimonialBlock, TitleAndRichTextBlock, MissionVisionTextBlock, MessageBlock


class HomePage(Page):
    banner = StreamField(StreamBlock([('banner', BannerBlock())], max_num=1, required=False), use_json_field=True,
                         null=True, blank=True)
    testimonial_text = models.CharField(max_length=256, null=True, blank=True)
    testimonial = StreamField(StreamBlock([('testimonial', TestimonialBlock())], max_num=10, required=False), null=True,
                              blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner'),
        FieldPanel('testimonial_text'),
        FieldPanel('testimonial'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        from about.models import AboutPage
        context['about'] = AboutPage.objects.all()
        return context

