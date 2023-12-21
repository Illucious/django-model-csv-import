from import_export import resources
from .models import Phones


class PhonesResource(resources.ModelResource):
    class Meta:
        model = Phones