import django_filters
from .models import Ad

class AdFilter(django_filters.FilterSet):
    
    class Meta:
        model = Ad
        fields = ('type',)
        
    def ad_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
            })
    
