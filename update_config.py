import json 
from solana.publickey import PublicKey
with open(f'../driftpy/protocol-v2/programs/drift/src/lib.rs', 'r') as f:
    data = f.read()
import re 
re_result = re.search('\[cfg\(not\(feature = \"mainnet-beta\"\)\)\]\ndeclare_id!\(\"(.*)\"\)', data)
pk = PublicKey(re_result.group(1))
print('program pk:', pk)

## update config program_id 
with open("config.json", 'r') as f: 
    data = json.load(f) 

# watch vault account balances 
import sys
sys.path.insert(0, '../driftpy/src/')
from driftpy.addresses import * 

accounts = []
n_spot_markets = 1
for i in range(n_spot_markets):
    spot_vault_public_key = get_spot_market_vault_public_key(pk, i)
    insurance_vault_public_key = get_insurance_fund_vault_public_key(pk, i)

    accounts.append(str(spot_vault_public_key))
    accounts.append(str(insurance_vault_public_key))

data['accounts_selector'] = {
    'owners': [str(pk)],
    'accounts' : accounts
}

with open("config.json", 'w') as f: 
    json.dump(data, f, indent=4)
