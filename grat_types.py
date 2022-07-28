''' 
define GRAT type objects
'''

from typing_extensions import TypedDict

# class Site(TypedDict, total=False):
class Site:

    def __init__(self):

        # need to see data source to confirm types 
        self.OBJECTID: int
        self.crop_list: str
        self.crop: str or None
        self.acres: float or int
        self.stor_ind: int
        self.cost_ind: int
        self.convey_ind: int
        self.vol_ind: int
        self.retent_ind: int
        self.parcel: int
        self.owner: str
        self.SAGBI_Class: str
        self.r_type: str
        self.precip_IDX: int
        self.GRATID: int
        self.infil_ind: int
        self.cost: float or int
        self.perc_rate: int or None
        self.capacity: int or float or None
        self.region_id: int
        self.cost_unused: int or float
        self.cost_pw: int or float
        self.cost_pump: int or float or None
        self.capital_cost: int or float or None
        self.subbasin: int
        self.Shape_Length: float
        self.Shape_Area: float
        self.potential: str
        self.SAGBI_AVG: float
        self.sequence: int or None
        self.bottleneck_id: int
        self.flowlimit_acrefeetdaily: int or float or None
        self.recharge: int or float
        self.DiversionSources: str
        self.INBASINRET: int or None
        self.FIRORP_combined_priority: int or None
        self.ECOFIRO_combined_priority: int or None

class BottleneckAttributes:

    def __init__(self):

        self.bottleneck_id: int
        self.CANAL: str
        self.FLOW_CFS: int or float
        self.acre_feet_per_day: int or float

class Bottleneck(BottleneckAttributes):

    def __init__(self):

        self.attributes = super().__init__()

