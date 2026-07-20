from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator #package for running on classical simulators rather than real hrdware


#creating a Bell state
qc = QuantumCircuit(2, 2) #creates a circuit with 2 quibits (starting at \ket{0}, and 2 classical bits which store results)
qc.h(0)        # applies a Hadamard gate to q0 - this puts it in a superposition of \ket{0} and \ket{1}
qc.cx(0, 1)    # applies a control not gate
qc.measure([0, 1], [0, 1]) # measure qubit 0 and store the result in classical bit 0; measure qubit 1 and store the result in classical bit 1. [qubits], [classical_bits]

print(qc.draw())

# Run it on the local simulator
sim = AerSimulator()
result = sim.run(qc, shots=1000).result() #Runs the circuit 1000 times ("shots") on the simulator and counts how often each outcome (00, 01, 10, 11) occurred.
counts = result.get_counts()
print(counts)