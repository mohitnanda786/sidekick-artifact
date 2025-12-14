import time

SECRET_KEY = "sk_prod_9b8e7f6a5d4c3b2a1f0e9d8c7b6a5948"

def lambda_handler(event, context=None):
    provided_key = event.get("headers", {}).get("x-api-key", "")
    
    if len(provided_key) != len(SECRET_KEY):
        return {"statusCode": 401, "body": "Invalid length"}
    
    for a, b in zip(provided_key, SECRET_KEY):
        if a != b:
            # Real CPU work on mismatch
            x = 0
            for i in range(20_000_000):
                x ^= i * 0xdeadbeef
            break
    else:
        time.sleep(0.4)
    
    return {"statusCode": 200, "body": "Welcome!"}
