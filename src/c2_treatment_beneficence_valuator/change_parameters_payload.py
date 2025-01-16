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

import json

from pydantic import BaseModel, Field


class ChangeParametersPayload(BaseModel):
	"""The payload of the message to change the parameters of teh component."""

	age_range_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the age range when calculate the beneficeince value.")
	ccd_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the ccd when calculate the beneficeince value.")
	maca_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the MACA when calculate the beneficeince value.")
	expected_survival_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the expected survival when calculate the beneficeince value.")
	frail_VIG_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the frail VIG when calculate the beneficeince value.")
	clinical_risk_group_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the clinical risk group when calculate the beneficeince value.")
	has_social_support_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has social support_weight when calculate the beneficeince value.")
	independence_at_admission_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the independence at admission weight when calculate the beneficeince value.")
	independence_instrumental_activities_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the independence instrumental activities when calculate the beneficeince value.")
	has_advance_directives_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has advance directives when calculate the beneficeince value.")
	is_competent_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the is competent when calculate the beneficeince value.")
	has_been_informed_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has been informed when calculate the beneficeince value.")
	is_coerced_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the is coerced when calculate the beneficeince value.")
	has_cognitive_impairment_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has cognitive impairment when calculate the beneficeince value.")
	has_emocional_pain_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has emocional pain when calculate the beneficeince value.")
	discomfort_degree_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the discomfort degree when calculate the beneficeince value.")

	@classmethod
	def from_json(cls, json_value:str):
		"""Loads a change parameters from a JSON inside a string.

		Parameters
		----------
		json_value: str
			The encoded change parameters in JSON.

		Returns
		----------
		ChangeParametersPayload
			The model encoded in the JSON.
		"""
		json_dict = json.loads(json_value)
		return ChangeParametersPayload(**json_dict)
