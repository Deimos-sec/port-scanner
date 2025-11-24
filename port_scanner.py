import socket

def scan_port(ip, port, timeout=0.5):
    """Devuelve True si el puerto está abierto."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0


def main():
    print("=== Simple Port Scanner ===")
    ip = input("Ingrese la dirección IP o dominio a escanear: ")

    print("\nSeleccione el rango de puertos:")
    start = int(input("Puerto inicial: "))
    end = int(input("Puerto final: "))

    print(f"\nEscaneando {ip} desde el puerto {start} al {end}...\n")

    for port in range(start, end + 1):
        if scan_port(ip, port):
            print(f"[+] Puerto abierto: {port}")

    print("\n--- Escaneo completado ---")


if __name__ == "__main__":
    main()

