import numpy as np
import matplotlib.pyplot as plt

# Example coordinates (replace these with your actual coordinates)
blue_coords = [(941, 114), (967, 115), (1058, 115), (1010, 119), (931, 137), (951, 138), (991, 139), (1022, 139), (1041, 140), (1063, 139), (897, 166), (933, 164), (953, 165), (975, 168), (999, 168), (1024, 167), (1054, 169), (1070, 165)] 
yellow_coords = [(856, 84), (852, 117), (853, 144), (857, 183), (860, 206), (861, 212), (916, 228), (966, 229), (1031, 237), (1087, 235), (1111, 217), (1113, 187), (1122, 117), (1125, 103), (1143, 85), (1145, 114), (1137, 140), (1143, 168), (1143, 194), (1138, 231), (1106, 268), (1069, 270), (1054, 269), (987, 257), (965, 257), (923, 258), (864, 252), (818, 226), (802, 185), (798, 125), (804, 86), (804, 84)] 

# Create the dataset
blue_labels = np.zeros(len(blue_coords))  # Label blue dots as 0
yellow_labels = np.ones(len(yellow_coords))  # Label yellow dots as 1

data = np.array(blue_coords + yellow_coords)
labels = np.concatenate((blue_labels, yellow_labels)).reshape(-1, 1)

# Normalize data
data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# Shuffle data
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        return z * (1 - z)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, output):
        m = X.shape[0]
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid_derivative(output)

        self.a1_error = self.output_delta.dot(self.W2.T)
        self.a1_delta = self.a1_error * self.sigmoid_derivative(self.a1)

        self.W2 += self.a1.T.dot(self.output_delta) / m
        self.b2 += np.sum(self.output_delta, axis=0, keepdims=True) / m
        self.W1 += X.T.dot(self.a1_delta) / m
        self.b1 += np.sum(self.a1_delta, axis=0) / m

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            
            if (epoch+1) % 100 == 0:
                loss = np.mean(np.square(y - output))
                print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss:.4f}')

# Initialize the neural network
input_size = 2
hidden_size = 10
output_size = 1

model = SimpleNN(input_size, hidden_size, output_size)

# Training parameters
epochs = 1000
learning_rate = 0.01

# Train the model
model.train(data, labels, epochs, learning_rate)

# Generate a grid of points
xx, yy = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
grid = np.c_[xx.ravel(), yy.ravel()]

# Get predictions for each point in the grid
predictions = model.forward(grid)

# Reshape the predictions back to the grid shape
zz = predictions.reshape(xx.shape)

# Plot the decision boundary
plt.contourf(xx, yy, zz, levels=[0, 0.5, 1], alpha=0.5, cmap='coolwarm')
plt.scatter(*zip(*blue_coords), color='blue', label='Blue')
plt.scatter(*zip(*yellow_coords), color='yellow', label='Yellow')
plt.legend()
plt.show()


