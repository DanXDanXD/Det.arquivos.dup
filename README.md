🎵 Script de Detecção e Organização de Músicas Duplicadas
Este projeto é um script em Python que identifica músicas duplicadas com base no Título + Artista dos arquivos .mp3.
As músicas duplicadas são movidas para uma pasta separada para fácil organização.

📋 Funcionalidades
Lê os metadados (ID3) dos arquivos .mp3.

Considera Título + Artista para identificar duplicatas (não apenas o nome do arquivo).

Move as músicas duplicadas para uma pasta específica.

Ignora arquivos muito pequenos ou corrompidos.

Evita múltiplas cópias: se a música já existir na pasta destino, a nova duplicata é apagada.

Gera mensagens claras durante o processo.

🛠️ Requisitos
Python 3.8 ou superior

Biblioteca mutagen

Para instalar as dependências, rode:

bash
Copiar
Editar
pip install mutagen
🚀 Como Usar
Clone este repositório ou copie o script para sua máquina.

Ajuste os caminhos das pastas de origem e de destino no código:

python
Copiar
Editar
src = r"D:\Musicas Itunes"  # Pasta com suas músicas
dest = r"D:\Nova Pasta"     # Pasta onde as duplicatas serão movidas
Execute o script:

bash
Copiar
Editar
python detecta_duplicatas.py
Pronto! As duplicatas serão movidas ou apagadas conforme configurado.

📁 Estrutura do Projeto
Copiar
Editar
📂 detecta-duplicatas-musicas
 ├── detecta_duplicatas.py
 └── README.md
⚠️ Observações
Apenas arquivos .mp3 com metadados ID3 válidos são analisados.

Arquivos corrompidos ou muito pequenos são ignorados automaticamente.

Sempre faça um backup das suas músicas antes de mover ou apagar arquivos!

✨ Melhorias Futuras
Gerar relatório em .txt com as duplicatas encontradas.

Suporte para outros formatos de áudio (.flac, .m4a, etc.).

Interface gráfica (GUI) para facilitar o uso.

📄 Licença
Este projeto está licenciado sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar! 🎶

🙋‍♂️ Autor
Feito com carinho por [Seu Nome Aqui].

🎵 Vamos organizar suas músicas como elas merecem! 🎶
