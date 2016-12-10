from django.db import models

# from django.utils.timezone import now

# from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedManyToManyField
from master_table.models import FundamentalProductType,\
    FPMiddleCat, FPLowerCat, FPItem, Shift


class FinishedProductReport(models.Model):
    name = models.CharField(max_length=100)
    # compound_production_item = models.ForeignKey(CompoundProductionItem)
    # fundamental_type = models.ForeignKey(FundamentalProductType)
    fundamental_type = models.ManyToManyField(FundamentalProductType)

    # middle_category_type = models.ForeignKey(FPMiddleCat)
    # middle_category_type = ChainedForeignKey(
    #     FPMiddleCat,
    #     chained_field="fundamental_type",
    #     chained_model_field="fundamental_type",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True
    # )
    middle_category_type = ChainedManyToManyField(
        FPMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        # show_all=False,
        # auto_choose=True,
        # sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedManyToManyField(
        FPLowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        # show_all=False,
        auto_choose=True,
        # sort=True
    )
    # production_item = models.ForeignKey(FinishedProductItem)
    finished_production_item = ChainedManyToManyField(
        FPItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        # show_all=False,
        auto_choose=True,
        # sort=True
    )
    finished_production_item = ChainedManyToManyField(
        FPItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        # show_all=False,
        auto_choose=True,
        # sort=True
    )
    # shift = models.ForeignKey(Shift, blank=True, null=True)
    shift = models.ManyToManyField(Shift, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # unit_amount = models.FloatField()

    def __str__(self):
        return self.name
