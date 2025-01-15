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

class BeneficienceValuator(object):
	"""The component that ovtain the benificence value from a patient treatement.
	"""
		
	def __init__(self,
		age_range_weigth:float = float(os.getenv('AGE_RANGE_WEIGHT',"0.04")),
		ccd_weigth:float = float(os.getenv('CCD_WEIGHT',"0.04")),
		maca_weigth:float = float(os.getenv('MACA_WEIGHT',"0.04")),
		expected_survival_weigth:float = float(os.getenv('EXPECTED_SURVIVAL_WEIGHT',"0.326")),
		frail_VIG_weigth:float = float(os.getenv('FRAIL_VIG_WEIGHT',"0.065")),
		clinical_risk_group_weigth:float = float(os.getenv('CLINICAL_RISK_GROUP_WEIGHT',"0.033")),
		has_social_support_weigth:float = float(os.getenv('HAS_SOCIAL_SUPPORT_WEIGHT',"0.000")),
		independence_at_admission_weigth:float = float(os.getenv('INDEPENDENCE_AT_ADMISSION_WEIGHT',"0.163")),
		independence_instrumental_activities_weigth:float = float(os.getenv('INDEPENDENCE_INSTRUMENTAL_ACTIVITIES_WEIGHT',"0.163")),
		has_advance_directives_weigth:float = float(os.getenv('HAS_ADVANCE_DIRECTIVES_WEIGHT',"0.057")),
		is_competent_weigth:float = float(os.getenv('IS_COMPETENT_WEIGHT',"0.000")),
		has_been_informed_weigth:float = float(os.getenv('HAS_BEEN_INFORMED_WEIGHT',"0.000")),
		is_coerced_weigth:float = float(os.getenv('IS_COERCED_WEIGHT',"0.000")),
		has_cognitive_impairment_weigth:float = float(os.getenv('HAS_COGNITIVE_IMPAIRMENT_WEIGHT',"0.016")),
		has_emocional_pain_weigth:float = float(os.getenv('HAS_EMOCIONAL_PAIN_WEIGHT',"0.000")),
		discomfort_degree_weigth:float = float(os.getenv('DISCOMFORT_DEGREE_WEIGHT',"0.057"))
		):
		"""Initialize the beneficience valuator

		Parameters
		----------
		age_range_weigth: float
			The importance of the age range when calculate the beneficeince value.
		ccd_weigth: float
			The importance of the ccd when calculate the beneficeince value.
		maca_weigth: float
			The importance of the MACA when calculate the beneficeince value.
		expected_survival_weigth: float
			The importance of the expected survival when calculate the beneficeince value.
		frail_VIG_weigth: float
			The importance of the frail VIG when calculate the beneficeince value.
		clinical_risk_group_weigth: float
			The importance of the clinical risk group when calculate the beneficeince value.
		has_social_support_weigth: float
			The importance of the has social support_weigth when calculate the beneficeince value.
		independence_at_admission_weigth: float
			The importance of the independence at admission weigth when calculate the beneficeince value.
		independence_instrumental_activities_weigth: float
			The importance of the independence instrumental activities when calculate the beneficeince value.
		has_advance_directives_weigth: float
			The importance of the has advance directives when calculate the beneficeince value.
		is_competent_weigth: float
			The importance of the is competent when calculate the beneficeince value.
		has_been_informed_weigth: float
			The importance of the has been informed when calculate the beneficeince value.
		is_coerced_weigth: float
			The importance of the is coerced when calculate the beneficeince value.
		has_cognitive_impairment_weigth: float
			The importance of the has cognitive impairment when calculate the beneficeince value.
		has_emocional_pain_weigth: float
			The importance of the has emocional pain when calculate the beneficeince value.
		discomfort_degree_weigth: float
			The importance of the discomfort degree when calculate the beneficeince value.
		"""
		self.age_range_weigth = age_range_weigth
		self.ccd_weigth = ccd_weigth
		self.maca_weigth = maca_weigth
		self.expected_survival_weigth = expected_survival_weigth
		self.frail_VIG_weigth = frail_VIG_weigth
		self.clinical_risk_group_weigth = clinical_risk_group_weigth
		self.has_social_support_weigth = has_social_support_weigth
		self.independence_at_admission_weigth = independence_at_admission_weigth
		self.independence_instrumental_activities_weigth = independence_instrumental_activities_weigth
		self.has_advance_directives_weigth = has_advance_directives_weigth
		self.is_competent_weigth = is_competent_weigth
		self.has_been_informed_weigth = has_been_informed_weigth
		self.is_coerced_weigth = is_coerced_weigth
		self.has_cognitive_impairment_weigth = has_cognitive_impairment_weigth
		self.has_emocional_pain_weigth = has_emocional_pain_weigth
		self.discomfort_degree_weigth = discomfort_degree_weigth


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

		if treatment.expected_status != None:
			
			alignment += self.age_range_weigth * (treatment.expected_status.normalized_age_range() - treatment.before_status.normalized_age_range()) 
			alignment += self.ccd_weigth * (treatment.expected_status.normalized_ccd() - treatment.before_status.normalized_ccd()) 
			alignment += self.maca_weigth * (treatment.expected_status.normalized_maca() - treatment.before_status.normalized_maca()) 
			alignment += self.expected_survival_weigth * (treatment.expected_status.normalized_expected_survival() - treatment.before_status.normalized_expected_survival()) 
			alignment += self.frail_VIG_weigth * (treatment.expected_status.normalized_frail_VIG() - treatment.before_status.normalized_frail_VIG()) 
			alignment += self.clinical_risk_group_weigth * (treatment.expected_status.normalized_clinical_risk_group() - treatment.before_status.normalized_clinical_risk_group()) 
			alignment += self.has_social_support_weigth * (treatment.expected_status.normalized_has_social_support() - treatment.before_status.normalized_has_social_support()) 
			alignment += self.independence_at_admission_weigth * (treatment.expected_status.normalized_independence_at_admission() - treatment.before_status.normalized_independence_at_admission()) 
			alignment += self.independence_instrumental_activities_weigth * (treatment.expected_status.normalized_independence_instrumental_activities() - treatment.before_status.normalized_independence_instrumental_activities()) 
			alignment += self.has_advance_directives_weigth * (treatment.expected_status.normalized_has_advance_directives() - treatment.before_status.normalized_has_advance_directives()) 
			alignment += self.is_competent_weigth * (treatment.expected_status.normalized_is_competent() - treatment.before_status.normalized_is_competent()) 
			alignment += self.has_been_informed_weigth * (treatment.expected_status.normalized_has_been_informed() - treatment.before_status.normalized_has_been_informed()) 
			alignment += self.is_coerced_weigth * (treatment.expected_status.normalized_is_coerced() - treatment.before_status.normalized_is_coerced()) 
			alignment += self.has_cognitive_impairment_weigth * (treatment.expected_status.normalized_has_cognitive_impairment() - treatment.before_status.normalized_has_cognitive_impairment()) 
			alignment += self.has_emocional_pain_weigth * (treatment.expected_status.normalized_has_emocional_pain() - treatment.before_status.normalized_has_emocional_pain()) 
			alignment += self.discomfort_degree_weigth * (treatment.expected_status.normalized_discomfort_degree() - treatment.before_status.normalized_discomfort_degree()) 

		return alignment