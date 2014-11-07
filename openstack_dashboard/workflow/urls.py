# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
URL patterns for the OpenStack Dashboard.
"""

from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa
from django.views.generic import TemplateView
from openstack_dashboard.workflow import launch
from openstack_dashboard.workflow import keypair

urlpatterns = patterns(
    '',
    url(r'^launch$', launch.LaunchInstanceView.as_view(),
        name='launch'),
    url(r'^launchTemplate$',
        TemplateView.as_view(template_name="workflow/launch.html"),
        name="launchTemplate"),
    url(r'^keypair$', keypair.KeypairView.as_view(),
        name='keypair'),
    url(r'^keypairCreateTemplate$',
        TemplateView.as_view(template_name="workflow/keypairCreate.html"),
        name="keypairCreateTemplate"),
    url(r'^keypairImportTemplate$',
        TemplateView.as_view(template_name="workflow/keypairImport.html"),
        name="keypairImportTemplate"),
)