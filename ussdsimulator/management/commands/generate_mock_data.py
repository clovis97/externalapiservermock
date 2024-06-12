# app/management/commands/generate_mock_data.py

from django.core.management.base import BaseCommand
from ressources.Scripts.mockData import create_sample_data

class Command(BaseCommand):
    help = "Génère des données d'échantillon pour les pensionnaires"

    def handle(self, *args, **kwargs):
        create_sample_data()
        self.stdout.write(self.style.SUCCESS("Les données d'échantillon ont été générées avec succès."))
