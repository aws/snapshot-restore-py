from snapshot_restore_py import register_before_snapshot, register_after_restore

class MyCustomClass:
    def __init__(self):
       register_before_snapshot(self.before_snapshot)
       register_after_restore(self.after_restore)
       pass

    # some class specific code

    def before_snapshot(self):
        # define your logic here
        pass

    def after_restore(self):
        # define your logic here
        pass
