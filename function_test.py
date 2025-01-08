def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
# Testes para a função eh_primo
testes = [2, 3, 4, 5, 10, 13, 17, 19, 23, 24, 29, 31]

for numero in testes:
    print(f"{numero} é primo: {eh_primo(numero)}")
