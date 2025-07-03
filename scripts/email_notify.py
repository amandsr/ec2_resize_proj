import json

with open('suggestion.json') as f:
    suggestion = json.load(f)

msg = f"""
EC2 Instance Type Change Completed
Suggested Type: {suggestion['suggested_type']}
Decision: {suggestion['decision']}
Reason: {suggestion['reason']}
"""

print("Sending notification:")
print(msg)
# Add SMTP or AWS SES logic as needed