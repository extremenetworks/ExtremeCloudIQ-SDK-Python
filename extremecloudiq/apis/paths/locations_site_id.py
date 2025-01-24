from extremecloudiq.paths.locations_site_id.get import ApiForget
from extremecloudiq.paths.locations_site_id.put import ApiForput
from extremecloudiq.paths.locations_site_id.delete import ApiFordelete


class LocationsSiteId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
