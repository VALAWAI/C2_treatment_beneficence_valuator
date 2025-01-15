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
					 age_weigth:float=float(os.getenv('AGE_WEIGHT',"0.040"))):
		"""Initialize the beneficience valuator

		Parameters
		----------
		age_weigth : float
			The importance of the age when calculate the beneficeince value.
		"""
		self.age_weigth = age_weigth

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

			#for i in range(N_CRITERIA):
			#		alignment += weights[i] * (post_criteria[i] - precriteria[i])

		return alignment