# Generated by Django 4.2.2 on 2023-07-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0017_alter_shopreport_report_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_price_id',
            field=models.CharField(default='Default'),
        ),
        migrations.AddField(
            model_name='product',
            name='stripe_product_id',
            field=models.CharField(default='Default'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]