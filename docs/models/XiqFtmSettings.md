# extremecloudiq.model.xiq_ftm_settings.XiqFtmSettings

The payload of FTM Settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of FTM Settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wgs84_override** | bool,  | BoolClass,  | World Geodetic System 1984 (WGS84) override | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**zsubelement_override** | bool,  | BoolClass,  | Z Subelement override. | 
**civic_address_override** | bool,  | BoolClass,  | Civic Address override. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**wgs84** | [**XiqWgs84**](XiqWgs84.md) | [**XiqWgs84**](XiqWgs84.md) |  | [optional] 
**zsubelement** | [**XiqZsubelement**](XiqZsubelement.md) | [**XiqZsubelement**](XiqZsubelement.md) |  | [optional] 
**civic_address** | str,  | str,  | Civic Address as hex encoded RFC4776 formatted string. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

