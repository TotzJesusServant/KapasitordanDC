import numpy as np
import matplotlib.pyplot as plt

# Parameter sinyal
t = np.linspace(0, 1, 1000)  # 1000 titik waktu dari 0 hingga 1 detik
f = 10  # Frekuensi sinyal AC
A = 5  # Amplitudo sinyal AC
DC_offset = 2  # Komponen DC

# Sinyal AC
signal_AC = A * np.sin(2 * np.pi * f * t)

# Sinyal input (gabungan AC dan DC)
signal_input = signal_AC + DC_offset

# Simulasi penyaringan kapasitor
C = 0.1  # Nilai kapasitor

# Penyaringan sinyal
filtered_signal = [0]  # Memulai dengan nilai awal 0 untuk tegangan keluaran
for Vin in signal_input:
    Vout = (Vin - filtered_signal[-1]) * (1 - np.exp(-1 / (C))) + filtered_signal[-1]
    filtered_signal.append(Vout)

# Plot hasil
plt.figure(figsize=(10, 6))

plt.plot(t, signal_input, label='Input (AC + DC)')
plt.plot(t, filtered_signal[:-1], label='Output (Filtered)')
plt.title('Input and Filtered Output Signals')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()

plt.tight_layout()
plt.show()
