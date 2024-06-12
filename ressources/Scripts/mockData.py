from ussdsimulator.models import *
from django.utils import timezone

def create_sample_data():
    pensionnaires_data = [
        {"name": "PANDA NGOIE MWADI CHRISTINE", "phone_number": "978942007", "num_cnssap": "11203195403581V"},
        {"name": "KAMBERE KIKUKU YVONNE", "phone_number": "994308623", "num_cnssap": "20603195719741H"},
        {"name": "MUNGAZI TWARA ONORE", "phone_number": "992085518", "num_cnssap": "11707193619594T"},
        {"name": "NTAWI PALUKU", "phone_number": "998548634", "num_cnssap": "11507193419447I"}
    ]

    paiements_data = [
        {"depositaire": "NDAYA MUKENA DORCAS", "montant_en_cdf": 9440, "reference": "CI240403.1043.C11373", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "KIYENGE MUNDUMOYA ADALBERT", "montant_en_cdf": 9470, "reference": "CI240403.1044.C11394", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "SELUDUA JIJIMA ANTOINETTE", "montant_en_cdf": 9470, "reference": "CI240403.1044.C11403", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "KASEREKA LWAYIVWEKA TIMOTHEE", "montant_en_cdf": 9470, "reference": "CI240403.1044.A37526", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "FURAHA KAHINDO JASMINE", "montant_en_cdf": 9720, "reference": "CI240403.1044.A37528", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "MUSHAILA MALWENA LUC", "montant_en_cdf": 9720, "reference": "CI240403.1044.B01281", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "NGONGO OMALOHENDA JOSEPH", "montant_en_cdf": 9720, "reference": "CI240403.1045.A37530", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "ILUNGA MANGAZA JOCELMINE", "montant_en_cdf": 9720, "reference": "CI240403.1045.D26396", "date": "2024-04-03 00:00", "etat": "PAYÉ"},
        {"depositaire": "KATUNGU PALUKU", "montant_en_cdf": 9760, "reference": "CI240403.1045.C11552", "date": "2024-04-03 00:00", "etat": "PAYÉ"}
    ]

    pensionnaires = []
    for data in pensionnaires_data:
        pensionnaires.append(Pensionnaire.objects.create(**data))

    for i, pensionnaire in enumerate(pensionnaires):
        for j in range(3):
            index = i * 3 + j
            if index < len(paiements_data):
                Paiement.objects.create(
                    pensionnaire=pensionnaire,
                    depositaire=paiements_data[index]["depositaire"],
                    montant_en_cdf=paiements_data[index]["montant_en_cdf"],
                    reference=paiements_data[index]["reference"],
                    date=timezone.datetime.strptime(paiements_data[index]["date"], "%Y-%m-%d %H:%M"),
                    etat=paiements_data[index]["etat"]
                )
            else:
                print(f"Pas assez de paiements pour le pensionnaire {pensionnaire.name}")
