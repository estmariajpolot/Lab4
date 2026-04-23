import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft, fftfreq
from scipy.signal import butter, filtfilt

# FUNCIONES

def filtro_pasabanda(x, fs, f1=20, f2=450, orden=4):
    nyq = 0.5 * fs
    b, a = butter(orden, [f1/nyq, f2/nyq], btype='band')
    return filtfilt(b, a, x)

def filtro_pasabajos(x, fs, fc=410, orden=4):
    nyq = 0.5 * fs
    b, a = butter(orden, fc/nyq, btype='low')
    return filtfilt(b, a, x)

def normalizar_11(X):
    X = X / np.max(np.abs(X))
    return 2*(X - 0.5)

def calcular_frecuencias(xi, fs):
    N = len(xi)
    X = np.abs(fft(xi))
    freqs = fftfreq(N, 1/fs)

    freqs = freqs[:N//2]
    X = X[:N//2]

    mask = (freqs >= 20) & (freqs <= 450)
    freqs = freqs[mask]
    X = X[mask]

    if np.sum(X) == 0:
        return None, None

    f_media = np.sum(freqs * X) / np.sum(X)

    acumulada = np.cumsum(X)
    mitad = acumulada[-1] / 2
    f_mediana = freqs[np.where(acumulada >= mitad)[0][0]]

    return f_media, f_mediana


# PARTE A

data = np.loadtxt("EMG3.txt", skiprows=1)
tA = data[:, 0]
xA = data[:, 1]

fsA = int(1 / (tA[1] - tA[0]))
xA_filtrada = filtro_pasabajos(xA, fsA)

# Señal
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,5), sharex=True)
ax1.plot(tA, xA, color='gray')
ax1.set_title("PARTE A - Señal Original")
ax1.grid()

ax2.plot(tA, xA_filtrada, color='blue')
ax2.set_title("PARTE A - Señal Filtrada")
ax2.grid()

plt.tight_layout()
plt.show()

# FFT GLOBAL PARTE A
N = len(xA_filtrada)
X = np.abs(fft(xA_filtrada))
X = normalizar_11(X)
freqs = fftfreq(N, 1/fsA)

