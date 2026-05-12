class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        code_lines = []

        code_lines.append("import sqlite3")
        code_lines.append("")
        code_lines.append("conn = sqlite3.connect('test.db')")
        code_lines.append("cursor = conn.cursor()")
        code_lines.append("")

        for node in self.ast:

            # INPUT
            if node[0] == "INPUT":
                variable = node[1]

                code_lines.append(
                    f"{variable} = input('Enter {variable}: ').strip()"
                )

                code_lines.append(
                    f"if not {variable}.isalnum():"
                )

                code_lines.append(
                    "    print('Invalid input detected!')"
                )

            # STRING
            elif node[0] == "STRING":
                variable = node[1]
                code_lines.append(f"{variable} = ''")

            # ARRAY
            elif node[0] == "ARRAY":
                variable = node[1]
                code_lines.append(f"{variable} = []")

            # POINTER
            elif node[0] == "POINTER":
                variable = node[1]
                code_lines.append(
                    f"{variable} = None  # Pointer simulation"
                )

            # SET
            elif node[0] == "SET":
                value = node[1]

                parts = value.split("=")

                if len(parts) == 2:
                    var = parts[0].strip()
                    val = parts[1].strip()

                    code_lines.append(f"{var} = {val}")

            # QUERY
            elif node[0] == "QUERY":

                code_lines.append(
                    "cursor.execute('SELECT * FROM users WHERE name=?', (username,))"
                )

            # PRINT
            elif node[0] == "PRINT":
                value = node[1]

                if "password" in value.lower():
                    code_lines.append(
                        "print('Password is hidden for security reasons')"
                    )

                else:
                    code_lines.append(f"print({value})")

        code_lines.append("")
        code_lines.append("conn.commit()")
        code_lines.append("conn.close()")

        return "\n".join(code_lines)