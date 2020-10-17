from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    max_count = 1

    banner_title = models.CharField(
        max_length=100, blank=False, null=True, verbose_name=_("banner title")
    )
    banner_subtitle = RichTextField(
        features=["bold", "italic"],
        verbose_name=_("banner subtitle"),
        null=True,
        blank=False,
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(
            {
                "categories": dict(settings.CATEGORY_CHOICES).values(),
            }
        )
        return context
