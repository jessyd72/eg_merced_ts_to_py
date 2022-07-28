'''
GRAT
'''

from collections import defaultdict
import numpy as np

class Site(object):

    def __init__(self, crop, acres, stor_ind, cost_ind, convey_ind, vol_ind, retent_ind,
                owner, SAGBI_Class, r_type, precip_IDX, GRATID, infil_ind, cost, perc_rate,
                capacity, cost_unused, cost_pw, cost_pump, capital_cost, subbasin, potential,
                SAGBI_AVG, sequence, OBJECTID, bottleneck_id, flowlimit_acrefeetdaily, recharge,
                DiversionSources, INBASINRET = None, FIRORP_combined_priority = None, ECOFIRO_combined_priority = None):

        self.crop_list = []
        self.crop = crop
        self.acres = acres
        self.stor_ind = stor_ind
        self.cost_ind = cost_ind
        self.convey_ind = convey_ind
        self.vol_ind = vol_ind
        self.retent_ind = retent_ind
        self.parcel = None # number
        self.owner = owner
        self.SAGBI_Class = SAGBI_Class
        self.r_type = r_type
        self.precip_IDX = precip_IDX
        self.GRATID = GRATID
        self.infil_ind = infil_ind
        self.cost = cost
        self.perc_rate = perc_rate
        self.capacity = capacity
        self.region_id = ''
        self.cost_unused = cost_unused
        self.cost_pw = cost_pw
        self.cost_pump = cost_pump
        self.capital_cost = capital_cost
        self.subbasin = subbasin
        self.potential = potential
        self.SAGBI_AVG = SAGBI_AVG
        self.sequence = sequence
        self.OBJECTID = OBJECTID
        self.bottleneck_id = bottleneck_id
        self.flowlimit_acrefeetdaily = flowlimit_acrefeetdaily
        self.recharge = recharge
        self.DiversionSources = DiversionSources

class QualityVolume:
    # k (str), v (list of numbers)
    qv_dict = defaultdict(list)

class CropCalendar:
    # k (str), v (dict-> QualityVolume.qv_dict)
    cc_dict = defaultdict(dict)

class WAFREntry:
    # k (str), v(list of numbers)
    wafr_dict = defaultdict(list)

class WAFRDataResponse:
    # k (str), v (dict-> WAFREntry.wafr_dict)
    wafr_datar_dict = defaultdict(dict)

class PrecipEntry:
    # k (str), v (list of numbers)
    precip_dict = defaultdict(list)

class PrecipDataResponse:
    # k (str), v (dict-> PrecipEntry.precip_dict)
    precip_datar_dict = defaultdict(dict)

class BottleneckAttributes:

    def __init__(self, bottleneck_id=None, canal=None, flow_cfs=None, af_per_day=None):
        
        self.bottleneck_id = bottleneck_id
        self.canal = canal
        self.flow_cfs = flow_cfs
        self.af_per_day = af_per_day

class Bottleneck:

    attributes = BottleneckAttributes

class BottleneckData:

    def __init__(self, canal=None):

        self.canal = canal
        # k (number), v (BottleneckAttributes object)
        self.bottleneck_dict = defaultdict(lambda: 'default')

class availableThroughputs:
    # k (number), v (list of numbers)
    avail_throughput_dict = defaultdict(list)

class CapacityLog:
    # k (number), v (list of numbers)
    cap_log_dict = defaultdict(list)

class SourceObject:

    def __init__(self, priority, id):

        self.priority = priority
        self.id = id

class SourceMap:
    # k (str), v (SourceObject object)
    source_map_dict = defaultdict(lambda: 'default')

class WAFRDataObjct:
    # k (str), v 
    wafr_data_obj_dict = defaultdict(lambda: 'default')

class cfsDataObject:
    # k (str), v 
    cfs_data_obj_dict = defaultdict(lambda: 'default')

class UpdateUsageFunction:

    def __init__(self, id=None, day=None, amount=None):

        self.id = id
        self.day = day
        self.amount = amount

class GetAvailableThroughputFunction:

    def __init__(self, id=None, day=None):

        self.id = id
        self.day = day





