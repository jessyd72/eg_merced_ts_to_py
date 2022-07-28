''' 
Use Canals
'''

# from dataclasses import dataclass
import numpy as np

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
        self.compat_srcs = []

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

