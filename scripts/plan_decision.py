import json
import os

with open('suggestion.json') as f:
    suggestion = json.load(f)

requested_type = os.getenv('REQUESTED_TYPE', '')
suggested_type = suggestion['suggested_type']
decision = suggestion['decision']

# Determine if approval is needed
approval_required = requested_type != suggested_type and requested_type != ''

with open('plan_result.json', 'w') as f:
    json.dump({
        'approval_required': approval_required,
        'suggested_type': suggested_type,
        'requested_type': requested_type,
        'decision': decision
    }, f)

print("Approval required:", approval_required)