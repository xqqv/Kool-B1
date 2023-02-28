def kool() -> tuple:
    opilased = [
        {"nimi": "Mari", "puudumised": 5},
        {"nimi": "Jüri", "puudumised": 8},
        {"nimi": "Kati", "puudumised": 12},
        {"nimi": "Mati", "puudumised": 3},
        {"nimi": "Toomas", "puudumised": 10},
        {"nimi": "Liisa", "puudumised": 2},
        {"nimi": "Kalle", "puudumised": 20},
        {"nimi": "Tõnu", "puudumised": 6},
        {"nimi": "Ago", "puudumised": 15},
        {"nimi": "Kadri", "puudumised": 4},
        {"nimi": "Eva", "puudumised": 11},
        {"nimi": "Peeter", "puudumised": 7},
        {"nimi": "Mare", "puudumised": 1},
        {"nimi": "Andres", "puudumised": 18},
        {"nimi": "Juhan", "puudumised": 9},
        {"nimi": "Kristiina", "puudumised": 13},
        {"nimi": "Mihkel", "puudumised": 14},
        {"nimi": "Kairi", "puudumised": 17},
        {"nimi": "Kaspar", "puudumised": 16},
        {"nimi": "Tiina", "puudumised": 19},
    ]
    puudumised = [opilane["puudumised"] for opilane in opilased]

    return opilased, puudumised

