# Cuaderno de trabajo — Pronóstico de ventas (Issue #2)

## Plan de 5 pasos

1. Conseguir los datos ✅
2. Mirar los datos ✅
3. Agrupar productos parecidos ⏳ (en curso)
4. Pronosticar las ventas y comparar
5. Sacar conclusiones

---

## Paso 1 — Conseguir los datos

- Fuente: Kaggle, "Store Item Demand Forecasting".
- Archivo: `datos/ventas/demanda.csv`.

## Paso 2 — Mirar los datos

**Columnas de la planilla:**

- `date` → el día
- `store` → la tienda
- `item` → el producto
- `sales` → cuántas unidades se vendieron

Ejemplo: el 2 de enero de 2013, la tienda 1 vendió 11 unidades del producto 1.

**Lo que descubrimos:**

- 913.001 renglones = 1 renglón de títulos + **913.000 registros**.
- Cada registro es: un día, en una tienda, de un producto.
- Fechas: desde el **1/1/2013** hasta el **31/12/2017** (5 años).
- **10 tiendas** y **50 productos** → 10 × 50 = **500 combinaciones**.
- 5 años = 1.826 días (2016 fue bisiesto).
- 500 × 1.826 = 913.000 → coincide: **no falta ningún día**. Los datos están completos.

**Comandos que usamos:**

- `head datos/ventas/demanda.csv` → ver los primeros renglones.
- `wc -l datos/ventas/demanda.csv` → contar renglones (no suma unidades).
- Python para ver la primera y última fecha, y contar tiendas y productos.

## Paso 3 — Agrupar productos parecidos (en curso)

**La idea:** para cada una de las 500 combinaciones (tienda + producto) armamos una **ficha** con:

- cuánto vende en promedio por día,
- cuánto cambia de un día a otro,
- qué días de la semana vende más.

Después la computadora junta las fichas parecidas en grupos (como ordenar un placard). Un producto que vende 50 por día y otro que vende 5 van en grupos distintos.

**Archivo:** `ventas/agrupar.py`

**Lo que hicimos:**

- Leímos la planilla con Python (`pandas`) y comprobamos que tiene 913.000 registros.
- Calculamos el **promedio de ventas por día** de cada tienda + producto, con `groupby` (parecido a una tabla dinámica de Excel).
- Ejemplo: la tienda 1 vende en promedio 20 unidades por día del producto 1, y 53 del producto 2.

- Agregamos el **desvío** (`std`): mide si un producto vende **parejo** o **variable**. Ejemplo del kiosco: A vende 10, 10, 10, 10 (parejo, fácil de adivinar); B vende 0, 20, 5, 15 (variable, difícil). Los dos promedian 10.
- Resultado: la tienda 1, producto 2 vende 53 por día con desvío 15 (el más variable de los 5 primeros; también el que más vende).
- Fichas de los primeros 5 productos de la tienda 1 (se calcularon las 500):

| Producto | Promedio por día | Desvío |
|---|---|---|
| 1 | 20 | 6,7 |
| 2 | 53 | 15,0 |
| 3 | 33 | 10,1 |
| 4 | 20 | 6,6 |
| 5 | 17 | 5,7 |

- Aprendimos a leer un error: `SyntaxError: '(' was never closed` en la línea 7 = faltaba cerrar un paréntesis.

**Cómo leer el resultado:** el número de tienda aparece una sola vez; los espacios vacíos debajo significan "sigue siendo la misma tienda" (como una celda combinada).

**Pendiente:** agregar a la ficha "días sin ventas" y "qué días de la semana vende más".

---

## Reglas importantes (para el paso 4)

**Fuga de datos = hacer trampa.** Para adivinar las ventas de un día solo se pueden usar datos de días **anteriores**.

Ejemplo del kiosco: para probar si adivino bien las ventas del miércoles, tapo el miércoles con la mano y miro solo lunes y martes. Después destapo y comparo.

Que los datos sean viejos no evita la trampa: igual hay que "tapar" los días que queremos adivinar.
