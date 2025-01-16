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

import os

from treatment import Treatment


class BeneficienceValuator:
	"""The component that ovtain the benificence value from a patient treatement.
	"""

	def __init__(self,
		age_range_weight:float = float(os.getenv('AGE_RANGE_WEIGHT',"0.04")),
		ccd_weight:float = float(os.getenv('CCD_WEIGHT',"0.04")),
		maca_weight:float = float(os.getenv('MACA_WEIGHT',"0.04")),
		expected_survival_weight:float = float(os.getenv('EXPECTED_SURVIVAL_WEIGHT',"0.326")),
		frail_VIG_weight:float = float(os.getenv('FRAIL_VIG_WEIGHT',"0.065")),
		clinical_risk_group_weight:float = float(os.getenv('CLINICAL_RISK_GROUP_WEIGHT',"0.033")),
		has_social_support_weight:float = float(os.getenv('HAS_SOCIAL_SUPPORT_WEIGHT',"0.000")),
		independence_at_admission_weight:float = float(os.getenv('INDEPENDENCE_AT_ADMISSION_WEIGHT',"0.163")),
		independence_instrumental_activities_weight:float = float(os.getenv('INDEPENDENCE_INSTRUMENTAL_ACTIVITIES_WEIGHT',"0.163")),
		has_advance_directives_weight:float = float(os.getenv('HAS_ADVANCE_DIRECTIVES_WEIGHT',"0.057")),
		is_competent_weight:float = float(os.getenv('IS_COMPETENT_WEIGHT',"0.0")),
		has_been_informed_weight:float = float(os.getenv('HAS_BEEN_INFORMED_WEIGHT',"0.0")),
		is_coerced_weight:float = float(os.getenv('IS_COERCED_WEIGHT',"0.0")),
		has_cognitive_impairment_weight:float = float(os.getenv('HAS_COGNITIVE_IMPAIRMENT_WEIGHT',"0.016")),
		has_emocional_pain_weight:float = float(os.getenv('HAS_EMOCIONAL_PAIN_WEIGHT',"0.0")),
		discomfort_degree_weight:float = float(os.getenv('DISCOMFORT_DEGREE_WEIGHT',"0.057"))
		):
		"""Initialize the beneficience valuator

		Parameters
		----------
		age_range_weight: float
			The importance of the age range when calculate the beneficeince value.
		ccd_weight: float
			The importance of the ccd when calculate the beneficeince value.
		maca_weight: float
			The importance of the MACA when calculate the beneficeince value.
		expected_survival_weight: float
			The importance of the expected survival when calculate the beneficeince value.
		frail_VIG_weight: float
			The importance of the frail VIG when calculate the beneficeince value.
		clinical_risk_group_weight: float
			The importance of the clinical risk group when calculate the beneficeince value.
		has_social_support_weight: float
			The importance of the has social support_weight when calculate the beneficeince value.
		independence_at_admission_weight: float
			The importance of the independence at admission weight when calculate the beneficeince value.
		independence_instrumental_activities_weight: float
			The importance of the independence instrumental activities when calculate the beneficeince value.
		has_advance_directives_weight: float
			The importance of the has advance directives when calculate the beneficeince value.
		is_competent_weight: float
			The importance of the is competent when calculate the beneficeince value.
		has_been_informed_weight: float
			The importance of the has been informed when calculate the beneficeince value.
		is_coerced_weight: float
			The importance of the is coerced when calculate the beneficeince value.
		has_cognitive_impairment_weight: float
			The importance of the has cognitive impairment when calculate the beneficeince value.
		has_emocional_pain_weight: float
			The importance of the has emocional pain when calculate the beneficeince value.
		discomfort_degree_weight: float
			The importance of the discomfort degree when calculate the beneficeince value.
		"""
		self.age_range_weight = age_range_weight
		self.ccd_weight = ccd_weight
		self.maca_weight = maca_weight
		self.expected_survival_weight = expected_survival_weight
		self.frail_VIG_weight = frail_VIG_weight
		self.clinical_risk_group_weight = clinical_risk_group_weight
		self.has_social_support_weight = has_social_support_weight
		self.independence_at_admission_weight = independence_at_admission_weight
		self.independence_instrumental_activities_weight = independence_instrumental_activities_weight
		self.has_advance_directives_weight = has_advance_directives_weight
		self.is_competent_weight = is_competent_weight
		self.has_been_informed_weight = has_been_informed_weight
		self.is_coerced_weight = is_coerced_weight
		self.has_cognitive_impairment_weight = has_cognitive_impairment_weight
		self.has_emocional_pain_weight = has_emocional_pain_weight
		self.discomfort_degree_weight = discomfort_degree_weight


	def align_beneficence(self,treatment:Treatment):
		"""Calculate the alignemnt of a treatemnt with the beneficence value.

		Parameters
		----------
		treatment : Treatment
			The treatemnt to apply inot a patient

		Returns
		-------
		float
			The align,ment of the treatment with the beneficence value.
		"""

		alignment = 0.0

		if treatment.expected_status is not None:

			alignment += self.age_range_weight * (treatment.expected_status.normalized_age_range() - treatment.before_status.normalized_age_range())
			alignment += self.ccd_weight * (treatment.expected_status.normalized_ccd() - treatment.before_status.normalized_ccd())
			alignment += self.maca_weight * (treatment.expected_status.normalized_maca() - treatment.before_status.normalized_maca())
			alignment += self.expected_survival_weight * (treatment.expected_status.normalized_expected_survival() - treatment.before_status.normalized_expected_survival())
			alignment += self.frail_VIG_weight * (treatment.expected_status.normalized_frail_VIG() - treatment.before_status.normalized_frail_VIG())
			alignment += self.clinical_risk_group_weight * (treatment.expected_status.normalized_clinical_risk_group() - treatment.before_status.normalized_clinical_risk_group())
			alignment += self.has_social_support_weight * (treatment.expected_status.normalized_has_social_support() - treatment.before_status.normalized_has_social_support())
			alignment += self.independence_at_admission_weight * (treatment.expected_status.normalized_independence_at_admission() - treatment.before_status.normalized_independence_at_admission())
			alignment += self.independence_instrumental_activities_weight * (treatment.expected_status.normalized_independence_instrumental_activities() - treatment.before_status.normalized_independence_instrumental_activities())
			alignment += self.has_advance_directives_weight * (treatment.expected_status.normalized_has_advance_directives() - treatment.before_status.normalized_has_advance_directives())
			alignment += self.is_competent_weight * (treatment.expected_status.normalized_is_competent() - treatment.before_status.normalized_is_competent())
			alignment += self.has_been_informed_weight * (treatment.expected_status.normalized_has_been_informed() - treatment.before_status.normalized_has_been_informed())
			alignment += self.is_coerced_weight * (treatment.expected_status.normalized_is_coerced() - treatment.before_status.normalized_is_coerced())
			alignment += self.has_cognitive_impairment_weight * (treatment.expected_status.normalized_has_cognitive_impairment() - treatment.before_status.normalized_has_cognitive_impairment())
			alignment += self.has_emocional_pain_weight * (treatment.expected_status.normalized_has_emocional_pain() - treatment.before_status.normalized_has_emocional_pain())
			alignment += self.discomfort_degree_weight * (treatment.expected_status.normalized_discomfort_degree() - treatment.before_status.normalized_discomfort_degree())

		return alignment
