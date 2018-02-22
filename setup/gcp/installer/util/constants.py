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

"""Constants used for the setup of Forseti."""

import os
from enum import Enum


class FirewallRuleAction(Enum):
    """Firewall rule action object."""
    ALLOW = 'ALLOW'
    DENY = 'DENY'


class FirewallRuleDirection(Enum):
    """Firewall rule direction object."""
    INGRESS = 'INGRESS'
    EGRESS = 'EGRESS'


MAXIMUM_LOOP_COUNT = 600

DEFAULT_BUCKET_FMT_V1 = 'gs://{}-data-{}'
DEFAULT_BUCKET_FMT_V2 = 'gs://{}-{}-data-{}'

REGEX_MATCH_FORSETI_V1_INSTANCE_NAME = r'^forseti-security-\d+-vm$'

FORSETI_V1_RULE_FILES = [
    'bigquery_rules.yaml',
    'blacklist_rules.yaml',
    'bucket_rules.yaml',
    'cloudsql_rules.yaml',
    'firewall_rules.yaml',
    'forwarding_rules.yaml',
    'group_rules.yaml',
    'iam_rules.yaml',
    'iap_rules.yaml',
    'instance_network_interface_rules.yaml',
    'ke_rules.yaml']

GCLOUD_MIN_VERSION = (180, 0, 0)
GCLOUD_VERSION_REGEX = r'Google Cloud SDK (.*)'
GCLOUD_ALPHA_REGEX = r'alpha.*'

SERVICE_ACCT_FMT = 'forseti-{}-{}-{}'
SERVICE_ACCT_EMAIL_FMT = '{}@{}.iam.gserviceaccount.com'

INPUT_DEPLOYMENT_TEMPLATE_FILENAME = {
    'server': 'deploy-forseti-server.yaml.in',
    'client': 'deploy-forseti-client.yaml.in'
}

INPUT_CONFIGURATION_TEMPLATE_FILENAME = {
    'server': 'forseti_conf_server.yaml.in',
    'client': 'forseti_conf_client.yaml.in'
}

NOTIFICATION_SENDER_EMAIL = 'forseti-notify@localhost.domain'

RESOURCE_TYPE_ARGS_MAP = {
    'organizations': ['organizations'],
    'folders': ['alpha', 'resource-manager', 'folders'],
    'projects': ['projects'],
    'forseti_project': ['projects'],
    'service_accounts': ['iam', 'service-accounts']
}

# Roles
GCP_READ_IAM_ROLES = [
    'roles/browser',
    'roles/compute.networkViewer',
    'roles/iam.securityReviewer',
    'roles/appengine.appViewer',
    'roles/bigquery.dataViewer',
    'roles/servicemanagement.quotaViewer',
    'roles/cloudsql.viewer'
]

GCP_WRITE_IAM_ROLES = [
    'roles/compute.securityAdmin'
]

PROJECT_IAM_ROLES_SERVER = [
    'roles/storage.objectViewer',
    'roles/storage.objectCreator',
    'roles/cloudsql.client',
    'roles/logging.logWriter'
]

PROJECT_IAM_ROLES_CLIENT = [
    'roles/storage.objectViewer',
    'roles/storage.objectCreator',
    'roles/logging.logWriter'
]

SVC_ACCT_ROLES = [
    'roles/iam.serviceAccountKeyAdmin'
]

# Required APIs
REQUIRED_APIS = [
    {'name': 'Admin SDK',
     'service': 'admin.googleapis.com'},
    {'name': 'AppEngine Admin',
     'service': 'appengine.googleapis.com'},
    {'name': 'BigQuery',
     'service': 'bigquery-json.googleapis.com'},
    {'name': 'Cloud Billing',
     'service': 'cloudbilling.googleapis.com'},
    {'name': 'Cloud Resource Manager',
     'service': 'cloudresourcemanager.googleapis.com'},
    {'name': 'Cloud SQL',
     'service': 'sql-component.googleapis.com'},
    {'name': 'Cloud SQL Admin',
     'service': 'sqladmin.googleapis.com'},
    {'name': 'Compute Engine',
     'service': 'compute.googleapis.com'},
    {'name': 'Deployment Manager',
     'service': 'deploymentmanager.googleapis.com'},
    {'name': 'IAM',
     'service': 'iam.googleapis.com'}
]

