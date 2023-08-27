import os

from django.db import migrations


def add_registry(apps, project_state):
    registry = apps.get_model('metrostandart', 'Registry')
    measuring_instrument = apps.get_model('metrostandart', 'MeasuringInstrument')
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'registry.txt')
    registry_dict = {}
    buf_key = ''
    with open(path, 'r') as file:
        for line in file:
            if line[0].isalpha():
                buf_key = line[:-2]
                registry_dict[line[:-2]] = []
            elif line[0].isdigit():
                registry_dict[buf_key].append(line[:-1])
    for key in registry_dict.keys():
        instrument = measuring_instrument.objects.create(name=key)
        for item in registry_dict[key]:
            registry.objects.create(measuring_instrument=instrument, number=item)


class Migration(migrations.Migration):
    dependencies = [
        ('metrostandart', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_registry)
    ]
