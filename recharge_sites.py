# from dataclasses import dataclass
import numpy as np
from .grats import Site, CropCalendar
from functools import map, reduce


class Canal:
    '''define canal and update recharge and use values'''

    def __init__(self, all_srcs):
        '''define canal properties'''

        self.name = 'Canal'
        self.max_capacity = 10000
        self.perc_rate = 600
        self.curr_capacity = 0
        self.used_vol = np.full(365, 0)
        self.daily_rchrg_vol = np.full(365, 0)
        self.sort_idx = 0
        if all_srcs is None:
            self.compat_srcs = []
        else:
            self.compat_srcs = all_srcs

    def set_daily_recharge(self, new_vol, day):
        '''sets the daily recharge value'''

        self.daily_rchrg_vol[day] += new_vol

    def update_daily_recharge(self, idx):
        ''' update daily_rchrg_vol values with
        minimum of perc_rate or curr_cap for given index'''

        recharge_vol = min(self.perc_rate, self.curr_capacity)
        self.set_daily_recharge(recharge_vol, idx)

    def update_usage(self, val, idx):
        '''update used_vol values with use value for given
        index and update the current capacity to use value'''

        self.used_vol[idx] += val
        self.curr_capacity += val

    def get_annual_recharge_AF(self):
        '''get annual recharge in AF''' # verify in AF and not CF

        annual_vol = sum(self.daily_rchrg_vol)
        return(annual_vol)

    def check_for_limited_cap(self, idx):
        '''limit max capacity based on day of water year'''

        self.max_capacity = 10000

        if idx >= 10 and idx <= 30:
            # limited capactiy in October (10/11-10/31)
            self.max_capacity = 5000
        elif idx >= 151 and idx < 182:
            # limited capacity in March, 151 = March 1, 152 leap years
            # circle back to leap year handling- does it matter?
            self.max_capacity = 9000

    def use_canal(self, idx, wafr):
        '''wut the wafr'''

        self.check_for_limited_cap(idx)

        for source in self.compat_srcs:
            vol_avail_from_wafr = wafr[source][idx]
            if vol_avail_from_wafr > 0:
                canal_accpt_vol = max(self.max_capacity - self.curr_capacity + self.perc_rate, 0)
                if vol_avail_from_wafr >= canal_accpt_vol:
                    usable_vol_from_source = canal_accpt_vol
                else:
                    usable_vol_from_source =  vol_avail_from_wafr
                self.update_usage(usable_vol_from_source, idx)
                wafr[source][idx] -= usable_vol_from_source
        
        self.update_daily_recharge(idx)

class BaseSite(Site):
    '''define base site and update use and recharge vals'''
    crop_calendar = CropCalendar

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.all_sources = list()

        self.unused_vol = np.full(365, 0)
        self.sort_idx = 0
        self.curr_capacity = 0
        self.used_vol = np.full(365, 0)
        self.daily_recharge_vol = np.full(365, 0)
        self.precip = np.full(365, 0)
        if self.capital_cost is None: self.capital_cost = 0
        if self.cost_pump is None: self.pumping_cost = 0
        if self.acres is None: self.acreage = 0
        if self.cost_unused is None: self.cost_unused = 0
        if self.cost is None: self.cost = 0
        if self.cost_pw is None: self.cost_pw = 0
        self.site_id = self.GRATID
        # self.bottleneck_id = self.bottleneck_id
        if self.flowlimit_acrefeetdaily is None: self.flow_limit = 0
        if self.capacity is None: self.capacity = 0
        if self.perc_rate is None: self.perc_rate = 0
        self.index = sum(filter(None, [self.stor_ind, self.cost_ind, self.convey_ind, 
            self.vol_ind, self.retent_ind, self.infil_ind]))
        self.soil_type = self.SAGBI_Class
        if self.crop is None: self.crop = self.r_type

        # continue here...
        ''' if the id num in DiversionSources (convert to int)
        exists in the source map, return the key (str) and append
        to the compatible source list'''
        # self.all_sources = ['Bear Canal', 'Another Canal']
        # self.DiversionSources = '1, 2, 3, 4'
        
        srcs = list(map(lambda a: int(a), self.DiversionSources.split(';')))
        for s in srcs:
            if s in self.all_sources

        self.compatible_sources = filter()
        

    def get_site_cost(self):

        num_times_used = reduce(lambda a, b: a + 1 if b > 0 else a, self.used_vol)
        annual_pumping_cost = sum(self.used_vol) * self.pumping_cost

        cost_per_used_day = num_times_used * (self.cost_pw/7) * self.acreage

        if num_times_used > 0:
            annual_cost = self.acreage *self.cost
        else:
            annual_cost = self.acreage * self.cost_unused
        
        r = sum(self.capital_cost + cost_per_used_day + annual_cost + annual_pumping_cost)
        return(r)

        
