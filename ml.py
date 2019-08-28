
# dupa exemplul din https://becominghuman.ai/making-a-simple-neural-network-2ea1de81ec20

'''
Let’s say there is a 4 button machine that gives you food if you press the right button 
( or perhaps energy if you are a robot),the objective will be to learn which button 
provides the goods
We can indicate when a button is pressed (graphically) in the following way:
'''
inputs = [0, 0, 1, 0] # the perception of which button was pressed

# Notice all the weights are zero, so the neural net is in a blank state yet fully connected, same as a newborn.
weights = [0, 0, 0, 0] # The numbers in between neurons indicate the weight of the connection
# We can call inputs and weights vectors for convenience.

desired_result = 1
learning_rate = 0.2 # bigger rate,bigger faster learnings : )
trials = 6

# Might look complex, but all it does is multiply weight/input pairs and adds the result.
def evaluate_neural_network(input_array, weight_array):
	result = 0
	for i in range(len(input_array)):
		layer_value = input_array[i] * weight_array[i]
		result += layer_value
	print("evaluate_neural_network: " + str(result))
	print("weights: " + str(weights))
	return result

# In order to detect a mismatch ( and by how much ) we will add an error function:
# Error = Desired Output - Neural Net Output
def evaluate_error(desired, actual):
	error = desired - actual
	print("evaluate_error: " + str(error))
	return error

# How one codes such an algorithm is a matter of choice, for simplicity sake I am just adding the learning rate to the weight
# In use this learn function would simply add our learning rate to the active neuron’s weight vector
def learn(input_array, weight_array):
	print("learning...")
	for i in range(len(input_array)):
		if input_array[i] > 0:
			weight_array[i] += learning_rate
			
def train(trials):
	for i in range(trials):
		neural_net_result = evaluate_neural_network(inputs, weights)
		learn(inputs, weights)
			
train(trials)
