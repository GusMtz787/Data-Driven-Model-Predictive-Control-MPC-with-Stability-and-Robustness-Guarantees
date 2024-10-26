import numpy as np
from icecream import ic

# Pi = np.block([
#     [np.kron(np.eye(L), R), np.kron(np.eye(L), S)],
#     [np.kron(np.eye(L), S.T), np.kron(np.eye(L), Q)]
# ])

L = 34
m = 2
p = 2
# R = 1e-4 * np.eye(m)
# print(R)

# uno = np.eye(L)
# print(uno.shape)
# dos = np.kron(uno, R)
# print(dos.shape)

R = 1e-4 * np.eye(m)  # input weighting
Q = 3 * np.eye(p)  # output weighting
S = np.zeros((m, p))

first = np.kron(np.eye(L), R)
second = np.kron(np.eye(L), S)
third = np.kron(np.eye(L), S.T)
fourth = np.kron(np.eye(L), Q)
ic(S)
ic(S.T)

ic(first.shape)
ic(second.shape)
ic(third.shape)
ic(fourth.shape)

# Constructing the Pi matrix
Pi = np.block([
    [np.kron(np.eye(L), R), np.kron(np.eye(L), S)],
    [np.kron(np.eye(L), S.T), np.kron(np.eye(L), Q)]
])

ic(Pi.shape)
