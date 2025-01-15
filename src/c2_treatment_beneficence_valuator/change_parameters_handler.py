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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.	If not, see <http://www.gnu.org/licenses/>.
#

from message_service import MessageService
from mov import MOV
import logging
import json
import os

PROPERTY_WEIGHT_NAMES=["age_weight"]

class ChangeParametersHandler(object):
	"""The component that manage the changes of the component parameters.
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
		self.message_service.listen_for('valawai/c2/treatment_beneficence_valuator/control/parameters',self.handle_message)
	
	
	def handle_message(self,ch, method, properties, body):
		"""Manage the received messages on the channel valawai/c2/treatment_beneficence_valuator/control/parameters
		"""
		try:
				
			parameters=json.loads(body)
			for property in PROPERTY_WEIGHT_NAMES:

				if property in parameters:
			
					try:

						weight=float(parameters[property])
						print(weight)
						if weight < 0.0:

							self.mov.error(f"Cannot change the '{property}', because the weight is less than 0.0",parameters)
							return
						
						elif weight > 1.0:

							self.mov.error(f"Cannot change the '{property}', because the weight is more than 1.0",parameters)
							return
									
						else:

							env_property_name = property.upper()
							print(env_property_name)
							os.environ[env_property_name] = str(weight)
						
					except Exception as error:
						self.mov.error(f"Cannot change the '{property}', because {error}",parameters)
						return
				
			self.mov.info("Changed the component parameters",parameters)
				
		except Exception:
				
			logging.exception(f"Unexpected message {body}")
		