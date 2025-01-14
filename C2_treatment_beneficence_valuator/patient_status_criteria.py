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
#

from enum import Enum

class AgeRangeOption(Enum):
	"""The different ranges of ages for a patient.
	"""

	# The age is between 0 and 19 years old.
	AGE_BETWEEN_0_AND_19 = 1

	# The age is between 20 and 29 years old.
	AGE_BETWEEN_20_AND_29 = 2

	# The age is between 30 and 39 years old.
	AGE_BETWEEN_30_AND_39 = 3

	# The age is between 40 and 49 years old.
	AGE_BETWEEN_40_AND_49 = 4

	# The age is between 50 and 59 years old.
	AGE_BETWEEN_50_AND_59 = 5

	# The age is between 60 and 69 years old.
	AGE_BETWEEN_60_AND_69 = 6

	# The age is between 70 and 79 years old.
	AGE_BETWEEN_70_AND_79 = 7

	# The age is between 80 and 89 years old.
	AGE_BETWEEN_80_AND_89 = 8

	# The age is between 90 and 99 years old.
	AGE_BETWEEN_90_AND_99 = 9

	# The age greater than 99 years old.
	AGE_MORE_THAN_99 = 10
	
class SurvivalOptions(Enum):
	"""The possible survival options.
	"""

	# The survival is less than 12 month
	LESS_THAN_12_MONTHS = 1

	# The survival is more than 12 month
	MORE_THAN_12_MONTHS = 2

	# The survival is unknown.
	UNKNOWN = 3

class SPICT_Scale(Enum):
	""" It helps identify the most fragile people who have one or more health
		problems. It is based on the comprehensive geriatric assessment (applicable
		to non-geriatric patients) that evaluates areas such as functional
		independence, nutritional status, cognitive, emotional, social, geriatric
		syndromes (confusion syndrome, falls, ulcers, polypharmacy, dysphagia),
		symptoms (pain or dyspnea) and diseases oncological, respiratory, cardiac,
		neurological, digestive or renal).
	"""

	# The low option of the SPICT scale.
	LOW = 1

	# The moderate option of the SPICT scale.
	MODERATE = 2

	# The high option of the SPICT scale.
	HIGH = 3

	# The level in the SPICT scale.
	UNKNOWN = 4
	
class ClinicalRiskGroupOption(Enum):
	""" The possible clinical risk groups.
	"""
	
	# The clinical risk group is promotion & prevention.
	PROMOTION_AND_PREVENTION = 1

	# The clinical risk group is self-management support.
	SELF_MANAGEMENT_SUPPORT =2

	# The clinical risk group is illness management.
	ILLNESS_MANAGEMENT = 3

	# The clinical risk group is case management.
	CASE_MANAGEMENT = 4

	# The clinical risk group is unknown.
	UNKNOWN = 5
	
class BarthelIndex(Enum):
	""" This index allow to check the functional independence for basic activities.
	"""
	
	# When the functional independence is between 0 and 20%.
	TOTAL = 1

	# When the functional independence is between 21 and 60%.
	SEVERE = 2

	# When the functional independence is between 61 and 90%.
	MODERATE = 3

	# When the functional independence is between 91 and 99%.
	MILD = 4

	# When the functional independence is 100%.
	INDEPENDENT = 5

	# When the functional independence is unknown.
	UNKNOWN = 6
	
class CognitiveImpairmentLevel(EMNum):
	""" Define the posible cognitive impairment levels.
	"""
	
	# The cognitive impairment is absent.
	ABSENT = 1

	# The cognitive impairment is mild-moderate.
	MILD_MODERATE = 2

	# cognitive impairment is severe.
	SEVERE = 3
	
	# The cognitive level is unknown.
	UNKNOWN = 4
	
