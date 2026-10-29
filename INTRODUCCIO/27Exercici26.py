# 6. Filtratge avançat d'empleats (Llistes per comprensió + Strings)

# Partint d'una llista de noms d'empleats amb majúscules desordenades i espais sobrants:
# ["  anna garcia ", "PERU martínez ", "  joan   "] (nota: neteja-les amb .strip()
# i .title()). Suposant que tens una llista paral·lela de sous, utilitza una llista
# per comprensió per generar un nou format de text només per a aquells empleats que
# guanyin més d'un determinat llindar, mostrant el seu nom net i majúscules invertides.

# CREEM DUES LLISTES PARAL·LELES: UNA AMB NOMS MAL ESCRITS I L'ALTRE AMB SOUS
noms = ["  anna garcÍa ", "PERE martínez ", "  juan PaMpIn", " arI pagÈS     "]
sous = [1900, 1200, 2500, 2100]

# CREEM UNA LLISTA PER COMPRENSIÓ, ARREGLANT ELS NOMS I FILTRANT ELS SOUS DE MÉS DE 1500
noms_sous = [(nom.strip().title(), sou) for nom, sou in zip(noms, sous) if sou > 1500]

for nom, sou in noms_sous:
    print(f"{nom} --> {sou}")


