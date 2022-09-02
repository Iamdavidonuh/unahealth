from pyexpat import model
from django.db import models

# Create your models here.


class UserGlucoseLevels(models.Model):

    user_id = models.CharField(max_length=50, blank=False, null=False)
    device = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    device_timestamp = models.DateTimeField()
    recording_type = models.CharField("Recording Type", max_length=10)
    glucose_history = models.CharField("Glucose History mg/dL", max_length=10)
    glucose_scan = models.CharField("Glucose Scan mg/dL", max_length=10)
    non_numeric_rapid_testing_insulin = models.CharField(
        "Non-Numeric Rapid-Acting Insulin", max_length=15
    )
    rapid_acting_insulin_units = models.CharField(
        "Rapid-Acting Insulin (Units)", max_length=15
    )
    non_numeric_nutritional_data = models.CharField(
        "Non-Numeric Nutritional Data", max_length=15
    )
    carbohydrate_grams = models.CharField("Carbohydrate (Grams)", max_length=15)
    carbohydrate_servings = models.CharField("Carbohydrate (Servings)", max_length=15)
    non_numeric_sustained_release_insulin = models.CharField(
        "Non-Numeric Sustained-Release Insulin", max_length=15
    )
    depot_insulin_units = models.CharField("Depot insulin (units)", max_length=15)
    notes = models.CharField("Notes", max_length=15)
    glucose_test_strips = models.CharField("glucose test strips mg/dL", max_length=15)
    ketone = models.CharField("ketone mmol/L", max_length=15)
    meal_insulin_units = models.CharField("meal insulin (units)", max_length=15)
    correction_insulin_units = models.CharField(
        "correction insulin (units)", max_length=15
    )
    insulin_change_by_user_units = models.CharField(
        "insulin change by user (units)", max_length=15
    )
