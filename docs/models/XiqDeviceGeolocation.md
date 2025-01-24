# extremecloudiq.model.xiq_device_geolocation.XiqDeviceGeolocation

Device geolocation info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Device geolocation info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orientation** | decimal.Decimal, int, float,  | decimal.Decimal,  | The orientation of the AP | value must be a 64 bit float
**last_reported** | decimal.Decimal, int,  | decimal.Decimal,  | The last updated time of the geolocation | value must be a 64 bit integer
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The height above sea level of the AP | value must be a 64 bit float
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The longitude of the AP | value must be a 64 bit float
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The latitude of the AP | [optional] value must be a 64 bit float
**major_axis** | decimal.Decimal, int, float,  | decimal.Decimal,  | The major axis of the AP | [optional] value must be a 64 bit float
**minor_axis** | decimal.Decimal, int, float,  | decimal.Decimal,  | The minor axis of the AP | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

