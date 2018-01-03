
import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '460686302:AAF2BU1py3Sq4r2PVL83JalLCfk9N21X1QM'
WEBHOOK_URL = 'https://5584508f.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
		'user',
		'bye',
		'state1',
		'state2',
		'state3',
		'state4',
		'state5',
		'state6',
		'state7',
		'state8',
		'state9',
		'state10',
		'state11',
		'state12',
		'state13',
		'state14',
		'state15',
		'state16',
		'state17',
		'state18',
		'state19',
		'state20',
		'state21',
		'state22',
		'stateA',
		'stateB',
		'stateC',
		'stateD',
		'finish'
    ],
    transitions=[
        
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
		
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
		
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'bye',
            'conditions': 'is_going_to_bye'
        },
		
		{
            'trigger': 'advance',
            'source': 'bye',
            'dest': 'bye',
        },
		
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'user',
            'conditions': 'return_again'
        },
		
		
		
		{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': '_1_is_going_to_state2'
        },
		
		{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state3',
            'conditions': '_1_is_going_to_state3'
        },
		
		{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': '_2_is_going_to_state4'
        },
		
		{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': '_2_is_going_to_state5'
        },
		
		{
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state2',
            'conditions': '_3_is_going_to_state2'
        },
		
		{
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state5',
            'conditions': '_3_is_going_to_state5'
        },
		
		{
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state6',
            'conditions': '_4_is_going_to_state6'
        },
		
		{
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state7',
            'conditions': '_4_is_going_to_state7'
        },
		
		{
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state4',
            'conditions': '_5_is_going_to_state4'
        },
		
		{
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state7',
            'conditions': '_5_is_going_to_state7'
        },
		
		{
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state8',
            'conditions': '_6_is_going_to_state8'
        },
		
		{
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state9',
            'conditions': '_6_is_going_to_state9'
        },
		
		{
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state6',
            'conditions': '_7_is_going_to_state6'
        },
		
		{
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state10',
            'conditions': '_7_is_going_to_state10'
        },
		
		{
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state11',
            'conditions': '_8_is_going_to_state11'
        },
		
		{
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state12',
            'conditions': '_8_is_going_to_state12'
        },
		
		{
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state8',
            'conditions': '_9_is_going_to_state8'
        },
		
		{
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state12',
            'conditions': '_9_is_going_to_state12'
        },
		
		{
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state9',
            'conditions': '_10_is_going_to_state9'
        },
		
		{
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state13',
            'conditions': '_10_is_going_to_state13'
        },
		
		{
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state14',
            'conditions': '_11_is_going_to_state14'
        },
		
		{
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state15',
            'conditions': '_11_is_going_to_state15'
        },
		
		{
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state11',
            'conditions': '_12_is_going_to_state11'
        },
		
		{
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state15',
            'conditions': '_12_is_going_to_state15'
        },
		
		{
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state12',
            'conditions': '_13_is_going_to_state12'
        },
		
		{
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state16',
            'conditions': '_13_is_going_to_state16'
        },
		
		{
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state17',
            'conditions': '_14_is_going_to_state17'
        },
		
		{
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state18',
            'conditions': '_14_is_going_to_state18'
        },
		
		{
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state14',
            'conditions': '_15_is_going_to_state14'
        },
		
		{
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state18',
            'conditions': '_15_is_going_to_state18'
        },
        
		{
            'trigger': 'advance',
            'source': 'state16',
            'dest': 'state15',
            'conditions': '_16_is_going_to_state15'
        },
		
		{
            'trigger': 'advance',
            'source': 'state16',
            'dest': 'state19',
            'conditions': '_16_is_going_to_state19'
        },
		
		{
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state20',
            'conditions': '_17_is_going_to_state20'
        },
		
		{
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state21',
            'conditions': '_17_is_going_to_state21'
        },
		
		{
            'trigger': 'advance',
            'source': 'state18',
            'dest': 'state17',
            'conditions': '_18_is_going_to_state17'
        },
		
		{
            'trigger': 'advance',
            'source': 'state18',
            'dest': 'state21',
            'conditions': '_18_is_going_to_state21'
        },
		
		{
            'trigger': 'advance',
            'source': 'state19',
            'dest': 'state18',
            'conditions': '_19_is_going_to_state18'
        },
		
		{
            'trigger': 'advance',
            'source': 'state19',
            'dest': 'state22',
            'conditions': '_19_is_going_to_state22'
        },
		
		{
            'trigger': 'advance',
            'source': 'state20',
            'dest': 'stateA',
            'conditions': '_20_is_going_to_stateA'
        },
		
		{
            'trigger': 'advance',
            'source': 'state20',
            'dest': 'stateB',
            'conditions': '_20_is_going_to_stateB'
        },
		
		{
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state20',
            'conditions': '_21_is_going_to_state20'
        },
		
		{
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'stateC',
            'conditions': '_21_is_going_to_stateC'
        },
		
		{
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state21',
            'conditions': '_22_is_going_to_state21'
        },
		
		{
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'stateD',
            'conditions': '_22_is_going_to_stateD'
        },
		{
			'trigger' : 'gofinal',
			'source' : [
				'stateA',
				'stateB',
				'stateC',
				'stateD',
			],
			'dest' : 'finish',
		},
        
		{
            'trigger': 'advance',
            'source': 'finish',
            'dest': 'state1',
            'conditions': 'useruser'
        },
		
		{
            'trigger': 'advance',
            'source': 'finish',
            'dest': 'bye',
            'conditions': 'byebye'
        },

    ],
    initial='user',
#    auto_transitions=False,
#    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
