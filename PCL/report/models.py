from django.db import models

# from django.utils.timezone import now


from smart_selects.db_fields import ChainedManyToManyField
from master_table.models import FundamentalProductType,\
    FPMiddleCat, FPLowerCat, FPItem, Shift, Customer, Deport


class Report(models.Model):

    start_time = models.DateField()
    end_time = models.DateField()

    deport = models.ForeignKey(Deport, blank=True, null=True)
    customer = models.ManyToManyField(Customer, blank=True)
    fundamental_type = models.ManyToManyField(
        FundamentalProductType, blank=True)
    middle_category_type = models.ManyToManyField(FPMiddleCat, blank=True)
    lower_category_type = models.ManyToManyField(FPLowerCat, blank=True)
    fp_item = models.ManyToManyField(FPItem, blank=True)


    @property
    def get_customer(self):
        if(self.customer):
            return self.customer.first()
        return None