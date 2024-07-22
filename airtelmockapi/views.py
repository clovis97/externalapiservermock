from django.shortcuts import render
from rest_framework.parsers import BaseParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import BaseRenderer, JSONRenderer


class XMLRenderer(BaseRenderer):
    media_type = 'application/xml'
    format = 'xml'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data.encode('utf-8')

class PlainTextParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read().decode('utf-8')

class PlainTextRenderer(BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return str(data).encode(self.charset)

class AirtelB2CLoginMockView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        response_data = {
            "token_type": "token_type",
            "expires_in": "expires_in",
            "access_token": "access_token",
        }
        return Response(response_data)

class AirtelC2BLoginMockView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        response_data = {
            "token_type": "token_type",
            "expires_in": "expires_in",
            "access_token": "access_token",
        }
        return Response(response_data)

class AirtelC2BMockView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        response_data = {
            "data": {
                "message": "Transaction Successful",
                "status": "SUCCESS",
                "transaction": {
                    "airtel_money_id": "product-partner-ABCD1234",
                    "id": "ABCD1234",
                },
            },
            "status": {
                "code": "200",
                "message": "SUCCESS",
                "response_code": "DP01000001001",
                "success": "true",
            },
        }
        return Response(response_data)



class AirtelB2CMockView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        response_data = {
            "data": {
                "transaction": {
                    "reference_id": "18*****3354",
                    "airtel_money_id": "partner-AB***41",
                    "id": "AB***41",
                    "status": "TS",
                },
            },
            "status": {
                "code": "200",
                "message": "Trans.ID :  CI2***02. You have sent ***** to 99****39, B****MA . Your available balance is ** 5**.21.",
                "result_code": "ESB000010",
                "response_code": "DP00900001001",
                "success": "true",
            },
        }
        return Response(response_data)

class AirtelDataMockView(APIView):
    renderer_classes = [XMLRenderer]
    def post(self, request, *args, **kwargs):
        response_xml = """<?xml version="1.0"?>
<COMMAND>
<TYPE> VASSELLRESP</TYPE>
<TXNSTATUS>200</TXNSTATUS >
<DATE>30/01/2024 10:30:00</DATE>
<EXTREFNUM>4223455</EXTREFNUM>
<TXNID>543</TXNID>
<MESSAGE>SUCCESS</MESSAGE>
</COMMAND>"""
        return Response(response_xml, content_type='text/xml')
    
class AirtelTopupBalanceMockView(APIView):
    renderer_classes = [XMLRenderer]
    def post(self, request, *args, **kwargs):
        response_xml = """<?xml version="1.0"?>
<COMMAND>
<TYPE>EXUSRBALRESP</TYPE>
<TXNSTATUS>200</TXNSTATUS>
<DATE>30/01/2024 10:30:00</DATE>
<EXTREFNUM>436365435635</EXTREFNUM>
<RECORD>
<PRODUCTCODE>2634244</PRODUCTCODE>
<PRODUCTSHORTNAME>007</PRODUCTSHORTNAME>
<BALANCE>3000</BALANCE>
</RECORD>
<RECORD>
<PRODUCTCODE>63282</PRODUCTCODE>
<PRODUCTSHORTNAME>004</PRODUCTSHORTNAME>
<BALANCE>500</BALANCE>
</RECORD>
<MESSAGE>SUCCESS</MESSAGE>
</COMMAND>"""
        return Response(response_xml, content_type='text/xml')
    

class AirtelTopupMockView(APIView):
    renderer_classes = [XMLRenderer]
    def post(self, request, *args, **kwargs):
        response_xml = """<?xml version="1.0"?>
<COMMAND>
<TYPE>EXRCTRFRESP</TYPE>
<TXNSTATUS>200</TXNSTATUS >
<DATE>30/01/2024 10:30:00</DATE>
<EXTREFNUM>436365435635</EXTREFNUM>
<TXNID>78021999</TXNID>
<MESSAGE>Success</MESSAGE>
</COMMAND>"""
        return Response(response_xml, content_type='text/plain')