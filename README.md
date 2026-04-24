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
El desarrollo del análisis se estructuró en varias etapas principales, utilizando herramientas de programación en Python para el procesamiento y estudio de señales electromiográficas (EMG).

En primer lugar, se definieron funciones para el filtrado de señales (pasa-banda y pasa-bajos), la normalización y el cálculo de parámetros espectrales como la frecuencia media y la frecuencia mediana a partir de la transformada de Fourier (FFT). Estas funciones permitieron establecer una base sólida para el procesamiento posterior de las señales.

En una segunda etapa, correspondiente a la Parte A, se cargó una señal EMG desde un archivo de texto, a partir del cual se obtuvo el vector de tiempo y la señal. Luego, se calculó la frecuencia de muestreo y se aplicó un filtro pasa-bajos para suavizar la señal. Se realizaron gráficas tanto de la señal original como de la filtrada, así como su análisis en frecuencia mediante la FFT global. Posteriormente, la señal fue segmentada en ventanas móviles, permitiendo calcular la frecuencia media y mediana en cada segmento. Estos resultados se organizaron en una tabla y se analizaron mediante gráficas junto con líneas de tendencia para observar su comportamiento a lo largo del tiempo.

Finalmente, en las Partes B y C, se procesaron señales adicionales provenientes de archivos distintos. En este caso, las señales fueron centradas eliminando su componente DC y filtradas con un filtro pasa-banda. Se repitió el análisis temporal y frecuencial, incluyendo la FFT global. Luego, las señales se dividieron en segmentos más amplios para evaluar la evolución de la frecuencia media y mediana, lo cual permitió analizar fenómenos como la fatiga muscular mediante tendencias en el tiempo. Adicionalmente, se realizó un análisis específico de la FFT en tres segmentos clave (inicio, medio y final), identificando la frecuencia pico en cada uno y evaluando su desplazamiento mediante gráficos de barras y líneas de tendencia.

En conjunto, este procedimiento permitió caracterizar el comportamiento espectral de las señales EMG y analizar su evolución temporal, facilitando la interpretación de cambios asociados a condiciones fisiológicas como la fatiga.

---

## Diagrama de Flujo
<p align="center">
  <img src="Diagrama.jpeg" width="700">
</p>

<p align="center">
  <em> Diagrama de flujo </em>
</p>

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
  <img src="T1.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

En la tabla y la gráfica de evolución se observa que la frecuencia media muestra una tendencia general creciente a lo largo del tiempo, pasando de ~77 Hz al inicio hasta ~163 Hz al final, lo cual podría asociarse a un incremento en el reclutamiento de unidades motoras durante contracciones más intensas. La frecuencia mediana, por su parte, permanece cercana a 0 Hz en la mayoría de segmentos iniciales y solo muestra valores significativos hacia el final del registro (segmentos 10–12), lo que sugiere que el contenido espectral relevante se concentra en frecuencias muy bajas en gran parte de la señal, posiblemente por la naturaleza de la señal emulada o por artefactos de segmentación.

<p align="center">
  <img src="A3.png" width="700">
</p>

<p align="center">
  <em> FFT GLOBAL </em>
</p>

<p align="center">
  <img src="A4.png" width="700">
</p>

<p align="center">
  <em> FFT POR VENTANAS </em>
</p>

---
### Parte B - Captura de la señal de paciente

Las dos señales reales capturadas sobre el bíceps de un voluntario sano mostraron, tras el filtrado pasa-banda entre 20 y 450 Hz y la eliminación del componente DC, un comportamiento espectral coherente con la fatiga muscular progresiva. En ambas señales se observó una tendencia decreciente en la frecuencia media y mediana a medida que avanzaban las contracciones, evidenciando el desplazamiento espectral hacia frecuencias más bajas asociado al agotamiento muscular. La comparación entre las dos señales permitió verificar la reproducibilidad del fenómeno dentro del mismo sujeto bajo condiciones similares.
Una parte fragmento de código clave corresponde al centrado y filtrado pasa-banda:
```python
# Eliminar componente DC (centrar la señal)
señal = señal - np.mean(señal)

# Filtro pasa-banda Butterworth orden 4: 20–450 Hz
from scipy.signal import butter, filtfilt

def filtro_pasabanda(señal, fs, f_low=20, f_high=450, orden=4):
    nyq = fs / 2
    low = f_low / nyq
    high = f_high / nyq
    b, a = butter(orden, [low, high], btype='band')
    return filtfilt(b, a, señal)

señal_filtrada = filtro_pasabanda(señal, fs)
```
Este bloque garantiza que la señal real quede libre de artefactos de movimiento (por debajo de 20 Hz) y de ruido eléctrico de alta frecuencia (por encima de 450 Hz), conservando únicamente el contenido muscular relevante para el análisis de fatiga.


