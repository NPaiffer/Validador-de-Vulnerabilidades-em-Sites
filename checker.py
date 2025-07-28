import requests
import json
import datetime
import ssl
import socket
from urllib.parse import urlparse
from datetime import timezone

SECURITY_HEADERS = {
    "Content-Security-Policy": "Evita execução de scripts maliciosos",
    "X-Content-Type-Options": "Evita sniffing de conteúdo",
    "X-Frame-Options": "Evita clickjacking",
    "Strict-Transport-Security": "Força o uso de HTTPS",
    "Referrer-Policy": "Controla envio do header Referer",
    "Permissions-Policy": "Restringe uso de APIs sensíveis"
}

class SecurityHeaderChecker:
    def __init__(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        self.url = url
        self.resultado = {}

    def verificar_headers(self):
        try:
            response = requests.get(self.url, timeout=10)
            for header, descricao in SECURITY_HEADERS.items():
                presente = header in response.headers
                self.resultado[header] = {
                    "presente": presente,
                    "descricao": descricao
                }
        except requests.RequestException as e:
            self.resultado["erro"] = str(e)

    def verificar_ssl_expiration(self):
        try:
            hostname = urlparse(self.url).netloc
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    expira_em = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    dias_restantes = (expira_em - datetime.datetime.now(timezone.utc)).days
                    self.resultado["certificado_ssl"] = {
                        "expira_em": expira_em.strftime('%Y-%m-%d'),
                        "dias_restantes": dias_restantes
                    }
        except Exception as e:
            self.resultado["certificado_ssl"] = {"erro": str(e)}

    def salvar_resultado_txt(self, nome_arquivo):
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"Resultado para: {self.url}\n\n")
            for header, info in self.resultado.items():
                if header in SECURITY_HEADERS:
                    status = "Presente" if info["presente"] else "Ausente"
                    f.write(f"[{status}] {header} - {info['descricao']}\n")
                elif header == "certificado_ssl":
                    ssl_info = info
                    if "erro" in ssl_info:
                        f.write(f"[SSL] Erro: {ssl_info['erro']}\n")
                    else:
                        f.write(f"[SSL] Expira em: {ssl_info['expira_em']} ({ssl_info['dias_restantes']} dias restantes)\n")
            if "erro" in self.resultado:
                f.write(f"Erro geral: {self.resultado['erro']}\n")

    def salvar_resultado_json(self, nome_arquivo):
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.resultado, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    url = input("Digite a URL do site (ex: https://exemplo.com): ").strip()
    checker = SecurityHeaderChecker(url)
    checker.verificar_headers()
    checker.verificar_ssl_expiration()

    checker.salvar_resultado_txt("relatorio.txt")
    checker.salvar_resultado_json("relatorio.json")

    print("\n Verificação concluída. Relatórios gerados: relatorio.txt e relatorio.json")
