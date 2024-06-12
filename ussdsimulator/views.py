from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from .models import Pensionnaire, SessionLevel, Paiement

@method_decorator(csrf_exempt, name='dispatch')
class USSDView(APIView):
    def post(self, request, *args, **kwargs):
        session_id = request.data.get('sessionId')
        phone_number = request.data.get('phoneNumber')
        text = request.data.get('text', '')

        session, _ = SessionLevel.objects.get_or_create(session_id=session_id, defaults={'phone_number': phone_number})
        text_array = text.split('*')
        level = session.level
        response = ""

        try:
            pensionnaire = Pensionnaire.objects.get(phone_number=phone_number)
        except Pensionnaire.DoesNotExist:
            pensionnaire = None

        if text == "" or text == "*123*2000#":
            # Demande initiale pour le numéro de téléphone ou PIN
            if pensionnaire and pensionnaire.pin:
                response = "Entrez votre PIN :"
                session.level = 2
            elif pensionnaire:
                response = "Bienvenue ! Veuillez creer un code PIN a 4 chiffres :"
                session.level = 10  # Niveau pour la création du PIN
            else:
                response = "Bienvenue ! Veuillez entrer votre numero de telephone :"
                session.level = 1
            session.save()

        elif level == 1:
            # Créer ou récupérer un pensionnaire
            pensionnaire, _ = Pensionnaire.objects.get_or_create(phone_number=phone_number)
            if pensionnaire.pin:
                response = "Entrez votre PIN :"
                session.level = 2
            else:
                response = "Bienvenue ! Veuillez creer un code PIN a 4 chiffres :"
                session.level = 10
            session.save()

        elif level == 2:
            # Vérification du PIN
            if pensionnaire.pin == text_array[-1]:
                response = self.main_menu(pensionnaire.name)
                session.level = 3
            else:
                response = "PIN incorrect. Entrez votre PIN :"
            session.save()

        elif level == 10:
            # Création du PIN
            if session.confirm_pin is not None and session.confirm_pin == text_array[-1]:
                pensionnaire.pin = text_array[-1]
                pensionnaire.save()
                response = f"PIN defini avec succes. Veuillez choisir une option :\n{self.main_menu(pensionnaire.name)}"
                session.level = 3
                session.confirm_pin = None
            else:
                session.confirm_pin = text_array[-1]
                response = "Confirmez votre code PIN a 4 chiffres :"
            session.save()

        elif level == 3:
            # Gestion des options du menu principal
            choix = text_array[-1]
            if choix == "1":
                response = "Entrez votre PIN pour consulter votre releve :"
                session.level = 4
            elif choix == "2":
                response = "Entrez votre PIN pour verifier le statut du dernier paiement :"
                session.level = 5
            elif choix == "3":
                response = "Entrez votre PIN pour voir vos informations personnelles :"
                session.level = 6
            elif choix == "4":
                response = "Entrez votre PIN pour vous abonner aux notifications :"
                session.level = 7
            elif choix == "5":
                response = "Entrez votre PIN actuel pour modifier votre code PIN :"
                session.level = 8
            elif choix == "99":
                response = self.main_menu(pensionnaire.name)
                session.level = 3
            elif choix == "00":
                response = "END Merci d'utiliser nos services."
                session.level = 0
            else:
                response = self.main_menu(pensionnaire.name)
                session.level = 3
            session.save()

        elif level in [4, 5, 6, 7, 8, 9]:  # Niveaux nécessitant une vérification du PIN pour les opérations
            if text_array[-1] == "99":
                response = self.main_menu(pensionnaire.name)
                session.level = 3
            elif text_array[-1] == "00":
                response = "END Merci d utiliser nos services."
                session.level = 0
            elif pensionnaire.pin == text_array[-1]:
                if level == 4:
                    response = self.handle_view_statement(pensionnaire)
                elif level == 5:
                    response = self.handle_check_payment()
                elif level == 6:
                    response = self.handle_view_info(pensionnaire)
                elif level == 7:
                    response = self.handle_subscribe_notifications(pensionnaire)
                elif level == 8:
                    response = "Entrez un nouveau code PIN à 4 chiffres :"
                    session.confirm_pin = None
                    session.level = 9
                    print(session.level)
                    level = 9
                    print(level)

            elif level == 9:
                session.confirm_pin = text_array[-1]
                response = "Confirmez votre nouveau code PIN a 4 chiffres :"
                session.level = 10

            else:
                response = "PIN incorrect. Veuillez reessayer :"
                session.level = level  # Reste au même niveau
            session.save()


        elif level == 77:
            # Vérifier la confirmation du nouveau PIN
            if session.confirm_pin == text_array[-1]:
                pensionnaire.pin = session.confirm_pin
                pensionnaire.save()
                response = "Code PIN modifie avec succes !\n99. Menu principal\n00. Terminer la session"
                session.level = 3
                session.confirm_pin = None
            else:
                response = "Les codes PIN ne correspondent pas. Veuillez essayer a nouveau :\nEntrez un nouveau code PIN a 4 chiffres :"
                session.level = 9
            session.save()

        return Response(response)

    def handle_view_statement(self, pensionnaire):
        paiements = Paiement.objects.filter(pensionnaire=pensionnaire).order_by('-date')[:3]
        if paiements.exists():
            response = "Voici vos derniers paiements :\n"
            for paiement in paiements:
                response += f"{paiement.date.strftime('%d/%m/%Y')}: {paiement.montant_en_cdf} CDF ({paiement.etat})\n"
            response += "99. Menu principal\n00. Terminer la session"
        else:
            response = "Aucun paiement trouve.\n99. Menu principal\n00. Terminer la session"
        return response

    def handle_check_payment(self):
        # Renvoie une réponse indiquant que le paiement du mois de mai n'est pas encore disponible
        return "Le paiement du mois de mai n est pas encore disponible.\n99. Menu principal\n00. Terminer la session"

    def handle_view_info(self, pensionnaire):
        return f"Informations personnelles :\nNom : {pensionnaire.name}\nTelephone : {pensionnaire.phone_number}\nNum CNSSAP : {pensionnaire.num_cnssap}\n99. Menu principal\n00. Terminer la session"

    def handle_subscribe_notifications(self, pensionnaire):
        return "Vous etes maintenant abonne aux notifications.\n99. Menu principal\n00. Terminer la session"

    def main_menu(self, name):
        return f"Bienvenue {name}, choisissez une option :\n1. Consulter mon relevé\n2. Verifier le statut de la derniere paie\n3. Consulter mes informations personnelles\n4. Abonnement aux notifications\n5. Modifier le code PIN\n99. Menu principal\n00. Terminer la session"
