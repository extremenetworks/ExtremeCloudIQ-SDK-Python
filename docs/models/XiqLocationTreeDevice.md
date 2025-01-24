# extremecloudiq.model.xiq_location_tree_device.XiqLocationTreeDevice

The device on the location hierarchy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device on the location hierarchy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_name** | str,  | str,  | The name of the device. | 
**mac_address** | str,  | str,  | The device MAC address. | 
**serial_number** | str,  | str,  | The device serial number. | [optional] 
**device_function** | str,  | str,  | The device function, such as AP, Router, Switch, etc. | [optional] 
**product_type** | str,  | str,  | The product type, such as: AP_230, BR_100, NX9600, etc. | [optional] 
**ip_address** | str,  | str,  | The device IPv4 address. | [optional] 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID of the device on the location hierarchy. | [optional] value must be a 64 bit integer
**map_name** | str,  | str,  | The associated background map for the device. | [optional] 
**x** | decimal.Decimal, int, float,  | decimal.Decimal,  | The x-position of the device relative to the horizontal scale in meter. | [optional] value must be a 64 bit float
**y** | decimal.Decimal, int, float,  | decimal.Decimal,  | The y-position of the device relative to the vertical scale in meter. | [optional] value must be a 64 bit float
**scale_x** | decimal.Decimal, int, float,  | decimal.Decimal,  | The horizontal scale for the background map in meter. | [optional] value must be a 64 bit float
**scale_y** | decimal.Decimal, int, float,  | decimal.Decimal,  | The vertical scale for the background map in meter. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

