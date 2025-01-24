# extremecloudiq.model.xiq_mac_object.XiqMacObject

The MAC Object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The MAC Object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The MAC object name | [optional] 
**description** | str,  | str,  | The MAC object description. | [optional] 
**predefined** | bool,  | BoolClass,  | Whether the MAC Oui is predefined | [optional] 
**value** | str,  | str,  | The MAC octets. | [optional] 
**mac_type** | [**XiqMacObjectType**](XiqMacObjectType.md) | [**XiqMacObjectType**](XiqMacObjectType.md) |  | [optional] 
**defender_defined** | bool,  | BoolClass,  | Whether defender is defined | [optional] 
**mac_address_end** | str,  | str,  | The MAC address end, only available for \&quot;MAC_RANGE\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

