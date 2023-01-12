from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock(required=True, max_length=400, help_text="maximum charachter limit is 400.")
    image = ImageChooserBlock(required=False)
    button = blocks.PageChooserBlock(required=False)
    # button = blocks.CharBlock(required=False)

    class Meta:
        icon = 'edit'
        label = "Text and banner"


class TitleAndRichTextBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()

    class Meta:
        icon = 'edit'
        label = "Title and Rich text"


class MissionVisionTextBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    image = ImageChooserBlock(required=False)
    description = blocks.RichTextBlock()

    class Meta:
        icon = 'edit'
        label = "Title and Rich text"


class MessageBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    name = blocks.CharBlock(required=True)
    position = blocks.CharBlock(required=False)
    qualification = blocks.CharBlock(required=False)
    message = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock()

    class Meta:
        icon = 'edit'
        label = "Message Text"


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()

    class Meta:
        icon = 'edit'
        label = "Title and text"


class TestimonialBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    qualification = blocks.CharBlock(required=False)
    message = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock()

    class Meta:
        icon = 'edit'