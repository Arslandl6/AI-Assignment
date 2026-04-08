import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# 1. Create dummy time series data
data = np.sin(np.linspace(0, 100, 500))

# 2. Normalize
scaler = MinMaxScaler()
data = scaler.fit_transform(data.reshape(-1,1))

# 3. Create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data)-seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

seq_length = 10
X, y = create_sequences(data, seq_length)

# 4. Train-test split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# 5. Convert to tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)

# 6. LSTM Model
class LSTMModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=50, batch_first=True)
        self.fc = nn.Linear(50,1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:,-1,:])
        return out

model = LSTMModel()

# 7. Training
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

losses = []

for epoch in range(20):
    output = model(X_train)
    loss = criterion(output, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    losses.append(loss.item())
    print(f"Epoch {epoch}, Loss: {loss.item()}")

# 8. Evaluation
model.eval()
X_test = torch.tensor(X_test, dtype=torch.float32)
pred = model(X_test).detach().numpy()

# 9. Plot loss
plt.plot(losses)
plt.title("Training Loss")
plt.show()

# 10. Plot predictions
plt.plot(pred, label="Predicted")
plt.plot(y_test, label="Actual")
plt.legend()
plt.show()