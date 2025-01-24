from extremecloudiq.paths.locations_building_id.get import ApiForget
from extremecloudiq.paths.locations_building_id.put import ApiForput
from extremecloudiq.paths.locations_building_id.delete import ApiFordelete


class LocationsBuildingId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
