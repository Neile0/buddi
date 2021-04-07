import django_filters
from .models import Ad, SitterOperatesInRegion

class AdFilter(django_filters.FilterSet):
    
    class Meta:
        model = Ad
        fields = ('type',)
        
    def ad_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
            })
    
"""
class SitterFilter(django_filters.FilterSet):
    
    class Meta:
        model = SitterOperatesInRegion
        fields=('sitter', 'region',)
        
    def sitter_filter(self, queryset, name, value):
        return queryset.filter9**{
            }
"""