<p align="center">
  <img src="B1.png" width="700">
</p>

<p align="center">
  <em> Señal 1 EMG (filtrada) </em>
</p>

La señal EMG filtrada muestra ráfagas de actividad muscular asociadas a la contracción del bíceps. Al inicio se observa mayor densidad y amplitud de los potenciales, mientras que hacia el final se evidencian cambios en la envolvente relacionados con la fatiga muscular. Esto refleja la progresiva alteración en el reclutamiento y comportamiento de las unidades motoras.

<p align="center">
  <img src="B2.png" width="700">
</p>

La frecuencia media y mediana presentan una tendencia creciente a lo largo del tiempo. Este comportamiento sugiere un reclutamiento adicional de unidades motoras tipo II en fases avanzadas de fatiga, elevando el contenido frecuencial de la señal, especialmente en el tramo final del registro.

<p align="center">
  <em> Evolución de frecuencias Señal 1  EMG (filtrada) </em>
</p>

<p align="center">
  <img src="T2.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

Los valores tabulados muestran la evolución cuantitativa de las frecuencias media y mediana por segmento. Se evidencia una tendencia general al aumento, con un incremento más pronunciado en los últimos intervalos, indicando cambios en la dinámica muscular durante el esfuerzo sostenido.

<p align="center">
  <img src="B3.png" width="700">
</p>

<p align="center">
  <em> Señal 1 FFT Global </em>
</p>

El espectro global concentra su energía principalmente entre 20 y 200 Hz, con un pico alrededor de 65 Hz. La distribución espectral es característica de señales EMG, confirmando la adecuada eliminación de ruido y la preservación de la información muscular relevante.

<p align="center">
  <img src="B4.png" width="700">
</p>

<p align="center">
  <em> Señal 1 FFT Ventanas</em>
</p>

La comparación entre inicio, mitad y final evidencia un desplazamiento progresivo del contenido espectral hacia frecuencias más bajas. Este fenómeno indica una disminución en la velocidad de conducción de los potenciales de acción debido a la fatiga muscular.

<p align="center">
  <img src="B5.png" width="700">
</p>

<p align="center">
  <em> Señal 1  desplazamiento del pico </em>
</p>

El pico espectral disminuye de forma sostenida desde el inicio hasta el final del ejercicio. Esta caída representa un indicador directo de fatiga, asociado a cambios fisiológicos en las fibras musculares y en la conducción eléctrica.

<p align="center">
  <img src="T3.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

Los datos muestran una reducción significativa de la frecuencia pico entre segmentos, confirmando cuantitativamente el desplazamiento espectral y validando su uso como métrica de fatiga muscular.

<p align="center">
  <img src="B2.1.png" width="700">
</p>

<p align="center">
  <em> Señal 2 EMG (filtrada) </em>
</p>

La segunda señal presenta un comportamiento similar a la primera, con actividad sostenida durante la contracción. Se observa una disminución progresiva en la intensidad de los bursts, consistente con el desarrollo de fatiga.

<p align="center">
  <img src="B2.2.png" width="700">
</p>

<p align="center">
  <em> Evolución de frecuencias Señal 2  EMG (filtrada) </em>
</p>

A diferencia de la Señal 1, tanto la frecuencia media como la mediana disminuyen progresivamente. Este patrón coincide con el comportamiento teórico esperado en procesos de fatiga muscular.

<p align="center">
  <img src="T4.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

Los valores reflejan una reducción sostenida de las frecuencias características. La frecuencia mediana presenta mayor sensibilidad al descenso, consolidándose como un indicador robusto de fatiga.

<p align="center">
  <img src="B2.3.png" width="700">
</p>

<p align="center">
  <em> Señal 2 FFT Global </em>
</p>
El espectro global mantiene una distribución similar a la Señal 1, con energía concentrada en el rango típico del EMG. La ligera diferencia en el pico se atribuye a variaciones experimentales en la adquisición.

<p align="center">
  <img src="B2.5.png" width="700">
</p>

<p align="center">
  <em> Señal 2  desplazamiento del pico </em>
</p>

El pico espectral también presenta una tendencia descendente clara. Este comportamiento confirma la reproducibilidad del fenómeno de fatiga en mediciones realizadas bajo las mismas condiciones experimentales. 

