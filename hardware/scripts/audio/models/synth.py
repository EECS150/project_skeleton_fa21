from dataclasses import dataclass, field
from typing import List

from FixedPoint import FXnum

from models.nco import NCO


@dataclass
class Synth:
    carrier_ncos: List[NCO]
    modulator_ncos: List[NCO]
    modulator_idx_shift: int = field(default=0)
    modulator_fcw: int = field(default=0)
    fcws: List[int] = field(init=False)
    note_enabled: List[bool] = field(init=False)
    # TODO: implement mixer

    def __post_init__(self):
        assert len(self.carrier_ncos) == len(self.modulator_ncos)
        assert all(self.carrier_ncos[0].fsamp == x.fsamp for x in self.carrier_ncos)
        assert all(self.modulator_ncos[0].fsamp == x.fsamp for x in self.modulator_ncos)
        self.fcws = [0] * len(self.carrier_ncos)
        self.note_enabled = [False] * len(self.carrier_ncos)

    def next_sample(self) -> FXnum:
        modulator_samples = [nco.next_sample(self.modulator_fcw)[0] if (en and self.modulator_fcw != 0) else nco.zero for nco, en in zip(self.modulator_ncos, self.note_enabled)]
        freq_modulated_fcws = [fcw + (mod_samp.scaledval << self.modulator_idx_shift) for fcw, mod_samp in zip(self.fcws, modulator_samples)]
        carrier_samples = [nco.next_sample(freq_modulated_fcws[idx])[0] if en else nco.zero for (idx, nco), en in zip(enumerate(self.carrier_ncos), self.note_enabled)]
        return sum(carrier_samples)
