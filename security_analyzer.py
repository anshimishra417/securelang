class SecurityAnalyzer:
    def __init__(self, ast):
        self.ast = ast

    def analyze(self):
        warnings = []

        for node in self.ast:

            # INPUT SECURITY
            if node[0] == "INPUT":

                if "password" in node[1].lower():
                    warnings.append(
                        "⚠️ Weak password handling detected!"
                    )

                if "admin" in node[1].lower():
                    warnings.append(
                        "⚠️ Admin field detected - privilege validation recommended!"
                    )

            # SQL SECURITY
            elif node[0] == "QUERY":

                query = node[1]

                if "+" in query:
                    warnings.append(
                        "⚠️ SQL Injection risk detected!"
                    )

                if "DROP" in query.upper():
                    warnings.append(
                        "⚠️ Dangerous SQL keyword detected: DROP"
                    )

                if "DELETE" in query.upper():
                    warnings.append(
                        "⚠️ DELETE operation detected - data loss risk!"
                    )

                if "UPDATE" in query.upper():
                    warnings.append(
                        "⚠️ UPDATE query detected - verify authorization!"
                    )

            # PRINT SECURITY
            elif node[0] == "PRINT":

                if "password" in node[1].lower():
                    warnings.append(
                        "⚠️ Sensitive data exposure risk!"
                    )

                if "token" in node[1].lower():
                    warnings.append(
                        "⚠️ Security token exposure risk!"
                    )

                if "secret" in node[1].lower():
                    warnings.append(
                        "⚠️ Secret key exposure risk!"
                    )

            # POINTER SECURITY
            elif node[0] == "POINTER":

                warnings.append(
                    "⚠️ Pointer usage detected - memory safety required!"
                )

            # SET SECURITY
            elif node[0] == "SET":

                value = node[1]

                if "eval" in value.lower():
                    warnings.append(
                        "⚠️ Dangerous function detected: eval()"
                    )

                if "exec" in value.lower():
                    warnings.append(
                        "⚠️ Dangerous function detected: exec()"
                    )

                if "http" in value.lower():
                    warnings.append(
                        "⚠️ External URL detected - validate source!"
                    )

        return warnings