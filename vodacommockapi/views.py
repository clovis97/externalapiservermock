from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os

class VodacashB2CMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """            
            <?xml version='1.0' encoding='UTF-8'?>
<S:Envelope
xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<S:Header>
<ns3:eventid
xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
xmlns:ns3="http://www.4cgroup.co.za/soapauth">12001
</ns3:eventid>
</S:Header>
<S:Body>
<ns2:getGenericResultResponse
xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
xmlns:ns3="http://www.4cgroup.co.za/soapauth">
<SOAPAPIResult>
<eventInfo>
<code>3</code>
<description>Processed</description>
<detail>Processed</detail>
<transactionID>74b2f36481524d1e9bf907edbc86291d</transactionID>
</eventInfo>
<request>
<dataItem>
<name>ServiceProviderName</name>
<type>String</type>
<value>ONE4ALL</value>
</dataItem>
<dataItem>
<name>CustomerMSISDN</name>
<type>String</type>
<value>243811835361</value>
</dataItem>
<dataItem>
<name>Currency</name>
<type>String</type>
<value>USD</value>
</dataItem>
<dataItem>
<name>Amount</name>
<type>String</type>
<value>1</value>
</dataItem>
<dataItem>
<name>TransactionDateTime</name>
<type>Date</type>
<value>20180601123700</value>
</dataItem>
<dataItem>
    <name>Shortcode</name>
    <type>String</type>
    <value>15058</value>
    </dataItem>
    <dataItem>
    <name>Language</name>
    <type>String</type>
    <value>EN</value>
    </dataItem>
    <dataItem>
    <name>ThirdPartyReference</name>
    <type>String</type>
    <value>Christian-Test1</value>
    </dataItem>
    <dataItem>
    <name>CallBackChannel</name>
    <type>String</type>
    <value>2</value>
    </dataItem>
    <dataItem>
    <name>CallBackDestination</name>
    <type>String</type>
    <value>https://callbackurl</value>
    </dataItem>
    <dataItem>
    <name>CommandID</name>
    <type>String</type>
    <value>InitTrans_one4allb2c</value>
    </dataItem>
    </request>
    <response>
    <dataItem>
    <name>Insight_txid</name>
    <type>String</type>
    <value>lurzsmmaxquh9l1svold6e3hx7x7jp9t</value>
    </dataItem>
    <dataItem>
    <name>ResponseCode</name>
    <type>String</type>
    <value>0</value>
    </dataItem>
    </response>
    </SOAPAPIResult>
    </ns2:getGenericResultResponse>
    </S:Body>
    </S:Envelope>
"""
        return Response(response_xml, content_type='text/xml')
    
class VodacashB2CLoginMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """
<?xml version='1.0' encoding='UTF-8'?>
            <S:Envelope
            xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
            <S:Header>
            <ns3:eventid
            xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
            xmlns:ns3="http://www.4cgroup.co.za/soapauth">2500
            </ns3:eventid>
            </S:Header>
            <S:Body>
            <ns2:getGenericResultResponse
            xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
            xmlns:ns3="http://www.4cgroup.co.za/soapauth">
            <SOAPAPIResult>
            <eventInfo>
            <code>3</code>
            <description>Processed</description>
            <detail>Processed</detail>
            <transactionID>0c49ec4bbebe44b082aa24e5f548b514</transactionID>
            </eventInfo>
            <request>
            <dataItem>
            <name>Username</name>
            <type>String</type>
            <value>thirdpartyc2bw</value>
            </dataItem>
            <dataItem>
            <name>Password</name>
            <type>String</type>
            <value>thirdpartyc2bw</value>
            </dataItem>
            </request>
            <response>
            <dataItem>
            <name>SessionID</name>
            <type>String</type>
            <value>dbcb63a40afd4191a990d66ed9cb62f7</value>
            </dataItem>
            </response>
            </SOAPAPIResult>
            </ns2:getGenericResultResponse>
            </S:Body>
            </S:Envelope>
"""
        return Response(response_xml, content_type='text/xml')
    
