import os
from solana.rpc.api import Client
from solders.signature import Signature
from dotenv import load_dotenv

load_dotenv()
rpc_url = os.getenv("RPC_URL")
solana_client = Client(rpc_url)

def fetch_transaction_data(signature_str: str):
    try:
        sig = Signature.from_string(signature_str)
        
        response = solana_client.get_transaction(
            sig, 
            max_supported_transaction_version=0
        )
        return response.value
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None

def calculate_risk(tx_data):
    if not tx_data or not tx_data.transaction.meta:
        return "ERROR", 0
    
    score = 0
    logs = tx_data.transaction.meta.log_messages
    
    risk_factors = {
        "Instruction: Approve": 3,
        "Instruction: SetAuthority": 3,
        "Instruction: Transfer": 2,
        "Instruction: InitializeMint": 1
    }

    for log in logs:
        for factor, weight in risk_factors.items():
            if factor in log:
                score += weight

    if score >= 3:
        level = "HIGH 🔴"
    elif score >= 1:
        level = "MEDIUM 🟡"
    else:
        level = "LOW 🟢"
        
    return level, score