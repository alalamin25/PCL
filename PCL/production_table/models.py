from django.db import models
from django.utils.timezone import now
from master_table.models import ProductionItem, Shift, CompoundProductionItem


class ProductionEntry(models.Model):

    production_item = models.ForeignKey(ProductionItem, blank=True, null=True)
    compound_production_item = models.ForeignKey(CompoundProductionItem, blank=True, null=True)
    shift = models.ForeignKey(Shift)
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100)
    comment = models.TextField()

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.production_item.name
