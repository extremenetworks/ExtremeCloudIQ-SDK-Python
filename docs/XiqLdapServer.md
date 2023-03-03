# XiqLdapServer

The common object - LDAP server
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**name** | **str** | The LDAP server name | 
**description** | **str** | The LDAP server description | [optional] 
**enable_tls** | **bool** | The LDAP server is enabled TLS or not | [optional] 
**bind_dn** | **str** | The LDAP server bind DN name | [optional] 
**bind_dn_password** | **str** | The LDAP server bind DN password | [optional] 
**base_dn** | **str** | The RADIUS user base DN | [optional] 
**l3_address_profile_id** | **int** | The L3 address profile ID | [optional] 
**protocol_type** | [**XiqLdapProtocolType**](XiqLdapProtocolType.md) |  | [optional] 
**enable_strip_realm_name** | **bool** | Enable strip realm name or not | [optional] 
**destination_port** | **int** | The LDAP server destination port | [optional] 
**verification_mode** | [**XiqLdapServerVerificationMode**](XiqLdapServerVerificationMode.md) |  | [optional] 
**ca_certificate_id** | **int** | The CA certificate ID | [optional] 
**client_certificate_id** | **int** | The client certificate ID | [optional] 
**client_key_id** | **int** | The client key ID | [optional] 
**client_key_password** | **str** | The LDAP server client key password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


