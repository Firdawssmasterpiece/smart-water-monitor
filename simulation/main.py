
print("=== Smart Engineering Assistant ===")

class DecisionSystem:
    def __init__(self, threshold):
        self.threshold = threshold

    def analyze(self, sensor_value):
        if sensor_value > self.threshold:
            return "ACTION: Activate system"
        elif sensor_value == self.threshold:
            return "ACTION: Standby"
        else:
            return "ACTION: Deactivate system"


# Simulation
system = DecisionSystem(threshold=50)

test_values = [20, 50, 75]

for value in test_values:
    decision = system.analyze(value)
    print(f"Sensor value: {value} -> {decision}")
