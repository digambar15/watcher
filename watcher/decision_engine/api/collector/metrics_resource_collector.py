# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class MetricsResourceCollector(object):
    def __init__(self):
        pass

    def get_average_usage_vm_cpu(self, uuid):
        raise NotImplementedError("Should have implemented this")

    def get_average_usage_vm_memory(self, uuid):
        raise NotImplementedError("Should have implemented this")

    def get_virtual_machine_capacity(self, uuid):
        raise NotImplementedError("Should have implemented this")

    def get_average_network_incomming(self, uuid):
        raise NotImplementedError("Should have implemented this")

    def get_average_network_outcomming(self, uuid):
        raise NotImplementedError("Should have implemented this")