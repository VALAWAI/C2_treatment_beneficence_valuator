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
import json

class TestTreatment(unittest.TestCase):
	"""Class to test the treatment
	"""
	
	def __load_treatement_json_as_dict(self):
		"""Obtain the distionary defined in the treatement.json"""

		value = None
		with Path(__file__).parent.joinpath('treatment.json').open() as file:
			value = json.load(file)
		return value
		
		
	def test_from_json(self):
		"""Test can obtain a treatement from a json
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

	def test_not_allow_define_empty_treatment(self):
		"""Test can create an empty treatment
		"""
		error = False
		try:

			treatment = Treatment()
			
		except: 
			error = True
			
		self.assertTrue(error,"Can create empty treatment")

	def test_fail_load_empty_json(self):
		"""Test can not load a treatment form a empty json
		"""
		error = False
		try:
			
			treatment = Treatment.from_json("{}")
			
		except: 
			error = True
			
		self.assertTrue(error,"Can create empty treatment")

	def test_fail_load_treatement_without_id(self):
		"""Test can not load a treatment without identifier
		"""
		error = False
		try:
			
			json_value = self.__load_treatement_json_as_dict();
			del json_value['id']
			treatment = Treatment(**json_value)
			
		except: 
			error = True
			
		self.assertTrue(error,"Can load a treatment without id")

	def test_fail_load_treatement_with_empty_id(self):
		"""Test can not load a treatment with empty identifier
		"""
		error = False
		try:
			
			json_value = self.__load_treatement_json_as_dict();
			json_value['id']=""
			treatment = Treatment(**json_value)
			
		except: 
			error = True
			
		self.assertTrue(error,"Can load a treatment with empty id")

	def test_load_treatement_without_patient_id(self):
		"""Test can load a treatment without a patient identifier
		"""
		json_value = self.__load_treatement_json_as_dict();
		del json_value['patient_id']
		treatment = Treatment(**json_value)
		self.assertIsNone(treatment.patient_id)

	def test_load_treatement_without_created_time(self):
		"""Test can load a treatment without a created time
		"""
		json_value = self.__load_treatement_json_as_dict();
		del json_value['created_time']
		treatment = Treatment(**json_value)
		self.assertIsNone(treatment.created_time)

	def test_fail_load_treatement_without_before_status(self):
		"""Test can not load a treatment without before status
		"""
		error = False
		try:
			
			json_value = self.__load_treatement_json_as_dict();
			del json_value['before_status']
			treatment = Treatment(**json_value)
			
		except: 
			error = True
			
		self.assertTrue(error,"Can load a treatment without before_status")

	def test_fail_load_treatement_without_actions(self):
		"""Test can not load a treatment without actions
		"""
		error = False
		try:
			
			json_value = self.__load_treatement_json_as_dict();
			del json_value['actions']
			treatment = Treatment(**json_value)
			
		except: 
			error = True
			
		self.assertTrue(error,"Can load a treatment without actions")

	def test_fail_load_treatement_with_empty_actions(self):
		"""Test can not load a treatment with empty actions
		"""
		error = False
		try:
			
			json_value = self.__load_treatement_json_as_dict();
			json_value['actions']=[]
			treatment = Treatment(**json_value)
			
		except: 
			error = True
			
		self.assertTrue(error,"Can load a treatment with empty actions")

	def test_load_treatement_without_expected_status(self):
		"""Test can load a treatment without a expected status
		"""
		json_value = self.__load_treatement_json_as_dict();
		del json_value['expected_status']
		treatment = Treatment(**json_value)
		self.assertIsNone(treatment.expected_status)

if __name__ == '__main__':
    unittest.main()