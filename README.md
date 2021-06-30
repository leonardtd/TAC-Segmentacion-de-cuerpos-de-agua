# Segmentación de cuerpos de agua con imágenes satelitales usando U-NET
#### Leonardo Torres Damián, Renzo Bedriñana Orozco y Mauricio Ochoa Samaniego

## Introducción
Actualmente, existe una gran cantidad de métodos que permiten la detección de cuerpos de agua, pero muchos
de ellos no son precisos. Por ello, se optó por algo diferente a los métodos convencionales. El Deep
Learning nos permite entrenar y adaptar un modelo según el problema que se tenga usando una gran cantidad de
muestras. Uno de los modelos más usados son las redes convolucionales propuestas por Yann LeCun. Hoy en
día, existen diversas arquitecturas de redes convolucionales, como SegNet y DenseNet las cuales buscan
solventar el problema propuesto.

Es por este motivo que en este estudio proponemos introducir el uso de la arquitectura U-NET para la
segmentación de cuerpos de agua con el fin de medir su desempeño dentro de un campo distinto a la de
medicina, donde ha sido tradicionalmente utilizado y así poder compararlo con otros modelos actualmente
empleados.

Nuestro modelo logra obtener un _validation accuracy_ de **89.25%** y un _f1 score_ de **82%** .