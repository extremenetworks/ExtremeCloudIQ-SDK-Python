# extremecloudiq.model.xiq_assign_devices_network_policy_request.XiqAssignDevicesNetworkPolicyRequest

Device network policy assignment for multiple devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Device network policy assignment for multiple devices | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**devices** | [**XiqDeviceFilter**](XiqDeviceFilter.md) | [**XiqDeviceFilter**](XiqDeviceFilter.md) |  | 
**network_policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned network policy | value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

