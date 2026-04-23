# Señales electromiográficas EMG 

## Asignatura

Procesamiento Digital de Señales

## Programa

Ingeniería Biomédica – Universidad Militar Nueva Granada

## Práctica de laboratorio

**Señales electromiográficas EMG**

## Integrantes

Danna Jimena Medina Ríos – Código 5600923
María José Polo Tovar – Código 5600894

---
## Descripción
Este repositorio contiene el desarrollo de la práctica de laboratorio "Señales electromiográficas EMG". El objetivo central fue identificar cambios en las características espectrales de una señal EMG cuando se alcanza la fatiga muscular. Se trabajó con dos tipos de señales: una señal emulada mediante un generador de señales biológicas, configurado en modo EMG a 200 Hz con una captura de 1 segundo, y una señal real adquirida de un voluntario sano mediante electrodos de superficie colocados sobre el bíceps, registrando una contracción sostenida hasta alcanzar la fatiga. La primera señal fue procesada en Python aplicando un filtro pasa-bajos con frecuencia de corte de 410 Hz, mientras que a la segunda se le aplicó un filtro pasa-banda entre 20 y 450 Hz; ambas señales fueron segmentadas en ventanas individuales para extraer parámetros espectrales clave: frecuencia media y frecuencia mediana. Adicionalmente, se aplicó la Transformada Rápida de Fourier (FFT) a cada ventana para obtener el espectro de amplitud y analizar la evolución del contenido frecuencial a lo largo del ejercicio. Los resultados de ambas señales fueron comparados y representados gráficamente para evidenciar el desplazamiento espectral asociado a la aparición de la fatiga muscular.

----
##  Metodología 



---

## Diagrama de Flujo


---
### Parte A — Captura de la señal emulada
Se cargó la señal EMG desde el archivo EMG3.txt y se determinó una frecuencia de muestreo a partir de los intervalos de tiempo. Luego se aplicó un filtro pasa-bajos Butterworth de orden 4 con frecuencia de corte de 410 Hz, con el fin de eliminar ruido de alta frecuencia sin afectar el contenido muscular relevante. En la gráfica de la señal en el tiempo se puede observar que la señal filtrada (naranja) sigue fielmente la envolvente de la señal original (azul), confirmando que el filtro actuó correctamente sin distorsionar la forma de onda.

<p align="center">
  <img src="A1.png" width="700">
</p>

<p align="center">
  <em> Señal EMG en el tiempo (filtrada) </em>
</p>

La señal filtrada fue dividida en segmentos usando una ventana de 0.2 s con paso de 0.08 s generando un solapamiento efectivo, obteniendo así un análisis temporal progresivo de la actividad muscular a lo largo del registro.
Para cada segmento se aplicó frecuencia media pondera las frecuencias por su magnitud espectral, mientras que la frecuencia mediana divide el espectro en dos mitades de igual energía acumulada. Ambos parámetros son indicadores clásicos de fatiga muscular: en condiciones de fatiga, se espera un desplazamiento hacia frecuencias más bajas.

```python

    X = np.abs(fft(xi))
    freqs = fftfreq(N, 1/fs)

    freqs = freqs[:N//2]
    X = X[:N//2]

    if np.sum(X) == 0:
        continue

    # Frecuencia media
    fm = np.sum(freqs * X) / np.sum(X)

    # Frecuencia mediana
    acumulada = np.cumsum(X)
    mitad = acumulada[-1] / 2
    fmed = freqs[np.where(acumulada >= mitad)[0][0]]

    tiempos_inicio.append(t_inicio)
    f_media.append(fm)
    f_mediana.append(fmed)
 ```
<p align="center">
  <img src="A2.png" width="700">
</p>

<p align="center">
  <em> Evolución de frecuencias EMG (filtrada) </em>
</p>

```python
# TABLA

tabla = pd.DataFrame({
    "Tiempo inicio (s)": tiempos_inicio,
    "Frecuencia Media (Hz)": f_media,
    "Frecuencia Mediana (Hz)": f_mediana
})

print("\nTABLA DE RESULTADOS:\n")
print(tabla)


#  EVOLUCIÓN DE FRECUENCIAS

plt.figure(figsize=(10,6))

plt.plot(tabla["Tiempo inicio (s)"], tabla["Frecuencia Media (Hz)"], 'o-', label="Frecuencia Media")
plt.plot(tabla["Tiempo inicio (s)"], tabla["Frecuencia Mediana (Hz)"], 's-', label="Frecuencia Mediana")

plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia (Hz)")
plt.title("Evolución de frecuencias EMG (filtrada)")
plt.legend()
plt.grid()

plt.show()
 ```

<p align="center">
  <img src="T.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

En la tabla y la gráfica de evolución se observa que la frecuencia media muestra una tendencia general creciente a lo largo del tiempo, pasando de ~77 Hz al inicio hasta ~163 Hz al final, lo cual podría asociarse a un incremento en el reclutamiento de unidades motoras durante contracciones más intensas. La frecuencia mediana, por su parte, permanece cercana a 0 Hz en la mayoría de segmentos iniciales y solo muestra valores significativos hacia el final del registro (segmentos 10–12), lo que sugiere que el contenido espectral relevante se concentra en frecuencias muy bajas en gran parte de la señal, posiblemente por la naturaleza de la señal emulada o por artefactos de segmentación.

---

### Parte B - Captura de la señal de paciente

<p align="center">
  <img src="B1.png" width="700">
</p>

<p align="center">
  <em> Señal 1 EMG (filtrada) </em>
</p>

<p align="center">
  <img src="B2.png" width="700">
</p>

<p align="center">
  <em> Evolución de frecuencias Señal 1  EMG (filtrada) </em>
</p>

<p align="center">
  <img src="B3.png" width="700">
</p>

<p align="center">
  <em> Señal 1 FFT Global </em>
</p>

<p align="center">
  <img src="B4.png" width="700">
</p>

<p align="center">
  <em> Señal 1 FFT Ventanas</em>
</p>

<p align="center">
  <img src="B5.png" width="700">
</p>

<p align="center">
  <em> Señal 1  desplazamiento del pico </em>
</p>

<p align="center">
  <img src="B1.png" width="700">
</p>

<p align="center">
  <em> Evolución de frecuencias EMG (filtrada) </em>
</p>

<p align="center">
  <img src="B1.png" width="700">
</p>

<p align="center">
  <em> Evolución de frecuencias EMG (filtrada) </em>
</p>

<p align="center">
  <img src="B1.png" width="700">
</p>

<p align="center">
  <em> Evolución de frecuencias EMG (filtrada) </em>
</p>

---
### Parte C - Análisis espectral mediante FFT

