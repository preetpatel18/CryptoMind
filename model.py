import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data, window_size=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))
    
    x, y = [], []
    for i in range(window_size, len(scaled_data)):
        x.append(scaled_data[i-window_size:i, 0])
        y.append(scaled_data[i, 0])
    
    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))
    return x, y, scaler

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(input_shape[1], 1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_lstm_model(data, window_size=60, epochs=1, batch_size=1):
    x, y, scaler = preprocess_data(data, window_size)
    model = build_lstm_model(x.shape)
    model.fit(x, y, epochs=epochs, batch_size=batch_size, verbose=1)
    return model, scaler

def lstm_strategy(data, model, scaler, window_size=60):
    scaled_data = scaler.transform(data['Close'].values.reshape(-1, 1))
    x = []
    for i in range(window_size, len(scaled_data)):
        x.append(scaled_data[i-window_size:i, 0])
    
    x = np.array(x)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))
    predictions = model.predict(x)
    predictions = scaler.inverse_transform(predictions)
    
    signals = pd.DataFrame(index=data.index[window_size:])
    signals['Buy'] = (data['Close'][window_size:].values < predictions.flatten()).astype(bool)
    signals['Sell'] = (data['Close'][window_size:].values > predictions.flatten()).astype(bool)
    
    return signals
