import json, sys
from client import PersonalCognitiveLoadBalancerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "personal-cognitive-load-balancer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "balance_cognitive_schedule", "description": "Calculates daily attention fragmentation index (AFI) and restructures agendas into protected deep work blocks."}]}}
    elif method == "tools/call":
        client = PersonalCognitiveLoadBalancerClient()
        res = client.balance_cognitive_schedule()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = PersonalCognitiveLoadBalancerClient()
        print(json.dumps(client.balance_cognitive_schedule(), indent=2))
