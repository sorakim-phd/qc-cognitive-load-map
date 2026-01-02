"""
QC Cognitive Load Map
--------------------
This module defines a conceptual and computational scaffold
for modeling cognitive load in highly regulated organizational systems.
"""

class CognitiveLoadModel:
    def __init__(self):
        self.task_switching = 0
        self.documentation_density = 0
        self.time_pressure = 0

    def compute_load(self):
        """
        Simple placeholder function.
        Later this will be replaced with a formal model.
        """
        return (
            self.task_switching
            + self.documentation_density
            + self.time_pressure
        )
