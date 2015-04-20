from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class ScheduledScene(models.Model):

    path = models.CharField(max_length=3)
    row = models.CharField(max_length=3)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'LC8 %s-%s' % (self.path, self.row)

    class Meta:
        verbose_name = _('Scheduled Scene')
        verbose_name_plural = _('Scheduled Scenes')