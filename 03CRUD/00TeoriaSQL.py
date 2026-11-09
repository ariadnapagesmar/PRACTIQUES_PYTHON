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


# SUBCONSULTES

# Una subconsulta no és res més que una consulta SQL dins d'una altra consulta SQL.
# Imagina que necessites buscar una dada, però per trobar-la primer necessites
# calcular una altra cosa prèvia. En comptes de fer dues peticions separades des
# del teu programa en Python, li dius a la base de dades que ho resolgui tot d'un sol cop.
# La subconsulta s'executa sempre primer, tancada entre parèntesis (), i el seu resultat
# s'utilitza com a valor o filtre per a la consulta principal (query externa).

# On s'acostumen a utilitzar? (Els 3 casos pràctics principals)

# 1. Dins de la clàusula WHERE (Comparar amb un valor calculat)
# És el cas més habitual. Imagina que vols saber quins vehicles tenen un quilometratge
# superior a la mitjana de tota la flota. No saps quin nombre és la mitjana, així
# que deixes que la subconsulta ho calculi:

SELECT MARCA, MODEL, QUILOMETRATGE
FROM VEHICLES
WHERE QUILOMETRATGE > (SELECT AVG(QUILOMETRATGE) FROM VEHICLES);
# Què passa aquí? Primer s'executa el SELECT AVG(...) (la subconsulta) i després la
# consulta principal filtra els cotxes que superen aquest nombre.

# 2. Amb l'operador IN (Filtrar a partir d'una llista d'IDs)
# Molt útil quan vols buscar registres que coincideixen amb un grup de dades d'una
# altra taula. Per exemple, vols saber el nom de tots els conductors que han fet
# algun manteniment o reserva (o que han fet una reserva d'un cotxe concret):

SELECT NOM
FROM CONDUCTORS
WHERE CONDUCTOR_ID IN (
    SELECT CONDUCTOR_ID
    FROM RESERVES
    WHERE ESTAT_RESERVA = 'ACTIVA'
);
# Què passa aquí? La subconsulta treu una llista d'IDs de conductors amb reserves
# actives, i el IN selecciona els conductors de la taula principal que estan
# en aquesta llista.

# Regla d'or de les subconsultes:
# Si la subconsulta retorna un sol valor (com un MAX(), un MIN() o un AVG()),
# pots fer servir operadors normals com >, <, = o <>.
# Si la subconsulta retorna múltiples files (una llista de valors), has de fer
# servir operadors de conjunts com IN, ANY o ALL.

# Resum de conceptes clau a recordar:

# cursor.execute(sql, valors): Executa l'ordre SQL protegit contra injeccions.
# connexio.commit(): Obligatori a INSERT, UPDATE i DELETE. Si te n'oblides,
# Python executarà el codi però la base de dades no desarà els canvis.
# cursor.fetchall(): S'utilitza només al SELECT per recollir les dades a
# una llista de tupla a Python.
