from pathlib import Path
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Копіює файли та сортує їх у піддиректорії за розширенням."
    )
    parser.add_argument("-s", "--source", type=Path, required=True, help="Папка з файлами")
    parser.add_argument("-o", "--output", type=Path, default=Path("output"), help="Папка для копіювання")
    
    args = parser.parse_args()

    return args

def copy_files(source: Path, output: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                copy_files(el, output)
            else:
                folder = el.name[:1]
                folder = output / folder
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, folder)

    except Exception as e:
        print(f"Помилка: {e}")
 


def main():
    args = parse_args()
    copy_files(args.source, args.output)


if __name__ == "__main__":
    main()
