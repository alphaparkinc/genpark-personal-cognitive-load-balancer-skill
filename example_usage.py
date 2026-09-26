import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import PersonalCognitiveLoadBalancerClient

def main():
    client = PersonalCognitiveLoadBalancerClient()
    res = client.balance_cognitive_schedule()
    print("=== Personal Cognitive Load Balancer Output ===")
    print(f"User: {res['user_name']} | AFI: {res['attention_fragmentation_index']} ({res['cognitive_health_status']})")
    print(f"Meetings: {res['meeting_count_today']} ({res['total_meeting_time_hours']}h) | Switch Latency: {res['estimated_context_switch_penalty_hours']}h")
    print(f"Focus Reserve: {res['uninterrupted_focus_available_hours']}h available")
    print(f"Agent Recommendation: {res['recommended_agent_action']}")
    print("\nProposed Restructured Schedule:")
    for k, v in res['recommended_focus_restructuring'].items():
        print(f"  * {k:35s}: {v}")

if __name__ == '__main__':
    main()
