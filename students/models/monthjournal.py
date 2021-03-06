from django.utils.translation import ugettext_lazy as _
from django.db import models
class MonthJournal(models.Model):
  
    class Meta:
      verbose_name = _(u'Monthly journal')
      verbose_name_plural = _(u'Monthly journals')
      
    student = models.ForeignKey('Student',
      verbose_name=_(u'Student'),
      blank=False,
      unique_for_month='date')
    date = models.DateField(
      verbose_name=_(u'Date'),
      blank=False)
    local_vars = locals()
    for num in range(1, 32):
      local_vars.update({'present_day'+str(num) : models.BooleanField(default=False)})
   
    def __unicode__(self):
      return u'%s: %d, %d' % (self.student.last_name, self.date.month,
        self.date.year)














