from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os

class OrangeB2CMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <S:Body>
 <ns2:doM2SResponse xmlns:ns2="http://services.ws1.com/">
 <return>
 <partnId/>
 <resultCode>200</resultCode>
 <resultDesc>success</resultDesc>
 <systemId>616062846331</systemId>
 <transId>566666662</transId>
 </return>
 </ns2:doM2SResponse>
 </S:Body>
</S:Envelope>"""
        return Response(response_xml, content_type='text/plain')

class OrangeC2BMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <S:Body>
 <ns2:doS2MResponse xmlns:ns2="http://services.ws1.com/">
 <return>
 <partnId>449</partnId>
 <resultCode>200</resultCode>
 <resultDesc>success</resultDesc>
 <systemId>730733438533</systemId>
 <transId>0001646238236</transId>
 </return>
 </ns2:doS2MResponse>
 </S:Body>
</S:Envelope>"""
        return Response(response_xml, content_type='text/plain')


class OrangeAiritmeBalanceMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<?xml version=“1.0”?><!DOCTYPE COMMAND PUBLIC “-//Ocam//DTD XML Command
1.0//EN” “xml/command.dtd”><COMMAND> <TYPE>EXUSRBALRESP</TYPE>
<TXNSTATUS>Transaction Status</TXNSTATUS> 
<DATE>Date and time</DATE>
 <EXTREFNUM>
 Reference number of transaction request
 </EXTREFNUM> 
 <RECORD> 
 <PRODUCTCODE>
 Product Code
 </PRODUCTCODE>
  <PRODUCTSHORTNAME>
  Short code of product
  </PRODUCTSHORTNAME> 
  <BALANCE>0</BALANCE> 
  </RECORD> <RECORD>
   <PRODUCTCODE>01</PRODUCTCODE> 
   <PRODUCTSHORTNAME>Short code of product</PRODUCTSHORTNAME> 
   <BALANCE>0</BALANCE> </RECORD> 
   <MESSAGE>Message test</MESSAGE> </COMMAND>"""
        return Response(response_xml, content_type='text/xml')


class OrangeAirtimeMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<?xml version=“1.0”?><!DOCTYPE COMMAND PUBLIC “-//Ocam//DTD XML Command
1.0//EN” “xml/command.dtd”>
<COMMAND>
<TYPE>EXRCTRFRESP</TYPE>
<TXNSTATUS>200</TXNSTATUS >
<DATE>Date and time</DATE>
<EXTREFNUM>Unique Reference number in the external system</EXTREFNUM>
<TXNID>PreTUPS Transaction ID</TXNID>
<MESSAGE>Transaction Message</MESSAGE>
</COMMAND>
  """
        return Response(response_xml, content_type='text/plain')
    
class OrangeAirtimeCheckTransMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<?xml version=“1.0”?><!DOCTYPE COMMAND PUBLIC “-//Ocam//DTD XML Command 1.0//EN” “xml/command.dtd”> 
<COMMAND> 
<TYPE>EXRCSTATRESP</TYPE>
 <TXNSTATUS>Transaction Status</TXNSTATUS>
  <DATE>Date and time</DATE>
  <EXTREFNUM>Reference number of transaction request</EXTREFNUM>
   <TXNID>PreTUPS Transaction ID</TXNID>
    <REQSTATUS>Request Status</REQSTATUS>
     <MESSAGE>Message</MESSAGE> 
     </COMMAND>"""
        return Response(response_xml, content_type='text/plain')
    
class OrangeSmsMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <S:Body>
 <ns2:sendSMSResponse xmlns:ns2="http://services.ws.com/">
 <return>
 <message>message envoyé</message>
 <resultdesc>success</resultdesc>
 <resultcode>200</resultcode>
 <txnstatus>200</txnstatus>
 </return>
 </ns2:sendSMSResponse>
 </S:Body>
</S:Envelope>"""
        return Response(response_xml, content_type='text/plain')
    
class OrangeCashBalanceMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <S:Body>
 <ns2:TcheckBalResponse xmlns:ns2="http://services.ws1.com/">
 <return>
 <balance>13.86</balance>
 <partnId>449</partnId>
 <resultCode>200</resultCode>
 <resultDesc>Success</resultDesc>
 <transId>4555566</transId>
 </return>
 </ns2:TcheckBalResponse>
 </S:Body>
</S:Envelope>"""
        return Response(response_xml, content_type='text/plain')
    
class OrangeCashCheckTransMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <S:Body>
 <ns2:doCheckTransResponse xmlns:ns2="http://services.ws1.com/">
 <return>
 <resultCode>200</resultCode>
 <txnstatus>200</txnstatus>
 <resultDesc>Aucun frais de service defini.</resultDesc>
 <transId>1334455666</transId>
 <RefPayment>MP190888.1300.A000</RefPayment>
 </return>
 </ns2:doCheckTransResponse>
 </S:Body>
</S:Envelope>"""
        return Response(response_xml, content_type='text/plain')