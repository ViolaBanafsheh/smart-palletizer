"""
Smart Palletizer - UR5e Robotic Palletizing Control System

A comprehensive Python control system for automating palletizing operations
with the UR5e collaborative robot. Includes path planning, collision avoidance,
mixed-SKU support, and real-time optimization.

Version: 0.1.0
License: MIT
"""

__version__ = "0.1.0"
__author__ = "Viola Banafsheh"
__license__ = "MIT"

from .core.robot_controller import RobotController
from .core.ur_script_generator import URScriptGenerator
from .planner.path_planner import PathPlanner
from .pallet.pallet_manager import PalletManager
from .safety.collision_checker import CollisionChecker
from .io.gripper_controller import GripperController
from .runtime.state_machine import StateMachine

__all__ = [
    "RobotController",
    "URScriptGenerator",
    "PathPlanner",
    "PalletManager",
    "CollisionChecker",
    "GripperController",
    "StateMachine",
]