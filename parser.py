class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        ast = []

        for token in self.tokens:
            token_type = token[0]
            token_value = token[1]

            if token_type == "INPUT":
                ast.append(("INPUT", token_value))

            elif token_type == "PRINT":
                ast.append(("PRINT", token_value))

            elif token_type == "QUERY":
                ast.append(("QUERY", token_value))

            elif token_type == "STRING":
                ast.append(("STRING", token_value))

            elif token_type == "ARRAY":
                ast.append(("ARRAY", token_value))

            elif token_type == "POINTER":
                ast.append(("POINTER", token_value))

            elif token_type == "SET":
                ast.append(("SET", token_value))

        return ast