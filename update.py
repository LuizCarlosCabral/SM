import requests
import json
import os
from github import Github, Auth

# === 1. Buscar dados da API ===
url = "https://integra.softmarketing.com.br/dbdiagnosticos/metricas_sac_assessoria"
print("🔄 Buscando dados da API...")
response = requests.get(url)
response.raise_for_status()
data = response.json()
print(f"✅ Dados recebidos: {len(data)} registros")

# === 2. Salvar localmente (para commit) ===
file_path = "dados.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
print("💾 Arquivo 'dados.json' atualizado localmente")

# === 3. Conectar ao GitHub ===
token = os.getenv("MY_GITHUB_TOKEN")
if not token:
    raise ValueError("❌ Token não encontrado. Verifique se MEU_TOKEN foi definido.")

auth=Auth.Token(token)
repo_name = "LuizCarlosCabral/SM"
repo = g.get_repo(repo_name)

# === 4. Atualizar o arquivo no repositório ===
try:
    contents = repo.get_contents(file_path)
    repo.update_file(
        path=contents.path,
        message="🔄 Atualizando JSON com dados da API",
        content=json.dumps(data, indent=4, ensure_ascii=False),
        sha=contents.sha
    )
    print("✅ Arquivo atualizado com sucesso no GitHub!")
except Exception as e:
    print(f"⚠️ Erro ao atualizar o arquivo: {e}")