# Org Resource Types
RESOURCE_TYPES = ['organization', 'folder', 'project']

# Paths
ROOT_DIR_PATH = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)))))

RULES_DIR_PATH = os.path.abspath(
    os.path.join(
        ROOT_DIR_PATH, 'rules'))

FORSETI_SRC_PATH = os.path.join(
    ROOT_DIR_PATH, 'google', 'cloud', 'forseti')

FORSETI_CONF_PATH = ('{bucket_name}/configs/{installer_type}/'
                     'forseti_conf_{installer_type}.yaml')

DEPLOYMENT_TEMPLATE_OUTPUT_PATH = '{}/deployment_templates/'

VERSIONFILE_REGEX = r'__version__ = \'(.*)\''

# Message templates
MESSAGE_GSUITE_DATA_COLLECTION = (
    'To complete setup for G Suite Groups data collection, '
    'follow the steps below:\n\n'
    '    1. Click on: '
    'https://console.cloud.google.com/iam-admin/serviceaccounts/'
    'project?project={}&organizationId={}\n\n'
    '    2. Locate the service account to enable '
    'G Suite Groups collection:{}\n\n'
    '    3. Select Edit and then the Enable G Suite Domain-wide '
    'Delegation checkbox. Save.\n\n'
    '    4. On the service account row, click View Client ID. '
    'On the Client ID for Service account client panel that '
    'appears, copy the Client ID value, which will be a large '
    'number.\n\n'
    '    5. Click on: '
    'https://admin.google.com/ManageOauthClients\n\n'
    '    6. In the Client Name box, paste the Client ID you '
    'copied above.\n\n'
    '    7. In the One or More API Scopes box, paste the '
    'following scope:\n\n'
    '        https://www.googleapis.com/auth/admin.directory.'
    'group.readonly,\n'
    '        https://www.googleapis.com/auth/admin.directory.'
    'user.readonly\n\n'
    '    8. Click Authorize\n\n'
    'or refer to the guides:'
    'http://forsetisecurity.org/docs/howto/configure/'
    'gsuite-group-collection\n\n')

MESSAGE_SKIP_EMAIL = (
    'If you would like to enable email notifications via '
    'SendGrid, please refer to:\n\n'
    '    '
    'http://forsetisecurity.org/docs/howto/configure/'
    'email-notification\n\n')

MESSAGE_HAS_ROLE_SCRIPT = (
    'Some roles could not be assigned to {} where you want '
    'to grant Forseti access. A script `grant_forseti_roles.sh` '
    'has been generated with the necessary commands to assign '
    'those roles. Please run this script to assign the Forseti '
    'roles so that Forseti will work properly.\n\n')

MESSAGE_ENABLE_GSUITE_GROUP = (
    'If you want to enable G Suite Groups collection in '
    'Forseti, for example, to use IAM Explain), follow '
    ' the steps in the guide below:\n\n'
    '    '
    'http://forsetisecurity.org/docs/howto/configure/'
    'gsuite-group-collection\n\n')

MESSAGE_ASK_GSUITE_SUPERADMIN_EMAIL = (
    '\nTo read G Suite Groups and Users data, '
    'please provide a G Suite super admin, '
    'please provide a G Suite super admin email address. '
    'This step is NOT optional.')

MESSAGE_ASK_SENDGRID_API_KEY = (
    'Forseti can send email notifications through SendGrid '
    'via an API key. '
    'This step is optional and can be configured later.')

MESSAGE_FORSETI_CONFIGURATION_ACCESS_LEVEL = (
    'Forseti can be configured to access an '
    'organization, folder, or project.')

MESSAGE_NO_CLOUD_SHELL = (
    'Forseti highly recommends running this setup within '
    'Cloud Shell. If you would like to run the setup '
    'outside Cloud Shell, please be sure to do the '
    'following:\n\n'
    '1) Create a project.\n'
    '2) Enable billing for the project.\n'
    '3) Install gcloud and authenticate your account using '
    '"gcloud auth login".\n'
    '4) Set your project using '
    '"gcloud config project set <PROJECT_ID>".\n'
    '5) Run this setup again, with the --no-cloudshell flag, '
    'i.e.\n\n    python setup_forseti.py --no-cloudshell\n')

