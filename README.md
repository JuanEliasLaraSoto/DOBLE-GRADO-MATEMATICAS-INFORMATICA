# Doble Grado en Matemáticas e Ingeniería Informática

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL%20%2F%20PL--SQL-4479A1?logo=oracle&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?logo=mathworks&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)

Ejercicios, prácticas y exámenes resueltos que he ido haciendo a lo largo del **Doble Grado en Matemáticas e Ingeniería Informática** en la **Universidad de Málaga (UMA)**.

No son apuntes: todo lo que hay aquí es trabajo práctico. En casi todas las carpetas está el enunciado (normalmente en PDF) junto a mi solución, ya sea código, un cuaderno de Jupyter, un script de R o un informe.

> **Autor:** Juan Elías Lara Soto

---

## Índice

- [Asignaturas](#asignaturas)
  - [Matemáticas](#matemáticas)
  - [Informática](#informática)
- [Detalle por asignatura](#detalle-por-asignatura)
- [Cómo ejecutar el código](#cómo-ejecutar-el-código)
- [Aviso](#aviso)

---

## Asignaturas

### Matemáticas

| Asignatura | Contenido | Tecnologías |
|---|---|---|
| [Métodos Numéricos I](METODOS%20NUMERICOS%201) | Aritmética en coma flotante, ecuaciones no lineales, interpolación e integración numérica | Python |
| [Métodos Numéricos II](METODOS%20NUMERICOS%202) | Álgebra lineal numérica: normas, sistemas triangulares, Gauss, LU, Cholesky, Householder | Python, Jupyter |
| [Análisis Numérico](ANALISIS%20NUMERICO) | Métodos numéricos para EDOs (unipaso y multipaso) y exámenes resueltos | Python |
| [Probabilidad](PROBABILIDAD) | Estadística descriptiva | Python, Colab |
| [Inferencia Estadística](INFERENCIA%20ESTADISTICA) | Estimación puntual, verosimilitud y error cuadrático medio | R, Quarto |
| [Optimización](OPTIMIZATION) | Modelado y resolución de problemas de optimización con AMPL | Python, AMPL |
| [Aprendizaje](APRENDIZAJE) | Árboles de decisión, SVM, redes neuronales, *random forest* y *boosting* | R, Quarto |

### Informática

| Asignatura | Contenido | Tecnologías |
|---|---|---|
| [Procesadores de Lenguajes](PROCESADORES%20DE%20LEGUAJES) | Compilador del lenguaje PLX y exámenes de 2014 a 2025 | Java, JFlex, CUP |
| [Ciberseguridad](CIBERSEGURIDAD) | Criptografía simétrica y asimétrica, protocolos, certificados y TLS | Python, PyCryptodome |
| [Machine Learning](MACHINE%20LEARNING) | Perceptrón simple, perceptrón multicapa y Extreme Learning Machine | MATLAB |
| [Robótica](ROBOTICA-PRACT) | Movimiento, percepción y localización de robots móviles | Python, Jupyter, ROS 2 |
| [Algoritmia y Complejidad](ALGORITMIA%20Y%20COMPLEJIDAD) | Demostración de que *k*-COLOR es NP-completo | LaTeX |
| [Bases de Datos](BASE%20DE%20DATOS) | Modelo E/R, paso a tablas, DDL y consultas SQL | SQL, Oracle Data Modeler |
| [Administración de Bases de Datos](ADMINISTRACION%20DE%20BASES%20DE%20DATOS) | Exámenes de PL/SQL: funciones, procedimientos y *triggers* | PL/SQL (Oracle) |
| [Sistemas de Información](SISTEMAS%20DE%20INFORMACION) | Informes sobre Tableau, ERP, PrestaShop, BPMN y Alfresco | Tableau, BPMN |
| [Internet](INTERNET) | Página web de una tienda online | HTML, CSS |

---

## Detalle por asignatura

<details>
<summary><b>Métodos Numéricos I</b> — Python</summary>

| Práctica | Tema |
|---|---|
| `practica0.py` | Primeros pasos con NumPy y Matplotlib |
| `PRACTICA 1` | Aritmética en coma flotante: épsilon de máquina, sumas parciales y errores de redondeo |
| `PRACTICA 2.1` | Ecuaciones no lineales: bisección, *regula falsi* y secante |
| `PRACTICA 2.2` | Iteración de punto fijo y método de Newton |
| `PRACTICA 3` | Interpolación: diferencias divididas, Horner, nodos de Chebyshev y *splines* |
| `PRACTICA 4` | Integración numérica: punto medio, trapecio y Simpson (simples y compuestas) |
| `examenes.py` | Ejercicios de examen |

</details>

<details>
<summary><b>Métodos Numéricos II</b> — Python / Jupyter</summary>

| Cuaderno | Tema |
|---|---|
| `practica-01.ipynb` | Introducción a NumPy |
| `practica-02.ipynb` | Definición de funciones propias que implementan algoritmos |
| `practica-03.ipynb` | Normas vectoriales y matriciales |
| `practica-04.ipynb` | Sistemas triangulares: métodos de descenso y remonte |
| `practica-05.ipynb` | Métodos directos de tipo Gauss |
| `practica-06.ipynb` | Factorizaciones LU y de Cholesky |
| `practica-07.ipynb` | Matrices de Householder |

`algoritmos.py` reúne las funciones implementadas a lo largo del curso.

</details>

<details>
<summary><b>Análisis Numérico</b> — Python</summary>

Resolución numérica de ecuaciones diferenciales ordinarias y sistemas:

- **Práctica 1:** métodos de Euler y de Taylor (órdenes 2 y 3).
- **Práctica 2:** métodos multipaso de Adams-Bashforth (AB2, AB3), Runge-Kutta y combinaciones unipaso/multipaso.
- **`dibuja_frontera.py`:** dibuja la frontera de la región de estabilidad absoluta de un método multipaso.
- **`algoritmos.py`:** recopilación de los métodos implementados.
- **Exámenes resueltos:** cursos 17-18 y 21-22, junio de 2022, controles de prácticas y un examen con nota 10 (`Exam-Grade-10.py`).

</details>

<details>
<summary><b>Probabilidad</b> — Python / Colab</summary>

- `Practica_Estadistica_Descriptiva.ipynb`: variables cualitativas y cuantitativas, representaciones gráficas, detección de *outliers*, medidas de tendencia central y de posición, y variables bidimensionales.

</details>

<details>
<summary><b>Inferencia Estadística</b> — R / Quarto</summary>

| Práctica | Tema |
|---|---|
| `PRACTICA 5` | Estimación puntual |
| `PRACTICA 6` | Funciones de verosimilitud |
| `PRACTICA 7` | Error cuadrático medio de estimadores (simulación) |

Cada práctica incluye el `.qmd` fuente y el PDF generado.

</details>

<details>
<summary><b>Optimización</b> — Python + AMPL</summary>

- [`Práctica1_Opt_ipynb_txt.ipynb`](Pr%C3%A1ctica1_Opt_ipynb_txt.ipynb) (en la raíz del repositorio): primeros pasos con AMPL desde Python mediante `amplpy`. Se puede abrir directamente en Google Colab.
- [`OPTIMIZATION/Juan elias lara soto.ipynb`](OPTIMIZATION/Juan%20elias%20lara%20soto.ipynb): examen práctico (diciembre de 2025). Despacho de un mercado eléctrico con productores cuyos costes son funciones lineales a trozos.

</details>

<details>
<summary><b>Aprendizaje</b> — R</summary>

- **`rcart-apredizaje`:** árboles de clasificación y regresión con `rpart` (CART).
- **`practica svm`:** máquinas de vectores soporte.
- **`primer examen`:** CART y SVM sobre el conjunto de datos *German Credit*.
- **`segundo examen aprendizaje`:** redes neuronales (`nnet`), *random forest* y árboles sobre el conjunto *kyphosis* (problema 1) y *boosting* con `adabag` (problema 2).

</details>

<details>
<summary><b>Procesadores de Lenguajes</b> — Java, JFlex, CUP</summary>

Compilador del lenguaje **PLX**, un lenguaje pequeño parecido a C. El analizador léxico está escrito con **JFlex**, el sintáctico con **CUP**, y el compilador genera código intermedio de tres direcciones (ficheros `.ctd`).

| Carpeta | Contenido |
|---|---|
| `ENUNCIADOS` | Enunciados en PDF de MINICORE, CORE y los exámenes de cada año |
| `MINICORE` | Primera versión del compilador |
| `CORE` | Versión completa de la práctica principal, base de los exámenes |
| `2014 EXAM` … `2025 EXAM` | Ampliaciones del compilador pedidas en cada examen (incluye las variantes `2016 WITH ARRAY`, `2021 WITH STRUCT`, `2022 A` y `2022 B`) |
| `cupexample` | Ejemplo mínimo de gramática en CUP |

Cada carpeta de examen contiene los `.flex` y `.cup`, las clases Java del árbol sintáctico y los programas de prueba `.plx` (`plxc-init*`).

</details>

<details>
<summary><b>Ciberseguridad</b> — Python (PyCryptodome)</summary>

| Práctica | Tema |
|---|---|
| `PRACTICA 0` | Criptografía clásica: cifrado César |
| `PRACTICA 1` | Cifrado simétrico con AES en los modos ECB, CBC, CFB, OFB, CTR y GCM |
| `PRACTICA 2` | Criptografía asimétrica: RSA, autoridad de certificación y comunicación Alice–Bob con *sockets* |
| `PRACTICA 3` | Protocolos de establecimiento de claves con un tercero de confianza (A, B, T) |
| `PRACTICA 4` | Certificados digitales (XCA) |
| `PRACTICA 5` | *Red Team* |
| `PRACTICA 6` | Protocolos y TLS: servidor HTTPS en Python |

</details>

<details>
<summary><b>Machine Learning</b> — MATLAB</summary>

- **Perceptrón Simple:** entrenamiento sobre AND, OR, XOR y conjuntos linealmente separables, con visualización de la frontera de decisión.
- **Perceptrón Multicapa:** retropropagación del error con función logística, problemas de clasificación y regresión sobre conjuntos de datos de UCI, y validación cruzada en *N* pliegues.
- **ELM:** *Extreme Learning Machine* aplicada al reconocimiento de escritura manuscrita.

Las carpetas incluyen el enunciado y un PDF con las respuestas.

</details>

<details>
<summary><b>Robótica</b> — Python / Jupyter / ROS 2</summary>

Trabajo hecho sobre el repositorio oficial de la asignatura, [`uma_robotics_2026`](https://github.com/jotaraul/uma_robotics_2026), del grupo MAPIR de la UMA:

1. **Bienvenida:** introducción a Jupyter y Python.
2. **Bases de probabilidad y estadística**, con un ejercicio extra.
3. **Movimiento del robot:** composición de poses y modelos de movimiento basados en velocidad y en odometría.
4. **Percepción:** modelos basados en *landmarks*, escáner láser y ROS 2.
5. **Localización:** EKF, filtro de partículas y AMCL en ROS 2.

</details>

<details>
<summary><b>Algoritmia y Complejidad</b> — LaTeX</summary>

Trabajo en LaTeX que demuestra que el problema ***k*-COLOR es NP-completo**: definición como lenguaje, ejemplos, aplicaciones de 3-COLOR y la reducción. Incluye un documento de preguntas, el `.tex` y los PDF compilados.

</details>

<details>
<summary><b>Bases de Datos</b> — SQL</summary>

- **Práctica 1:** modelo en Oracle SQL Developer Data Modeler (`.dmd`) y el DDL generado.
- **Práctica 2:** diagrama E/R, paso a tablas y sentencias `CREATE TABLE`.
- **Práctica 5:** relación de consultas SQL (DML).

</details>

<details>
<summary><b>Administración de Bases de Datos</b> — PL/SQL</summary>

Exámenes de PL/SQL resueltos (funciones, procedimientos, *triggers*, etc.): junio de 2017, junio de 2019, septiembre de 2022, junio de 2023, noviembre de 2023 y junio de 2024, además de la Práctica 1. Las soluciones están en `PL-SQL/sql/` y los enunciados en PDF en `PL-SQL/`.

</details>

<details>
<summary><b>Sistemas de Información</b></summary>

| Práctica | Tema |
|---|---|
| `PRACTICA 1` | Visualización de datos con Tableau |
| `PRACTICA 2` | Evaluación de aplicaciones de gestión comercial para pymes |
| `PRACTICA 3` | Comercio electrónico con PrestaShop |
| `PRACTICA 4` | Modelado de procesos de negocio con BPMN |
| `PRACTICA 5` | Gestor de contenidos Alfresco |

Cada práctica incluye el guion y el informe entregado.

</details>

<details>
<summary><b>Internet</b> — HTML / CSS</summary>

- `proyectohtml`: página de una tienda online básica, maquetada con HTML y CSS.

</details>

---

## Cómo ejecutar el código

Cada asignatura usa sus propias herramientas. Esto es lo mínimo que hace falta en cada caso:

| Tecnología | Asignaturas | Requisitos |
|---|---|---|
| **Python** | Métodos Numéricos I y II, Análisis Numérico, Probabilidad, Optimización, Robótica | `numpy`, `scipy` y `matplotlib`. Ciberseguridad usa además `pycryptodome`, y Optimización `amplpy` |
| **Jupyter** | Métodos Numéricos II, Probabilidad, Optimización, Robótica | Jupyter Notebook/Lab o Google Colab |
| **R** | Aprendizaje, Inferencia Estadística | R (o RStudio) con `rpart`, `rpart.plot`, `e1071`, `kernlab`, `caret`, `nnet`, `randomForest`, `adabag` y `pROC`, y Quarto para los `.qmd` |
| **MATLAB** | Machine Learning | MATLAB (u Octave, aunque puede haber incompatibilidades) |
| **Java** | Procesadores de Lenguajes | JDK, [JFlex](https://jflex.de/) y [CUP](http://www2.cs.tum.edu/projects/cup/) |
| **SQL / PL/SQL** | Bases de Datos, Administración de Bases de Datos | Oracle Database y SQL Developer |
| **LaTeX** | Algoritmia y Complejidad | Cualquier distribución de LaTeX (TeX Live, MiKTeX) u Overleaf |

Por ejemplo, para ejecutar una práctica de Métodos Numéricos I:

```bash
pip install numpy scipy matplotlib
python "METODOS NUMERICOS 1/PRACTICA 3/practica3.py"
```

Para los cuadernos de Robótica, el repositorio de la asignatura incluye su propio [`requirements.txt`](ROBOTICA-PRACT/uma_robotics_2026/requirements.txt).

---

## Aviso

- Las soluciones son **mías** y pueden contener errores. Si encuentras alguno, abre un *issue* o una *pull request*.
- Los **enunciados**, guiones y materiales de partida pertenecen a los profesores de la Universidad de Málaga que imparten cada asignatura. Aquí solo se incluyen como contexto de las soluciones.
- Este repositorio sirve **de consulta y para aprender**. Si estás cursando alguna de estas asignaturas, úsalo para comparar tu solución o desatascarte, no para copiar: respeta la normativa académica de tu universidad.

---

⭐ Si te resulta útil, dale una estrella al repositorio.
