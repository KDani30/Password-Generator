# Generador de Contraseñas Seguras con Streamlit

Este proyecto es un generador de contraseñas seguras desarrollado con Python y Streamlit. Permite a los usuarios crear contraseñas personalizadas con una longitud específica y la opción de incluir caracteres especiales. La aplicación es fácil de usar y sigue las mejores prácticas de seguridad para la creación de contraseñas.

---

### Más información sobre Streamlit:

Para obtener más información sobre la librería Streamlit, visita el siguiente enlace:  
[Documentación oficial de Streamlit](https://docs.streamlit.io/)

---

## Características principales

- **Longitud personalizable:** El usuario puede seleccionar la longitud de la contraseña, con un mínimo de 8 caracteres y un máximo de 20.
- **Caracteres especiales:** Opción para incluir o excluir caracteres especiales en la contraseña.
- **Interfaz intuitiva:** Interfaz gráfica sencilla y amigable creada con Streamlit.
- **Consejos de seguridad:** Proporciona recomendaciones para crear contraseñas seguras.

---

## Requisitos

- Python 3.12.3 o superior.
- Librería Streamlit instalada.

---

## Instalación y configuración

### Crear un entorno virtual
Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto. Puedes crear uno con el siguiente comando:

```bash
python -m venv nombre_de_entorno_virtual
```

Activación<br/>

```bash
.\nombre_del_entorno\Scripts\activate
```
Dentro del entorno virtual se instalan las dependencias necesarias para el funcionamiento de la aplicacion.

```bash
pip install streamlit
```

Nota: Debes estar en el directorio principal del proyecto

## Linux

Creación<br/>

```bash
sudo apt install python3.12-venv -y
python3.12 -m venv nombre_del_entorno
```

Activación<br/>

```bash
source nombre_del_entorno/bin/activate
```

**Desactivacion**
tanto en windows como en linux, utilice el siguiente comando:<br/>

```bash
/deactivate
```

### Instalar dependencias
Instala la librería Streamlit usando pip:

```bash
pip install streamlit
```

## Ejecutar la aplicación

### Iniciar la aplicación

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
streamlit run main.py
```

Esto iniciará la aplicación en tu navegador predeterminado, generalmente en http://localhost:8501.

 ## Especificar host y puerto

Si deseas ejecutar la aplicación en un host y puerto específicos, utiliza los siguientes parámetros:

```bash
streamlit run main.py --server.address=0.0.0.0 --server.port=8000
```

Esto iniciará la aplicación en http://0.0.0.0:8000.


## Recomendaciones de seguridad

- **Longitud:** Utiliza contraseñas de al menos 16 caracteres.
- **Complejidad:** Combina letras mayúsculas, minúsculas, números y caracteres especiales.
- **Evitar información personal:** No uses nombres, fechas de nacimiento o palabras comunes.
- **Verificación de seguridad:** Utiliza herramientas como [Kaspersky Password Checker](https://password.kaspersky.com/es/) para evaluar la fortaleza de tu contraseña.
