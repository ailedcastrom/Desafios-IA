#Mi intento
palindro = input ("Ingresa una palabra: ")
if palindro == palindro[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#Con ayuda IA
import re
import unicodedata


def normalize_text(s: str) -> str:
    """Normaliza la cadena: quita acentos, elimina caracteres no alfanuméricos y pasa a minúsculas."""
    # Normalizar (descomponer caracteres con acento)
    s = unicodedata.normalize('NFKD', s)
    # Eliminar marcas diacríticas (acentos)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    # Mantener sólo letras y números
    s = re.sub(r'[^A-Za-z0-9]', '', s)
    return s.lower()


def is_palindrome(s: str) -> bool:
    """Devuelve True si s es palíndromo (ignorando puntuación y mayúsculas)."""
    cleaned = normalize_text(s)
    return cleaned == cleaned[::-1]


def main() -> None:
    s = input("Ingresa una palabra o frase: ")
    if not s or not s.strip():
        print("No ingresaste texto.")
        return

    if is_palindrome(s):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


if __name__ == '__main__':
    main()