class DiscomfortDegree(Enum):
	""" The degree of discomfort.
	"""
	
	# The discomfort degree is Low or no discomfort.
	LOW = 1

	# The discomfort degree is medium.
	MEDIUM = 2

	# The discomfort degree is medium.
	HIGH =3

	# The cognitive level is unknown.
	UNKNOWN = 4
	
class NITLevel(Enum):
	""" The level of therapeutic intensity.
	"""
	
	# It includes all possible measures to prolong survival
	ONE = 1

	# Includes all possible measures except CPR.
	TWO_A = 2

	# Includes all possible measures except CPR and ICU.
	TWO_B = 3

	# Includes complementary scans and non-invasive treatments.
	THREE = 4

	# It includes empiric symptomatic treatments according to clinical suspicion,
	# which can be agreed as temporary.
	FOUR = 5

	# No complementary examinations or etiological treatments are carried out, only
	# treatments for comfort.
	FIVE = 6
	
class PatientStatusCriteria():
	"""The status of a patient by some criteria.
	"""

	def __init__(
		self,
		age_range: AgeRangeOption,
		ccd: bool,
		maca: bool,
		expected_survival: SurvivalOptions,
		frail_VIG: SPICT_Scale,
		clinical_risk_group: ClinicalRiskGroupOption,
		has_social_support: bool,
		independence_at_admission: BarthelIndex,
		independence_instrumental_activities: int,
		has_advance_directives: bool,
		is_competent: bool,
		has_been_informed: bool,
		is_coerced: bool,
		has_cognitive_impairment: CognitiveImpairmentLevel,
		has_emocional_pain: bool,
		discomfort_degree: DiscomfortDegree,
		nit_level: NITLevel:
	):
	"""Create a patient status.
	
	Parameters
    ----------
	age_range: AgeRangeOption
		The range of age of the patient status.
	ccd: bool
		Check if the patient status has a Complex Cronic Disease (CCD).
	maca: bool
		A MACA patient status has answered no to the question: Would you be surprised
		if this patient died in less than 12 months?
	expected_survival: SurvivalOptions
		The expected survival time for the patient status.
	frail_VIG: SPICT_Scale
		The fragility index of the patient status.
	clinical_risk_group: ClinicalRiskGroupOption
		The clinical risk group of the patient status.
	has_social_support: bool
		Check if the patient status has social support.
	independence_at_admission: BarthelIndex
		The independence for basic activities of daily living at admission.
	independence_instrumental_activities: int
		The index that measures the independence for instrumental activities.
	has_advance_directives: bool
		The answers to the question: Does the patient status have advance directives?
	is_competent: bool
		The answers to the question: Is the patient status competent to understand
		the instructions of health personnel?
	has_been_informed: bool
		The answers to the question: To the patient status or his/her referent
		authorized has been informed of possible treatments and the consequences of
		receiving it or No.
	is_coerced: bool
		The answers to the question: Is it detected that the patient status has seen
		coerced/pressured by third parties?
	has_cognitive_impairment: CognitiveImpairmentLevel
		Inform if the patient status has cognitive impairment.
	has_emocional_pain: bool
		Inform if the patient status has emotional pain.
	discomfort_degree: DiscomfortDegree
		Describe the degree of discomfort of the patient status before applying any action.
	nit_level: NITLevel
		Describe the level of therapeutic intensity of the patient.
	"""
	
		self.age_range = age_range
		self.ccd = ccd
		self.maca = maca
		self.expected_survival = expected_survival
		self.frail_VIG = frail_VIG
		self.clinical_risk_group = clinical_risk_group
		self.has_social_support = has_social_support
		self.independence_at_admission = independence_at_admission
		self.independence_instrumental_activities = independence_instrumental_activities
		self.has_advance_directives = has_advance_directives
		self.is_competent = is_competent
		self.has_been_informed = has_been_informed
		self.is_coerced = is_coerced
		self.has_cognitive_impairment = has_cognitive_impairment
		self.has_emocional_pain = has_emocional_pain
		self.discomfort_degree = discomfort_degree
		self.nit_level = nit_level
