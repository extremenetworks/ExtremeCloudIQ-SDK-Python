# extremecloudiq.model.xiq_rp_mac_oui_profile.XiqRpMacOuiProfile

The payload of config for the radio profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of config for the radio profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**name** | str,  | str,  | The product model | [optional] 
**description** | str,  | str,  | The product description | [optional] 
**predefined** | bool,  | BoolClass,  | Whether the MAC Oui is predefined. | [optional] 
**value** | str,  | str,  | The MAC octets | [optional] 
**mac_type** | str,  | str,  | The type or \&quot;MAC_OUI\&quot; | [optional] 
**defender_defined** | bool,  | BoolClass,  | Whether defender is defined | [optional] 
**extreme_iot_defined** | bool,  | BoolClass,  | Whether is the Extreme Iot Defined | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

