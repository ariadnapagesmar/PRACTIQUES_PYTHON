# 1. SELECT (Llegir / Consultar dades)

# Per consultar informació de les taules. Pots filtrar, ordenar i combinar dades.

# Bàsic: SELECT * FROM VEHICLES; (Tanca tots els camps de la taula).
# Amb filtre (WHERE): SELECT * FROM VEHICLES WHERE ESTAT = 'DISPONIBLE';
# Ordenat (ORDER BY): SELECT * FROM VEHICLES ORDER BY QUILOMETRATGE DESC; (De més a menys km).
# Unió de taules (JOIN):

SELECT NOM, MARCA, DATA_INICI
FROM RESERVES
JOIN CONDUCTOR USING (CONDUCTOR_ID)
JOIN VEHICLES USING (VEHICLE_ID);

# 2. INSERT (Crear / Afegir dades)
# Per introduir nous registres a una taula.
# Sintaxi:

INSERT INTO CONDUCTOR (NOM, CARNET, TELEFON)
VALUES ('Nom Cognom', '12345678X', '600112233');

# 3. UPDATE (Actualitzar / Modificar dades)
# Per canviar dades que ja existeixen (compte de no oblidar el WHERE o
# actualitzaràs tota la taula!).
# Sintaxi:

UPDATE VEHICLES
SET ESTAT = 'OCUPAT', QUILOMETRATGE = 16000
WHERE MATRICULA = '1234ABC';

# 4. DELETE (Esborrar dades)
# Per eliminar registres d'una taula.
# Sintaxi:

DELETE FROM RESERVES
WHERE ESTAT_RESERVA = 'FINALITZADA';

# Funcions d'agregació útils:
# Comptar registres: SELECT COUNT(*) FROM VEHICLES;
# Màxim / Mínim: SELECT MAX(QUILOMETRATGE) FROM VEHICLES;
# Mitjana: SELECT AVG(COST) FROM MANTENIMENTS;

# Altres funcions importants:

# ORDER BY...ASC/DESC: ordena alfabèticament o numèricament, tu li dius si vols en
# ordre ascendent (ASC) o descendent (DESC)

# GROUP BY (Agrupar dades)
# El GROUP BY s'utilitza juntament amb les funcions d'agregació (COUNT, SUM, AVG, etc.)
# per agrupar files que tenen un valor en comú i calcular alguna cosa per a cada grup.
# Exemple pràctic: Vols saber quants vehicles tens de cada estat (quants estan
# disponibles, quants ocupats i quants al taller):

SELECT ESTAT, COUNT(*) AS TOTAL_VEHICLES
FROM VEHICLES
GROUP BY ESTAT;

# Un altre exemple: Calcular quin és el cost total dels manteniments per a cada
# vehicle (agrupant per VEHICLE_ID):

SELECT VEHICLE_ID, SUM(COST) AS COST_TOTAL
FROM MANTENIMENTS
GROUP BY VEHICLE_ID;

# HAVING (Filtrar grups)
# Molts cops la gent es pregunta: per què no puc fer servir un WHERE després d'un GROUP BY?
# El WHERE filtra les dades abans d'agrupar.
# El HAVING serveix per filtrar després d'haver fet el GROUP BY (especialment útil
# per filtrar resultats de funcions com COUNT o SUM).
# Exemple pràctic: Mostrar només aquells vehicles que hagin acumulat un cost total
# de manteniment superior a 200 euros:

SELECT VEHICLE_ID, SUM(COST) AS COST_TOTAL
FROM MANTENIMENTS
GROUP BY VEHICLE_ID
HAVING SUM(COST) > 200;

# LIMIT i OFFSET (Paginació)
# Quan tens milers de registres, no vols mostrar-los tots de golpe. El LIMIT et
# permet tallar el nombre de resultats, i l' OFFSET serveix per saltar-te un
# nombre de files (ideal per fer paginacions a les teves futures rutes de FastAPI).
# Exemple pràctic: Trobar el vehicle amb més quilometratge de tota la flota
# (ordenant de més a menys i agafant només el primer):

SELECT *
FROM VEHICLES
ORDER BY QUILOMETRATGE DESC
LIMIT 1;

# Operadors lògics i filtres avançats (LIKE i IN)
# LIKE (Per a cerques de text): Molt útil si vols buscar conductors el nom dels
# quals contingui una lletra o comenci per alguna cosa (utilitzant el comodí %).
SELECT *
FROM CONDUCTOR
WHERE NOM LIKE '%Ariadna%';

# IN (Per comprovar múltiples valors): Evita haver de fer molts OR.
SELECT *
FROM VEHICLES
WHERE ESTAT IN ('DISPONIBLE', 'EN TALLER');

# CASE WHEN (Condicionals dins de SQL)
# És com un if/else directament a la consulta SQL. Et permet transformar com
# es mostren les dades al resultat.
# Exemple pràctic: Imagina que vols mostrar un missatge personalitzat segons
# els quilometratge del vehicle:

SELECT MARCA, MODEL, QUILOMETRATGE,
  CASE
    WHEN QUILOMETRATGE < 20000 THEN 'Seminou'
    WHEN QUILOMETRATGE BETWEEN 20000 AND 40000 THEN 'Mitjà ús'
    ELSE 'Molts quilòmetres'
  END AS TIPUS_KM
FROM VEHICLES;