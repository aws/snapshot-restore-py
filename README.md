# Snapshot Restore for Python

### Description

This is the Snapshot Restore for Python library which can be used for registering [runtime hooks](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks-python.html) in Snapstart enabled Python Lambda functions

This library provides two decorators that you can use to define your runtime hooks:

* `@register_before_snapshot` - For code you want to run before a snapshot is taken
* `@register_after_restore` - For code you want to run after a snapshot is restored

Alternatively, you can use the following methods to register callables for runtime hooks:

* `register_before_snapshot(func, *args, **kwargs)`
* `register_after_restore(func, *args, **kwargs)`

## Code sample

### Register hooks using decoratores
```
from snapshot_restore_py import register_before_snapshot, register_after_restore

def lambda_handler(event, context):
    # lambda handler code
    ...

@register_before_snapshot
def fn_before_snapshot():
    # your logic here
    ...

@register_after_restore
def fn_after_restore():
    # your logic here
    ...
```

### Register hooks using functions
```
from snapshot_restore_py import register_before_snapshot, register_after_restore

def lambda_handler(event, context):
    # lambda handler code
    ...

def fn_before_snapshot():
    # your logic here
    ...

def fn_after_restore():
    # your logic here
    ...

register_before_snapshot(fn_before_snapshot)
register_after_restore(fn_after_restore)

```

Please refer to the [examples provided](examples) for more details.

## Important points to note

### Execution order

  - BeforeSnapshot hooks will run in the **reverse** order** as they were registered
  - AfterRestore hooks will run in the **same order** as they were registered.

### Best Practices

  - While decorators are convenient, using functions for hook registration can offer more explicit control over the order of execution and improve code readability.

### Registering functions with arguments

  - To register a function with specific arguments, just use the `register_...(func, *args, **kwargs)` method.

### Importing Modules

  - If you register a hook in a file that isn’t imported in your main handler, it will be ignored.
  - If you import hooks within the `lambda_handler`, they won’t be executed. Instead, make sure all essential imports are at the **top level** of your code. This way, your hooks will be recognized and executed as intended!

### Duplicate registrations

  - If you register a function more than once (like decorating it and registering it again), it’ll run multiple times.

### Local environment

- **Pre-installed in Lambda Runtime**: When deploying to AWS Lambda, you do not need to include this library in your deployment package, as it is already pre-installed in the Lambda runtime environment.

- **Local Testing Consideration**: For local testing, ensure that you include the library in your development dependencies to avoid any import issues during testing.
