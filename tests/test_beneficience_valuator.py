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

import unittest
from C2_treatment_beneficence_valuator.beneficience_valuator import BeneficienceValuator
from C2_treatment_beneficence_valuator.treatment import Treatment

class TestBeneficienceValuator(unittest.TestCase):
    """Class to test the beneficience valuator
    """
    
    def setUp(self):
        """Create the valuator.
        """
        self.valuator = BeneficienceValuator()
    
    def test_generate_reply(self):
        """Test the reply generation
        """
        
		value = ''
		with open('treatement.json', 'r') as file:
			value = file.read()
				
		treatment = Treatment.from_json(value)
        
        alignment = self.generator.align_beneficence(treatment)
        self.assertEquals(alignment,0.39184,"Unexpected treatment beneficience alignment vlaue")
