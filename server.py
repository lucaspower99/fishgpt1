# server.py (NOVO ARQUIVO)

from index import app as application 
# O Vercel espera que a instância principal do Flask seja chamada 'application'
# Aqui, importamos sua instância 'app' (do arquivo index.py) e a renomeamos.

# O Vercel agora usará 'application' para iniciar o servidor.