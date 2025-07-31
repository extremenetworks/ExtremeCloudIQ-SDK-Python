# extremecloudiq.model.xiq_afc_mobileapp_coordinates.XiqAfcMobileappCoordinates

The Location provided by MobileApp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Location provided by MobileApp | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude expressed as a floating point number | [optional] value must be a 64 bit float
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude expressed as a floating point number | [optional] value must be a 64 bit float
**ts** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of the acquired geolocation (milliseconds from epoch) | [optional] value must be a 64 bit integer
**source** | [**XiqAfcCoordinatesSource**](XiqAfcCoordinatesSource.md) | [**XiqAfcCoordinatesSource**](XiqAfcCoordinatesSource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

