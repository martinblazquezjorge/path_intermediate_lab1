# Guía de inicio · Lab 1

Este documento te ayuda a comenzar aunque sea tu primer proyecto Python con varios archivos y pruebas. El objetivo del Lab es transformar incidencias sintéticas de un CSV en predicciones explicadas en JSON. La guía principal detalla las seis tareas; aquí se prepara el entorno y el vocabulario.

## 1. Localiza la carpeta de trabajo

Abre una terminal en la carpeta que contiene `README.md`, `requirements.txt`, `data/`, `src/` y `tests/`. Todas las rutas de esta práctica parten de ahí. Si has descargado un ZIP, extráelo primero. Si quieres guardar cambios en GitHub, haz un fork y clona tu fork. Un fork es una copia del repositorio en tu cuenta; un clon es una copia en tu PC.

## 2. Prepara Python sin mezclar instalaciones

Usa Python 3.12 de 64 bits y comprueba `py -3.12 --version`. Un entorno virtual mantiene las dependencias de esta práctica separadas del resto de tu equipo. Desde la raíz del Lab, en PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest --collect-only -q
```

La última orden debe recoger 12 casos. Recoger no es lo mismo que ejecutarlos: comprueba que Python encuentra los módulos y las pruebas. Para ejecutarlas usa `-m pytest -q`. Al principio fallarán algunas con `NotImplementedError` porque falta tu implementación. Usa la ruta completa al Python de `.venv` si la activación del entorno está bloqueada.

La primera instalación necesita conexión. Si `py -3.12` no existe o la descarga está bloqueada, pide al docente un intérprete o entorno preparado. No cambies las versiones al azar para intentar resolverlo.

## 3. Entiende la estructura

| Carpeta o archivo | Responsabilidad |
|---|---|
| `data/incidents.csv` | Tres incidencias sintéticas que se clasificarán |
| `data/training.csv` | Ejemplos para el clasificador proporcionado |
| `src/frc_incidents/domain.py` | Entidades e invariantes de entrada/salida |
| `src/frc_incidents/repositories.py` | Traducción de CSV a objetos |
| `src/frc_incidents/classifier.py` | Clasificador proporcionado; no hay que reimplementarlo |
| `src/frc_incidents/service.py` | Política de prioridad, coordinación y exportación |
| `src/frc_incidents/cli.py` | Interfaz que conecta los componentes y recibe argumentos |
| `tests/` | Casos que demuestran el comportamiento esperado |
| `EVIDENCIAS.md` | Registro de tus resultados y explicaciones |

Un módulo es un archivo Python; un paquete agrupa módulos e incluye `__init__.py`. La instalación local declarada en `requirements.txt` permite importar `frc_incidents` sin copiar archivos a otra carpeta.

## 4. Conceptos antes de programar

Una **entidad** representa información del caso, como una incidencia. Una **invariante** es una regla que siempre debe cumplirse: por ejemplo, un importe negativo no es válido en este dataset. Las validaciones deben vivir en el dominio para funcionar tanto desde un CSV como desde un test.

`@dataclass` genera parte del código repetitivo de una clase a partir de sus campos. `frozen=True` impide cambiar sus campos después de crear el objeto. `__post_init__` se ejecuta tras el constructor y permite comprobar las invariantes. La guía indica exactamente cuáles debes implementar; no necesitas aprender toda la librería antes de empezar.

Un **repositorio de datos** lee CSV y convierte cadenas a tipos Python; no decide prioridad. Un **servicio** coordina componentes. La **inyección de dependencias** consiste aquí en recibir un clasificador y una política desde fuera en vez de crearlos dentro de cada operación. `Protocol` describe el contrato mínimo que debe respetar un componente compatible.

La **categoría** describe el tipo de incidencia y procede del clasificador. La **prioridad** ordena su atención según las reglas explícitas de importe/urgencia. Son dos campos diferentes. Ninguna predicción ejecuta una acción sobre un cliente.

Una **excepción** señala que una entrada o una operación incumple un contrato. Una prueba negativa espera precisamente que aparezca esa excepción: un rechazo correcto es un resultado válido de la prueba.

## 5. Lee y ejecuta una prueba

Un test prepara un caso, llama al código y compara el resultado con lo esperado. En pytest, `assert` comprueba una condición y `pytest.raises` verifica que se rechaza una entrada. Los tests parametrizados repiten el mismo contrato con varios datos; por eso hay 12 casos aunque no haya 12 funciones distintas.

Ejemplo de comando para ejecutar únicamente una comprobación de la primera tarea:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_lab.py::test_incident_rejects_negative_amount
```

No copies el resultado esperado como si fuera tu ejecución. Anota el comando y lo que observaste. Si falla, lee primero el nombre del test, la primera línea de tu archivo implicada y la diferencia entre resultado esperado y obtenido.

## 6. Trabaja en pasos pequeños

Lee el objetivo de una tarea, localiza el TODO, implementa una parte y ejecuta su prueba. No hace falta reescribir los componentes de apoyo. Una vez que funcione, explica qué entra, qué se valida y qué sale. Continúa en el orden de la guía: dominio, CSV, clasificador, política, servicio y CLI.

Si llevas ocho minutos sin avanzar, registra la entrada, salida esperada, primer error y prueba ejecutada y pide una pista. Anota la ayuda en EVIDENCIAS.md y comprueba que puedes explicar el resultado.

## 7. Errores habituales

| Síntoma | Qué comprobar |
|---|---|
| `ModuleNotFoundError: frc_incidents` | Usa el Python del entorno y ejecuta la instalación de requirements.txt desde la raíz del Lab |
| No se encuentra un CSV | Comprueba la carpeta actual y las rutas de `data/` |
| `NotImplementedError: TODO...` | Es un punto pendiente; localiza la tarea correspondiente en la guía |
| PowerShell bloquea Activate.ps1 | Usa directamente `.venv\Scripts\python.exe`, sin cambiar la política del equipo |
| El test esperaba una excepción y no ocurrió | Revisa la invariante o conversión que debía rechazar la entrada |
| La confianza se confunde con la prioridad | Revisa por separado contrato del clasificador y regla de prioridad |

## 8. Antes de entregar

Ejecuta la suite completa y el CLI. Comprueba que el JSON tiene tres predicciones y conserva categoría, confianza, prioridad y explicación. Completa EVIDENCIAS.md con resultados reales y revisa cada criterio de la rúbrica. Entrega código, pruebas y evidencias sin entorno virtual, cachés ni secretos.

Continúa en la [guía del alumno](../GUIA_ALUMNO.md) y consulta la [rúbrica](../RUBRICA.md).
