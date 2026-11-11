# Path Intermediate · Lab 1

**Clasificación y prioridad de incidencias FRC con Python orientado a objetos.** Material del alumno: guía, rúbrica de 0 a 100, datos sintéticos, tests y código inicial para completar. Duración prevista: **5 horas**, con entorno preparado, descanso y margen de depuración.

## Empieza aquí

1. Lee la [guía de inicio](./docs/GUIA_DE_INICIO.md) ([Word](./docs/GUIA_DE_INICIO.docx)) si es tu primer proyecto Python con esta estructura.
2. Sigue la [guía del alumno](./GUIA_ALUMNO.md) ([Word](./GUIA_ALUMNO.docx)), tarea por tarea.
3. Consulta [qué debes completar](./LEEME_PRACTICA.md), la [rúbrica](./RUBRICA.md) ([Word](./RUBRICA.docx)) y la plantilla [EVIDENCIAS.md](./EVIDENCIAS.md).

## 1. Haz tu copia

Este repositorio público se utiliza como material de referencia. Puedes leerlo, clonarlo y hacer **fork**. Para guardar tus cambios en GitHub, pulsa **Fork** y clona el repositorio de tu cuenta; trabajarás sobre tu copia, sin permisos de escritura sobre el original.

Si solo quieres trabajar en tu PC sin publicar cambios:

```powershell
git clone https://github.com/martinblazquezjorge/path_intermediate_lab1.git
cd path_intermediate_lab1
```

También puedes pulsar **Code → Download ZIP**, extraer el archivo y abrir una terminal en la carpeta que contiene este README. No necesitas modificar ningún otro repositorio ni copiar archivos de otros Labs.

## 2. Prepara el entorno

Usa **Python 3.12 de 64 bits**. Comprueba primero:

```powershell
py -3.12 --version
```

Desde la raíz de este repositorio, en PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```

Usar la ruta del intérprete evita tener que activar el entorno o cambiar la política de ejecución del equipo. Si prefieres activarlo, ejecuta `.\.venv\Scripts\Activate.ps1` y después podrás usar los comandos `python ...` de la guía. En macOS/Linux, usa `python3.12 -m venv .venv` y `.venv/bin/python` para instalar y ejecutar.

La primera instalación requiere conexión. El Lab funciona después con archivos locales, sin cuenta cloud, claves ni modelos de pago. `requirements.txt` incluye la instalación del paquete local y utiliza `constraints.txt` para fijar las versiones comprobadas. Si Python 3.12 no está disponible o tienes restricciones de instalación, solicita al docente el entorno preparado.

## 3. Entiende los fallos iniciales

**Al empezar, los tests no pasan todos.** Los métodos que debes implementar contienen `NotImplementedError("TODO ...")`. Esos fallos son intencionados: no borres ni debilites las pruebas para ponerlas en verde.

| Archivo | Qué debes completar |
|---|---|
| `src/frc_incidents/domain.py` | Validaciones de `Incident.__post_init__` y `Prediction.__post_init__` |
| `src/frc_incidents/repositories.py` | Carga de incidencias en `IncidentCsvRepository.load` |
| `src/frc_incidents/service.py` | Política de prioridad y método `IncidentClassificationService.classify` |

Son **cinco métodos pendientes**. El clasificador, el writer JSON, el CLI y otros componentes de apoyo ya están implementados para concentrar el aprendizaje. El repositorio no incluye las soluciones completas de las tareas ni guías docentes.

Se proporcionan **12 casos de prueba**. Para comprobar únicamente que se pueden recoger antes de implementar:

```powershell
.\.venv\Scripts\python.exe -m pytest --collect-only -q
```

Resultado esperado: `12 tests collected`. Después de completar las tareas debe pasar la suite entera. Sigue la guía para ejecutar las pruebas concretas de cada paso.

## 4. Ejecuta tu aplicación al terminar

```powershell
.\.venv\Scripts\python.exe -m frc_incidents.cli --output output/predictions.json
```

El CLI lee `data/training.csv` y `data/incidents.csv`, procesa tres incidencias sintéticas y genera JSON con identificador, categoría, confianza, prioridad y explicación. Antes de completar los TODO, el comando puede fallar intencionadamente. No decide ni ejecuta acciones bancarias materiales.

## 5. Entrega y evaluación

Completa [EVIDENCIAS.md](./EVIDENCIAS.md) con comandos y resultados reales, un caso positivo, casos negativos/límites, dos decisiones explicadas, una limitación y la ayuda consultada. Usa la [rúbrica de 100 puntos](./RUBRICA.md) para autoevaluarte.

Entrega o publica en **tu fork** el código de tu práctica, los tests y las evidencias según indique el docente. Excluye `.venv`, cachés, salidas temporales, credenciales y datos reales; `.gitignore` ya contempla esos archivos. El repositorio original permanece como punto de partida común.

Los tiempos son estimaciones docentes pendientes de validar con alumnos; la preparación del entorno debe resolverse antes de la sesión. Si llevas ocho minutos bloqueado, anota entrada, resultado esperado y primer error y pide una pista. Usar ayuda no resta puntos automáticamente: debes comprobar y explicar el resultado.
