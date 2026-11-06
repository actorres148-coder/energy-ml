"""src/domain/crecidas/modelos.py — Entidades del dominio de crecidas (sin dependencias externas)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Escenario(str, Enum):
    """Escenario de nivel de río, de menor a mayor riesgo."""

    NORMAL = "normal"
    VIGILANCIA = "vigilancia"
    ALERTA = "alerta"
    CRECIDA = "crecida"


@dataclass(frozen=True)
class Umbrales:
    """Niveles de río (en metros sobre el cero de la escala) que delimitan los escenarios.

    Invariante: vigilancia < alerta < crecida.
    """

    vigilancia_m: float
    alerta_m: float
    crecida_m: float

    def __post_init__(self) -> None:
        if not (self.vigilancia_m < self.alerta_m < self.crecida_m):
            raise ValueError(
                "Los umbrales deben cumplir vigilancia < alerta < crecida "
                f"(recibido: {self.vigilancia_m}, {self.alerta_m}, {self.crecida_m})"
            )


@dataclass(frozen=True)
class AlertaTemprana:
    """Alerta emitida cuando el nivel previsto alcanza alerta o crecida.

    Guarda los datos que la dispararon para que sea auditable.
    """

    escenario: Escenario
    nivel_previsto_m: float
    horizonte_horas: int
    umbral_disparado_m: float


@dataclass(frozen=True)
class NivelRio:
    """Una observación de altura hidrométrica (metros) en un instante dado."""

    instante: datetime
    nivel_m: float
