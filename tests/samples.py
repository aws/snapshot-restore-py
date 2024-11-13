from snapshot_restore_py import register_before_snapshot, register_after_restore

@register_before_snapshot
def fun_1():
    return 1

@register_after_restore
def fun_2():
    return 2

def fun_3(x, **kwargs):
    print(**kwargs)
    return x

register_before_snapshot(fun_3, 1)
register_after_restore(fun_3, 2, arg1="Lambda", arg2="SnapStart")

