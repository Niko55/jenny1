from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from validate_email import validate_email

import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.events import SlotSet

logger = logging.getLogger(__name__)


class isvalidemail(Action):
    def name(self):
        return 'action_isvalidemail'
    
    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        is_valid = validate_email(email)
        if is_valid is False:
            dispatcher.utter_message("Email Id you entered is not valid.")
            return []
        else:
			return []

def lenDigits(x): 
    x = abs(x)
    if x < 10:
        return 1
    return 1 + lenDigits(x / 10)
	
class isvalidid(Action):
    def name(self):
        return 'action_isvalidid'
    
    def run(self, dispatcher, tracker, domain):
        psaid = tracker.get_slot('PSAID')
        lenid = lenDigits(psaid)
        if lenid != 6:
            dispatcher.utter_message("PSAID you entered is not valid.")
            return []
        else:
			return []