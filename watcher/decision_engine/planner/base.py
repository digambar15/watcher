# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Authors: Jean-Emile DARTOIS <jean-emile.dartois@b-com.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
The :ref:`Watcher Planner <watcher_planner_definition>` is part of the
:ref:`Watcher Decision Engine <watcher_decision_engine_definition>`.

This module takes the set of :ref:`Actions <action_definition>` generated by a
:ref:`Strategy <strategy_definition>` and builds the design of a workflow which
defines how-to schedule in time those different
:ref:`Actions <action_definition>` and for each
:ref:`Action <action_definition>` what are the prerequisite conditions.

It is important to schedule :ref:`Actions <action_definition>` in time in order
to prevent overload of the :ref:`Cluster <cluster_definition>` while applying
the :ref:`Action Plan <action_plan_definition>`. For example, it is important
not to migrate too many instances at the same time in order to avoid a network
congestion which may decrease the :ref:`SLA <sla_definition>` for
:ref:`Customers <customer_definition>`.

It is also important to schedule :ref:`Actions <action_definition>` in order to
avoid security issues such as denial of service on core OpenStack services.

:ref:`Some default implementations are provided <watcher_planners>`, but it is
possible to :ref:`develop new implementations <implement_planner_plugin>`
which are dynamically loaded by Watcher at launch time.

See :doc:`../architecture` for more details on this component.
"""

import abc
import six

from watcher.common.loader import loadable


@six.add_metaclass(abc.ABCMeta)
class BasePlanner(loadable.Loadable):

    @classmethod
    def get_config_opts(cls):
        """Defines the configuration options to be associated to this loadable

        :return: A list of configuration options relative to this Loadable
        :rtype: list of :class:`oslo_config.cfg.Opt` instances
        """
        return []

    @abc.abstractmethod
    def schedule(self, context, audit_uuid, solution):
        """The planner receives a solution to schedule

        :param solution: A solution provided by a strategy for scheduling
        :type solution: :py:class:`~.BaseSolution` subclass instance
        :param audit_uuid: the audit uuid
        :type audit_uuid: str
        :return: Action plan with an ordered sequence of actions such that all
                 security, dependency, and performance requirements are met.
        :rtype: :py:class:`watcher.objects.ActionPlan` instance
        """
        # example: directed acyclic graph
        raise NotImplementedError()
