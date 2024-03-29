import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0,2,1,0],
							[1,4,1,0],
							[1,1,5,1],
							[0,1,3,0]])

training_outputs = np.array([[0,4,5,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((4,1)) - 1

print("Случайные инициализирующие веса:")
print(synaptic_weights)

for i in range(100):
	input_layer = training_inputs
	outputs = sigmoid(np.dot(input_layer, synaptic_weights))

	err = training_outputs - outputs
	adjustment = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
	synaptic_weights += adjustment

print("Weights after training: ")
print(synaptic_weights)

print("Result after training: ")
print(outputs)

new_inputs = np.array([1,1,1,1])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print("New situation: ")
print(output)