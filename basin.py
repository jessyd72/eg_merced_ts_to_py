''' 
Use Basins
'''

from functools import reduce
from .base_site import BaseSite

class Basin(BaseSite):

    def __init__(self):

        super().__init__()
        self.curr_capacity = 0

    def update_daily_vals(self, idx):
        '''update daily recharge vol array's value 
        based on index update the current capacity'''

        recharge_vol = min(self.perc_rate, self.capacity)
        self.set_daily_recharge(recharge_vol, idx)
        self.curr_capacity = max(self.capacity - self.perc_rate, 0)

    def get_site_cost(self):
        '''get site cost to sort site results'''

        num_times_used = reduce(lambda a, v: 
                        a + 1 if v > 0 else a,
                        self.used_vol, 0)

        if num_times_used > 0:
            return(self.cost)
        else:
            return(self.cost_unused)

    def get_site_vol(self):

        return(self.capacity - self.curr_capacity + self.perc_rate)

    def set_used_vol(self, new_vol, day):

        self.used_vol[day] += new_vol
        self.curr_capacity = self.curr_capacity + new_vol

    def use_site(self, idx, wafr, bottlenecks, daily_precip):

        for src in self.compatible_sources:

            vol_avail_from_wafr = wafr[src][idx]
            self.set_precip(daily_precip, idx)
            avail_site_vol = max(self.get_site_vol(idx), 0)
            site_vol_need = max(avail_site_vol - daily_precip, 0)
            # need to understand these bottleneck functions...
            avail_throughput = max(bottlenecks.getAvailableThroughput(self.bottleneck_id, idx), 0)

            wafr_applied = min(site_vol_need, vol_avail_from_wafr, avail_throughput)

            self.set_used_vol(wafr_applied, idx)
            wafr[src][idx] -= wafr_applied

            bottlenecks.updateUsage(self.bottleneck_id, idx, wafr_applied)

            self.update_daily_vals(idx)

