# extremecloudiq.model.xiq_update_site_request.XiqUpdateSiteRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country_code** | decimal.Decimal, int,  | decimal.Decimal,  | The site country code. Get the list of country codes from /countries XAPI. | value must be a 32 bit integer
**name** | str,  | str,  | The site name | 
**parent_id** | decimal.Decimal, int,  | decimal.Decimal,  | The parent site group ID | [optional] value must be a 64 bit integer
**address** | [**XiqAddress**](XiqAddress.md) | [**XiqAddress**](XiqAddress.md) |  | [optional] 
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The latitude coordinate for the site | [optional] value must be a 64 bit float
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The longitude coordinate for the site | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

