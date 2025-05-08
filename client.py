import json
import subprocess

# A pergunta para o MCP
payload = {
    "question": "Repita: testando com MCP",
    "tools": ["echo"]
}

# Inicia o MCP no modo stdio e envia a pergunta
proc = subprocess.Popen(
    ["python", "main.py"],  # isso roda o MCP no mesmo processo (alternativa a rodar manualmente)
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Envia o JSON e espera resposta
stdout, stderr = proc.communicate(input=json.dumps(payload))

print("🟢 RESPOSTA:")
print(stdout.strip())

if stderr:
    print("⚠️ STDERR:")
    print(stderr.strip())
