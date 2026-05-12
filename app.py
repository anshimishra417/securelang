from flask import Flask, render_template, request

from lexer import Lexer
from parser import Parser
from security_analyzer import SecurityAnalyzer
from code_generator import CodeGenerator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    warnings = []
    output_code = ""
    score = 100
    security_level = "🟢 Safe"

    if request.method == "POST":

        code = request.form.get("code", "")

        # LEXER
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        # PARSER
        parser = Parser(tokens)
        ast = parser.parse()

        # SECURITY ANALYSIS
        analyzer = SecurityAnalyzer(ast)
        warnings = analyzer.analyze()

        # SECURITY SCORE
        score = 100

        for warning in warnings:

            # CRITICAL RISKS
            if "SQL Injection" in warning:
                score -= 40

            elif "Dangerous function" in warning:
                score -= 40

            elif "DROP" in warning:
                score -= 40

            # HIGH RISKS
            elif "Sensitive data" in warning:
                score -= 30

            elif "Secret key" in warning:
                score -= 30

            elif "DELETE" in warning:
                score -= 30

            # MEDIUM RISKS
            elif "Weak password" in warning:
                score -= 20

            elif "UPDATE" in warning:
                score -= 20

            elif "token" in warning.lower():
                score -= 20

            # LOW RISKS
            elif "Pointer usage" in warning:
                score -= 5

        # LIMIT SCORE
        if score < 0:
            score = 0

        if score > 100:
            score = 100

        # SECURITY LEVEL
        if score >= 75:
            security_level = "🟢 Safe"

        elif score >= 35:
            security_level = "🟡 Medium Risk"

        else:
            security_level = "🔴 High Risk"

        # CODE GENERATION
        generator = CodeGenerator(ast)
        output_code = generator.generate()

    return render_template(
        "index.html",
        warnings=warnings,
        output_code=output_code,
        score=score,
        security_level=security_level
    )


if __name__ == "__main__":
    app.run(debug=True)