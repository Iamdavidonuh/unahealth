from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from records.models import UserGlucoseLevels

# Create your tests here.


class TestModel(TestCase):
    @staticmethod
    def get_payload():
        payload = {
            "user_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            "device": "FreeStyle LibreLink",
            "serial_number": "006A3043-6E08-4C19-B3F1-B0D95C5737CA",
            "device_timestamp": "2021-02-18T11:19:00",
            "recording_type": "0",
            "glucose_history": "97",
            "glucose_scan": "",
            "non_numeric_rapid_testing_insulin": "",
            "rapid_acting_insulin_units": "",
            "non_numeric_nutritional_data": "",
            "carbohydrate_grams": "",
            "carbohydrate_servings": "",
            "non_numeric_sustained_release_insulin": "",
            "depot_insulin_units": "",
            "notes": "",
            "glucose_test_strips": "",
            "ketone": "",
            "meal_insulin_units": "",
            "correction_insulin_units": "",
            "insulin_change_by_user_units": "",
        }
        return payload

    def test_create_user_glucose_levels_model(self):

        payload = self.get_payload()
        model_object = UserGlucoseLevels.objects.create(**payload)
        self.assertEqual(model_object.user_id, payload["user_id"])
        query = UserGlucoseLevels.objects.filter(user_id=payload["user_id"])
        self.assertIsNotNone(query)


class TestAPIEndpoints(APITestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.client = APIClient()
        super().__init__(methodName)

    def test_list_user_records(self):
        pass
