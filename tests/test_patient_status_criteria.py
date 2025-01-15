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
import math
from c2_treatment_beneficence_valuator.patient_status_criteria import PatientStatusCriteria, AgeRangeOption

class TestPatientStatusCriteria(unittest.TestCase):
	"""Class to test the patient status criteria.
	"""
		
	def setUp(self):
		"""Create the criteria for the test.
		"""
		self.criteria = PatientStatusCriteria()
				
	def test_normalized_age_range(self):
		"""Check that is calculated the normalized age range.
		"""
		
		self.criteria.age_range = None
		expected = 0.0
		normalized = self.criteria.normalized_age_range()
		self.assertEqual(normalized, expected)
				
		for value in AgeRangeOption:
			
			self.criteria.age_range = value
			expected += 0.1
			normalized = self.criteria.normalized_age_range()
			self.assertTrue(math.isclose(normalized, expected),f"Unexpected normlaized for {value.name}")
				
if __name__ == '__main__':
    unittest.main()