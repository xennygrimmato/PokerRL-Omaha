"""Mock pycrayon module to bypass dependency issues"""

class CrayonClient:
    def __init__(self, hostname="localhost"):
        self.hostname = hostname
        self._experiments = {}
    
    def create_experiment(self, xp_name):
        return MockExperiment(xp_name)
    
    def remove_experiment(self, xp_name):
        if xp_name in self._experiments:
            del self._experiments[xp_name]

class MockExperiment:
    def __init__(self, xp_name):
        self.xp_name = xp_name
    
    def add_scalar_value(self, name, step, value):
        pass
    
    def to_zip(self, filename):
        pass
