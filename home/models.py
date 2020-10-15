from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.translation import gettext_lazy as _


class HomePage(Page):
    max_count = 1

    banner_title = models.CharField(
        max_length=100, blank=False, null=True, verbose_name=_("banner title")
    )
    banner_subtitle = RichTextField(
        features=["bold", "italic"], verbose_name=_("banner subtitle")
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("banner image"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
    ]

    class Meta:

        verbose_name = _("alignment")
        verbose_name_plural = _("alignments")
