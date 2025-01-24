# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from extremecloudiq.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    UNIVERSAL_COMPUTE_PLATFORM = "Universal Compute Platform"
    AUTHENTICATION = "Authentication"
    AUTHORIZATION = "Authorization"
    OPERATION = "Operation"
    ACCOUNT = "Account"
    USER = "User"
    HIQ = "HIQ"
    LOCATION = "Location"
    DEVICE = "Device"
    NETWORK_POLICY = "Network Policy"
    CLIENT = "Client"
    APPLICATION = "Application"
    ALERT = "Alert"
    LOG = "Log"
    NOTIFICATION = "Notification"
    NOS = "NOS"
    CONFIGURATION__DEPLOYMENT = "Configuration - Deployment"
    CONFIGURATION__BASIC = "Configuration - Basic"
    CONFIGURATION__USER_MANAGEMENT = "Configuration - User Management"
    CONFIGURATION__POLICY = "Configuration - Policy"
    CONFIGURATION__NETWORK = "Configuration - Network"
    CONFIGURATION__AUTHENTICATION = "Configuration - Authentication"
    CONFIGURATION__CERTIFICATE = "Configuration - Certificate"
    COPILOT__CONNECTIVITY_EXPERIENCE = "Copilot - Connectivity Experience"
    COPILOT__ANOMALIES = "Copilot - Anomalies"
    PACKET_CAPTURE = "Packet Capture"
    NETWORK_SCORECARD = "Network Scorecard"
    ESSENTIALS__EXTREME_LOCATION = "Essentials - ExtremeLocation"
    MISC = "Misc"
    THREAD = "Thread"
    AFCENDPOINT = "afc-endpoint"
    RTTSENDPOINT = "rtts-endpoint"
