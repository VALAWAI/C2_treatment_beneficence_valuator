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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import unittest
from c2_treatment_beneficence_valuator.beneficience_valuator import BeneficienceValuator
from c2_treatment_beneficence_valuator.treatment import Treatment
from c2_treatment_beneficence_valuator.patient_status_criteria import PatientStatusCriteria
from pathlib import Path
import math
import json

class TestBeneficienceValuator(unittest.TestCase):
	"""Class to test the beneficience valuator
	"""
  
	def setUp(self):
		"""Create the valuator.
		"""
		self.valuator = BeneficienceValuator()
		self.treatment_json_str = ''
		with Path(__file__).parent.joinpath('treatment.json').open() as file:
			self.treatment_json_str = file.read()
  
	def test_align_beneficence(self):
		"""Test calculate alignment for a treatment
		"""
    
		treatment = Treatment.from_json(self.treatment_json_str)
    
		alignment = self.valuator.align_beneficence(treatment)
		self.assertTrue(math.isclose(alignment, 0.39184),"Unexpected treatment beneficience alignment value")

	def test_align_beneficence_for_treatment_without_expected_status(self):
		"""Test calculate alignment with an empty treatment
		"""
    
		treatment_dict = json.loads(self.treatment_json_str)
		del treatment_dict['expected_status']
		treatment = Treatment(**treatment_dict)
		alignment = self.valuator.align_beneficence(treatment)
		self.assertTrue(math.isclose(alignment, 0.0),"Unexpected treatment beneficience alignment value")

	def test_align_beneficence_for_treatment_with_empty_expected_status(self):
		"""Test calculate alignment with an empty treatment
		"""
    
		treatment = Treatment.from_json(self.treatment_json_str)
		treatment.expected_status = PatientStatusCriteria()
		alignment = self.valuator.align_beneficence(treatment)
		self.assertTrue(math.isclose(alignment, -0.32445),"Unexpected treatment beneficience alignment value")

if __name__ == '__main__':
    unittest.main()