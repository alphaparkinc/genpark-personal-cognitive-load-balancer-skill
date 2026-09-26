import json
import math
from typing import List, Dict, Any, Optional

class PersonalCognitiveLoadBalancerClient:
    """
    Production-grade personal cognitive load and context-switching balancer.
    Evaluates daily task schedules, calculates attention fragmentation index (AFI),
    and deterministically restructures agendas into protected deep-work blocks.
    """
    def __init__(self, target_deep_work_hours: float = 3.5):
        self.target_deep_work_hours = target_deep_work_hours

    def balance_cognitive_schedule(
        self,
        user_name: str = "Alex Morgan",
        calendar_events: Optional[List[Dict[str, Any]]] = None,
        backlog_tasks: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not calendar_events:
            calendar_events = [
                {"title": "Morning Standup", "duration_min": 30, "type": "meeting", "cognitive_intensity": "low"},
                {"title": "Product Architecture Review", "duration_min": 60, "type": "meeting", "cognitive_intensity": "high"},
                {"title": "Slack Triage & Inbox Clearing", "duration_min": 45, "type": "async", "cognitive_intensity": "low"},
                {"title": "1:1 Sync with Design Lead", "duration_min": 30, "type": "meeting", "cognitive_intensity": "medium"},
                {"title": "Client Status Check-in", "duration_min": 45, "type": "meeting", "cognitive_intensity": "medium"}
            ]

        if not backlog_tasks:
            backlog_tasks = [
                {"task": "Draft Q4 Strategic Roadmap Dossier", "estimated_hours": 2.5, "focus_required": "deep_work"},
                {"task": "Approve Expense Reports & Invoices", "estimated_hours": 0.5, "focus_required": "shallow_work"},
                {"task": "Review Smart Contract Security Audit", "estimated_hours": 1.5, "focus_required": "deep_work"}
            ]

        total_meeting_min = sum(e["duration_min"] for e in calendar_events if e["type"] == "meeting")
        meeting_count = sum(1 for e in calendar_events if e["type"] == "meeting")
        
        # Context-Switch Penalty: 22 minutes cognitive latency per fragmented meeting switch
        switch_latency_min = meeting_count * 22
        effective_work_day_min = 8 * 60
        remaining_free_min = max(0, effective_work_day_min - total_meeting_min - switch_latency_min)
        
        # Attention Fragmentation Index (0.00 = pure flow, 1.00 = severe ADHD/hyper-fragmented)
        afi = round(min(1.0, (total_meeting_min + switch_latency_min) / effective_work_day_min), 2)
        
        # Scheduling recommendation
        deep_work_blocks = []
        shallow_work_blocks = []
        for t in backlog_tasks:
            if t["focus_required"] == "deep_work":
                deep_work_blocks.append(f"{t['task']} ({t['estimated_hours']}h Focus)")
            else:
                shallow_work_blocks.append(f"{t['task']} ({t['estimated_hours']}h Batch)")

        status = "CRITICAL_ATTENTION_DEFICIT" if afi >= 0.70 else "MODERATE_FRAGMENTATION" if afi >= 0.45 else "HEALTHY_FOCUS_RESERVE"

        return {
            "balancer_id": "cgn_load_9901",
            "user_name": user_name,
            "meeting_count_today": meeting_count,
            "total_meeting_time_hours": round(total_meeting_min / 60.0, 1),
            "estimated_context_switch_penalty_hours": round(switch_latency_min / 60.0, 1),
            "uninterrupted_focus_available_hours": round(remaining_free_min / 60.0, 1),
            "attention_fragmentation_index": afi,
            "cognitive_health_status": status,
            "recommended_focus_restructuring": {
                "protected_morning_deep_work_block": "09:00 - 11:30 (Deep Work No-Meeting Zone)",
                "batched_afternoon_meeting_window": "13:30 - 15:30 (Consolidated Sprints)",
                "shallow_async_triage_buffer": "16:30 - 17:15 (Batch Communications)"
            },
            "scheduled_deep_work_tasks": deep_work_blocks,
            "scheduled_shallow_tasks": shallow_work_blocks,
            "recommended_agent_action": "REJECT_OR_DEFLECT_NEW_INVITES_TODAY" if afi >= 0.60 else "PERMIT_SELECTIVE_MEETINGS"
        }
