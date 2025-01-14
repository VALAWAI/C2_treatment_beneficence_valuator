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

import unittest
from C2_treatment_beneficence_valuator.treatment import Treatment
from C2_treatment_beneficence_valuator.treatment_action import TreatmentAction

class TestTreatment(unittest.TestCase):
	"""Class to test the treatment
	"""
		
		
	def test_from_json(self):
		"""Test can obtain from json
		"""
				
		value = ''
		with open('treatement.json', 'r') as file:
			value = file.read()
				
		treatment = Treatment.from_json(value)
		self.assertEqual("treatment_1",treatment.id)
		self.assertEqual("patient_1",treatment.patient_id)
		self.assertEqual(1736865373,treatment.created_time)
		self.assertTrue(treatment.before_status != None)
		
		self.assertTrue(treatment.actions != None)
		
		self.assertEqual(1,len(treatment.actions))
		self.assertEqual(TreatmentAction.MEDIUM_CLINICAL_TRIAL,treatment.actions[0])
		
		self.assertTrue(treatment.expected_status != None)
