# extremecloudiq.model.essentials_eloc_last_known_location.EssentialsElocLastKnownLocation

The client's last known location on the floor plan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The client&#x27;s last known location on the floor plan | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | str,  | str,  | The located client&#x27;s last known timestamp in format of date, time and abbreviated timezone | [optional] 
**x** | decimal.Decimal, int, float,  | decimal.Decimal,  | The located client&#x27;s last known horizontal value on the floor plan | [optional] value must be a 64 bit float
**y** | decimal.Decimal, int, float,  | decimal.Decimal,  | The located client&#x27;s last known vertical value on the floor plan | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

