# WhatsReport

Herramienta de escritorio desarrollada en Python (Flet) orientada a la automatización de procesos operativos de TI. Extrae y procesa historiales de chat exportados de WhatsApp (`.txt`) para consolidar reportes formales de monitoreo en Microsoft Excel (`.xlsx`) en cuestión de segundos.

---

## Requisitos Previos

* **Python 3.10+** instalado en el sistema.
* **Inno Setup 6** (requerido únicamente para compilar el instalador formal `.exe`).

---

## Instalación y Entorno Local

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

## Generación del Programa (Versión Portable)

1. Ejecuta el siguiente comando para crear la versión portable de esta aplicación:
   ```bash
   pyinstaller --noconsole --onefile --icon="icons/favicon.ico" --add-data "icons;icons" --name "WhatsReport" main.py

2. Dirigete a la carpeta `/dist` y verás el programa portable listo para usar.

## Creación del Instalable para Windows 10 + (.exe)

1. Asegurate de tener instalado el programa Inno Setup.

2. Con dicho programa, abre el archivo `instalador.iss`

3. Correlo en el entorno de Inno Setup (dandole al botón de Play).

4. Una vez terminado el proceso, dirigete a la carpeta `/dist_installer`. Ahí encontrarás el archivo `.exe` creado y listo para instalar el programa en Windows.