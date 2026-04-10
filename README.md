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
Este repositorio contiene el desarrollo de la práctica de laboratorio "Señales electromiográficas EMG". El objetivo central fue identificar cambios en las características espectrales de una señal EMG cuando se alcanza la fatiga muscular. Se trabajó con dos tipos de señales: una señal emulada mediante un generador de señales biológicas (simulando aproximadamente 5 contracciones musculares voluntarias) y una señal real capturada sobre un voluntario sano mediante electrodos de superficie colocados en un grupo muscular (antebrazo o bíceps), registrando contracciones repetidas hasta alcanzar la fatiga. Cada señal fue procesada en Python aplicando un filtro pasa banda (20–450 Hz) y segmentada en las contracciones individuales para extraer parámetros clave como: frecuencia media y frecuencia mediana por contracción. Adicionalmente, se aplicó la Transformada Rápida de Fourier (FFT) a cada contracción para obtener el espectro de amplitud y analizar la evolución del contenido frecuencial a lo largo del ejercicio. Los resultados se compararon entre la señal emulada y la señal real, y se representaron gráficamente para evidenciar el desplazamiento espectral asociado a la aparición de la fatiga muscular.

----
##  Metodología 



---

## Diagrama de Flujo


---
### Parte A — Captura de la señal emulada

---

### Parte B - Captura de la señal de paciente

---
### Parte C - Análisis espectral mediante FFT

