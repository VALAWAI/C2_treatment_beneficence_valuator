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
from c2_treatment_beneficence_valuator.treatment import Treatment, TreatmentAction
from c2_treatment_beneficence_valuator.patient_status_criteria import AgeRangeOption, SurvivalOptions, SPICT_Scale, ClinicalRiskGroupOption, BarthelIndex, CognitiveImpairmentLevel, DiscomfortDegree, NITLevel
from pathlib import Path

class TestTreatment(unittest.TestCase):
	"""Class to test the treatment
	"""
		
		
	def test_from_json(self):
		"""Test can obtain from json
		"""
				
		value = ''
		with Path(__file__).parent.joinpath('treatment.json').open() as file:
			value = file.read()
				
		treatment = Treatment.from_json(value)
		self.assertEqual("treatment_1",treatment.id)
		self.assertEqual("patient_1",treatment.patient_id)
		self.assertEqual(1736865373,treatment.created_time)
		
		self.assertTrue(treatment.before_status != None)
		self.assertEqual(AgeRangeOption.AGE_BETWEEN_80_AND_89,treatment.before_status.age_range)
		self.assertFalse(treatment.before_status.ccd)
		self.assertTrue(treatment.before_status.maca)
		self.assertEqual(SurvivalOptions.LESS_THAN_12_MONTHS,treatment.before_status.expected_survival)
		self.assertEqual(SPICT_Scale.HIGH,treatment.before_status.frail_VIG)
		self.assertEqual(ClinicalRiskGroupOption.ILLNESS_MANAGEMENT,treatment.before_status.clinical_risk_group)
		self.assertFalse(treatment.before_status.has_social_support)
		self.assertEqual(BarthelIndex.SEVERE,treatment.before_status.independence_at_admission)
		self.assertEqual(6,treatment.before_status.independence_instrumental_activities)
		self.assertTrue(treatment.before_status.has_advance_directives)
		self.assertTrue(treatment.before_status.is_competent)
		self.assertFalse(treatment.before_status.has_been_informed)
		self.assertTrue(treatment.before_status.is_coerced)
		self.assertEqual(CognitiveImpairmentLevel.MILD_MODERATE,treatment.before_status.has_cognitive_impairment)
		self.assertFalse(treatment.before_status.has_emocional_pain)
		self.assertEqual(DiscomfortDegree.LOW,treatment.before_status.discomfort_degree)
		self.assertEqual(NITLevel.TWO_A,treatment.before_status.nit_level)
		
		self.assertTrue(treatment.actions != None)
		self.assertEqual(1,len(treatment.actions))
		self.assertEqual(TreatmentAction.MEDIUM_CLINICAL_TRIAL,treatment.actions[0])
		
		self.assertTrue(treatment.expected_status != None)

		
if __name__ == '__main__':
    unittest.main()