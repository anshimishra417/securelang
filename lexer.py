class Lexer:
    def __init__(self, code):
        self.code = code

    def tokenize(self):
        tokens = []
        lines = self.code.splitlines()

        for line in lines:
            line = line.strip()

            if line.startswith("INPUT"):
                value = line.replace("INPUT", "").strip()
                tokens.append(("INPUT", value))

            elif line.startswith("PRINT"):
                value = line.replace("PRINT", "").strip()
                tokens.append(("PRINT", value))

            elif line.startswith("QUERY"):
                value = line.replace("QUERY", "").strip()
                tokens.append(("QUERY", value))

            elif line.startswith("STRING"):
                value = line.replace("STRING", "").strip()
                tokens.append(("STRING", value))

            elif line.startswith("ARRAY"):
                value = line.replace("ARRAY", "").strip()
                tokens.append(("ARRAY", value))

            elif line.startswith("POINTER"):
                value = line.replace("POINTER", "").strip()
                tokens.append(("POINTER", value))

            elif line.startswith("SET"):
                value = line.replace("SET", "").strip()
                tokens.append(("SET", value))

        return tokens