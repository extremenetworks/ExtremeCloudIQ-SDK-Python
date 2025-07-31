# extremecloudiq.model.xiq_certificate_bundle.XiqCertificateBundle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**[certificates](#certificates)** | list, tuple,  | tuple,  | The Certificate Bundle list of certificates. | 
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The Certificate Bundle name. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**description** | str,  | str,  | The Certificate Bundle description. | [optional] 
**bundle_type** | str,  | str,  | The Certificate Bundle type. | [optional] must be one of ["TRUST_POINT", "CA", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# certificates

The Certificate Bundle list of certificates.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Certificate Bundle list of certificates. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCertificate**](XiqCertificate.md) | [**XiqCertificate**](XiqCertificate.md) | [**XiqCertificate**](XiqCertificate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

