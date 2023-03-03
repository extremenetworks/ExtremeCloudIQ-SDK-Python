# XiqCreateInternalRadiusServerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The internal RADIUS server name | 
**description** | **str** | The internal RADIUS server description | [optional] 
**authentication_method_group** | [**XiqInternalRadiusServerAuthenticationMethodGroup**](XiqInternalRadiusServerAuthenticationMethodGroup.md) |  | 
**default_authentication_method** | [**XiqInternalRadiusServerAuthenticationMethod**](XiqInternalRadiusServerAuthenticationMethod.md) |  | 
**enable_verify_server_cert** | **bool** | Enable verify server cert or not | 
**server_key_password** | **str** | password for server key | [optional] 
**enable_check_cert_common_name** | **bool** | Enable check cert common name or not | 
**enable_check_user_for_tls_auth** | **bool** | Enable check user for TLS auth or not | 
**enable_check_user_for_peap_auth** | **bool** | Enable check user for PEAP auth or not, for Active Directory as the external user directory only | [optional] 
**enable_check_user_for_ttls_auth** | **bool** | Enable check user for TTLS auth or not, for Active Directory as the external user directory only | [optional] 
**enable_authentication_server** | **bool** | Enable the RADIUS server as authentication or not | 
**enable_radius_accounting_settings** | **bool** | Enable the RADIUS server as accounting or not, must enable authentication server if want to enable accounting settings | 
**authentication_server_port** | **int** | Port for the authentication, must enable authentication. Max:65535, Min:1 | [optional] [default to 1812]
**active_session_limit** | **int** | Active session limit, must enable accounting setting. Max:15, Min:0 | [optional] [default to 0]
**active_session_age_timeout** | **int** | Active session age timeout in seconds, must enable accounting setting. Max:300000000, Min:30 | [optional] [default to 1800]
**external_user_directory** | [**XiqExternalUserDirectory**](XiqExternalUserDirectory.md) |  | 
**ca_certificate_id** | **int** | The CA certificate ID, which could be fetched from endpoint: &#39;/certificates&#39; and pick up with type &#39;CA&#39; | 
**server_certificate_id** | **int** | The Server certificate ID, which could be fetched from endpoint: &#39;/certificates&#39; and pick up with type &#39;CERT&#39; | 
**server_key_id** | **int** | The Server key ID, which could be fetched from endpoint: &#39;/certificates&#39; and pick up with type &#39;KEY&#39; | 
**device_ids** | **list[int]** | The list of device ID associated with the internal RADIUS server | 
**clients** | [**list[XiqRadiusClient]**](XiqRadiusClient.md) | The RADIUS clients of RADIUS proxy, which could be fetched from endpoint: &#39;/radius-proxy&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


