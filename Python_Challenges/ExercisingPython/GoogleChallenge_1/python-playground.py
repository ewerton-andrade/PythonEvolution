import random
from choice_string import STRING

alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}


# Test case 1 (F length equal to 1)

# generate S string function
def gen_s_string(s_max_length: int) -> str:
    """
    :param s_max_length: max length of the return string, not necessarily the same, it's random.
    :return: the random string of random size between 0 until s_max_length
    """
    s_number_elements = [element for element in range(s_max_length)]  # Array de tamanhos da string S
    s_random_elements_number = random.choice(s_number_elements)  # numero de letras aleatorio da string S
    _s = ""
    for i in range(0, s_random_elements_number):
        alphabet_random_choice = random.choice(list(alphabet))
        _s += alphabet_random_choice
    return _s


# generate F string function
def gen_f_string(f_max_length: int, _alphabet: dict) -> str:
    """
    :param f_max_length: _f string max length generated
    :param _alphabet: alphabet dict, example: {"a":1, "b":2,... "z":26}
    :return: random _f string with the max length
    """
    _f = ""
    for i in range(0, f_max_length):
        _f += random.choice(list(_alphabet))
    return _f


# # Test set 1 simulation (F size equal to one)
# S = gen_s_string(1000000)
# F = gen_f_string(1, alphabet)
#
# #verificar a string F: tamanho e quais as letras contidas
# print("-"*50)
# print(f"======>>>>>> F string: {F}")
# print("-"*50)

# print(f"======>>>>>> S string: {S}")
# print("-"*50)

f = "vf"
s = STRING


# metodo para verificar o tamanho da string F
def get_f_length(_f: str) -> int:
    return len(_f)


def is_in_f_string(_letter: str, _f_string: str) -> bool:
    return _letter in _f_string


#   preciso contar os casos e numero de operacoes: conta o numero operacoes enquanto o valor que
# retorna de is_in_f_string for falso (exceto logo apos um valor True, o valor False que vier logo
# em seguida de um valor True nao pode ser contabilizado como uma operacao, pois, e apenas a constatacao
# de que aquele valor nao esta na string F)
def count_operations_and_cases():
    # Se o parametro recebido for True ele retorna
# retorna o numero de operacoes e casos apenas se o valor recebido no parametro for True,
    # se o parametro recebido for falso, ele conta um numero de operacao

def print_case(_is_equal: bool, _case_number: int, _operation_number: int):
    print(f"Case #{_case_number}: {_operation_number}")


for i in s:
    print("-" * 50)
    print(f"Is {i} in {f}?")
    print("Processing...")
    print(f"...{i in f}")

# for i in S:
#     print
# Analisar cada letra da string S para ver se ela e igual a letra que esta na string F
# for i in F:
#     for j in S:
# se j for igual a i entao a contagem de tentativas e igual a zero e passa para a segunda contagem

#    Se F tiver mais de uma letra, cada letra em S deve ser uma das letras contidas em F.
# Exemplo: Se F = "ou" e S = "etjo"  a letra "e" podera ser "o" ou "u" assim como a letra "t" podera
# ser a letra "o" ou a letra "u".
