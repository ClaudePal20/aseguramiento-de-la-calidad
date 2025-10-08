# 🧪 Pruebas de Rendimiento en Python — API Flask

Incluye pruebas de:
- Carga máxima  
- Volumen  
- Tiempo prolongado  
- Picos (spike)  
- Concurrencia  
- Degradación de recursos  
- Prueba combinada  

---

## 🚀 1. Requisitos

Asegúrate de tener instalado:

- **Python 3.9+**
- **pip** (gestor de paquetes)
- **virtualenv** (opcional, recomendado)

---

## 📦 2. Instalación

```bash
# Clona el repositorio o crea una carpeta nueva
git clone https://github.com/ClaudePal20/aseguramiento-de-la-calidad.git
cd flask-performance-tests

# (Opcional) Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
pip install flask requests psutil