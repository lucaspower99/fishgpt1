# api.py (O novo ponto de entrada Serverless para o Vercel)
import json
# Usaremos a biblioteca padrão do Python para requisições HTTP
from http.server import BaseHTTPRequestHandler
# A linha abaixo importa a sua lógica de IA do arquivo que você renomeou e limpou
from ia_logic import requisitar_informacoes # Importa a função de IA

# A classe 'handler' é o padrão que o Vercel procura para iniciar a Função Serverless.
class handler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        
        try:
            # 1. Lendo os dados JSON (peixe_nome e action) que virão do JavaScript
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            peixe_nome = data.get('peixe_nome', '')
            action = data.get('action', '')
        except Exception as e:
            # Erro na leitura dos dados (400 Bad Request)
            self._send_response(400, {"erro": "Dados inválidos."})
            return

        # 2. Chamando a sua lógica de IA (Função requisitar_informacoes)
        if peixe_nome and action:
            # Adaptamos o nome do action para o que sua função 'requisitar_informacoes' espera:
            if action == 'buscar_basico':
                tipo_busca = "basico"
            elif action == 'buscar_detalhes':
                # No seu código, a busca detalhada usa o parâmetro "detalhado"
                tipo_busca = "detalhado" 
            else:
                self._send_response(400, {"erro": "Tipo de busca inválido."})
                return
                
            # Chama a função principal de IA do seu ia_logic.py
            resultado_ia_texto = requisitar_informacoes(peixe_nome, tipo_busca)
            
            # TODO: Opcional: Se quiser buscar a imagem também, você pode importar e chamar aqui:
            # from ia_logic import buscar_imagem
            # image_url = buscar_imagem(peixe_nome) 
            
            # 3. Enviando a resposta (200 OK)
            response_data = {"resultado": resultado_ia_texto}
            self._send_response(200, response_data)
        else:
            # 4. Enviando erro se faltarem parâmetros (400 Bad Request)
            self._send_response(400, {"erro": "Parâmetros peixe ou action faltando."})

    def _send_response(self, status_code, data):
        """Função auxiliar para enviar a resposta HTTP formatada."""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        # CORS (Importante para o JavaScript funcionar):
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))