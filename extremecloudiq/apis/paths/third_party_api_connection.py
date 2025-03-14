from extremecloudiq.paths.third_party_api_connection.get import ApiForget
from extremecloudiq.paths.third_party_api_connection.put import ApiForput
from extremecloudiq.paths.third_party_api_connection.delete import ApiFordelete


class ThirdPartyApiConnection(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
