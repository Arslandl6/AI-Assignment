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

# ===== BONUS TASK: TEXT CLASSIFICATION USING LSTM =====

import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Sample dataset (positive=1, negative=0)
texts = [
    "I love this product",
    "This is amazing",
    "Very bad experience",
    "I hate this",
    "Awesome work",
    "Worst service ever",
    "I am very happy",
    "Not good",
]

labels = [1,1,0,0,1,0,1,0]

# 2. Simple tokenization
vocab = {}
def tokenize(sentence):
    words = sentence.lower().split()
    return [vocab.setdefault(word, len(vocab)+1) for word in words]

tokenized = [tokenize(t) for t in texts]

# 3. Padding
max_len = max(len(seq) for seq in tokenized)
padded = [seq + [0]*(max_len - len(seq)) for seq in tokenized]

X = torch.tensor(padded, dtype=torch.long)
y = torch.tensor(labels, dtype=torch.float32)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 5. LSTM Model
class TextLSTM(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size+1, 10)
        self.lstm = nn.LSTM(10, 16, batch_first=True)
        self.fc = nn.Linear(16,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.lstm(x)
        out = self.fc(out[:,-1,:])
        return self.sigmoid(out)

model = TextLSTM(len(vocab))

# 6. Training
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(20):
    output = model(X_train).squeeze()
    loss = criterion(output, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.item()}")

# 7. Evaluation
model.eval()
pred = model(X_test).detach().numpy()
pred = [1 if p > 0.5 else 0 for p in pred]

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))