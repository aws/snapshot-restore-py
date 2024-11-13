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
