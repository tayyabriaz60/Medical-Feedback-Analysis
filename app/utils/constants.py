"""
Application constants and configuration values.
"""

# Medical departments available in the system
DEPARTMENTS = [
    "Emergency",
    "OPD",
    "IPD",
    "Lab",
    "Pharmacy",
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "General Medicine",
]

# Feedback statuses
FEEDBACK_STATUSES = [
    "pending_analysis",
    "reviewed",
    "in_progress",
    "resolved",
    "analysis_failed",
]

# Urgency levels
URGENCY_LEVELS = [
    "critical",
    "high",
    "medium",
    "low",
]

# Sentiment types
SENTIMENT_TYPES = [
    "positive",
    "negative",
    "neutral",
    "mixed",
]

