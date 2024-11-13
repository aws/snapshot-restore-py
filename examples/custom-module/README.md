# Lambda Snapshot and Restore Hooks

This project demonstrates how to use snapshot and restore hooks in AWS Lambda functions with SnapStart enabled using the `snapshot_restore_py` library with a custom module.

## Usage

### my_module.py

This file contains the functions that will be executed before snapshot and after restore operations.

```python
from snapshot_restore_py import register_before_snapshot, register_after_restore

@register_before_snapshot
def before_snapshot_function():
    # Define your logic here
    pass

@register_after_restore
def after_restore_function():
    # Define your logic here
    pass
```

### lambda_function.py

This is your main Lambda function file. It imports the `my_module`, which automatically registers the hooks.

```python
# When you import your custom module, the Runtime Hook automatically registers your hooks
from my_module import my_module

def lambda_handler(event: dict, context):
   # Define your Lambda function logic here
   pass
```

## How It Works

1. The `@register_before_snapshot` decorator registers a function to be executed before a snapshot is taken.
2. The `@register_after_restore` decorator registers a function to be executed after a restore operation.
3. When you import `my_module` in your Lambda function, the hooks are automatically registered.
4. The Lambda runtime will execute these hooks at the appropriate times during snapshot and restore operations.

## Configuration

No additional configuration is required. Simply define your hook functions in `my_module.py` and import the module in your Lambda function.

