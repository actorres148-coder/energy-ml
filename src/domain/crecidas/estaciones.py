"""src/domain/crecidas/estaciones.py — Niveles oficiales de Prefectura Naval para Tigre (río Luján).

Fuente: reporte "Registro del estado de los ríos" de Prefectura Naval Argentina
(https://contenidosweb.prefecturanaval.gob.ar/alturas/pdf.php), confirmado también en la API
del INA (estación Tigre, id_externo 430). Alturas en metros sobre el cero de la escala de Tigre.
"""

ALERTA_TIGRE_M: float = 3.30
EVACUACION_TIGRE_M: float = 3.80
AGUAS_BAJAS_TIGRE_M: float = 0.30
