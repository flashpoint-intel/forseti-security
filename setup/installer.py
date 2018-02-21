# Copyright 2017 The Forseti Security Authors. All rights reserved.
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

""" Forseti Installer.

A stub to call gcp/run_forseti_installer.py which installs into GCP.
"""

import getpass
import pip

INSTALLER_REQUIRED_PACKAGES = [
    'ruamel.yaml'
]

def install(package_name):
    """Install package.

    Args:
        package_name (str): Name of the package to install.
    """
    user = getpass.getuser()
    pip.main(['install', package_name, '--user', user])


def install_required_packages():
    """Install required packages."""
    for package in INSTALLER_REQUIRED_PACKAGES:
        install(package)


if __name__ == '__main__':
    # We need to install all the required packages before importing our modules

    # Installing required packages
    install_required_packages()

    # Importing our own modules
    from gcp import run_forseti_installer
    run_forseti_installer.run()
