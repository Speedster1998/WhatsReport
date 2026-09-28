# WhatsReport

Herramienta de escritorio desarrollada en Python (Flet) orientada a la automatización de procesos operativos de TI[cite: 1]. Parsea y extrae historiales de chat exportados de WhatsApp (`.txt`) para consolidar reportes formales de monitoreo en Microsoft Excel (`.xlsx`) en cuestión de segundos[cite: 1, 3].

---

## 🛠️ Requisitos Previos

* **Python 3.10+** instalado en el sistema.
* **Inno Setup 6** (requerido únicamente para compilar el instalador formal `.exe`).

---

## 🚀 Instalación y Entorno Local

1. Clona el repositorio y sitúate en la raíz del proyecto:
   ```bash
   git clone [https://github.com/TU_USUARIO/WhatsReport.git](https://github.com/TU_USUARIO/WhatsReport.git)
   cd WhatsReport

2. Instalar las dependencias del proyecto:
   ```bash
   pip install flet pandas openpyxl pyinstaller

3. Probar si el proyecto corre con normalidad:
   ```bash
   python main.py