#%%
import json 
from solana.publickey import PublicKey
with open(f'../driftpy/protocol-v2/programs/clearing_house/src/lib.rs', 'r') as f:
    data = f.read()
import re 
re_result = re.search('\[cfg\(not\(feature = \"mainnet-beta\"\)\)\]\ndeclare_id!\(\"(.*)\"\)', data)
pk = PublicKey(re_result.group(1))
print('program pk:', pk)

## update config program_id 
with open("config.json", 'r') as f: 
    data = json.load(f) 

data['accounts_selector'] = {'owners': [str(pk)]}

with open("config.json", 'w') as f: 
    json.dump(data, f, indent=4)