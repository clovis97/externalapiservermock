from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BaseRenderer

class PlainTextRenderer(BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return str(data).encode(self.charset)


class AfricellB2CMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_data = {
  "txnStatus": 'TS',
  "serviceRequestId": '2c64acd0-c24e-4221-be9d-34962b2611e1',
  "mfsTenantId": 'mfsPrimaryTenant',
  "language": 'en',
  "serviceFlow": 'CASHIN',
  "message": 'Cash In transaction of USD 1 has been successfully completed between the sender: 077223344 and receiver: 077928284. Txn ID: CI200426.1306.B70017',
  "transactionId": 'CI200426.1306.B70017',
  "originalServiceRequestId": '2c64acd0-c24e-4221-be9d-34962b2611e1',
  "status": 'SUCCEEDED',
}
        return Response(response_data)

class AfricellBalanceCheckMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_data = {
  "Code": '0',
  "Description": '500 000',
  "MMTransactionID": '4321',
  "AfrTransactionID": '4321',
}
        return Response(response_data)
    
class AfricellDataBundleMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_data = {
  "Code": '0',
  "Description": 'Successful',
  "MMTransactionID": '1234',
  "AfrTransactionID": '1234',
}
        return Response(response_data)
    
class AfricellDataBundleListMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_data = data = [
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 1.0,
        "BundleDescription": "15MB= 10u",
        "ID": "6f6e2c01-e144-460d-8d49-f22827e2a93d",
        "Price": 10.0,
        "Period": 2.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 2.0,
        "BundleDescription": "20MB= 25u",
        "ID": "e5c24d96-7cb4-49d8-93b6-5a4d374f2d97",
        "Price": 25.0,
        "Period": 3.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 3.0,
        "BundleDescription": "40MB= 30u",
        "ID": "53b6b09d-a2f4-41ed-9ee4-a7dbbbe8e5c4",
        "Price": 30.0,
        "Period": 3.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 4.0,
        "BundleDescription": "70MB= 50u",
        "ID": "a07dd775-19f2-49c5-ad2e-886ca6265376",
        "Price": 50.0,
        "Period": 3.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 5.0,
        "BundleDescription": "100MB=60u",
        "ID": "a51d21ad-2525-4ed1-a667-1a0141619c95",
        "Price": 60.0,
        "Period": 3.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 6.0,
        "BundleDescription": "180MB= 100",
        "ID": "72cbd150-45fa-4470-b77d-598dcbcd1170",
        "Price": 100.0,
        "Period": 7.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 7.0,
        "BundleDescription": "550MB= 200u",
        "ID": "116ece9c-b524-46a0-9d69-03f7abc5691c",
        "Price": 200.0,
        "Period": 7.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 8.0,
        "BundleDescription": "2500MB= 500u",
        "ID": "9dbca964-53fd-4cfe-862a-979d69ff7810",
        "Price": 500.0,
        "Period": 7.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 9.0,
        "BundleDescription": "2.5GB=1000 U",
        "ID": "f2ca5f26-609f-403f-8648-9450c1cf40b5",
        "Price": 1000.0,
        "Period": 30.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 10.0,
        "BundleDescription": "6GB= 2000u",
        "ID": "bf6a7164-7b87-4701-afcd-73e9bba6a336",
        "Price": 2000.0,
        "Period": 30.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 11.0,
        "BundleDescription": "25GB= 5000u",
        "ID": "4b19288f-a160-4306-924e-5bbd650f4bbf",
        "Price": 5000.0,
        "Period": 30.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 12.0,
        "BundleDescription": "30GB= 6000u",
        "ID": "2e87d084-c59e-4523-b9fc-5e8f38ce2538",
        "Price": 6000.0,
        "Period": 60.0,
    },
    {
        "CatOrder": 1,
        "Name": "Forfait Internet",
        "BundleOrder": 13.0,
        "BundleDescription": "125GB= 10000u",
        "ID": "400c6a5a-5dd9-4bb3-95d0-60640e937b7a",
        "Price": 10000.0,
        "Period": 60.0,
    },
    {
        "CatOrder": 2,
        "Name": "Forfait Kitokos",
        "BundleOrder": 1.0,
        "BundleDescription": "10u=1.6Min,10MB + 400% Bonus",
        "ID": "4418499e-6c68-4fc9-bbf6-6b6c588fbe94",
        "Price": 0.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 2,
        "Name": "Forfait Kitokos",
        "BundleOrder": 2.0,
        "BundleDescription": "20u=3.2Min,20MB + 400% Bonus",
        "ID": "3348f4d4-4510-4ea8-b13e-4a8b588e39dd",
        "Price": 0.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 2,
        "Name": "Forfait Kitokos",
        "BundleOrder": 3.0,
        "BundleDescription": "50u=8.2Min,50 MB + 200% Bonus",
        "ID": "34bafe4b-a482-452a-a69c-c4245374a37a",
        "Price": 0.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 2,
        "Name": "Forfait Kitokos",
        "BundleOrder": 4.0,
        "BundleDescription": "100u=16.4Min,100MB + 150% Bonus",
        "ID": "7d6ea383-9a67-499b-8f74-2a61b6967351",
        "Price": 0.0,
        "Period": 3.0,
    },
    {
        "CatOrder": 2,
        "Name": "Forfait Kitokos",
        "BundleOrder": 5.0,
        "BundleDescription": "2500u= 400Min,800MBs + 75% bonus",
        "ID": "f47866e2-a56e-4d5d-b189-84d58a05f8a7",
        "Price": 2500.0,
        "Period": 30.0,
    },
    {
        "CatOrder": 2,
        "Name": "Forfait Kitokos",
        "BundleOrder": 6.0,
        "BundleDescription": "5000u= 800Min, 1600MBs + 50% bonus",
        "ID": "3a0f35eb-6418-443b-9f86-1304d4ec892f",
        "Price": 5000.0,
        "Period": 30.0,
    },
    {
        "CatOrder": 3,
        "Name": "Reseaux Sociaux",
        "BundleOrder": 1.0,
        "BundleDescription": "10MB=5u",
        "ID": "cb19f753-086d-4dc9-972d-83ad80cac0a2",
        "Price": 5.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 3,
        "Name": "Reseaux Sociaux",
        "BundleOrder": 2.0,
        "BundleDescription": "85MB=10u",
        "ID": "bd583bce-02f1-4eec-8cae-fd9e9fc5fb18",
        "Price": 10.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 3,
        "Name": "Reseaux Sociaux",
        "BundleOrder": 3.0,
        "BundleDescription": "350MB=50u",
        "ID": "7fdd36f8-a76e-4e65-8231-40356d4844cd",
        "Price": 50.0,
        "Period": 5.0,
    },
    {
        "CatOrder": 3,
        "Name": "Reseaux Sociaux",
        "BundleOrder": 4.0,
        "BundleDescription": "700MB=100u",
        "ID": "a12dcbb5-10cb-4237-901d-ecde5773d6ff",
        "Price": 100.0,
        "Period": 10.0,
    },
    {
        "CatOrder": 3,
        "Name": "Reseaux Sociaux",
        "BundleOrder": 5.0,
        "BundleDescription": "1000MB=200u",
        "ID": "cdce6dad-72da-41f8-a3c5-eed566ec0f87",
        "Price": 200.0,
        "Period": 10.0,
    },
    {
        "CatOrder": 11,
        "Name": "Offre Speciale",
        "BundleOrder": 1.0,
        "BundleDescription": "70MB = 30u",
        "ID": "6c070f1e-093b-4b55-84b9-bd73020c287a",
        "Price": 30.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 11,
        "Name": "Offre Speciale",
        "BundleOrder": 2.0,
        "BundleDescription": "150MB = 60",
        "ID": "fde44967-dda1-4b9b-9564-2c61c7adbfb6",
        "Price": 60.0,
        "Period": 2.0,
    },
    {
        "CatOrder": 11,
        "Name": "Offre Speciale",
        "BundleOrder": 3.0,
        "BundleDescription": "1GB = 100u",
        "ID": "d6c282d7-8839-44a3-af74-addc4e24e3fe",
        "Price": 100.0,
        "Period": 1.0,
    },
    {
        "CatOrder": 11,
        "Name": "Offre Speciale",
        "BundleOrder": 4.0,
        "BundleDescription": "1.5GB = 15",
        "ID": "9f27ec71-d63a-4f1c-b430-6802c7e43b23",
        "Price": 150.0,
        "Period": 1.5,
    },
]

        return Response(response_data)
    
class AfricellSendSmsMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_data = {
  "Code": '0',
  "Description": 'Successful',
  "MMTransactionID": '1234',
  "AfrTransactionID": '1234',
}
        return Response(response_data)
    
import logging

logger = logging.getLogger(__name__)

class AfricellTopUpMockView(APIView):
    renderer_classes = [PlainTextRenderer]

    def post(self, request, *args, **kwargs):
        logger.info("Received request: %s", request.data)
        response_data = """{
            "Code": "0",
            "Description": "Successful",
            "MMTransactionID": "1234",
            "AfrTransactionID": "1234"
        }"""
        logger.info("Sending response: %s", response_data)
        return Response(response_data, content_type='text/plain')

    
class AfricellTransactionLoadMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_data = [
    {
        "MSISDN": "24363727387 ",
        "BalanceChange": "-500.0",
        "ChangeDate": "2020-09-21",
        "ChangeDateTime": "2020-09-21T14:07:00.000+01:00",
        "Name": "xxxxxxxxx",
        "OpeningBalance": "4137646.283",
        "OperatorId": "11695",
        "Target": "243xxxxx ",
        "UpdateMethod": "91"
    },
    {
        "MSISDN": "2437378299 ",
        "BalanceChange": "-150.0",
        "ChangeDate": "2020-09-21",
        "ChangeDateTime": "2020-09-21T13:36:00.000+01:00",
        "Name": "xxxxx",
        "OpeningBalance": "4137796.283",
        "OperatorId": "10415",
        "Target": "243xxxxx ",
        "UpdateMethod": "91"
    },
    {
        "MSISDN": "24383648393 ",
        "BalanceChange": "-1000.0",
        "ChangeDate": "2020-09-21",
        "ChangeDateTime": "2020-09-21T12:50:00.000+01:00",
        "Name": "xxxxx",
        "OpeningBalance": "4138796.283",
        "OperatorId": "11917",
        "Target": "xxxxx",
        "UpdateMethod": "91"
    },
    {
        "MSISDN": "243837483",
        "BalanceChange": "-50.0",
        "ChangeDate": "2020-09-21",
        "ChangeDateTime": "2020-09-21T11:51:00.000+01:00",
        "Name": "xxxxxxx",
        "OpeningBalance": "4138846.283",
        "OperatorId": "15015",
        "Target": "xxxxxx",
        "UpdateMethod": "91"
    }
]
        return Response(response_data)