---
### Parte C -  Análisis espectral mediante FFT
El análisis de la FFT en tres segmentos clave (inicio, medio y final) de cada señal real evidenció un desplazamiento progresivo del pico espectral hacia frecuencias más bajas conforme avanzaba el ejercicio. Este resultado es consistente con la teoría de fatiga muscular: la reducción de la velocidad de conducción de los potenciales de acción desplaza la energía espectral de la señal EMG hacia componentes frecuenciales menores. Los gráficos de barras y líneas de tendencia del pico espectral por segmento confirmaron visualmente esta tendencia en ambas señales, validando el uso de la FFT como herramienta diagnóstica objetiva para la detección de fatiga en electromiografía de superficie.
Una parte fragmento de código clave corresponde al FFT por segmento y detección del pico espectral:

```python
from scipy.fft import fft, fftfreq
import numpy as np

segmentos = np.array_split(señal_filtrada, 3)  # inicio, medio, final
etiquetas = ['Inicio', 'Medio', 'Final']
picos = []

for seg, etiqueta in zip(segmentos, etiquetas):
    N = len(seg)
    X = np.abs(fft(seg))[:N//2]
    freqs = fftfreq(N, 1/fs)[:N//2]

    # Frecuencia pico
    f_pico = freqs[np.argmax(X)]
    picos.append(f_pico)

    plt.plot(freqs, X, label=etiqueta)

plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title("FFT por segmento")
plt.legend()
plt.grid()
plt.show()

# Gráfico de barras del desplazamiento del pico
plt.bar(etiquetas, picos, color=['green', 'orange', 'red'])
plt.ylabel("Frecuencia pico (Hz)")
plt.title("Desplazamiento del pico espectral")
plt.grid(axis='y')
plt.show()
```
Este bloque divide la señal en tres partes representativas del ejercicio, calcula la FFT de cada una e identifica la frecuencia de mayor magnitud en cada segmento, permitiendo cuantificar y visualizar el desplazamiento espectral asociado a la fatiga.


<p align="center">
  <img src="B2.4.png" width="700">
</p>

<p align="center">
  <em> Señal 2 FFT Ventanas</em>
</p>
La comparación entre los espectros de inicio, mitad y final muestra una redistribución de la energía hacia frecuencias más bajas. La reducción de componentes de alta frecuencia evidencia el deterioro funcional del músculo durante la contracción sostenida.

<p align="center">
  <img src="B4.png" width="700">
</p>

<p align="center">
  <em> Señal 1 FFT Ventanas</em>
</p>

Los espectros muestran un desplazamiento progresivo del contenido frecuencial hacia la zona baja del espectro. Este comportamiento refleja el efecto de la fatiga sobre la dinámica de las unidades motoras.

<p align="center">
  <img src="B2.5.png" width="700">
</p>


<p align="center">
  <img src="B5.png" width="700">
</p>

<p align="center">
  <em> Señal 1  desplazamiento del pico </em>
</p>

Se observa un descenso progresivo de la frecuencia pico a lo largo del ejercicio. Este desplazamiento hacia frecuencias más bajas es un indicador claro de fatiga muscular, asociado a la disminución de la velocidad de conducción de los potenciales de acción en las fibras musculares.

<p align="center">
  <em> Señal 2  desplazamiento del pico </em>
</p>

El pico espectral presenta una tendencia descendente consistente, confirmando el proceso de fatiga. La variación es similar a la observada en la Señal 1, lo que respalda la reproducibilidad del fenómeno.

<p align="center">
  <img src="T3.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

Los valores de frecuencia pico por segmento evidencian una disminución significativa entre el inicio y el final. Esta tendencia cuantifica el desplazamiento espectral observado gráficamente.

<p align="center">
  <img src="T5.png" width="700">
</p>

<p align="center">
  <em> Tabla de resultados </em>
</p>

Los datos confirman una reducción sostenida de la frecuencia pico. La consistencia con la Señal 1 valida el uso de este parámetro como indicador confiable de fatiga muscular.

---
### Conclusiones

