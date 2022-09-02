CSV_HEADERS = "Gerät,Seriennummer,Gerätezeitstempel,Aufzeichnungstyp,Glukosewert-Verlauf mg/dL,Glukose-Scan mg/dL,Nicht numerisches schnellwirkendes Insulin,Schnellwirkendes Insulin (Einheiten),Nicht numerische Nahrungsdaten,Kohlenhydrate (Gramm),Kohlenhydrate (Portionen),Nicht numerisches Depotinsulin,Depotinsulin (Einheiten),Notizen,Glukose-Teststreifen mg/dL,Keton mmol/L,Mahlzeiteninsulin (Einheiten),Korrekturinsulin (Einheiten),Insulin-Änderung durch Anwender (Einheiten".split(
    ","
)


class NameNormalizer:
    def __init__(self) -> None:

        self.payload = dict
        field_names = "device,serial_number,device_timestamp,recording_type,glucose_history,glucose_scan,non_numeric_rapid_testing_insulin,rapid_acting_insulin_units,non_numeric_nutritional_data,carbohydrate_grams,carbohydrate_servings,non_numeric_sustained_release_insulin,depot_insulin_units,notes,glucose_test_strips,ketone,meal_insulin_units,correction_insulin_units,insulin_change_by_user_units,meal_insulin_units"

        field_names_list = field_names.split(",")

        for field_name, german_name in zip(field_names_list, CSV_HEADERS):
            print(field_name, german_name)
            self.payload.update({field_name: german_name})

        print(self.payload)

    def get_field_name_german(self, field_name):
        return self.payload[field_name]

    def get_field_name_english(self, name):
        return list(self.payload.keys())[list(self.payload.values()).index(name)]