freqs = freqs[:N//2]
X = X[:N//2]

mask = freqs > 0
freqs = freqs[mask]
X = X[mask]

plt.figure(figsize=(10,5))
plt.semilogx(freqs, X)
plt.title("FFT Global - Parte A ")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud [-1,1]")
plt.grid(which='both')
plt.show()

# Frecuencias
ventana = int(0.2 * fsA)
paso = int(0.08 * fsA)

f_media = []
f_mediana = []
tiempos = []

for i in range(0, len(xA_filtrada)-ventana, paso):
    xi = xA_filtrada[i:i+ventana]
    fm, fmed = calcular_frecuencias(xi, fsA)

    if fm is not None:
        tiempos.append(tA[i])
        f_media.append(fm)
        f_mediana.append(fmed)

tabla_A = pd.DataFrame({
    "Tiempo inicio (s)": tiempos,
    "Frecuencia Media (Hz)": f_media,
    "Frecuencia Mediana (Hz)": f_mediana
})

print("\nTABLA PARTE A\n")
print(tabla_A)

# Regresión
coef_media_A = np.polyfit(tiempos, f_media, 1)
coef_mediana_A = np.polyfit(tiempos, f_mediana, 1)

plt.figure(figsize=(10,5))
plt.plot(tiempos, f_media, 'o-', color='red', label="Media")
plt.plot(tiempos, f_mediana, 's-', color='blue', label="Mediana")

plt.plot(tiempos, np.poly1d(coef_media_A)(tiempos), '--', color='salmon')
plt.plot(tiempos, np.poly1d(coef_mediana_A)(tiempos), '--', color='skyblue')

plt.title("PARTE A - Frecuencias")
plt.xlabel("Tiempo (s)")
plt.ylabel("Hz")
plt.legend()
plt.grid()
plt.show()

# FFT Parte A ventanas
plt.figure(figsize=(10,5))
segmentos_A = [
    (0, int(len(xA_filtrada)*0.2)),
    (int(len(xA_filtrada)*0.4), int(len(xA_filtrada)*0.6)),
    (int(len(xA_filtrada)*0.8), len(xA_filtrada))
]

for i, (ini, fin) in enumerate(segmentos_A):
    xi = xA_filtrada[ini:fin]
    N = len(xi)
    xi = xi * np.hamming(N)

    X = np.abs(fft(xi))
    X = normalizar_11(X)

    freqs = fftfreq(N, 1/fsA)
    freqs = freqs[:N//2]
    X = X[:N//2]

    mask = (freqs >= 20) & (freqs <= 450) & (freqs > 0)
    freqs = freqs[mask]
    X = X[mask]

    plt.semilogx(freqs, X, label=["Inicio","Mitad","Final"][i])

plt.title("FFT Parte A ")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud [-1,1]")
plt.legend()
plt.grid(which='both')
plt.show()


# PARTE B Y C

def procesar_senal(nombre_archivo, color):

    df = pd.read_csv(nombre_archivo, sep="\s+", comment="#", header=None)
    df.columns = ["nSeq", "I1", "I2", "O1", "O2", "A1"]

    x = df["A1"].values
    fs = 1000
    t = np.arange(len(x)) / fs

    x = x - np.mean(x)
    x_filtrada = filtro_pasabanda(x, fs)

    # Señal
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,5), sharex=True)
    ax1.plot(t, x, color='gray')
    ax1.set_title(f"{nombre_archivo} - Original")
    ax1.grid()

    ax2.plot(t, x_filtrada, color=color)
    ax2.set_title(f"{nombre_archivo} - Filtrada")
    ax2.grid()

    plt.tight_layout()
    plt.show()

    # FFT GLOBAL PARTE B
    N = len(x_filtrada)
    X = np.abs(fft(x_filtrada))
    X = normalizar_11(X)
    freqs = fftfreq(N, 1/fs)

    freqs = freqs[:N//2]
    X = X[:N//2]

    mask = freqs > 0
    freqs = freqs[mask]
    X = X[mask]

    plt.figure(figsize=(10,5))
    plt.semilogx(freqs, X, color=color)
    plt.title(f"FFT Global - {nombre_archivo}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud [-1,1]")
    plt.grid(which='both')
    plt.show()

    # Ventanas
    ventana = int(5.4* fs)
    paso = int(ventana * 0.7)

    segmentos = []
    i = 0
    while i + ventana <= len(x_filtrada):
        segmentos.append((i, i + ventana))
        i += paso

    f_media = []
    f_mediana = []
    tiempos = []

    for seg in segmentos:
        xi = x_filtrada[seg[0]:seg[1]]
        fm, fmed = calcular_frecuencias(xi, fs)

        if fm is not None:
            tiempos.append(t[seg[0]])
            f_media.append(fm)
            f_mediana.append(fmed)

    tabla = pd.DataFrame({
        "Tiempo inicio (s)": tiempos,
        "Frecuencia Media (Hz)": f_media,
        "Frecuencia Mediana (Hz)": f_mediana
    })

    print(f"\nTABLA - {nombre_archivo}\n")
    print(tabla)

    # Regresión

    coef_media = np.polyfit(tiempos, f_media, 1)
    coef_mediana = np.polyfit(tiempos, f_mediana, 1)
    
    poly_media = np.poly1d(coef_media)
    poly_mediana = np.poly1d(coef_mediana)
    
    plt.figure(figsize=(10,5))
    
    # Datos originales
    plt.plot(tiempos, f_media, 'o-', label="Media")
    plt.plot(tiempos, f_mediana, 's--', alpha=0.6, label="Mediana")
    
    # Tendencias (regresiones)
    plt.plot(tiempos, poly_media(tiempos), '--',
             label=f"Tendencia Media ({coef_media[0]:.2f} Hz/s)")
    
    plt.plot(tiempos, poly_mediana(tiempos), ':',
             label=f"Tendencia Mediana ({coef_mediana[0]:.2f} Hz/s)")
    
    plt.title(f"Fatiga - {nombre_archivo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Hz")
    plt.legend()
    plt.grid()
    plt.show()

    # FFT + pico
    plt.figure(figsize=(10,5))

    indices = [0, len(segmentos)//2, len(segmentos)-1]
    picos = []
    tiempos_fft = []

    for i, idx in enumerate(indices):
        seg = segmentos[idx]
        xi = x_filtrada[seg[0]:seg[1]]

        N = len(xi)
        xi = xi * np.hamming(N)

        X = np.abs(fft(xi))
        X = normalizar_11(X)

        freqs = fftfreq(N, 1/fs)
        freqs = freqs[:N//2]
        X = X[:N//2]

        mask = (freqs >= 20) & (freqs <= 450) & (freqs > 0)
        freqs = freqs[mask]
        X = X[mask]

        f_pico = freqs[np.argmax(X)]
        picos.append(f_pico)
        tiempos_fft.append(t[seg[0]])

        print(f"{nombre_archivo} | t={t[seg[0]]:.2f}s → Pico: {f_pico:.2f} Hz")

        plt.semilogx(freqs, X, label=["Inicio","Mitad","Final"][i])

    plt.title(f"FFT- {nombre_archivo}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud [-1,1]")
    plt.legend()
    plt.grid(which='both')
    plt.show()

    # Desplazamiento del pico
    coef_pico = np.polyfit(tiempos_fft, picos, 1)

    plt.figure(figsize=(8,4))
    plt.plot(tiempos_fft, picos, 'o-', color=color)
    plt.plot(tiempos_fft, np.poly1d(coef_pico)(tiempos_fft),
             '--', color=color,
             label=f"Tendencia ({coef_pico[0]:.2f} Hz/s)")

    plt.title(f"Desplazamiento del pico - {nombre_archivo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Frecuencia pico (Hz)")
    plt.legend()
    plt.grid()
    plt.show()


# EMG TOMADAS
procesar_senal("SEÑALEMG1.txt", "blue")
procesar_senal("SEÑALEMG2.txt", "red")