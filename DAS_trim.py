#%%
from obspy import read, UTCDateTime
import os, glob
# variable
data_path = '/home/patrick/Work/DAS_phasenet/PhaseNet/data/test_062913.mseed'
sac_path = '/raid1/SM_data/archive/2023/TW/preprocessing/SM01/EPZ.D/TW.SM01.00.EPZ.D.2023.284'
test_path = '/home/patrick/Work/DAS_phasenet/PhaseNet/data'
os.makedirs(test_path, exist_ok=True)
test_2_path = '/home/patrick/Work/DAS_phasenet/PhaseNet/data_2'
os.makedirs(test_2_path, exist_ok=True)
#event_time = UTCDateTime("2023-01-02T:06:29:13.29")
event_time = UTCDateTime("2023-10-11T:10:36:57")
start_time = event_time - 30
end_time = event_time + 90
# main
st = read(sac_path)
#%%
if len(st) > 1:
    st = st.merge(fill_value = 'interpolate')
st.trim(starttime=start_time, endtime=end_time)
output_path = os.path.join(test_2_path, f"test_0.sac")
st.write(output_path, format="SAC")
# %%
