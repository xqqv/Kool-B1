from typing import list


def show_n_best_students(opilased: list[dict]) -> None:
    n = int(input("Sisesta n: "))
    n_parimat = sorted(opilased, key=lambda opilane: opilane["puudumised"])[:n]
    print(f"{n} parimat õpilast:")
    for i, opilane in enumerate(n_parimat):
        print(f"{i+1}. {opilane['nimi']} ({opilane['puudumised']} puudumist)")


def sort_students_by_absences(opilased: list[dict], puudumised: list[int]) -> None:
    sorteering = sorted(zip(opilased, puudumised), key=lambda paar: paar[1])
    print("Õpilased järjestatud puudumiste arvu järgi:")
    for i, paar in enumerate(sorteering):
        print(f"{i+1}. {paar[0]['nimi']} ({paar[1]} puudum)")
