import os
import shutil
from mutagen.easyid3 import EasyID3

def main():
    src = r"F:\Musicas Itunes"  # Pasta de origem
    dest = r"F:\Nova Pasta"  # Pasta de destino

    if not os.path.exists(dest):
        os.makedirs(dest)

    title_artist_files = {}

    for filename in os.listdir(src):
        if filename.lower().endswith(".mp3"):
            filepath = os.path.join(src, filename)

            try:
                if os.path.getsize(filepath) < 50 * 1024:  # Ignora arquivos muito pequenos (<50 KB)
                    print(f"Arquivo muito pequeno: '{filename}'. Ignorando.")
                    continue

                audio = EasyID3(filepath)
                title = audio.get("title", [None])[0]
                artist = audio.get("artist", [None])[0]

                if not title or not artist:
                    print(f"Arquivo sem título ou artista: '{filename}'. Ignorando.")
                    continue

                key = f"{title.strip()} - {artist.strip()}"  # Combinação Título + Artista
                title_artist_files.setdefault(key, []).append(filepath)

            except Exception as e:
                print(f"Arquivo inválido ou sem metadados: '{filename}'. Ignorando.")
                continue

    # Verifica duplicatas
    for key, files in title_artist_files.items():
        if len(files) > 1:
            print(f"\nDuplicatas encontradas para: {key}")

            for file in files:
                dest_file = os.path.join(dest, os.path.basename(file))

                if os.path.exists(dest_file):
                    print(f"Já existe uma cópia de '{os.path.basename(file)}' em {dest}")
                    print(f"Excluindo '{file}' para evitar terceira cópia.")
                    os.remove(file)  # Apaga a terceira cópia
                else:
                    print(f"Movendo '{file}' para '{dest}'")
                    shutil.move(file, dest_file)

if __name__ == "__main__":
    main()
