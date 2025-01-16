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

import json
import logging
import os

from change_parameters_payload import ChangeParametersPayload
from message_service import MessageService
from mov import MOV


class ChangeParametersHandler:
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


	def handle_message(self, _ch, _method, _properties, body):
		"""Manage the received messages on the channel valawai/c2/treatment_beneficence_valuator/control/parameters
		"""
		try:

			json_dict = json.loads(body)
			parameters =  ChangeParametersPayload(**json_dict)

			for property_name in json_dict:

				weight = json_dict[property_name]
				env_property_name = property_name.upper()
				os.environ[env_property_name] = str(weight)

			self.mov.info("Changed the component parameters",parameters)

		except Exception:

			msg=f"Unexpected message {body}"
			logging.exception(msg)
