import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "Evita execução de scripts maliciosos",
    "X-Content-Type-Options": "Evita sniffing de conteúdo",
    "X-Frame-Options": "Evita clickjacking",
    "Strict-Transport-Security": "Força o uso de HTTPS",
    "Referrer-Policy": "Controla o que é enviado no header Referer",
    "Permissions-Policy": "Restringe uso de APIs como câmera, microfone, etc."
}

def verificar_headers(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"\n🔎 Verificando: {url}\n")
        
        for header, descricao in SECURITY_HEADERS.items():
            if header in response.headers:
                print(f"[✅] {header}: Encontrado")
            else:
                print(f"[❌] {header}: Não encontrado  ⚠️ ({descricao})")

    except requests.exceptions.RequestException as e:
        print(f"\n Erro ao acessar o site: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do site (ex: https://exemplo.com): ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    verificar_headers(url)
