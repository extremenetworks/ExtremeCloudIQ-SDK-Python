# extremecloudiq.model.xiq_update_ldap_server_request.XiqUpdateLdapServerRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The LDAP server name | [optional] 
**description** | str,  | str,  | The LDAP server description | [optional] 
**enable_tls** | bool,  | BoolClass,  | enable TLS or not, if ture, caCertificateId, clientCertificateId and clientKeyId must be specified | [optional] 
**bind_dn** | str,  | str,  | The LDAP server bind DN name | [optional] 
**bind_dn_password** | str,  | str,  | The LDAP server bind DN password | [optional] 
**base_dn** | str,  | str,  | The RADIUS user base DN | [optional] 
**l3_address_profile_id** | decimal.Decimal, int,  | decimal.Decimal,  | The L3 address profile ID | [optional] value must be a 64 bit integer
**protocol_type** | [**XiqLdapProtocolType**](XiqLdapProtocolType.md) | [**XiqLdapProtocolType**](XiqLdapProtocolType.md) |  | [optional] 
**enable_strip_realm_name** | bool,  | BoolClass,  | enable strip realm name or not | [optional] 
**destination_port** | decimal.Decimal, int,  | decimal.Decimal,  | The LDAP server destination port (1 ~ 65535) | [optional] value must be a 32 bit integer
**verification_mode** | [**XiqLdapServerVerificationMode**](XiqLdapServerVerificationMode.md) | [**XiqLdapServerVerificationMode**](XiqLdapServerVerificationMode.md) |  | [optional] 
**ca_certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | The CA certificate ID, refer to XiqCertificate | [optional] value must be a 64 bit integer
**client_certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client certificate ID, refer to XiqCertificate | [optional] value must be a 64 bit integer
**client_key_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client key ID, refer to XiqCertificate | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

