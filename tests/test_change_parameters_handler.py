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

import json
import logging
import os
import random
import time
import unittest
import urllib.parse
import uuid

import requests

from c2_treatment_beneficence_valuator.change_parameters_handler import ChangeParametersHandler
from c2_treatment_beneficence_valuator.message_service import MessageService
from c2_treatment_beneficence_valuator.mov import MOV


class TestChangeParametersHandler(unittest.TestCase):
    """Class to test the handler of the receiver e-mails to reply
    """

    def setUp(self):
        """Create the handler.
        """
        self.message_service = MessageService()
        self.mov = MOV(self.message_service)
        self.msgs = []
        self.handler = ChangeParametersHandler(self.message_service, self.mov)

    def tearDown(self):
        """Stops the message service.
        """
        self.mov.unregister_component()
        self.message_service.close()

    def callback(self, ch, method, properties, body):
        """Called when a message is received from a listener.
        """
        try:

            logging.debug("Received %s", body)
            msg = json.loads(body)
            self.msgs.append(msg)

        except Exception as error:
            print(error)

    def test_capture_bad_json_message_body(self):
        """Check that the handler can manage when the body is not a valid json
        """

        with self.assertLogs() as cm:

            self.handler.handle_message(None, None, None, "{")

        self.assertEqual(1, len(cm.output))
        self.assertRegex(cm.output[0], r'Unexpected message \{')

    def __capture_last_logs_from_mov(self, min:int=1):
        """Capture the last logs messages provided in the MOV
        """

        url_params = urllib.parse.urlencode(
            {
                'order':'-timestamp',
                'offset':0,
                'limit':100
            }
        )
        url = f"http://host.docker.internal:8083/v1/logs?{url_params}"
        for i in range(10):

            time.sleep(2)
            response = requests.get(url)
            content = response.json()
            if 'total' in content and content['total'] >= min and 'logs' in content:
                return content['logs']

        self.fail("Could not get the logs from the MOV")

    def __assert_process_change_parameters(self, level:str, parameters):
        """Check that
        
        Parameters
        ----------
        level: str
            The expected level of the message when the parameters are changed
        parameters: object
            The parameters that can not be set
        """
        self.message_service.start_consuming_and_forget()
        self.message_service.publish_to('valawai/c2/treatment_beneficence_valuator/control/parameters', parameters)

        expected_payload = json.dumps(parameters)
        for i in range(11):

            logs = self.__capture_last_logs_from_mov(2)
            for log in logs:

                if 'payload' in log and log['payload'] == expected_payload and 'level' in log and log['level'] == level:
                    # Found the expected log
                    return

        self.fail("Not generated the expected logs to the MOV")

    def test_not_change_age_weight_with_a_bad_value(self):
        """Check that the handler not change the 'age_weight' when it is not valid
        """

        parameters = {
            'age_weight':str(uuid.uuid4())
        }
        self.__assert_process_change_parameters('ERROR', parameters)

    def test_not_change_age_weight_with_a_value_less_than_100(self):
        """Check that the handler not change the 'age_weight' if the value is less than 100
        """

        parameters = {
            'age_weight': -0.00000001-random.random()
        }
        self.__assert_process_change_parameters('ERROR', parameters)

    def test_not_change_age_weight_with_a_value_more_than_1000(self):
        """Check that the handler not change the 'age_weight' if the value is more than 1000
        """

        parameters = {
            'age_weight':random.random()+1.00000000001
        }
        self.__assert_process_change_parameters('ERROR', parameters)

    def test_change_age_weight(self):
        """Check that the handler change the 'age_weight'
        """

        age_weight = random.random()
        parameters = {
            'age_weight':age_weight
        }
        self.__assert_process_change_parameters('INFO', parameters)
        self.assertEqual(str(age_weight), os.getenv("AGE_WEIGHT"))


    def test_change_parameters(self):
        """Check that the handler change the parameters
        """

        age_weight = random.random()
        parameters = {
            'age_weight':age_weight
        }
        self.__assert_process_change_parameters('INFO', parameters)
        self.assertEqual(str(age_weight), os.getenv("AGE_WEIGHT"))

if __name__ == '__main__':
    unittest.main()
