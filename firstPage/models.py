from django.db import models


# Create your models here.

class Exchange(models.Model):
    class Meta:
        db_table = 'Exchange'

    name = models.CharField(max_length=60, db_column='Exchange')
    index = models.CharField(max_length=5, db_column='INDEX')

    def __str__(self):
        return self.name


class Industry(models.Model):
    class Meta:
        db_table = 'Industry'

    industry_code = models.IntegerField(primary_key=False, db_column='Industry_code')
    industry = models.CharField(primary_key=False, max_length=50, db_column='Industry')

    def __str__(self):
        return self.industry


class Company(models.Model):
    class Meta:
        db_table = 'Company'

    ticker = models.CharField(max_length=10, db_column='Ticker')
    name = models.CharField(max_length=60, db_column='Name')
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE, db_column='Industry CODE'
                                 , blank=True, null=True)
    exchange = models.ForeignKey('Exchange', on_delete=models.CASCADE, db_column='INDEX'
                                 , blank=True, null=True)

    def __str__(self):
        return self.name


class StatementEntries(models.Model):
    class Meta:
        db_table = 'Statement'

    entry_code = models.IntegerField(primary_key=True, db_column='Entry Code')
    statement_title = models.CharField(max_length=25, db_column='Statement Title')

    def __str__(self):
        return self.statement_title


class ItemSetting(models.Model):
    class Meta:
        db_table = 'Item'

    entry_code = models.ForeignKey('StatementEntries', on_delete=models.CASCADE, db_column='Statement Code')
    item_code = models.IntegerField(db_column='Item Code')
    item_order = models.IntegerField(db_column='Order')
    item_description = models.CharField(max_length=255, db_column='Description')
    item_properties = models.CharField(max_length=255, db_column='Properties')
    item_title = models.CharField(max_length=255, db_column='Title')

    def __str__(self):
        return self.item_title


class ItemFact(models.Model):
    class Meta:
        db_table = 'Item Fact'
        unique_together = [['ticker', 'year', 'item_code']]

    item_code = models.ForeignKey('ItemSetting', on_delete=models.CASCADE, db_column='Item Code')
    ticker = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='Ticker')
    year = models.IntegerField(db_column='Year')
    value = models.BigIntegerField(db_column='Value')

    def __str__(self):
        return self.item_code.item_title + str(self.value)


class StockInfo(models.Model):
    class Meta:
        db_table = 'Stock'
        unique_together = [['ticker', 'day']]

    ticker = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='Ticker')
    day = models.DateField(db_column='Date')
    close = models.FloatField(db_column='Close')
    volume = models.IntegerField(db_column='Volume')

    def __str__(self):
        return self.ticker.ticker + str(self.close)


class IndexInfo(models.Model):
    class Meta:
        db_table = 'INDEX'
        unique_together = [['exchange', 'day']]

    exchange = models.ForeignKey('Exchange', on_delete=models.CASCADE, db_column='Ticker')
    day = models.DateField(db_column='Date')
    close = models.FloatField(db_column='Close')
    volume = models.IntegerField(db_column='Volume')

    def __str__(self):
        return self.exchange.index + str(self.close)
