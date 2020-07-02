# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdataworks_public.endpoint import endpoint_data

class ListRemindsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListReminds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SearchText(self):
		return self.get_body_params().get('SearchText')

	def set_SearchText(self,SearchText):
		self.add_body_params('SearchText', SearchText)

	def get_Founder(self):
		return self.get_body_params().get('Founder')

	def set_Founder(self,Founder):
		self.add_body_params('Founder', Founder)

	def get_RemindTypes(self):
		return self.get_body_params().get('RemindTypes')

	def set_RemindTypes(self,RemindTypes):
		self.add_body_params('RemindTypes', RemindTypes)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_AlertTarget(self):
		return self.get_body_params().get('AlertTarget')

	def set_AlertTarget(self,AlertTarget):
		self.add_body_params('AlertTarget', AlertTarget)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_NodeId(self):
		return self.get_body_params().get('NodeId')

	def set_NodeId(self,NodeId):
		self.add_body_params('NodeId', NodeId)