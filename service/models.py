from django.db import models
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page

from home.blocks import TitleAndTextBlock


class ServiceModel(models.Model):
    is_popular = models.BooleanField(default=False)
    content = RichTextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    slug = models.SlugField(blank=True, null=True)

    panels = [
        FieldPanel('is_popular'),
        FieldPanel('content'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        import random
        import string
        from django.template.defaultfilters import slugify
        if not self.slug:
            slug = slugify(self.name[:30])
            while ServiceModel.objects.filter(slug=slug).exists():
                slug = slugify(self.name[:30]) + '-' + ''.join(random.choices(string.ascii_uppercase, k=5))
            self.slug = slug
        super(ServiceModel, self).save(*args, **kwargs)


class ServicePage(Page):
    service_text = StreamField(StreamBlock([('event_text', TitleAndTextBlock())], max_num=6, required=False),
                               null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('service_text'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['services'] = ServiceModel.filter(is_popular=True)[:2]
        return context
