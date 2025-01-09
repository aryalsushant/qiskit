from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit
qc = QuantumCircuit(2, 2)
qc.h(0)  # Apply Hadamard gate
qc.cx(0, 1)  # Apply CNOT gate
qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

print("Simulation Results:", counts)
