from django.db import models
import csv

class Record(models.Model):
    name = models.CharField(max_length=100)
    blood_sugar = models.FloatField()
    bmi = models.FloatField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    glycemic_index = models.IntegerField()
    calories = models.FloatField()
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    fiber = models.FloatField()
    sodium = models.FloatField()
    potassium = models.FloatField()
    magnesium = models.FloatField()
    calcium = models.FloatField()
    suitable_for_diabetes = models.BooleanField()
    suitable_for_bp = models.BooleanField()

    def __str__(self):
        return self.name

    @property
    def gi_category(self):
        """Categorizes food based on Glycemic Index (GI) values."""
        if self.glycemic_index <= 55:
            return "Low"
        elif 56 <= self.glycemic_index <= 69:
            return "Medium"
        else:
            return "High"

    @classmethod
    def import_csv(cls, file_path):
        """Imports food data from a CSV file safely."""
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            def safe_float(value):
                """Converts a value to float, returning 0.0 if empty or invalid."""
                try:
                    return float(value.strip()) if value and value.strip() else 0.0
                except ValueError:
                    return 0.0  # Handle invalid numbers gracefully

            for row in reader:
                try:
                    cls.objects.create(
                        name=row.get('name', 'Unknown').strip(),
                        glycemic_index=int(row['glycemic_index'].strip()) if row.get('glycemic_index', '').strip().isdigit() else 0,
                        calories=safe_float(row.get('calories', '0')),
                        carbohydrates=safe_float(row.get('carbohydrates', '0')),
                        protein=safe_float(row.get('protein', '0')),
                        fat=safe_float(row.get('fat', '0')),
                        fiber=safe_float(row.get('fiber', '0')),
                        sodium=safe_float(row.get('sodium', '0')),
                        potassium=safe_float(row.get('potassium', '0')),
                        magnesium=safe_float(row.get('magnesium', '0')),
                        calcium=safe_float(row.get('calcium', '0')),
                        suitable_for_diabetes=row.get('suitable_for_diabetes', '').strip().lower() == 'true',
                        suitable_for_bp=row.get('suitable_for_bp', '').strip().lower() == 'true'
                    )
                except Exception as e:
                    print(f"⚠️ Error importing row {row}: {e}")

        print("✅ Food data successfully imported!")
