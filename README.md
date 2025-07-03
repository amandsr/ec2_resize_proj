# EC2 Instance Optimizer

This GitHub Actions-based project analyzes EC2 CPU and memory usage to suggest and apply instance type changes.

## Features
- Monitors usage via CloudWatch
- Recommends downgrade/upgrade based on thresholds
- Auto-applies changes if safe
- Optional manual approval

## Usage
Trigger the `trigger.yml` workflow manually with:
- `instance_id`
- `region`
- Optional `requested_type`