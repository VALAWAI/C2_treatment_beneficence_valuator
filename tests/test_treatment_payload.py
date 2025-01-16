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

import json
import unittest
from pathlib import Path

from pydantic import ValidationError

from c2_treatment_beneficence_valuator.patient_status_criteria import (
	AgeRangeOption,
	BarthelIndex,
	ClinicalRiskGroupOption,
	CognitiveImpairmentLevel,
	DiscomfortDegree,
	NITLevel,
	SPICT_Scale,
	SurvivalOptions,
)
from c2_treatment_beneficence_valuator.treatment_payload import TreatmentAction, TreatmentPayload


class TestTreatmentPayload(unittest.TestCase):
	"""Class to test the treatment"""

	def __load_treatment_json_as_dict(self):
		"""Obtain the distionary defined in the treatment.json"""

		with Path(__file__).parent.joinpath('treatment.json').open() as file:
			return json.load(file)

	def test_from_json(self):
		"""Test can obtain a treatment from a json"""

		value = ''
		with Path(__file__).parent.joinpath('treatment.json').open() as file:
			value = file.read()

		treatment = TreatmentPayload.from_json(value)
		assert treatment.id == "treatment_1"
		assert treatment.patient_id == "patient_1"
		assert treatment.created_time == 1736865373

		assert treatment.before_status is not None
		assert treatment.before_status.age_range == AgeRangeOption.AGE_BETWEEN_80_AND_89
		assert treatment.before_status.ccd  is False
		assert treatment.before_status.maca
		assert treatment.before_status.expected_survival == SurvivalOptions.LESS_THAN_12_MONTHS
		assert treatment.before_status.frail_VIG == SPICT_Scale.HIGH
		assert treatment.before_status.clinical_risk_group == ClinicalRiskGroupOption.ILLNESS_MANAGEMENT
		assert treatment.before_status.has_social_support  is False
		assert treatment.before_status.independence_at_admission == BarthelIndex.SEVERE
		assert treatment.before_status.independence_instrumental_activities == 6
		assert treatment.before_status.has_advance_directives
		assert treatment.before_status.is_competent
		assert treatment.before_status.has_been_informed  is False
		assert treatment.before_status.is_coerced
		assert treatment.before_status.has_cognitive_impairment == CognitiveImpairmentLevel.MILD_MODERATE
		assert treatment.before_status.has_emocional_pain is False
		assert treatment.before_status.discomfort_degree == DiscomfortDegree.LOW
		assert treatment.before_status.nit_level == NITLevel.TWO_A

		assert treatment.actions is not None
		assert len(treatment.actions) == 1
		assert treatment.actions[0] == TreatmentAction.MEDIUM_CLINICAL_TRIAL

		assert treatment.expected_status is None

	def test_not_allow_define_empty_payload(self):
		"""Test can create an empty treatment"""

		error = False
		try:

			treatment = TreatmentPayload()
			assert treatment is None

		except ValidationError:
			error = True

		# Can create empty treatment
		assert error

	def test_fail_load_empty_json(self):
		"""Test can not load a treatment from an empty json"""

		error = False
		try:

			treatment = TreatmentPayload.from_json("{}")
			assert treatment is None

		except ValidationError:
			error = True

		# Can create empty treatment
		assert error

	def test_fail_load_treatment_with_bad_field(self):
		"""Test can not load a treatment with a bad field"""

		error = False
		try:

			json_value = self.__load_treatment_json_as_dict()
			json_value['undefined_field']="Undefined value"
			treatment = TreatmentPayload(**json_value)
			assert treatment is None

		except ValidationError:
			error = True

		# Can load a treatment with an undefined field
		assert error

	def test_fail_load_treatment_without_id(self):
		"""Test can not load a treatment without identifier"""

		error = False
		try:

			json_value = self.__load_treatment_json_as_dict()
			del json_value['id']
			treatment = TreatmentPayload(**json_value)
			assert treatment is None

		except ValidationError:
			error = True

		# Can load a treatment without id
		assert error

	def test_fail_load_treatment_with_empty_id(self):
		"""Test can not load a treatment with empty identifier"""

		error = False
		try:

			json_value = self.__load_treatment_json_as_dict()
			json_value['id']=""
			treatment = TreatmentPayload(**json_value)
			assert treatment is None

		except ValidationError:
			error = True

		# Can load a treatment with empty id
		assert error

	def test_load_treatment_without_patient_id(self):
		"""Test can load a treatment without a patient identifier"""

		json_value = self.__load_treatment_json_as_dict()
		del json_value['patient_id']
		treatment = TreatmentPayload(**json_value)
		assert treatment.patient_id is None

	def test_load_treatment_without_created_time(self):
		"""Test can load a treatment without a created time"""

		json_value = self.__load_treatment_json_as_dict()
		del json_value['created_time']
		treatment = TreatmentPayload(**json_value)
		assert treatment.created_time is None

	def test_fail_load_treatment_without_before_status(self):
		"""Test can not load a treatment without before status"""

		error = False
		try:

			json_value = self.__load_treatment_json_as_dict()
			del json_value['before_status']
			treatment = TreatmentPayload(**json_value)
			assert treatment is None

		except ValidationError:

			error = True

		# Can load a treatment without before_status
		assert error

	def test_fail_load_treatment_without_actions(self):
		"""Test can not load a treatment without actions"""

		error = False
		try:

			json_value = self.__load_treatment_json_as_dict()
			del json_value['actions']
			treatment = TreatmentPayload(**json_value)
			assert treatment is None

		except ValidationError:
			error = True

		# Can load a treatment with empty actions
		assert error

	def test_fail_load_treatment_with_empty_actions(self):
		"""Test can not load a treatment with empty actions"""

		error = False
		try:

			json_value = self.__load_treatment_json_as_dict()
			json_value['actions']=[]
			treatment = TreatmentPayload(**json_value)
			assert treatment is None

		except ValidationError:

			error = True

		# Can load a treatment with empty actions
		assert error

	def test_load_treatment_without_expected_status(self):
		"""Test can load a treatment without a expected status"""

		json_value = self.__load_treatment_json_as_dict()
		del json_value['expected_status']
		treatment = TreatmentPayload(**json_value)
		assert treatment.expected_status is None

if __name__ == '__main__':
    unittest.main()
