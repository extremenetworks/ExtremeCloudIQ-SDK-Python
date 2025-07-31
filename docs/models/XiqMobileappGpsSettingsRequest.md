# extremecloudiq.model.xiq_mobileapp_gps_settings_request.XiqMobileappGpsSettingsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gps_anchor** | bool,  | BoolClass,  | Use this AP as GPS anchor to derive geo-coordinates of other APs on the floor | [optional] 
**distance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Distance between AP and the phone hosting the mobile APP in meters. | [optional] value must be a 64 bit float
**cep** | decimal.Decimal, int, float,  | decimal.Decimal,  | Circular error probability, CEP68 is based on Android OS. | [optional] value must be a 64 bit float
**coordinates** | [**XiqAfcMobileappCoordinates**](XiqAfcMobileappCoordinates.md) | [**XiqAfcMobileappCoordinates**](XiqAfcMobileappCoordinates.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

