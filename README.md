
<div align="center">
   
# ⚙️ PDF Renamer Security Suite (PDF-RSS)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010%2B-success)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


</div>

## 🌟 Resumen del Proyecto

**PDF Renamer Security Suite (PDF-RSS)** es una solución completa de escritorio desarrollada en **Python** utilizando **Tkinter** y **Pandas**.

Su propósito es automatizar y simplificar el flujo de trabajo para el **renombrado por lotes** y la **protección con contraseña** de documentos PDF. La aplicación centraliza la preparación de datos, permitiendo al usuario generar plantillas de Excel, editar la información de los nuevos nombres y claves de acceso dentro de la misma interfaz, y finalmente procesar los archivos de forma segura.

---

## ✨ Características Principales

* **Generador de Plantillas (Excel):** Genera archivos `.xlsx` con estructuras predefinidas (Facturas, Contratos, Pacientes, etc.) para recopilar los datos de renombrado y contraseñas.
* **Interfaz Gráfica (GUI):** Flujo de trabajo intuitivo dividido en 3 pestañas: **1. Seleccionar Estructura**, **2. Editar Datos** y **3. Procesar PDFs**.
* **Edición de Datos Integrada:** Carga y modifica la plantilla de Excel directamente en una tabla dentro de la GUI, sin necesidad de herramientas externas.
* **Renombrado y Protección por Lotes:** Asigna un nuevo nombre a cada PDF y lo protege con una contraseña única, basándose en la fila correspondiente del archivo Excel.
* **Múltiples Estructuras:** Soporte para estructuras de datos específicas de negocio (e.g., Facturas, Contratos, Pacientes) que se utilizan para generar las plantillas.
* **Log de Ejecución Detallado:** Muestra un registro en tiempo real de los PDFs procesados y cualquier advertencia o error durante la ejecución.

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
| :--- | :--- |
| **Python** | Lenguaje de programación principal. |
| **Tkinter / ttk** | Creación de la Interfaz Gráfica de Usuario (GUI). |
| **Pandas** | Gestión de datos: Creación, lectura y escritura del archivo Excel de plantilla. |
| **openpyxl** | Módulo backend necesario para que Pandas maneje archivos `.xlsx`. |
| **`os` & `pathlib`** | Manejo del sistema de archivos y directorios. |
| **[Librería PDF]** | *Pendiente de integrar* (e.g., `pypdf`) para la manipulación y protección de los archivos PDF. |

---

## 💡 Información General y Propósito

| Detalle | Descripción |
| :--- | :--- |
| **Creador** | LSCF |
| **Propósito** | Optimizar y asegurar el proceso de renombrado y cifrado de documentos PDF por lotes. |
| **Origen** | Evolución del proyecto `Renamer_PDF_Security` con enfoque en GUI y preparación de datos. |

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- Windows 10/11 (o cualquier sistema compatible con Tkinter)
---

### 1. Instalación de Dependencias

El proyecto requiere librerías externas para la gestión de datos (Excel).

1.  **Clona el repositorio**
    ```bash
    git clone https://github.com/LSCF84/PDF-Renamer-Security-Suite-PDF-RSS/
    cd PDF-Renamer-Security-Suite
    ```
2.  **Instala dependencias**
    ```bash
    pip install -r requirements.txt
    ```
    (Asegúrate de que `requirements.txt` contenga al menos `pandas` y `openpyxl`).

### 2. Ejecución

1.  Descarga o clona el archivo principal (ej: `main.py`).
2.  Ejecuta el *script* desde tu terminal:

    ```bash
    python main.py
    ```

### 3. Guía de Uso Rápido

1.  **Seleccionar Estructura:** Elige la categoría de documentos (ej. "Facturas") para generar una plantilla de Excel con las columnas adecuadas.
2.  **Editar Datos:** Carga el Excel generado y rellena las columnas de **ID del archivo original**, **Nuevo Nombre de Salida** y **Contraseña** directamente en la tabla de la GUI.
3.  **Procesar PDFs:** Selecciona el directorio con tus PDFs originales, la ruta de salida y el archivo Excel completado. Haz clic en **PROCESAR PDFs**.

---

## 👨‍💻 Autor

**LSCF**

## 🤝 ¿Quieres contribuir?

¡Claro! Abre un Issue o un Pull Request para ayudar a mejorar esta suite. Usa la plantilla al crear un Issue.

---

⭐️ Si te sirvió, ¡dale una estrella al repositorio!
