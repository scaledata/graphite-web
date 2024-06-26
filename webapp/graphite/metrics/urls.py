"""Copyright 2009 Chris Davis

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^/index\.json$', views.index_json, name='metrics_index'),
    re_path(r'^/find/?$', views.find_view, name='metrics_find'),
    re_path(r'^/expand/?$', views.expand_view, name='metrics_expand'),
    re_path(r'^/get-metadata/?$', views.get_metadata_view,
        name='metrics_get_metadata'),
    re_path(r'^/set-metadata/?$', views.set_metadata_view,
        name='metrics_set_metadata'),
    re_path(r'^/?$', views.find_view, name='metrics'),
]
