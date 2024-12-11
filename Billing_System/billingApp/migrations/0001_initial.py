# Generated by Django 4.2.9 on 2024-12-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BillInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_email", models.EmailField(max_length=254)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Billinfo",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("product_id", models.CharField(max_length=100, unique=True)),
                ("available_stocks", models.PositiveIntegerField()),
                ("unit_price", models.FloatField()),
                ("tax_percentage", models.FloatField()),
            ],
            options={
                "db_table": "Product",
            },
        ),
        migrations.CreateModel(
            name="Denomination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("denomination_2000", models.IntegerField(default=0)),
                ("denomination_500", models.IntegerField(default=0)),
                ("denomination_200", models.IntegerField(default=0)),
                ("denomination_100", models.IntegerField(default=0)),
                ("denomination_50", models.IntegerField(default=0)),
                ("denomination_20", models.IntegerField(default=0)),
                ("denomination_10", models.IntegerField(default=0)),
                ("denomination_5", models.IntegerField(default=0)),
                ("denomination_2", models.IntegerField(default=0)),
                ("denomination_1", models.IntegerField(default=0)),
                ("cashPaidbyCustomer", models.IntegerField(default=0)),
                (
                    "billno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billingApp.billinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BillDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "billno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billingApp.billinfo",
                    ),
                ),
                (
                    "product_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billingApp.product",
                    ),
                ),
            ],
        ),
    ]