MESSAGE_FORSETI_CONFIGURATION_GENERATED = (
    'A Forseti configuration file (configs/{installer_type}/'
    'forseti_conf_{installer_type}_{datetimestamp}.yaml) '
    'has been generated. If you wish to change your '
    'Forseti configuration or rules, e.g. enabling G Suite '
    'Groups collection, either download the conf file in '
    'your bucket `{bucket_name}` or edit your local copy, then follow '
    'the guide below to copy the files to Cloud Storage:\n\n'
    '    http://forsetisecurity.org/docs/howto/deploy/'
    'gcp-deployment.html#move-configuration-to-gcs\n\n')

MESSAGE_FORSETI_CONFIGURATION_GENERATED_DRY_RUN = (
    'A Forseti configuration file has been generated. '
    'After you create your deployment, copy this file to '
    'the bucket created in the deployment:\n\n'
    '    gsutil cp {} {}/configs/forseti_conf_server.yaml\n\n')

MESSAGE_DEPLOYMENT_HAD_ISSUES = (
    'Your deployment had some issues. Please review the error '
    'messages. If you need help, please either file an issue '
    'on our Github Issues or email '
    'discuss@forsetisecurity.org.\n')

MESSAGE_FORSETI_BRANCH_DEPLOYED = (
    'Forseti Security (branch/version: {}) has been '
    'deployed to GCP.\n')

MESSAGE_DEPLOYMENT_TEMPLATE_LOCATION = (
    'Your generated Deployment Manager template can be '
    'found here:\n\n    {}\n\n    {}\n\n')

MESSAGE_VIEW_DEPLOYMENT_DETAILS = (
    'You can view the details of your deployment in the '
    'Cloud Console:\n\n    '
    'https://console.cloud.google.com/deployments/details/'
    '{}?project={}&organizationId={}\n\n')

MESSAGE_GCLOUD_VERSION_MISMATCH = (
    'You need the following gcloud setup:\n\n'
    'gcloud version >= {}\n'
    'gcloud alpha components\n\n'
    'To install gcloud alpha components: '
    'gcloud components install alpha\n\n'
    'To update gcloud: gcloud components update\n')

MESSAGE_CREATE_ROLE_SCRIPT = (
    'One or more roles could not be assigned. Writing a '
    'script with the commands to assign those roles. Please '
    'give this script to someone (like an admin) who can '
    'assign these roles for you. If you do not assign these '
    'roles, Forseti may not work properly!')

MESSAGE_BILLING_NOT_ENABLED = (
    '\nIt seems that billing is not enabled for your project. '
    'You can check whether billing has been enabled in the '
    'Cloud Platform Console:\n\n'
    '    https://console.cloud.google.com/billing/linkedaccount?'
    'project={}&organizationId={}\n\n'
    'Once you have enabled billing, re-run this setup.\n')

MESSAGE_NO_ORGANIZATION = (
    'You need to have an organization set up to use Forseti. '
    'Refer to the following documentation for more information.\n\n'
    'https://cloud.google.com/resource-manager/docs/'
    'creating-managing-organization')

# Questions templates
QUESTION_ENABLE_WRITE_ACCESS = (
    'Enable write access for Forseti? '
    'This allows Forseti to make changes to policies '
    '(e.g. for Enforcer) (y/n) ')

QUESTION_GSUITE_SUPERADMIN_EMAIL = (
    'What is your organization\'s G Suite super admin email? '
    '(press [enter] to skip) ')

QUESTION_SENDGRID_API_KEY = (
    'What is your SendGrid API key? '
    '(press [enter] to skip) ')

QUESTION_NOTIFICATION_RECIPIENT_EMAIL = (
    'At what email address do you want to receive '
    'notifications? (press [enter] to skip) ')

QUESTION_FORSETI_CONFIGURATION_ACCESS_LEVEL = (
    'At what level do you want to enable Forseti '
    'read (and optionally write) access? ')

QUESTION_ACCESS_TO_GRANT_ROLES = (
    'Do you have access to grant Forseti IAM '
    'roles on the target {}? (y/n) ')

QUESTION_CHOOSE_FOLDER = (
    'To find the folder, go to Cloud Console:\n\n'
    '    https://console.cloud.google.com/'
    'cloud-resource-manager?organizationId={}\n\n'
    'Enter the folder id where you want '
    'Forseti to crawl for data: ')
