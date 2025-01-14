# This file is part of the C2_treatment_beneficense_valuator distribution (https://github.com/VALAWAI/C2_treatment_beneficence_valuator).
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

from setuptools import setup, find_packages
setup(
    name='C2_Treatment_beneficence_valuator',
    version='1.0.0',
    packages=find_packages(include=['C2_treatment_beneficence_valuator', 'C2_treatment_beneficence_valuator.*']),
    install_requires=[
        'torch>=2.4.0',
        'transformers>=4.44.2',
        'accelerate>=0.33.0',
        'pika>=1.3.2',
        'html2text>=2024.2.26'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)

   