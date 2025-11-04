import requests
import json
from github import Github

# Busca dados
url = "https://integra.softmarketing.com.br/dbdiagnosticos/metricas_sac_assessoria"
response = requests.get(url)
data = response.json()

# Atualiza o JSON
with open("dados.json", "w", encoding="utf-8") as f:json.dump(data, f, indent=4, ensure_ascii=False)

# Envia atualização para o GitHub
token = "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"
repo_name = "LuizCarlosCabral/SM"
file_path = "dados.json"
g = Github(token)
repo = g.get_repo(repo_name)

# Pega arquivo
contents = repo.get_contents(file_path)

# Atualiza arquivo e dá feedback
repo.update_file(contents.path, "Atualizando JSON com dados da API", json.dumps(data, indent=4, ensure_ascii=False), contents.sha)
print("✅ JSON atualizado no GitHub!")
