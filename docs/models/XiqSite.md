# extremecloudiq.model.xiq_site.XiqSite

The site location information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The site location information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country_code** | decimal.Decimal, int,  | decimal.Decimal,  | The country code for the site | value must be a 32 bit integer
**unique_name** | str,  | str,  | The site unique name | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The site name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**type** | str,  | str,  | The location type | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**parent_id** | decimal.Decimal, int,  | decimal.Decimal,  | The parent site group ID | [optional] value must be a 64 bit integer
**address** | [**XiqAddress**](XiqAddress.md) | [**XiqAddress**](XiqAddress.md) |  | [optional] 
**created_by** | decimal.Decimal, int,  | decimal.Decimal,  | The user ID used to create the site | [optional] value must be a 64 bit integer
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The latitude coordinate for the site | [optional] value must be a 64 bit float
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The longitude coordinate for the site | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

