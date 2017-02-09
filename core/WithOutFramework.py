from rest_framework.views import APIView
from django.http import HttpResponse as Response
from ussd.core import ussd_session

class DemoUssdWithoutUssdAirflow(APIView):

    @staticmethod
    def post(req):
        phone_number = req.data['phoneNumber'].strip('+'),
        session_id = req.data['sessionId'],
        ussd_input = req.data['text'],
        service_code = req.data['serviceCode'],
        language = req.data.get('language', 'en')

        # create session
        session = ussd_session(session_id)

        # get next_screen
        next_screen = session.get("next_screen")

        screen_text = "Welcome to Ussd Airflow Demo. " \
                "Ussd Airflow aim is to cater for easy " \
                "creations of Ussd Menus. In this demo, " \
                "I will how each demo works. " \
                "For the HttpScreen. " \
                "I will use github public api to fetch " \
                "Ussd Airflow " \
                "data such a number of contributors, " \
                "number of Pull Requests pending. " \
                "In each screen I will end by stating" \
                " which type of screen this. For example. " \
                "This is a menu screen\n" \
                "1. Start Demo\n" \
                "2. Do it sometime later\n"

        if next_screen is None: # its the first screen
            # set screen
            session['next_screen'] = "welcome_screen"

        elif next_screen == "welcome_screen":
            screen_text = "You have choosen to the demo later."

        return Response(screen_text)