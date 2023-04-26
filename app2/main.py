# Copyright 2023 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

from lib import hello_world, requests_version, pyyaml_version


def binary_version():
    return requests.__version__


hello_world()
print(binary_version())
print(requests_version())
print(pyyaml_version())
print("HEEEEEEEEEEEEELLLLLLLLOOOOOOOOOOOOOO!!!!!!!!!!!1")
