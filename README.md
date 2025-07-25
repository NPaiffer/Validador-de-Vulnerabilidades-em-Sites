
# 🔐 Validador de Vulnerabilidades em Sites

Esse é um projeto bem simples em Python para verificar se um site possui os principais **headers de segurança HTTP**. Ele ajuda a identificar configurações básicas de proteção que deveriam estar presentes nas respostas dos servidores.

---

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/vulnerability-checker.git
cd vulnerability-checker
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o script
```bash
python checker.py
```

### 4. Digite a URL do site
Informe no terminal uma URL no formato:
```
https://exemplo.com
```

---

## 🔍 Headers verificados

| Header                    | Função                                                                  |
|---------------------------|-------------------------------------------------------------------------|
| Content-Security-Policy   | Evita execução de scripts maliciosos                                   |
| X-Content-Type-Options    | Evita o navegador interpretar tipos incorretos de conteúdo              |
| X-Frame-Options           | Protege contra ataques de clickjacking                                  |
| Strict-Transport-Security | Garante o uso de HTTPS em conexões futuras                             |
| Referrer-Policy           | Controla o que é enviado no header "Referer"                            |
| Permissions-Policy        | Restringe uso de APIs sensíveis (microfone, câmera, localização, etc.)  |

---

## Exemplo de saída

```
🔎 Verificando: https://exemplo.com

[✅] Content-Security-Policy: Encontrado
[❌] X-Frame-Options: Não encontrado  ⚠️ (Protege contra clickjacking)
[✅] Referrer-Policy: Encontrado
[❌] Strict-Transport-Security: Não encontrado  ⚠️ (Garante o uso de HTTPS)
```

---

## 📚 Tecnologias Usadas

- Python 3.x
- Biblioteca [requests](https://pypi.org/project/requests/)

---
