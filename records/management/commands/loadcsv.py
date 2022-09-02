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
        for data in sample_records:
            with open(os.path.join(settings.SAMPLE_CSV_DATA, data), "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                # the below statement will skip the two lines
                next(csv_reader)
                next(csv_reader)
                user_id = os.path.splitext(data)[0]
                for lines in csv_reader:
                    UserGlucoseLevels.objects.create(
                        user_id=user_id,
                        device=lines[0],
                        serial_number=lines[1],
                        device_timestamp=parser.parse(lines[2]),
                        recording_type=lines[3],
                        glucose_history=lines[4],
                        glucose_scan=lines[5],
                        non_numeric_rapid_testing_insulin=lines[6],
                        rapid_acting_insulin_units=lines[7],
                        non_numeric_nutritional_data=lines[8],
                        carbohydrate_grams=lines[9],
                        carbohydrate_servings=lines[10],
                        non_numeric_sustained_release_insulin=lines[11],
                        depot_insulin_units=lines[12],
                        notes=lines[13],
                        glucose_test_strips=lines[14],
                        ketone=lines[15],
                        meal_insulin_units=lines[16],
                        correction_insulin_units=lines[17],
                        insulin_change_by_user_units=lines[18],
                    )
            self.stdout.write(
                self.style.SUCCESS('Successfully CSV file "%s" into DB ' % data)
            )
