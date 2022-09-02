import os
from os import listdir
import csv
from dateutil import parser
from django.core.management.base import BaseCommand
from django.conf import settings
import pandas as pd
from records.models import UserGlucoseLevels
from records.utils import CSV_HEADERS, NameNormalizer


class Command(BaseCommand):
    help = "Loads csv files into userglucoselevels model"

    def handle(self, *args, **options):
        sample_records = [
            f
            for f in listdir(settings.SAMPLE_CSV_DATA)
            if os.path.isfile(os.path.join(settings.SAMPLE_CSV_DATA, f))
        ]
        name_normalizer = NameNormalizer()
        for data in sample_records:
            with open(os.path.join(settings.SAMPLE_CSV_DATA, data), "r") as csv_file:
                df = pd.read_csv(csv_file, header=None, names=CSV_HEADERS)

                for _, row in df.iterrows():
                    UserGlucoseLevels.objects.create(
                        user_id=csv_file.name,
                        device=row[name_normalizer.get_field_name_german("device")],
                        serial_number=row[
                            name_normalizer.get_field_name_german("serial_number")
                        ],
                        device_timestamp=parser.parse(
                            row[
                                name_normalizer.get_field_name_german(
                                    "device_timestamp"
                                )
                            ]
                        ),
                        recording_type=row[
                            name_normalizer.get_field_name_german("recording_type")
                        ],
                        glucose_history=row[
                            name_normalizer.get_field_name_german("glucose_history")
                        ],
                        glucose_scan=row[
                            name_normalizer.get_field_name_german("glucose_scan")
                        ],
                        non_numeric_rapid_testing_insulin=row[
                            name_normalizer.get_field_name_german(
                                "non_numeric_rapid_testing_insulin"
                            )
                        ],
                        rapid_acting_insulin_units=row[
                            name_normalizer.get_field_name_german(
                                "rapid_acting_insulin_units"
                            )
                        ],
                        non_numeric_nutritional_data=row[
                            name_normalizer.get_field_name_german(
                                "non_numeric_nutritional_data"
                            )
                        ],
                        carbohydrate_grams=row[
                            name_normalizer.get_field_name_german("carbohydrate_grams")
                        ],
                        carbohydrate_servings=row[
                            name_normalizer.get_field_name_german(
                                "carbohydrate_servings"
                            )
                        ],
                        non_numeric_sustained_release_insulin=row[
                            name_normalizer.get_field_name_german(
                                "non_numeric_sustained_release_insulin"
                            )
                        ],
                        depot_insulin_units=row[
                            name_normalizer.get_field_name_german("depot_insulin_units")
                        ],
                        notes=row[name_normalizer.get_field_name_german("notes")],
                        glucose_test_strips=row[
                            name_normalizer.get_field_name_german("glucose_test_strips")
                        ],
                        ketone=row[name_normalizer.get_field_name_german("ketone")],
                        meal_insulin_units=row[
                            name_normalizer.get_field_name_german("meal_insulin_units")
                        ],
                        correction_insulin_units=row[
                            name_normalizer.get_field_name_german(
                                "correction_insulin_units"
                            )
                        ],
                        insulin_change_by_user_units=row[
                            name_normalizer.get_field_name_german(
                                "insulin_change_by_user_units"
                            )
                        ],
                    )
            self.stdout.write(
                self.style.SUCCESS('Successfully CSV file "%s" into DB ' % data)
            )
