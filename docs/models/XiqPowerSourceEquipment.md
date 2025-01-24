# extremecloudiq.model.xiq_power_source_equipment.XiqPowerSourceEquipment

Copilot LLdp-Cdp Info For Anomalous Access Points

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot LLdp-Cdp Info For Anomalous Access Points | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_lldp_cdp_enabled** | bool,  | BoolClass,  | Check if lldp-cdp enabled on anomalous accesspoints | [optional] 
**uplink_switch_system_name** | str,  | str,  | Uplink switch system name | [optional] 
**uplink_switch_system_id** | str,  | str,  | Uplink switch model | [optional] 
**location_name** | str,  | str,  | The location name for anomalous access points with lldp-cdp info not enabled | [optional] 
**floor_name** | str,  | str,  | The location name for anomalous access points with lldp-cdp info not enabled | [optional] 
**[affected_downlink_devices](#affected_downlink_devices)** | list, tuple,  | tuple,  | The list of affected downlink devices | [optional] 
**[unaffected_downlink_devices](#unaffected_downlink_devices)** | list, tuple,  | tuple,  | The list of unaffected downlink devices | [optional] 
**uplink_switch_device_id** | decimal.Decimal, int,  | decimal.Decimal,  |  The uplink device id | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# affected_downlink_devices

The list of affected downlink devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of affected downlink devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAffectedDownlinkDevice**](XiqAffectedDownlinkDevice.md) | [**XiqAffectedDownlinkDevice**](XiqAffectedDownlinkDevice.md) | [**XiqAffectedDownlinkDevice**](XiqAffectedDownlinkDevice.md) |  | 

# unaffected_downlink_devices

The list of unaffected downlink devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of unaffected downlink devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUnaffectedDownlinkDevice**](XiqUnaffectedDownlinkDevice.md) | [**XiqUnaffectedDownlinkDevice**](XiqUnaffectedDownlinkDevice.md) | [**XiqUnaffectedDownlinkDevice**](XiqUnaffectedDownlinkDevice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

