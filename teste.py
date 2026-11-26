#Aqui vou desenvolver meu código de teste para a revisão.

# Lista (array) global para armazenar os dicionários com os dados dos motores
motores = []
proximo_id = 1


def cadastrar_motor():
    global proximo_id
    print("\n--- CADASTRAR NOVO MOTOR ---")
    modelo = input("Modelo/Código do motor: ").strip()
    fabricante = input("Fabricante (ex: WEG, Siemens): ").strip()

    try:
        potencia = float(input("Potência (em CV): "))
        tensao = int(input("Tensão nominal (em Volts, ex: 220, 380): "))
        rpm = int(input("Rotação (RPM): "))
    except ValueError:
        print("\n[ERRO] Potência, tensão e RPM devem ser valores numéricos!")
        return

    motor = {
        "id": proximo_id,
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia_cv": potencia,
        "tensao_v": tensao,
        "rpm": rpm,
    }

    motores.append(motor)
    proximo_id += 1
    print(f"\n[SUCESSO] Motor '{modelo}' cadastrado com ID {motor['id']}!")


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for m in motores:
        print(
            f"ID: {m['id']} | Modelo: {m['modelo']} | Fabricante: {m['fabricante']} | "
            f"Potência: {m['potencia_cv']} CV | Tensão: {m['tensao_v']}V | {m['rpm']} RPM"
        )


def buscar_motor():
    print("\n--- BUSCAR MOTOR ---")
    termo = input("Digite o modelo ou fabricante para buscar: ").strip().lower()

    encontrados = [
        m
        for m in motores
        if termo in m["modelo"].lower() or termo in m["fabricante"].lower()
    ]

    if not encontrados:
        print("Nenhum motor encontrado com esse termo.")
        return

    print(f"\nForam encontrados {len(encontrados)} motor(es):")
    for m in encontrados:
        print(
            f"ID: {m['id']} | Modelo: {m['modelo']} | Fabricante: {m['fabricante']} | "
            f"Potência: {m['potencia_cv']} CV | Tensão: {m['tensao_v']}V | {m['rpm']} RPM"
        )


def excluir_motor():
    listar_motores()
    if not motores:
        return

    try:
        id_excluir = int(input("\nDigite o ID do motor que deseja excluir: "))
    except ValueError:
        print("[ERRO] Digite um ID numérico válido.")
        return

    for i, m in enumerate(motores):
        if m["id"] == id_excluir:
            removido = motores.pop(i)
            print(
                f"\n[SUCESSO] Motor '{removido['modelo']}' (ID {id_excluir}) removido!"
            )
            return

    print(f"\n[AVISO] Nenhum motor encontrado com o ID {id_excluir}.")


def menu():
    while True:
        print("\n" + "=" * 35)
        print("   SISTEMA DE CADASTRO DE MOTORES")
        print("=" * 35)
        print("1. Cadastrar motor")
        print("2. Listar todos os motores")
        print("3. Buscar motor")
        print("4. Excluir motor")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            excluir_motor()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\n[ERRO] Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()