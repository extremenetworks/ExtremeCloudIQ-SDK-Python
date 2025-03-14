# extremecloudiq.model.xiq_wireless_wifi2.XiqWirelessWifi2

The unique identifier of the wireless interface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The unique identifier of the wireless interface | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ssid_count** | decimal.Decimal, int,  | decimal.Decimal,  | The count of SSIDs | [optional] value must be a 32 bit integer
**[ssids](#ssids)** | list, tuple,  | tuple,  | The list of SSIDs | [optional] 
**number_of_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of clients | [optional] value must be a 64 bit integer
**channel_utilization** | decimal.Decimal, int,  | decimal.Decimal,  | The value for channel utilization | [optional] value must be a 32 bit integer
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | The value for channel | [optional] value must be a 32 bit integer
**channel_width** | decimal.Decimal, int,  | decimal.Decimal,  | The value for channel width | [optional] value must be a 32 bit integer
**load_balancing** | bool,  | BoolClass,  | The value for load balancing | [optional] 
**band_steering** | bool,  | BoolClass,  | The value for band steering | [optional] 
**channel_utilization_details** | [**XiqChannelUtilizationDetails**](XiqChannelUtilizationDetails.md) | [**XiqChannelUtilizationDetails**](XiqChannelUtilizationDetails.md) |  | [optional] 
**xiq_ap_afc_status** | str,  | str,  | The value for afc status | [optional] must be one of ["PENDING", "GRACE_PERIOD", "AVAILABLE", "NA", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssids

The list of SSIDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of SSIDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The list of SSIDs | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

