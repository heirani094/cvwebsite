# myapp/templatetags/custom_filters.py

from django import template
import jdatetime

register = template.Library()


@register.filter
def to_jalali(date):
    if not date:
        return ''
    jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
    return jalali_date.strftime('%Y/%m/%d')
