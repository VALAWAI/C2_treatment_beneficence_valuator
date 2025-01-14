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

from treatment_action import TreatmentAction
from patient_status_criteria import PatientStatusCriteria
import json

class Treatment:
	"""The treatment to apply to a patient.
	"""
	
	def __init__(
		self,
		id:str,
		patient_id:str,
		created_time: int,
		before_status: PatientStatusCriteria,
		actions:TreatmentAction[],
		expected_status:PatientStatusCriteria
	):
	"""Create a treatment for a patient.
	
	Parameters
    ----------
    id: str
     	The identifier of the treatment.
    patient_id: str
     	The identifier of the patient that the treatment is applied.
    created_time: int
	 	The epoch time, in seconds, when the patient treatment is created.
	before_status: PatientStatusCriteria
		The status before to apply the treatment.
	actions:TreatmentAction[]
		The treatment actions to apply over the patient.
	expected_status:PatientStatusCriteria
		The expected status of the patient after applying the treatment.
	"""
	
		self.id = id
		self.patient_id = patient_id
		self.created_time = created_time
		self.before_status = before_status
		self.creaactionsted_time = actions
		self.expected_status = expected_status
		
	@classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
	