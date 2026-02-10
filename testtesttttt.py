import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "tango_with_django_project/templates/rango")
print(" ")
print(str(TEMPLATE_DIR))

