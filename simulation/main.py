
print("Smart Engineering Assistant - Simulation démarrée")

def decision_system(input_value):
    if input_value > 50:
        return "Action A"
    else:
        return "Action B"

test_value = 42
print("Décision :", decision_system(test_value))
