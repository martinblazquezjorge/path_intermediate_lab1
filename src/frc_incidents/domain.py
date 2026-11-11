"""Entidades de dominio e invariantes del Lab 1.

Una entidad de dominio representa información relevante para el negocio. Las
validaciones viven aquí para que se apliquen igual desde el CSV, el CLI o un
test. En un sistema bancario real, esta capa evita que un dato imposible avance
hasta una clasificación o un informe operativo.
"""

from dataclasses import dataclass


class DomainValidationError(ValueError):
    """Indica que un dato de dominio no cumple las reglas mínimas."""


@dataclass(frozen=True)
class Incident:
    """Incidencia FRC validada que puede entrar en el clasificador.

    ``frozen=True`` impide cambiar sus campos después de crearla. Así, la misma
    incidencia no puede tener un importe al clasificar y otro al priorizar.
    """

    incident_id: str
    description: str
    amount_eur: float
    urgent: bool

    def __post_init__(self) -> None:
        """Comprueba las reglas que siempre deben cumplir las incidencias."""
        # ``strip`` elimina espacios: un identificador formado solo por espacios
        # también se considera vacío.
        raise NotImplementedError("TODO: completar Incident.__post_init__")


@dataclass(frozen=True)
class Prediction:
    """Salida explicada que se entrega para revisión humana."""

    incident_id: str
    category: str
    confidence: float
    priority: str
    explanation: str

    def __post_init__(self) -> None:
        """Evita probabilidades y prioridades fuera del contrato."""
        raise NotImplementedError("TODO: completar Prediction.__post_init__")
