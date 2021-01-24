"""StoppingCriteria class"""

"""
Copyright (c) 2016-2020, EPFL/Blue Brain Project
 This file is part of BluePyOpt <https://github.com/BlueBrain/BluePyOpt>
 This library is free software; you can redistribute it and/or modify it under
 the terms of the GNU Lesser General Public License version 3.0 as published
 by the Free Software Foundation.
 This library is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
 details.
 You should have received a copy of the GNU Lesser General Public License
 along with this library; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# pylint: disable=R0912, R0914

import logging
import numpy

import bluepyopt.stoppingCriteria

logger = logging.getLogger('__main__')


class MaxNGen(bluepyopt.stoppingCriteria.StoppingCriteria):
    """Max ngen stopping criteria class"""
    name = "Max ngen"

    def __init__(self, max_ngen):
        """Constructor"""
        super(MaxNGen, self).__init__()
        self.max_ngen = max_ngen
        self.min_hof = 0
        self.cnt = 0
    def check(self, kwargs):
        """Check if the maximum number of iteration is reached"""
        gen = kwargs.get("gen")
        hof = kwargs.get("hof")

        if gen > self.max_ngen:
            self.criteria_met = True
        if hof == self.min_hof:
            self.cnt+=1
            # the HOF might be zero, but also want population to converge around 
            # zero, this requires generations.
            if self.cnt>7:
                self.criteria_met = True
