 
import os

# Dateien/Module und ihre erwartete Kernel-Referenz
files = [
    ("modules/llm.md", "../language-kernel.yaml"),
    ("modules/rights-guardian.yaml", "../language-kernel.yaml"),
    ("audit/logbook.md", "../language-kernel.yaml"),
    ("tests/test_health.md", "../language-kernel.yaml"),
]

results = []

def check_file_kernel(path, kernel_ref):
    if not os.path.exists(path):
        return f"[ERROR] {path} fehlt"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        if f"kernel: {kernel_ref}" in content or f"kernel: {kernel_ref.replace('/', '\\')}" in content:
            return f"[OK] {path}: Kernelverbindung korrekt"
        else:
            return f"[FEHLER] {path}: Kernelverbindung fehlt oder falsch"

# Check Hauptkernel
if os.path.exists("language-kernel.yaml"):
    results.append("[OK] Kern existiert")
else:
    results.append("[ERROR] Kern fehlt!")

# Check alle Module, Logs, Tests
for file, kernel in files:
    results.append(check_file_kernel(file, kernel))

# Ausgabe & Logging
with open("audit/log_kernelcheck.log", "w", encoding="utf-8") as log:
    for line in results:
        print(line)
        log.write(line + "\n")
