# Lambda Snapshot and Restore Hooks

This project demonstrates how to use snapshot and restore hooks in AWS Lambda functions with SnapStart enabled using the `snapshot_restore_py` library with a custom module.


## Usage

### lambda_function.py

This is your main Lambda function file. Here we import required methods from `snapshot_restore_py` and use them to register runtime hooks

```python
from snapshot_restore_py import register_before_snapshot, register_after_restore

@register_before_snapshot
def before_snapshot_function():
    # define your logic here
    pass

@register_after_restore
def after_restore_function():
    # define your logic here
    pass

def lambda_handler(event: dict, context):
   # define your logic here
   pass
```

## How It Works

1. The `@register_before_snapshot` decorator registers a function to be executed before a snapshot is taken.
2. The `@register_after_restore` decorator registers a function to be executed after a restore operation.
3. The Lambda runtime will execute these hooks at the appropriate times during snapshot and restore operations.

## Configuration

No additional configuration is required
