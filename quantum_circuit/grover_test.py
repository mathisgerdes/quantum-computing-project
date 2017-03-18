from .mainframe import State
from .functional_gates import Gate as FunctionalGate
from .matrix_gates import Gate as MatrixGate
import .gates_library as g_lib
import numpy as np
import math

# arbitrary number of qubits
qubit_count = 4
basis_size = 1 << qubit_count
# arbitrary key: 1000 - 1 gives the marked state
key = 0b0001
# optimal number of iterations of Grover step
n = math.floor(math.pi / (4*math.asin(basis_size ** (-1/2))))
# initial state
state = State.from_basis_state(1 << qubit_count, 0)
# matrix to apply the phase flip
flip_gate = g_lib.phase_flip_gate(qubit_count, key)
# matrix to apply diffusion
diff_gate = g_lib.diffusion_gate(qubit_count)
# matrix to apply Hadamard to every qubit
gate_list = [g_lib.hadamard for i in range(qubit_count)]
H_n = g_lib.create_gate(qubit_count, gate_list)

#create superposition by applying Hadamard to every qubit
state = State(np.dot(state, H_n.matrix))
#perform Grover step required number of times
full = flip_gate * diff_gate
for i in range(n-1):
    full *= flip_gate * diff_gate
#apply the matrix to get the final state
final = State(np.dot(state, full.matrix))
print (final)