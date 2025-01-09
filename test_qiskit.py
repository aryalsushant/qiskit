from qiskit import QuantumCircuit

# Create a quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate
qc.measure(0, 0)

print("Quantum Circuit created successfully!")