class VodacashC2BMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """
<?xml version='1.0' encoding='UTF-8'?>
<S:Envelope
xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<S:Header>
<ns3:eventid
xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
xmlns:ns3="http://www.4cgroup.co.za/soapauth">80049
</ns3:eventid>
</S:Header>
<S:Body>
<ns2:getGenericResultResponse
xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
xmlns:ns3="http://www.4cgroup.co.za/soapauth">
<SOAPAPIResult>
<eventInfo>
<code>3</code>
<description>Processed</description>
<detail>Processed</detail>
<transactionID>80db41ffab3c4b88ab7f937f9fd7ccc9</transactionID>
</eventInfo>
<request>
<dataItem>
<name>CustomerMSISDN</name>
<type>String</type>
<value>243811835361</value>
</dataItem>
<dataItem>
<name>ServiceProviderCode</name>
<type>String</type>
<value>8337</value>
</dataItem>
<dataItem>
<name>Currency</name>
<type>String</type>
<value>CDF</value>
</dataItem>
<dataItem>
<name>Amount</name>
<type>String</type>
<value>10</value>
</dataItem>
<dataItem>
<name>Date</name>
<type>String</type>
<value>20170901155250</value>
</dataItem>
<dataItem>
<name>ThirdPartyReference</name>
<type>String</type>
<value>Test100</value>
</dataItem>
<dataItem>
<name>CommandId</name>
<type>String</type>
<value>InitTrans_oneForallC2B</value>
</dataItem>
<dataItem>
<name>Language</name>
<type>String</type>
<value>EN</value>
</dataItem>
<dataItem>
<name>CallBackChannel</name>
<type>String</type>
<value>4</value>
</dataItem>
<dataItem>
<name>CallBackDestination</name>
<type>String</type>
<value>Christian.Belewete@vodacom.cd</value>
</dataItem>
<dataItem>
<name>Surname</name>
<type>String</type>
<value>Surname</value>
</dataItem>
<dataItem>
<name>Initials</name>
<type>String</type>
<value>Initials</value>
</dataItem>
</request>
<response>
<dataItem>
<name>InsightReference</name>
<type>String</type>
<value>7272C194D0B50616E054002128FBA42E</value>
</dataItem>
<dataItem>
<name>ResponseCode</name>
<type>String</type>
<value>0</value>
</dataItem>
<dataItem>
<name>CustomerMSISDN</name>
<type>String</type>
<value>243811835361</value>
</dataItem>
</response>
</SOAPAPIResult>
</ns2:getGenericResultResponse>
</S:Body>
</S:Envelope>
"""
        return Response(response_xml, content_type='text/xml')
    

class VodacashC2BLoginMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """
<?xml version='1.0' encoding='UTF-8'?>
<S:Envelope
xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<S:Header>
<ns3:eventid
xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
xmlns:ns3="http://www.4cgroup.co.za/soapauth">2500
</ns3:eventid>
</S:Header>
<S:Body>
<ns2:getGenericResultResponse
xmlns:ns2="http://www.4cgroup.co.za/genericsoap"
xmlns:ns3="http://www.4cgroup.co.za/soapauth">
<SOAPAPIResult>
<eventInfo>
<code>3</code>
<description>Processed</description>
<detail>Processed</detail>
<transactionID>0c49ec4bbebe44b082aa24e5f548b514</transactionID>
</eventInfo>
<request>
<dataItem>
<name>Username</name>
<type>String</type>
<value>thirdpartyc2bw</value>
</dataItem>
<dataItem>
<name>Password</name>
<type>String</type>
<value>thirdpartyc2bw</value>
</dataItem>
</request>
<response>
<dataItem>
<name>SessionID</name>
<type>String</type>
<value>dbcb63a40afd4191a990d66ed9cb62f7</value>
</dataItem>
</response>
</SOAPAPIResult>
</ns2:getGenericResultResponse>
</S:Body>
</S:Envelope>
"""
        return Response(response_xml, content_type='text/xml')
    
class VodacashAirtimeBalanceMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Body>
        <api:Result
            xmlns:api="http://cps.huawei.com/synccpsinterface/api_requestmgr"
            xmlns:res="http://cps.huawei.com/synccpsinterface/result">
            <res:Header>
                <res:Version>1.0</res:Version>
                <res:OriginatorConversationID>S_X2013012921001</res:OriginatorConversationID>
                <res:ConversationID>AG_20130129T102103</res:ConversationID>
            </res:Header>
            <res:Body>
                <res:ResultType>0</res:ResultType>
                <res:ResultCode>0</res:ResultCode>
                <res:ResultDesc>Process service request successfully.</res:ResultDesc>
                <res:QueryOrganizationBalanceResult>
                    <res:BOCompletedTime>20180404185018</res:BOCompletedTime>
                    <res:AccountBalanceData>
                        <res:AccountBalanceItem>
                            <res:AccountHolderID>1000</res:AccountHolderID>
                            <res:AccountHolderPublicName>1000 -
                                1000</res:AccountHolderPublicName>
                            <res:AccountTypeName>Agent Airtime Account for
                                EVC</res:AccountTypeName>
                            <res:AccountTypeAlias>Agent Airtime Account for
                                EVC</res:AccountTypeAlias>
                            <res:AccountNo>500000000200090032</res:AccountNo>
                            <res:AccountName>DefaultAccount</res:AccountName>
                            <res:AccountStatus>Active</res:AccountStatus>
                            <res:Currency>USD</res:Currency>
                            <res:AvailableBalance>68.00</res:AvailableBalance>
                            <res:ReservedBalance>0.00</res:ReservedBalance>
                            <res:UnclearedBalance>0.00</res:UnclearedBalance>
<res:CurrentBalance>68.00</res:CurrentBalance>
</res:AccountBalanceItem>
</res:AccountBalanceData>
</res:QueryOrganizationBalanceResult>
</res:Body>
</api:Result>
</soapenv:Body>
</soapenv:Envelope>
"""
        return Response(response_xml, content_type='text/xml')
    
class VodacashAirtimeMockView(APIView):
    def post(self, request, *args, **kwargs):
        response_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<api:Result
xmlns:api="http://cps.huawei.com/synccpsinterface/api_requestmgr"
xmlns:res="http://cps.huawei.com/synccpsinterface/result">
<res:Header>
<res:Version>1.0</res:Version>
<res:OriginatorConversationID>S_X208880166688</res:OriginatorConversationID>
<res:ConversationID>AG_20180404_00005bb3dc687b62804d</res:ConversationID>
</res:Header>
<res:Body>
<res:ResultType>0</res:ResultType>
<res:ResultCode>0</res:ResultCode>
<res:ResultDesc>Process service request successfully.</res:ResultDesc>
<res:TransactionResult>
<res:TransactionID>0000000204705010</res:TransactionID>
</res:TransactionResult>
</res:Body>
</api:Result>
</soapenv:Body>
</soapenv:Envelope>` },
{ id: 6, xml: `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<api:Result
xmlns:api="http://cps.huawei.com/synccpsinterface/api_requestmgr"
xmlns:res="http://cps.huawei.com/synccpsinterface/result">
<res:Header>
<res:Version>1.0</res:Version>
<res:OriginatorConversationID>S_X2013012921001</res:OriginatorConversationID>
<res:ConversationID>AG_20130129T102103</res:ConversationID>
</res:Header>
<res:Body>
<res:ResultType>0</res:ResultType>
<res:ResultCode>0</res:ResultCode>
<res:ResultDesc>Process service request successfully.</res:ResultDesc>
<res:QueryOrganizationBalanceResult>
<res:BOCompletedTime>20180404185018</res:BOCompletedTime>
<res:AccountBalanceData>
<res:AccountBalanceItem>
<res:AccountHolderID>1000</res:AccountHolderID>
<res:AccountHolderPublicName>1000 -
1000</res:AccountHolderPublicName>
<res:AccountTypeName>Agent Airtime Account for
EVC</res:AccountTypeName>
<res:AccountTypeAlias>Agent Airtime Account for
EVC</res:AccountTypeAlias>
<res:AccountNo>500000000200090032</res:AccountNo>
<res:AccountName>DefaultAccount</res:AccountName>
<res:AccountStatus>Active</res:AccountStatus>
<res:Currency>USD</res:Currency>
<res:AvailableBalance>68.00</res:AvailableBalance>
<res:ReservedBalance>0.00</res:ReservedBalance>
<res:UnclearedBalance>0.00</res:UnclearedBalance>
<res:CurrentBalance>68.00</res:CurrentBalance>
</res:AccountBalanceItem>
</res:AccountBalanceData>
</res:QueryOrganizationBalanceResult>
</res:Body>
</api:Result>
</soapenv:Body>
</soapenv:Envelope>
"""
        return Response(response_xml, content_type='text/xml')