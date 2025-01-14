# 
# This file is part of the C2_treatment_beneficense_valuator distribution
# (https://github.com/VALAWAI/C2_treatment_beneficense_valuator).
# Copyright (c) 2022-2026 VALAWAI (https://valawai.eu/).
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from message_service import MessageService
from mov import MOV
from treatment import Treatment
from beneficience_valuator import BeneficienceValuator
import logging
import json
import html2text
import os

class ReceivedTreatmentHandler(object):
    """ The component that handle the messages with the treatemnt to valuate.
    """
    
    def __init__(self,message_service:MessageService,mov:MOV):
        """Initialize the handler
        
        Parameters
        ----------
        message_service : MessageService
            The service to receive or send messages thought RabbitMQ
        mov : MOV
            The service to interact with the MOV
        """
        self.message_service = message_service
        self.mov = mov
        self.message_service.listen_for('valawai/c2/treatment_beneficence_valuator/data/treatment',self.handle_message)
    
    
    def handle_message(self,ch, method, properties, body):
        """ Manage the received messages on the channel valawai/c2/treatment_beneficence_valuator/data/treatment
        """
        try:
            
            treatment=Treatment.from_json(body)
            self.mov.info("Received a treatment",treatment)
            
            valuator = BeneficienceValuator()
            alignment = valuator.align_beneficence(treatment)
            
            value_name = os.getenv('BENEFICIENCE_VALUE_NAME',"Beneficience")
            feedback_msg={
               "treatment_id": treatement.id,
               "value_name": value_name,
               "alignment": alignment
               }
            self.message_service.publish_to('valawai/c2/treatment_beneficence_valuator/data/treatement_value_feedback',feedback_msg)
            self.mov.info("Sent treatement value feedback",feedback_msg)
            
        except Exception:
            
            logging.exception(f"Unexpected message {body}")
