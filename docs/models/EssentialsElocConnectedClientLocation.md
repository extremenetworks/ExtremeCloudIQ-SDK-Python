# extremecloudiq.model.essentials_eloc_connected_client_location.EssentialsElocConnectedClientLocation

A connected client on a floor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A connected client on a floor | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mac_address** | str,  | str,  | Client MAC address | [optional] 
**display_name** | str,  | str,  | Client display name | [optional] 
**timestamp** | str,  | str,  | Timestamp of the location (ISO 8601) | [optional] 
**x** | decimal.Decimal, int, float,  | decimal.Decimal,  | X coordinate on the floor plan | [optional] value must be a 64 bit float
**y** | decimal.Decimal, int, float,  | decimal.Decimal,  | Y coordinate on the floor plan | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

