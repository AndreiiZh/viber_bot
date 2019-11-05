from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage

# Create your views here.
bot_configuration = BotConfiguration(
    name='PythonSampleBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4a863de418a7d536-8b96513f085b6607-e7706b966accc4b7'
)
viber = Api(bot_configuration)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        viber.send_messages(
            viber_request.sender.id,
            TextMessage(text='Hi')
        )
        print(viber_request)

    return HttpResponse(status=200)
