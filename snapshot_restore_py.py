"""
snapshot-restore-py

This module provides functionality to register callables that will be executed
before creating a snapshot or after restoring an execution environment from a snapshot.

Key Features:
- Register functions to be called before snapshot creation
- Register functions to be called after environment restoration
- Support for both function calls and decorator syntax

Public Functions:
- register_before_snapshot: Register a function to be executed before snapshot creation
- register_after_restore: Register a function to be executed after environment restoration

Usage:
    from snapshot_restore_py import register_before_snapshot, register_after_restore

    @register_before_snapshot
    def cleanup():
        # Perform cleanup before snapshot

    @register_after_restore
    def reinitialize(arg1, arg2="default"):
        # Reinitialize after restoration
"""

__version__ = "1.0.0"
__author__ = """Amazon Web Services"""
__all__ = ["register_before_snapshot", "register_after_restore"]


from collections.abc import Callable
from typing import Any


_before_snapshot_registry: list[Callable[..., Any]] = []
_after_restore_registry: list[Callable[..., Any]] = []

def register_before_snapshot(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Callable[..., Any]:
    """
    Register a function to be executed before a snapshot is taken.

    This function can be used as a decorator or called directly.

    Params
    ------
    func: Callable
        The function to be registered.
    *args
        Positional arguments to be passed to the function when called.
    **kwargs
        Keyword arguments to be passed to the function when called.

    Returns
    -------
    Callable
        func is returned to facilitate usage as a decorator

    Example:
        @register_before_snapshot
        def cleanup():
            # Cleanup code here
    """
    _before_snapshot_registry.append((func, args, kwargs))
    return func

def register_after_restore(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Callable[..., Any]:
    """
    Register a function to be executed after the execution environment is restored from a snapshot.

    This function can be used as a decorator or called directly.

    Params
    ------
    func: Callable
        The function to be registered.
    *args
        Positional arguments to be passed to the function when called.
    **kwargs
        Keyword arguments to be passed to the function when called.

    Returns
    -------
    Callable
        func is returned to facilitate usage as a decorator

    Example:
        @register_after_restore
        def reinitialize(arg1="default"):
            # Reinitialization code here
    """
    _after_restore_registry.append((func, args, kwargs))
    return func


def get_before_snapshot() -> list[Callable[..., Any]]:
    """
    Retrieve the registry of functions to be executed before snapshot creation.

    Used by the execution environment that manages the snapshotting and restore process

    Returns
    -------
    list[Callable[..., Any]]:
        A list of tuples containing the registered functions and their arguments.
    """
    return _before_snapshot_registry

def get_after_restore() -> list[Callable[..., Any]]:
    """
    Retrieve the registry of functions to be executed after environment restoration.

    Used by the execution environment that manages the snapshotting and restore process

    Returns
    -------
    list[Callable[..., Any]]:
        A list of tuples containing the registered functions and their arguments.
    """
    return _after_restore_registry
