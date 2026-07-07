# extremecloudiq.model.xiq_rm_device_metadata_response.XiqRmDeviceMetadataResponse

RM Metadata Response Class

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RM Metadata Response Class | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[default_gateway](#default_gateway)** | list, tuple,  | tuple,  | The device default gateway | [optional] 
**[software_version](#software_version)** | list, tuple,  | tuple,  | The device OS software version | [optional] 
**[product_type](#product_type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The product type map, eg. Key - AP_350, Value(displayed on UI) - AP350 | [optional] 
**[device_admin_state](#device_admin_state)** | list, tuple,  | tuple,  | The device admin state | [optional] 
**[country_code](#country_code)** | list, tuple,  | tuple,  | The assigned country code on the device | [optional] 
**[managed_by](#managed_by)** | list, tuple,  | tuple,  | The managed application for the device | [optional] 
**[display_managed_by](#display_managed_by)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The display managed by map | [optional] 
**[sim_type](#sim_type)** | list, tuple,  | tuple,  | The device type - REAL or SIMULATED | [optional] 
**[country_code_name](#country_code_name)** | list, tuple,  | tuple,  | The assigned country name on the device | [optional] 
**[network_policy](#network_policy)** | list, tuple,  | tuple,  | The network policy applied to the device | [optional] 
**[uplink_speeds](#uplink_speeds)** | list, tuple,  | tuple,  | The Eth0 and Eth1 port speed | [optional] 
**[serial_number](#serial_number)** | list, tuple,  | tuple,  | The serial number of the device | [optional] 
**[copilot_license_statuses](#copilot_license_statuses)** | list, tuple,  | tuple,  | The Copilot license status of the device | [optional] 
**[anchor_ap](#anchor_ap)** | list, tuple,  | tuple,  | Distinct values present for the Anchor AP icon filter in the matched device set. | [optional] 
**[locally_managed](#locally_managed)** | list, tuple,  | tuple,  | Distinct values present for the Locally Managed icon filter in the matched device set. | [optional] 
**[afc_status](#afc_status)** | list, tuple,  | tuple,  | Distinct AFC status values present in the matched device set (e.g., AVAILABLE, PENDING). | [optional] 
**[device_update_unsuccessful](#device_update_unsuccessful)** | list, tuple,  | tuple,  | Distinct values present for the Device Update Unsuccessful icon filter in the matched device set. | [optional] 
**[provisioned_device](#provisioned_device)** | list, tuple,  | tuple,  | Distinct values present for the Provisioned Device icon filter in the matched device set. | [optional] 
**[configuration_roll_back](#configuration_roll_back)** | list, tuple,  | tuple,  | Distinct values present for the Configuration Roll Back icon filter in the matched device set. | [optional] 
**[undetermined](#undetermined)** | list, tuple,  | tuple,  | Distinct values present for the Undetermined icon filter in the matched device set. | [optional] 
**[configured_at_device_level](#configured_at_device_level)** | list, tuple,  | tuple,  | Distinct values present for the Configured At Device Level icon filter in the matched device set. | [optional] 
**[monitoring_unassociated_clients](#monitoring_unassociated_clients)** | list, tuple,  | tuple,  | Distinct values present for the Monitoring Unassociated Clients icon filter in the matched device set. | [optional] 
**[switch_stack](#switch_stack)** | list, tuple,  | tuple,  | Distinct values present for the Switch Stack icon filter in the matched device set. | [optional] 
**[switch_stack_warning](#switch_stack_warning)** | list, tuple,  | tuple,  | Distinct values present for the Switch Stack Warning icon filter in the matched device set. | [optional] 
**[radsec_proxy_server](#radsec_proxy_server)** | list, tuple,  | tuple,  | Distinct values present for the Radsec Proxy Server icon filter in the matched device set. | [optional] 
**[sensor_mode_interface](#sensor_mode_interface)** | list, tuple,  | tuple,  | Distinct values present for the Sensor Mode Interface icon filter in the matched device set. | [optional] 
**[spectrum_intelligence](#spectrum_intelligence)** | list, tuple,  | tuple,  | Distinct values present for the Spectrum Intelligence icon filter in the matched device set. | [optional] 
**[vpn_server](#vpn_server)** | list, tuple,  | tuple,  | Distinct VPN Server status values present in the matched device set (e.g., UP, DOWN, UP_DOWN). | [optional] 
**[vpn_client](#vpn_client)** | list, tuple,  | tuple,  | Distinct VPN Client status values present in the matched device set (e.g., UP, DOWN, UP_DOWN). | [optional] 
**[fabric_attach](#fabric_attach)** | list, tuple,  | tuple,  | Distinct values present for the Fabric Attach icon filter in the matched device set. | [optional] 
**[fabric_attach_issue](#fabric_attach_issue)** | list, tuple,  | tuple,  | Distinct values present for the Fabric Attach Issue icon filter in the matched device set. | [optional] 
**[digital_twin](#digital_twin)** | list, tuple,  | tuple,  | Distinct values present for the Digital Twin icon filter in the matched device set. | [optional] 
**[managed_by_extreme_iot](#managed_by_extreme_iot)** | list, tuple,  | tuple,  | Distinct values present for the Managed By Extreme IoT icon filter in the matched device set. | [optional] 
**[swap_for_real_device](#swap_for_real_device)** | list, tuple,  | tuple,  | Distinct values present for the Swap for Real Device icon filter in the matched device set. | [optional] 
**[configuration_pending](#configuration_pending)** | list, tuple,  | tuple,  | Distinct values present for the Configuration Pending icon filter in the matched device set. | [optional] 
**[connected](#connected)** | list, tuple,  | tuple,  | Distinct values present for the connected icon filter in the matched device set. | [optional] 
**[config_mismatch](#config_mismatch)** | list, tuple,  | tuple,  | Distinct values present for the Configuration mismatch icon filter in the matched device set. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# default_gateway

The device default gateway

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device default gateway | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The device default gateway | 

# software_version

The device OS software version

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device OS software version | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The device OS software version | 

# product_type

The product type map, eg. Key - AP_350, Value(displayed on UI) - AP350

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The product type map, eg. Key - AP_350, Value(displayed on UI) - AP350 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type The product type map, eg. Key - AP_350, Value(displayed on UI) - AP350 | [optional] 

# device_admin_state

The device admin state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device admin state | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | 

# country_code

The assigned country code on the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The assigned country code on the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The assigned country code on the device | value must be a 32 bit integer

# managed_by

The managed application for the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The managed application for the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The managed application for the device | 

# display_managed_by

The display managed by map

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The display managed by map | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type The display managed by map | [optional] 

# sim_type

The device type - REAL or SIMULATED

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device type - REAL or SIMULATED | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDeviceType**](XiqDeviceType.md) | [**XiqDeviceType**](XiqDeviceType.md) | [**XiqDeviceType**](XiqDeviceType.md) |  | 

# country_code_name

The assigned country name on the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The assigned country name on the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCountryCodeName**](XiqCountryCodeName.md) | [**XiqCountryCodeName**](XiqCountryCodeName.md) | [**XiqCountryCodeName**](XiqCountryCodeName.md) |  | 

# network_policy

The network policy applied to the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The network policy applied to the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The network policy applied to the device | 

# uplink_speeds

The Eth0 and Eth1 port speed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Eth0 and Eth1 port speed | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The Eth0 and Eth1 port speed | 

# serial_number

The serial number of the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The serial number of the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The serial number of the device | 

# copilot_license_statuses

The Copilot license status of the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Copilot license status of the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCopilotLicenseStatus**](XiqCopilotLicenseStatus.md) | [**XiqCopilotLicenseStatus**](XiqCopilotLicenseStatus.md) | [**XiqCopilotLicenseStatus**](XiqCopilotLicenseStatus.md) |  | 

# anchor_ap

Distinct values present for the Anchor AP icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Anchor AP icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Anchor AP icon filter in the matched device set. | 

# locally_managed

Distinct values present for the Locally Managed icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Locally Managed icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Locally Managed icon filter in the matched device set. | 

# afc_status

Distinct AFC status values present in the matched device set (e.g., AVAILABLE, PENDING).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct AFC status values present in the matched device set (e.g., AVAILABLE, PENDING). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Distinct AFC status values present in the matched device set (e.g., AVAILABLE, PENDING). | 

# device_update_unsuccessful

Distinct values present for the Device Update Unsuccessful icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Device Update Unsuccessful icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Device Update Unsuccessful icon filter in the matched device set. | 

# provisioned_device

Distinct values present for the Provisioned Device icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Provisioned Device icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Provisioned Device icon filter in the matched device set. | 

# configuration_roll_back

Distinct values present for the Configuration Roll Back icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Configuration Roll Back icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Configuration Roll Back icon filter in the matched device set. | 

# undetermined

Distinct values present for the Undetermined icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Undetermined icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Undetermined icon filter in the matched device set. | 

# configured_at_device_level

Distinct values present for the Configured At Device Level icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Configured At Device Level icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Configured At Device Level icon filter in the matched device set. | 

# monitoring_unassociated_clients

Distinct values present for the Monitoring Unassociated Clients icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Monitoring Unassociated Clients icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Monitoring Unassociated Clients icon filter in the matched device set. | 

# switch_stack

Distinct values present for the Switch Stack icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Switch Stack icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Switch Stack icon filter in the matched device set. | 

# switch_stack_warning

Distinct values present for the Switch Stack Warning icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Switch Stack Warning icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Switch Stack Warning icon filter in the matched device set. | 

# radsec_proxy_server

Distinct values present for the Radsec Proxy Server icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Radsec Proxy Server icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Radsec Proxy Server icon filter in the matched device set. | 

# sensor_mode_interface

Distinct values present for the Sensor Mode Interface icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Sensor Mode Interface icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Sensor Mode Interface icon filter in the matched device set. | 

# spectrum_intelligence

Distinct values present for the Spectrum Intelligence icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Spectrum Intelligence icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Spectrum Intelligence icon filter in the matched device set. | 

# vpn_server

Distinct VPN Server status values present in the matched device set (e.g., UP, DOWN, UP_DOWN).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct VPN Server status values present in the matched device set (e.g., UP, DOWN, UP_DOWN). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Distinct VPN Server status values present in the matched device set (e.g., UP, DOWN, UP_DOWN). | 

# vpn_client

Distinct VPN Client status values present in the matched device set (e.g., UP, DOWN, UP_DOWN).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct VPN Client status values present in the matched device set (e.g., UP, DOWN, UP_DOWN). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Distinct VPN Client status values present in the matched device set (e.g., UP, DOWN, UP_DOWN). | 

# fabric_attach

Distinct values present for the Fabric Attach icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Fabric Attach icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Fabric Attach icon filter in the matched device set. | 

# fabric_attach_issue

Distinct values present for the Fabric Attach Issue icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Fabric Attach Issue icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Fabric Attach Issue icon filter in the matched device set. | 

# digital_twin

Distinct values present for the Digital Twin icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Digital Twin icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Digital Twin icon filter in the matched device set. | 

# managed_by_extreme_iot

Distinct values present for the Managed By Extreme IoT icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Managed By Extreme IoT icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Managed By Extreme IoT icon filter in the matched device set. | 

# swap_for_real_device

Distinct values present for the Swap for Real Device icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Swap for Real Device icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Swap for Real Device icon filter in the matched device set. | 

# configuration_pending

Distinct values present for the Configuration Pending icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Configuration Pending icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Configuration Pending icon filter in the matched device set. | 

# connected

Distinct values present for the connected icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the connected icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the connected icon filter in the matched device set. | 

# config_mismatch

Distinct values present for the Configuration mismatch icon filter in the matched device set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Distinct values present for the Configuration mismatch icon filter in the matched device set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  | Distinct values present for the Configuration mismatch icon filter in the matched device set. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

