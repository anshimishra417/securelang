from lexer import Lexer
from parser import Parser
from security_analyzer import SecurityAnalyzer
from code_generator import CodeGenerator

def main():
    with open("sample.sec", "r") as file:
        code = file.read()

    print("\n--- SecureLang Input ---\n")
    print(code)

    # Step 1: Lexical Analysis
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    # Step 2: Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # Step 3: Security Analysis
    analyzer = SecurityAnalyzer(ast)
    warnings = analyzer.analyze()

    print("\n--- Security Warnings ---")
    for w in warnings:
        print("⚠️", w)

    # Step 4: Code Generation
    generator = CodeGenerator(ast)
    output_code = generator.generate()

    print("\n--- Generated Safe Python Code ---\n")
    print(output_code)

    with open("output.py", "w") as f:
        f.write(output_code)

if __name__ == "__main__":
    main()