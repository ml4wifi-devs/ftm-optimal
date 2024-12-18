from ctypes import *


MEMBLOCK_KEY = 2333
MEM_SIZE = 64


# ns3-ai environment structure
class Env(Structure):
    _pack_ = 1
    _fields_ = [
        ('ftmSuccessRate', c_double)
    ]


# ns3-ai action structure
class Act(Structure):
    _pack_ = 1
    _fields_ = [
        ('numberOfBurstExponent', c_uint8),
        ('burstDuration', c_uint8),
        ('minDeltaFtm', c_uint8),
        ('partialTsfTimer', c_uint16),
        ('partialTsfNoPref', c_bool),
        ('asap', c_bool),
        ('ftmsPerBurst', c_uint8),
        ('burstPeriod', c_uint16)
    ]
