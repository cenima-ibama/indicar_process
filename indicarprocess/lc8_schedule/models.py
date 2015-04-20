from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext, ugettext_lazy as _


class ScheduledScene(models.Model):

    path = models.CharField(max_length=3)
    row = models.CharField(max_length=3)
    creation_date = models.DateField(auto_now_add=True)
    last_date = models.DateField(_('Last Download Date'), null=True, blank=True)

    def __str__(self):
        return 'LC8 %s-%s' % (self.path, self.row)

    def clean(self):
        self.clean_fields()
        try:
            ScheduledScene.objects.get(path=self.path, row=self.row)
            raise ValidationError(
                _('There is already a scheduled scene with this path and row.')
                )
        except self.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ScheduledScene, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Scheduled Scene')
        verbose_name_plural = _('Scheduled Scenes')