A partir del desarrollo de esta práctica de laboratorio se pueden establecer las siguientes conclusiones:
Se logró identificar el desplazamiento espectral hacia frecuencias más bajas en las señales EMG reales como indicador de fatiga muscular, confirmando la utilidad de la frecuencia media y la frecuencia mediana como parámetros diagnósticos en el análisis electromiográfico. Este comportamiento fue coherente con los mecanismos fisiológicos asociados a la acumulación de metabolitos y la reducción de la velocidad de conducción de las fibras musculares durante contracciones sostenidas.
La señal emulada, aunque permitió familiarizarse con el procesamiento y la segmentación de señales EMG, no reprodujo el patrón espectral esperado de fatiga, lo cual resalta la importancia de trabajar con señales reales para validar fenómenos fisiológicos de esta naturaleza.
La aplicación del filtrado Butterworth —pasa-bajos para la señal emulada y pasa-banda entre 20 y 450 Hz para las señales reales— resultó fundamental para eliminar ruido y artefactos sin distorsionar el contenido muscular relevante, garantizando la confiabilidad del análisis posterior.
Respecto a la factibilidad de emplear técnicas espectrales en escenarios no controlados, como el entrenamiento de atletas, se concluye que si bien estas herramientas son prometedoras, su implementación práctica requiere sistemas de adquisición portátiles con alta inmunidad al ruido, algoritmos de procesamiento robustos y protocolos estandarizados de colocación de electrodos. En ausencia de estas condiciones, la variabilidad de la señal puede comprometer la precisión del diagnóstico de fatiga en campo abierto.

---
### Preguntas para la Discusión
- ¿Cambian los valores de frecuencia media y mediana a medida que el músculo se acerca a la fatiga? ¿A qué podría atribuirse este cambio?
  
Sí, en condiciones de fatiga muscular real, tanto la frecuencia media como la frecuencia mediana experimentan una disminución progresiva a lo largo de las contracciones sostenidas. Este cambio se atribuye principalmente a la reducción de la velocidad de conducción de los potenciales de acción en las fibras musculares, causada por la acumulación de iones de hidrógeno (H⁺) producto del metabolismo anaeróbico, el agotamiento de los depósitos de ATP y fosfocreatina, y la acumulación de lactato intramuscular. Estos factores alteran la excitabilidad de la membrana celular y prolongan la duración de cada potencial de acción, lo cual desplaza la energía espectral de la señal EMG hacia componentes de menor frecuencia. Adicionalmente, durante la fatiga se produce un reclutamiento progresivo de unidades motoras de tipo II (fibras de contracción rápida), que generan potenciales de mayor amplitud pero también más lentos en su fase final, contribuyendo al desplazamiento espectral observado.

- ¿Cómo justifica el uso de herramientas como la transformada de Fourier en escenarios como terapias de rehabilitación?
  
La Transformada de Fourier permite descomponer una señal EMG en sus componentes frecuenciales, revelando información que no es perceptible en el dominio del tiempo. En el contexto de terapias de rehabilitación, esta herramienta resulta de gran valor porque permite cuantificar objetivamente el nivel de fatiga muscular de un paciente durante una sesión de ejercicio terapéutico, sin necesidad de procedimientos invasivos. De esta manera, el terapeuta puede ajustar en tiempo real la intensidad y duración del ejercicio, previniendo la sobrecarga muscular y reduciendo el riesgo de lesiones. Además, el seguimiento longitudinal de parámetros espectrales como la frecuencia mediana permite evaluar la evolución de la capacidad muscular del paciente a lo largo del proceso de rehabilitación, aportando evidencia objetiva del progreso clínico. Esto convierte al análisis espectral en una herramienta diagnóstica y de monitoreo de alta utilidad en entornos clínicos supervisados.

---
### Bibliografía
[1] Y. Tan et al., "Change of bio-electric interferential currents of acute fatigue and recovery in male sprinters," Sports Medicine and Health Science, vol. 2, no. 1, pp. 1–6, 2020. https://doi.org/10.1016/j.smhs.2020.02.004

[2] K. Sahlin, "Metabolic factors in fatigue," Sports Medicine, vol. 13, no. 2, pp. 99–107, 1992. https://doi.org/10.2165/00007256-199213020-00005

[3] D. Constantin-Teodosiu y D. Constantin, "Molecular mechanisms of muscle fatigue," International Journal of Molecular Sciences, vol. 22, no. 21, art. 11587, 2021. https://doi.org/10.3390/ijms222111587

[4] A. Urdampilleta et al., "La fatiga muscular en los deportistas," Archivos de Medicina del Deporte, vol. 32, no. 1, pp. 36–43, 2015.

[5] N. Dimitrova y G. Dimitrov, "Interpretation of EMG changes with fatigue," Journal of Electromyography and Kinesiology, vol. 13, no. 1, pp. 13–36, 2003. https://doi.org/10.1016/S1050-6411(02)00083-4

[6] A. V. Oppenheim y R. W. Schafer, Discrete-Time Signal Processing, 3ra ed. Prentice Hall, 2010.

[7] P. Virtanen et al., "SciPy 1.0: Fundamental algorithms for scientific computing in Python," Nature Methods, vol. 17, pp. 261–272, 2020. https://doi.org/10.1038/s41592-019-0686-2


