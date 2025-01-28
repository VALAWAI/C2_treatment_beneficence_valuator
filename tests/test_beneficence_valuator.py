#
# This file is part of the C2_treatment_beneficence_valuator distribution
# (https://github.com/VALAWAI/C2_treatment_beneficence_valuator).
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

import math
import unittest

from json_resources import load_treatment_json

from c2_treatment_beneficence_valuator.beneficence_valuator import BeneficenceValuator
from c2_treatment_beneficence_valuator.patient_status_criteria import PatientStatusCriteria
from c2_treatment_beneficence_valuator.treatment_payload import TreatmentPayload


class TestBeneficenceValuator(unittest.TestCase):
	"""Class to test the beneficence valuator
	"""

	def setUp(self):
		"""Create the valuator.
		"""
		self.valuator = BeneficenceValuator(
				age_range_weight=0.04,
				ccd_weight=0.04,
				maca_weight=0.04,
				expected_survival_weight=0.326,
				frail_VIG_weight=0.065,
				clinical_risk_group_weight=0.033,
				has_social_support_weight=0.0,
				independence_at_admission_weight=0.163,
				independence_instrumental_activities_weight=0.163,
				has_advance_directives_weight=0.057,
				is_competent_weight=0.0,
				has_been_informed_weight=0.0,
				is_coerced_weight=0.0,
				has_cognitive_impairment_weight=0.016,
				has_emocional_pain_weight=0.0,
				discomfort_degree_weight=0.057
			)


	def test_align_beneficence(self):
		"""Test calculate alignment for a treatment
		"""

		treatment = TreatmentPayload(**load_treatment_json())
		alignment = self.valuator.align_beneficence(treatment)
		assert math.isclose(alignment, 0.39184), 'Unexpected treatment beneficence alignment value'

	def test_align_beneficence_for_treatment_without_expected_status(self):
		"""Test calculate alignment with an empty treatment
		"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.expected_status = None
		alignment = self.valuator.align_beneficence(treatment)
		assert math.isclose(alignment, 0.0), 'Unexpected treatment beneficence alignment value'

	def test_align_beneficence_for_treatment_with_empty_expected_status(self):
		"""Test calculate alignment with an empty treatment
		"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.expected_status = PatientStatusCriteria()
		alignment = self.valuator.align_beneficence(treatment)
		assert math.isclose(alignment, -0.38145), 'Unexpected treatment beneficence alignment value'

if __name__ == '__main__':
    unittest.main()
