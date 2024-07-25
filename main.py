from write_tse_pypulseq import main as write_seq
from packages.simulate_seq import simulate_seq
from packages.plot_sim import plot_sim

seq_name = "tse_pypulseq"

write_seq(plot=False, write_seq=True, seq_filename=seq_name + '.seq')

simulate_seq(save=True, seq_filename=seq_name + '.seq')

plot_sim(plot={
    "phantom": True,
    "seq": True,
    "kspace": True,
    "reco": True
    }, seq_filename=seq_name) 