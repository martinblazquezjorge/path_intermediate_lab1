# Rúbrica · Lab 1 · OOP y clasificación de incidencias · 0 a 100 puntos

La nota se calcula con subcriterios independientes. Para cada subcriterio concede sus puntos completos si la evidencia demuestra todo lo escrito; en caso contrario concede 0 y señala qué falta. No se concede puntuación por mencionar una tecnología sin demostrar el comportamiento. Una solución alternativa correcta puede obtener 100. La suma de los máximos es exactamente 100.

Primero calcula la puntuación bruta. Después aplica los máximos por errores críticos; si concurren varios, usa el menor máximo. No restes dos veces por el mismo fallo: el límite se aplica a la suma final, no como otra resta. Calificación final = mínimo(puntuación bruta, máximos críticos aplicables). Redondear no es necesario: todos los subcriterios tienen puntos enteros.

Orientación para comunicar el nivel: 90–100 dominio sólido; 70–89 objetivos principales logrados con mejoras; 50–69 desarrollo parcial; 0–49 evidencia insuficiente. El umbral docente recomendado es 70/100 con los controles críticos subsanados. Con datos reales, secretos o acciones materiales, deja el resultado pendiente hasta retirarlos; no inventes una nota final.


| Área | Máximo | Evidencia a consultar |

|---|---:|---|

| Dominio e invariantes | 15 | domain.py y pruebas negativas |

| Lectura CSV | 15 | repositories.py, dataset y resultados |

| Integración del clasificador | 10 | classifier.py y llamada desde servicio/CLI |

| Política de prioridad | 15 | PriorityPolicy y tabla de casos límite |

| Servicio y explicación | 15 | classify, classify_all y ejemplo |

| Exportación y CLI | 10 | comando y JSON resultante |

| Pruebas y casos negativos | 10 | salida real de pytest y tests añadidos |

| Comprensión y entrega | 10 | EVIDENCIAS.md y explicación breve |

| **Total** | **100** | Código/deliverables, ejecuciones y explicación |

## Dominio e invariantes · 15 puntos

Evidencia: domain.py y pruebas negativas.


- **4 puntos:** Incident y Prediction son dataclasses congeladas.

- **4 puntos:** Rechaza ID vacío y descripción menor de diez caracteres.

- **4 puntos:** Rechaza importe negativo.

- **3 puntos:** Rechaza confianza fuera de [0,1] y prioridad desconocida.

## Lectura CSV · 15 puntos

Evidencia: repositories.py, dataset y resultados.


- **5 puntos:** Carga tres Incident tipados desde incidents.csv.

- **5 puntos:** Valida urgent y convierte false a False sin bool(cadena).

- **5 puntos:** Carga pares de entrenamiento y conserva las validaciones de dominio.

## Integración del clasificador · 10 puntos

Evidencia: classifier.py y llamada desde servicio/CLI.


- **5 puntos:** Usa fit y predict con sus contratos sin reimplementar Naive Bayes.

- **5 puntos:** Conserva categoría no vacía y confianza válida.

## Política de prioridad · 15 puntos

Evidencia: PriorityPolicy y tabla de casos límite.


- **5 puntos:** Urgencia o importe ≥10.000 da HIGH.

- **5 puntos:** Entre 1.000 y menos de 10.000 sin urgencia da MEDIUM; por debajo da LOW.

- **5 puntos:** Demuestra 999,99 / 1.000 / 9.999,99 / 10.000 y urgente con importe bajo.

## Servicio y explicación · 15 puntos

Evidencia: classify, classify_all y ejemplo.


- **5 puntos:** Recibe dependencias y delega categoría y prioridad.

- **5 puntos:** Conserva identificador, orden y número de entradas.

- **5 puntos:** Cada predicción incluye una explicación coherente con sus campos.

## Exportación y CLI · 10 puntos

Evidencia: comando y JSON resultante.


- **5 puntos:** CLI procesa los tres registros desde las rutas indicadas.

- **5 puntos:** JSON UTF-8 válido con todos los campos y carpeta de salida creada.

## Pruebas y casos negativos · 10 puntos

Evidencia: salida real de pytest y tests añadidos.


- **5 puntos:** La suite proporcionada pasa sin desactivar aserciones.

- **5 puntos:** Aporta evidencia de límites y del rechazo de urgent inválido.

## Comprensión y entrega · 10 puntos

Evidencia: EVIDENCIAS.md y explicación breve.


- **4 puntos:** Explica categoría frente a prioridad y una invariante.

- **3 puntos:** Registra comandos, resultados reales y ayuda consultada.

- **3 puntos:** Declara datos sintéticos, limitación y decisión humana.

## Errores críticos y tratamiento

| Hallazgo demostrado | Consecuencia |

|---|---|

| Datos reales, secretos o acciones bancarias materiales | Entrega pendiente de saneamiento; conservar puntuación académica provisional sin emitir resultado final. |

| JSON no reproducible o CLI que no procesa el dataset | Exportación/CLI puntúa solo lo demostrado; no anula otros criterios. |

## Hoja de corrección

| Área/subcriterio | Puntos concedidos | Evidencia: archivo, prueba o ejecución | Mejora necesaria |
|---|---:|---|---|
| Copiar una fila por subcriterio | 0 | Pendiente de corregir | Indicar comportamiento concreto |

Puntuación bruta: __/100. Límites críticos aplicados y motivo: __. Nota final: __/100. Una evidencia lograda: __. Próxima acción y comprobación: __.

## Ejemplo de aplicación

Una entrega obtiene 78 puntos en subcriterios demostrados. Si no hay error crítico, su nota es 78/100. Si corresponde un máximo de 60, su nota es min(78,60) = 60/100. Un test que no existe no prueba el comportamiento; puede sustituirse por una demostración reproducible cuando el subcriterio no exija un test concreto.
