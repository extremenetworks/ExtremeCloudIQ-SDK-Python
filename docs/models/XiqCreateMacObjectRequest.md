# extremecloudiq.model.xiq_create_mac_object_request.XiqCreateMacObjectRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mac_type** | [**XiqMacObjectType**](XiqMacObjectType.md) | [**XiqMacObjectType**](XiqMacObjectType.md) |  | 
**name** | str,  | str,  | The product model | 
**value** | str,  | str,  | The MAC octets. | 
**description** | str,  | str,  | The product description | [optional] 
**mac_address_end** | str,  | str,  | The MAC address end, only available for \&quot;MAC_RANGE\&quot; type. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

