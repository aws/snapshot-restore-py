# Lambda Snapshot and Restore Hooks

The project uses a custom class `MyCustomClass` to manage snapshot and restore hooks. This class provides methods to register functions that will be executed before a snapshot is taken and after a restore operation is performed.

## Usage

### my_custom_class.py

This file contains the `MyCustomClass` definition, which registers runtime hooks in it's constructor

```python
from snapshot_restore_py import register_before_snapshot, register_after_restore

class MyCustomClass:
    def __init__(self):
       register_before_snapshot(self.before_snapshot)
       register_after_restore(self.after_restore)

    # some class specific code

    def before_snapshot(self):
        # define your logic here
        pass

    def after_restore(self):
        # define your logic here
        pass

```

### lambda_function.py

This is your main Lambda function file. It uses the `MyCustomClass` to register and manage hooks.

```python
from my_custom_class import MyCustomClass

my_custom_class = MyCustomClass()

def lambda_handler(event: dict, context):
   # define your Lambda function logic here
   pass
```

## How It Works

1. `MyCustomClass` is instantiated at the module level.
2. The `MyCustomClass` init method register hooks using the `register_before_snapshot` and `register_after_restore`
3. The Lambda runtime will execute these hooks at the appropriate times during snapshot and restore operations.

## Configuration

No additional configuration is required. Simply define your hooks in a class and import/initialize them in the `lambda_handler.py`.
