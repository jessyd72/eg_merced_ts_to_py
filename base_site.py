'''
base site
'''

import numpy as np
from .grats import Site

class BaseSite(Site):
    '''define base site 
    inheret from Site'''

    def __init__(self):

        super().__init__()
        self.used_vol = np.full(365, 0)
        self.precip = np.full(365, 0)
        self.sort_index: int
        self.owner = self.owner
        self.sequence = self.owner
        self.index: int
        self.crop = self.crop if self.crop else self.r_type
        self.capitalCost = self.capital_cost
        self.pumpingCost: int or float
        self.acerage: int or float
        self.perc_rate: int
        self.cost_unused: int
        self.capacity: int
        self.currentCapacity: int
        self.cost: int
        self.cost_pw: int
        self.siteID: int
        self.bottleneck_id: int
        self.soilType: str
        self.r_type: str
        self.flowLimit: int
        self.precip_IDX: int
        self.compatible_sources = []
        #self.cropCalendar: CropCalendar
        self.subbasin: int
        self.dailyRechargeVolumes = []
        self.unusedVolume = []
        self.DiversionSources: str

    def set_daily_recharge(self, new_vol, day):

        self.dailyRechargeVolumes[day] += new_vol

    def set_precip(self, vol, day):

        self.precip[day] = vol

