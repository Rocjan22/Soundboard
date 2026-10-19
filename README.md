# 🔊 Soundboard

Panel de sonidos de escritorio hecho en Python con PySide6.
Agrega tus archivos `.mp3` y cada uno se convierte en un botón listo para reproducirse con un clic.

> ⚠️ **Proyecto en fase alfa.** Funciona, pero todavía le faltan funciones. Consulta las [limitaciones conocidas](#️-limitaciones-conocidas).

## ✨ Funciones

- Agregar sonidos `.mp3` y elegir el nombre de su botón
- Los sonidos se copian a una carpeta propia, así que el tablero no depende de los archivos originales
- Reproducir con un clic (un sonido nuevo detiene al anterior)
- Botón **Stop** e indicador del sonido en reproducción
- Cuadrícula que se adapta al tamaño de la ventana
- Los sonidos se guardan entre sesiones

## 📥 Descarga

Descarga el `.exe` más reciente desde la sección de [Releases](https://github.com/Rocjan22/soundboard/releases).
No necesitas tener Python instalado.

Al abrirlo por primera vez se crea una carpeta `data` junto al `.exe`, donde se guardan tus sonidos.
Si mueves el programa, mueve también esa carpeta.

## 🛠️ Ejecutar desde el código

Requisitos: **Python 3.13** o superior.

```bash
# 1. Clonar el repositorio
git clone https://github.com/Rocjan22/soundboard.git
cd soundboard

# 2. Crear y activar un entorno virtual
python -m venv .venv
source .venv/Scripts/activate   # Git Bash
# .venv\Scripts\activate        # PowerShell

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python main.py
```

### Generar el ejecutable

```bash
pip install -r requirements-dev.txt
pyinstaller Soundboard.spec
```

El `.exe` se genera en la carpeta `dist/`.

## 📁 Estructura del proyecto

```
soundboard/
├── models/       # Modelo de datos (Sound)
├── audio/        # Reproducción de audio (AudioPlayer)
├── storage/      # Guardado y carga de sonidos (SoundRepository)
└── ui/           # Interfaz gráfica (MainWindow, SoundButton)
main.py           # Punto de entrada
```

Cada paquete tiene una sola responsabilidad: por ejemplo, solo `audio/` usa pygame y solo `storage/` lee y escribe archivos.

## ⚠️ Limitaciones conocidas

- Todavía no se pueden eliminar ni renombrar sonidos desde la aplicación.
- Si un sonido termina por sí solo, el indicador "Reproduciendo" no se borra hasta presionar **Stop**.
- Solo se admiten archivos `.mp3`.
- Por ahora, el ejecutable solo está disponible para Windows.

## 🗺️ Próximamente

- [ ] Eliminar y renombrar sonidos
- [ ] Estilo visual oscuro
- [ ] Tiempo de reproducción (actual / total)
- [ ] Control de volumen
- [ ] Varios tableros con pestañas

## 🧰 Tecnologías

- [Python](https://www.python.org/)
- [PySide6](https://doc.qt.io/qtforpython-6/) (Qt para Python)
- [pygame](https://www.pygame.org/) (reproducción de audio)
- [PyInstaller](https://pyinstaller.org/) (empaquetado)
