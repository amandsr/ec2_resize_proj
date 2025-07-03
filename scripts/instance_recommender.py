import json

with open('metrics.json') as f:
    data = json.load(f)

cpu = data['cpu_avg']
mem = data['memory_avg']

# Mock instance type mappings (downgrade/upgrade logic)
with open('config/instance_type_matrix.json') as f:
    matrix = json.load(f)

# Assuming instance type is passed from env or fixed for now
current_type = 't3.medium'

suggested_type = current_type
reason = ""

if cpu > 70 or mem > 70:
    suggested_type = matrix[current_type]['upgrade']
    reason = "High CPU or memory, suggesting upgrade."
elif cpu < 30 and mem < 30:
    suggested_type = matrix[current_type]['downgrade']
    reason = "Low CPU and memory, suggesting downgrade."
else:
    reason = "No change needed."

with open('suggestion.json', 'w') as f:
    json.dump({
        'suggested_type': suggested_type,
        'decision': 'upgrade' if suggested_type != current_type and (cpu > 70 or mem > 70) else 'downgrade' if suggested_type != current_type else 'none',
        'reason': reason
    }, f)

print("Suggested instance type:", suggested_type)