# Actividad 4: Evaluacion comparativa de modelos preentrenados

Este repositorio contiene un prototipo reproducible para comparar tres modelos de vision preentrenados en la clasificacion de componentes de tornillo de bolas con y sin pitting.

## Objetivo

Evaluar ResNet-50, ConvNeXt-Tiny y ViT-Base bajo condiciones equivalentes de entrenamiento y seleccionar la alternativa con el mejor equilibrio entre deteccion de defectos y tiempo de inferencia.

## Dataset

Se utiliza el conjunto publico `2OBe/Ball_Screw_Drive_Classification`, disponible en Hugging Face. Las imagenes se agrupan en dos clases:

- `N`: pieza sin defecto
- `P`: pieza con pitting

La muestra empleada se genero con la semilla 42 y conserva un balance exacto entre clases.

| Division | Total | Sin defecto | Pitting |
| --- | ---: | ---: | ---: |
| Entrenamiento | 3,000 | 1,500 | 1,500 |
| Validacion | 600 | 300 | 300 |
| Prueba | 1,000 | 500 | 500 |

El archivo `data/dataset_muestra_balanceada.csv` registra los nombres, etiquetas y divisiones de las imagenes utilizadas. Las imagenes originales no se incluyen en este repositorio y se descargan desde Hugging Face al ejecutar el notebook.

## Modelos comparados

- Microsoft ResNet-50
- Facebook ConvNeXt-Tiny
- Google ViT-Base Patch16 224

Los modelos se inicializan con pesos preentrenados en ImageNet y se adaptan a una clasificacion binaria. Todos usan imagenes de 224 x 224 pixeles, AdamW, una tasa de aprendizaje de `2e-5`, lotes de 32 imagenes y dos epocas.

## Resultados

| Modelo | Accuracy | Precision | Recall | F1 score | Latencia |
| --- | ---: | ---: | ---: | ---: | ---: |
| ConvNeXt-Tiny | 96.50 % | 94.46 % | 98.80 % | 96.58 % | 6.58 ms |
| ViT-Base | 96.10 % | 93.08 % | 99.60 % | 96.23 % | 16.03 ms |
| ResNet-50 | 70.60 % | 66.30 % | 83.80 % | 74.03 % | 7.25 ms |

ConvNeXt-Tiny fue seleccionado porque obtuvo el mayor F1 score y la menor latencia de los tres modelos evaluados. ViT-Base alcanzo un recall ligeramente mayor, pero su latencia fue aproximadamente 2.4 veces superior.

## Entorno de ejecucion

- Google Colab
- Python 3
- GPU NVIDIA T4
- PyTorch y Torchvision
- Transformers y Hugging Face Datasets
- Scikit-learn, Pandas, Matplotlib y Seaborn

## Ejecucion

1. Abrir `notebooks/Actividad4.ipynb` en Google Colab.
2. Seleccionar un entorno con GPU desde `Entorno de ejecucion > Cambiar tipo de entorno de ejecucion`.
3. Crear el secreto `HF_TOKEN` en Colab con un token de lectura de Hugging Face.
4. Ejecutar las celdas en orden.
5. Descargar los archivos CSV generados al finalizar la ejecucion.

El dataset se descarga automaticamente. El entrenamiento completo puede tardar varios minutos y depende de la disponibilidad de la GPU asignada por Colab.

## Estructura del repositorio

```text
.
|-- data/
|   `-- dataset_muestra_balanceada.csv
|-- docs/
|   `-- Actividad_4.docx
|-- notebooks/
|   `-- Actividad4.ipynb
|-- results/
|   `-- resultados_comparacion_modelos.csv
|-- src/
|   |-- config.py
|   `-- metrics.py
|-- .gitignore
|-- README.md
`-- requirements.txt
```

## Conclusiones

Los resultados muestran que la transferencia de aprendizaje permite obtener un desempeño competitivo aun con una muestra controlada y balanceada. ConvNeXt-Tiny presento el mejor compromiso entre sensibilidad ante defectos, precision de las alertas y velocidad de inferencia. Su F1 score de 96.58 % y una latencia promedio de 6.58 ms por imagen lo convierten en la opcion mas adecuada para continuar con el prototipo.

Estos resultados no representan una autorizacion para controlar o bloquear un proceso productivo. Antes de una aplicacion industrial es necesario validar el modelo con imagenes de la camara real, variaciones de iluminacion, enfoque, suciedad, desgaste y diferentes numeros de parte. Tambien se deben medir falsos OK y falsos NOK, definir un umbral de confianza y conservar un metodo de referencia durante el piloto.

## Autor

Erick Emmanuel Covarrubias Avila

