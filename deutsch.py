from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator #package for running on classical simulators rather than real hrdware

# f:{0,1} -> {0,1}
# if f(0) = f(1), f is constant. if f(0) =/= f(1), f is balanced
# classically, you need 2 calls to determine if f is constant or balanced. quantumly, you only need 1.
# deutsch algorithm determines if it is constant or balanced. the circuit is H -> f -> H, w ancilla qubit initialised to \ket{-}


qc = QuantumCircuit(2, 2) #creates a circuit with 2 quibits (starting at \ket{0}, and 2 classical bits which store results)
qc.x(1) #flipping flip qubit 1 to |1>  (qubit 0 stays |0>)

print(qc.draw())



#=====initial state=====
qc.h(0) #applies a Hadamard gate to q0 - this puts it in a superposition of \ket{0} and \ket{1}
qc.h(1) #H to q1 (ancilla initialised to \ket{-})


#====applying CU=====
# qc.cu(theta, phi, lam, gamma, control_qubit, target_qubit). The four angles (theta, phi, lam, gamma) define exactly which single-qubit unitary you're controlling

#f:{0,1} -> {0,1} gives us 4 distinct functions; define them all individually
def deutsch_oracle(function_type):
    qc = QuantumCircuit(2)  # qubit 0 = input, qubit 1 = output/answer

    if function_type == 'constant_0':
        pass  # f(x) = 0 always -> do nothing
    elif function_type == 'constant_1':
        qc.x(1)  # f(x) = 1 always -> flip output unconditionally
    elif function_type == 'identity':
        qc.cx(0, 1)  # f(x) = x -> CNOT (this IS a controlled-X, the simplest CU)
    elif function_type == 'negation':
        qc.x(0)
        qc.cx(0, 1)
        qc.x(0)      # f(x) = NOT x -> flip input, CNOT, flip input back

    return qc



qc.measure(0,1) # meaasure quibit 1 and store it in classical bit 1

print(qc.draw())

# Run it on the local simulator
sim = AerSimulator()
result = sim.run(qc, shots=1000).result() #Runs the circuit 1000 times ("shots") on the simulator and counts how often each outcome (00, 01, 10, 11) occurred.
counts = result.get_counts()
print(counts)