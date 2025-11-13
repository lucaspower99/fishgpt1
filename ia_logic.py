// Localize a tag <script> no seu index.html e substitua o conteúdo:

document.addEventListener('DOMContentLoaded', () => {
    // 1. Identifica o Formulário e a Área de Resultados
    const form = document.getElementById('search-form');
    const resultadoDiv = document.getElementById('resultado-info');
    const imagemDiv = document.getElementById('resultado-imagem');
    const infoArea = document.getElementById('info-area');
    
    // Mostra um estado de carregamento
    const loadingHtml = '<div class="loading-spinner"></div><p>Buscando informações com a IA...</p>';

    if (form) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault(); // Impede o envio tradicional do formulário (que o Flask usava)
            
            // Exibe o carregamento
            resultadoDiv.innerHTML = loadingHtml;
            imagemDiv.innerHTML = ''; // Limpa a imagem anterior

            // 2. Coleta os dados do Formulário
            const formData = new FormData(form);
            const peixeNome = formData.get('peixe');
            const action = event.submitter.value; // Pega o valor do botão clicado ('buscar_basico' ou 'buscar_detalhes')

            if (!peixeNome) {
                resultadoDiv.innerHTML = '<p class="error">Por favor, digite o nome de um peixe.</p>';
                return;
            }

            // 3. Monta o Objeto de Dados para enviar ao Python
            const dataToSend = {
                peixe_nome: peixeNome,
                action: action // Envia 'buscar_basico' ou 'buscar_detalhes'
            };

            try {
                // 4. CHAMA A NOVA ROTA SERVERLESS (/api)
                const response = await fetch('/api', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dataToSend)
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.erro || `Erro HTTP: ${response.status}`);
                }

                const result = await response.json();
                
                // 5. PROCESSA A RESPOSTA DO PYTHON
                if (result.erro) {
                    resultadoDiv.innerHTML = `<p class="error">❌ Erro da IA: ${result.erro}</p>`;
                } else {
                    // Exibe a informação da IA (Markdown)
                    // Nota: Se você usava uma biblioteca de markdown para HTML, mantenha-a.
                    resultadoDiv.innerHTML = `<h3>Resultado da Busca para ${peixeNome}</h3><p>${result.resultado}</p>`; 

                    // TODO: Para buscar a imagem, você precisaria de outra chamada fetch
                    // ou adaptar o api.py para retornar a URL junto com o texto.
                    // Por enquanto, vamos manter o placeholder:
                    imagemDiv.innerHTML = `<img src="https://source.unsplash.com/400x300/?${peixeNome},fishing" alt="${peixeNome}" class="img-fluid" />`;
                }

            } catch (error) {
                resultadoDiv.innerHTML = `<p class="error">❌ Falha na comunicação com o servidor. Detalhes: ${error.message}</p>`;
            }
        });
    }
});                
                // 5. PROCESSA A RESPOSTA DO PYTHON
                if (result.erro) {
                    resultadoDiv.innerHTML = `<p class="error">❌ Erro da IA: ${result.erro}</p>`;
                } else {
                    // Exibe a informação da IA (Markdown)
                    // Nota: Se você usava uma biblioteca de markdown para HTML, mantenha-a.
                    resultadoDiv.innerHTML = `<h3>Resultado da Busca para ${peixeNome}</h3><p>${result.resultado}</p>`; 

                    // TODO: Para buscar a imagem, você precisaria de outra chamada fetch
                    // ou adaptar o api.py para retornar a URL junto com o texto.
                    // Por enquanto, vamos manter o placeholder:
                    imagemDiv.innerHTML = `<img src="https://source.unsplash.com/400x300/?${peixeNome},fishing" alt="${peixeNome}" class="img-fluid" />`;
                }

            } catch (error) {
                resultadoDiv.innerHTML = `<p class="error">❌ Falha na comunicação com o servidor. Detalhes: ${error.message}</p>`;
            }
        });
    }
});// Localize a tag <script> no seu index.html e substitua o conteúdo:

document.addEventListener('DOMContentLoaded', () => {
    // 1. Identifica o Formulário e a Área de Resultados
    const form = document.getElementById('search-form');
    const resultadoDiv = document.getElementById('resultado-info');
    const imagemDiv = document.getElementById('resultado-imagem');
    const infoArea = document.getElementById('info-area');
    
    // Mostra um estado de carregamento
    const loadingHtml = '<div class="loading-spinner"></div><p>Buscando informações com a IA...</p>';

    if (form) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault(); // Impede o envio tradicional do formulário (que o Flask usava)
            
            // Exibe o carregamento
            resultadoDiv.innerHTML = loadingHtml;
            imagemDiv.innerHTML = ''; // Limpa a imagem anterior

            // 2. Coleta os dados do Formulário
            const formData = new FormData(form);
            const peixeNome = formData.get('peixe');
            const action = event.submitter.value; // Pega o valor do botão clicado ('buscar_basico' ou 'buscar_detalhes')

            if (!peixeNome) {
                resultadoDiv.innerHTML = '<p class="error">Por favor, digite o nome de um peixe.</p>';
                return;
            }

            // 3. Monta o Objeto de Dados para enviar ao Python
            const dataToSend = {
                peixe_nome: peixeNome,
                action: action // Envia 'buscar_basico' ou 'buscar_detalhes'
            };

            try {
                // 4. CHAMA A NOVA ROTA SERVERLESS (/api)
                const response = await fetch('/api', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dataToSend)
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.erro || `Erro HTTP: ${response.status}`);
                }

                const result = await response.json();
                
                // 5. PROCESSA A RESPOSTA DO PYTHON
                if (result.erro) {
                    resultadoDiv.innerHTML = `<p class="error">❌ Erro da IA: ${result.erro}</p>`;
                } else {
                    // Exibe a informação da IA (Markdown)
                    // Nota: Se você usava uma biblioteca de markdown para HTML, mantenha-a.
                    resultadoDiv.innerHTML = `<h3>Resultado da Busca para ${peixeNome}</h3><p>${result.resultado}</p>`; 

                    // TODO: Para buscar a imagem, você precisaria de outra chamada fetch
                    // ou adaptar o api.py para retornar a URL junto com o texto.
                    // Por enquanto, vamos manter o placeholder:
                    imagemDiv.innerHTML = `<img src="https://source.unsplash.com/400x300/?${peixeNome},fishing" alt="${peixeNome}" class="img-fluid" />`;
                }

            } catch (error) {
                resultadoDiv.innerHTML = `<p class="error">❌ Falha na comunicação com o servidor. Detalhes: ${error.message}</p>`;
            }
        });
    }
});if __name__ == '__main__':
    # Esta parte só roda se você estiver testando no seu computador (localmente)
    # No Vercel, o Vercel é quem inicia o app (na linha app.run() padrão)
    app.run(debug=True)
