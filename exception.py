class InputUtils:
    @staticmethod
    def input_int(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Ingresa un número entero válido.")
    @staticmethod
    def input_float(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: Ingresa un número decimal válido.")