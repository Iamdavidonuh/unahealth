# Generated by Django 4.1 on 2022-09-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserGlucoseLevels",
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
                ("user_id", models.CharField(max_length=50)),
                ("device", models.CharField(max_length=50)),
                ("serial_number", models.CharField(max_length=100)),
                ("device_timestamp", models.DateTimeField()),
                (
                    "recording_type",
                    models.CharField(max_length=10, verbose_name="Recording Type"),
                ),
                (
                    "glucose_history",
                    models.CharField(
                        max_length=10, verbose_name="Glucose History mg/dL"
                    ),
                ),
                (
                    "glucose_scan",
                    models.CharField(max_length=10, verbose_name="Glucose Scan mg/dL"),
                ),
                (
                    "non_numeric_rapid_testing_insulin",
                    models.CharField(
                        max_length=15, verbose_name="Non-Numeric Rapid-Acting Insulin"
                    ),
                ),
                (
                    "rapid_acting_insulin_units",
                    models.CharField(
                        max_length=15, verbose_name="Rapid-Acting Insulin (Units)"
                    ),
                ),
                (
                    "non_numeric_nutritional_data",
                    models.CharField(
                        max_length=15, verbose_name="Non-Numeric Nutritional Data"
                    ),
                ),
                (
                    "carbohydrate_grams",
                    models.CharField(
                        max_length=15, verbose_name="Carbohydrate (Grams)"
                    ),
                ),
                (
                    "carbohydrate_servings",
                    models.CharField(
                        max_length=15, verbose_name="Carbohydrate (Servings)"
                    ),
                ),
                (
                    "non_numeric_sustained_release_insulin",
                    models.CharField(
                        max_length=15,
                        verbose_name="Non-Numeric Sustained-Release Insulin",
                    ),
                ),
                (
                    "depot_insulin_units",
                    models.CharField(
                        max_length=15, verbose_name="Depot insulin (units)"
                    ),
                ),
                ("notes", models.CharField(max_length=15, verbose_name="Notes")),
                (
                    "glucose_test_strips",
                    models.CharField(
                        max_length=15, verbose_name="glucose test strips mg/dL"
                    ),
                ),
                (
                    "ketone",
                    models.CharField(max_length=15, verbose_name="ketone mmol/L"),
                ),
                (
                    "meal_insulin_units",
                    models.CharField(
                        max_length=15, verbose_name="meal insulin (units)"
                    ),
                ),
                (
                    "correction_insulin_units",
                    models.CharField(
                        max_length=15, verbose_name="correction insulin (units)"
                    ),
                ),
                (
                    "insulin_change_by_user_units",
                    models.CharField(
                        max_length=15, verbose_name="insulin change by user (units)"
                    ),
                ),
            ],
        ),
    ]
