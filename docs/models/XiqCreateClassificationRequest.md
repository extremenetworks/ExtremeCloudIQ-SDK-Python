# extremecloudiq.model.xiq_create_classification_request.XiqCreateClassificationRequest

The details of rule assignments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details of rule assignments | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**match** | bool,  | BoolClass,  | Contains or not contains | 
**classification_type** | str,  | str,  | Classification type | must be one of ["CLASSIFICATION_TYPE_UNSPECIFIED", "CLASSIFICATION_TYPE_LOCATION", "CLASSIFICATION_TYPE_CLOUD_CONFIG_GROUP", "CLASSIFICATION_TYPE_IP_ADDRESS", "CLASSIFICATION_TYPE_IP_SUBNET", "CLASSIFICATION_TYPE_IP_RANGE", "UNRECOGNIZED", ] 
**classification_type_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of location, cloud config group, IP address, IP subnet or IP range. | value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

