from functions.run_python_file import run_python_file


def run_tests():
    print("=== Testing run_python_file ===")

    # Test 1: Run main.py (Usage instructions)
    print("\n1. Running 'main.py' (No args):")
    print(run_python_file("calculator", "main.py"))

    # Test 2: Run main.py with calculation
    print("\n2. Running 'main.py' with ['3 + 5']:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    # Test 3: Run tests.py (Should pass)
    print("\n3. Running 'tests.py':")
    print(run_python_file("calculator", "tests.py"))

    # Test 4: Security Violation (Relative path)
    print("\n4. Running '../main.py' (Should Error):")
    print(run_python_file("calculator", "../main.py"))

    # Test 5: Non-existent file
    print("\n5. Running 'nonexistent.py' (Should Error):")
    print(run_python_file("calculator", "nonexistent.py"))

    # Test 6: Wrong file type
    print("\n6. Running 'lorem.txt' (Should Error):")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    run_tests()
