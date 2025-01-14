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

class TreatmentAction(Enum):
	"""The possible action to do for a treatment.
	"""

	# The patient can receive a Cardiopulmonary resuscitation.
	CPR = 1

	
	# The patient need an organ transplant.
	TRANSPLANT = 2

	# The patient can be in the intensive curing unit.
	ICU = 3

	
	# The patient can have non-invasive mechanical ventilation.
	NIMV = 4

	
	# The patient can receive vasoactive drugs.	
	VASOACTIVE_DRUGS = 5

	
	# The patient can have dialysis.	
	DIALYSIS = 6

	
	# The patient can receive simple clinical trials.	
	SIMPLE_CLINICAL_TRIAL = 7

	
	# The patient can receive medium clinical trials.	
	MEDIUM_CLINICAL_TRIAL = 8

	
	# The patient can receive advanced clinical trials.	
	ADVANCED_CLINICAL_TRIAL = 9

	
	# The patient can have palliative surgery.	
	PALLIATIVE_SURGERY = 10

	
	# The patient can have surgery with the intention of curing.	
	CURE_SURGERY = 11
