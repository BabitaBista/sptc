from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page

from home.blocks import TitleAndTextBlock


class EventModel(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=255)
    datetime_created = models.DateTimeField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('title'),
        FieldPanel('address'),
        FieldPanel('date'),
        FieldPanel('time'),
        FieldPanel('image'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from django.template.defaultfilters import slugify
        if not self.slug:
            slug = slugify(self.title[:30])
            self.slug = slug
        super(EventModel, self).save(*args, **kwargs)


class EventPage(Page):
    max_count = 1
    event_text = StreamField(StreamBlock([('event_text', TitleAndTextBlock())], max_num=6, required=False),
                             null=True, blank=True, use_json_field=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('event_text')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['populars'] = EventModel.objects.filter(is_popular=True)[:2]
        context['events'] = EventModel.objects.all()
        return context