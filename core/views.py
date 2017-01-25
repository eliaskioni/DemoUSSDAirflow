from django.shortcuts import render

# Create your views here.
from ussd.core import UssdView, UssdRequest
from django.http import HttpResponse
from core import path


class DemoAirflowUssdGateway(UssdView):
    customer_journey_namespace = "AfricasTalkingUssdGateway"
    customer_journey_conf = path + "/customer_journey.yml"

    @staticmethod
    def post(req):
        text = req.data['text']
        if "*" in text:
            text = text.strip("*")[-1]
        ussd_request = UssdRequest(
            phone_number=req.data['phoneNumber'].strip('+'),
            session_id=req.data['sessionId'],
            ussd_input=text,
            service_code=req.data['serviceCode'],
            language=req.data.get('language', 'en')
        )

        return ussd_request

    @staticmethod
    def ussd_response_handler(ussd_response):
        if ussd_response.status:
            res = 'CON' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        else:
            res = 'END' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        return response