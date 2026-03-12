import os
import sys
import uuid
import jwt
import subprocess
from urllib.parse import urlencode

# Environment variables
ACCESS_KEY = os.environ.get('UPBIT_ACCESS_KEY')
SECRET_KEY = os.environ.get('UPBIT_SECRET_KEY')

def generate_jwt(query_params=None):
    payload = {
        'access_key': ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
    }
    
    if query_params:
        import hashlib
        query_string = urlencode(query_params).encode('utf-8')
        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()
        payload['query_hash'] = query_hash
        payload['query_hash_alg'] = 'SHA512'

    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jwt_token

def execute_aif_order(command, ticker, side, amount_or_volume):
    query_params = {'market': ticker, 'side': side, 'ord_type': 'price' if side == 'bid' else 'market'}
    if side == 'bid':
        query_params['price'] = str(amount_or_volume)
    else:
        query_params['volume'] = str(amount_or_volume)
        
    token = generate_jwt(query_params)
    
    aif_path = "aif-upbit" # Assuming it's in PATH or same dir
    
    # Login to save token
    subprocess.run([aif_path, "auth", "login", "--token", token], stdout=subprocess.DEVNULL)
    
    # Execute actual command
    args = [aif_path, command, "--market", ticker, "--side", side, "--ord_type", query_params['ord_type']]
    if side == 'bid':
        args.extend(["--price", str(amount_or_volume)])
    else:
        args.extend(["--volume", str(amount_or_volume)])
        
    subprocess.run(args)