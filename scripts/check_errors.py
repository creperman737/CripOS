"""CripOS loyihasidagi barcha Python fayllarni tekshirish skripti."""
import os
import ast
import sys

def check_python_files():
    errors = []
    warnings = []
    py_files = []
    
    for root, dirs, files in os.walk('.'):
        # Skip build and __pycache__ directories
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'build', 'node_modules']]
        for f in files:
            if f.endswith('.py'):
                py_files.append(os.path.join(root, f))
    
    print(f"Jami Python fayllar: {len(py_files)}")
    
    for filepath in py_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                ast.parse(content)
            except SyntaxError as e:
                errors.append(f"SYNTAX ERROR: {filepath}:{e.lineno}: {e.msg}")
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()
                try:
                    ast.parse(content)
                except SyntaxError as e:
                    errors.append(f"SYNTAX ERROR: {filepath}:{e.lineno}: {e.msg}")
            except Exception as e:
                errors.append(f"READ ERROR: {filepath}: {e}")
        except Exception as e:
            errors.append(f"ERROR: {filepath}: {e}")
    
    if errors:
        print("\n=== XATOLAR TOPILDI ===")
        for err in errors:
            print(err)
    else:
        print("\n=== SINTaksis XATOLAR YO'Q ===")
    
    return len(errors)

if __name__ == '__main__':
    count = check_python_files()
    sys.exit(1 if count > 0 else 0)