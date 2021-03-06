import os
import zipfile 
from pathlib import Path


def build():
    os.chdir("src/")
    x = Path('./')
    packs = list(filter(lambda y: y.is_dir(), x.iterdir()))
    packs = [pack for pack in packs if not str(pack).startswith((".", "__"))]


    print("Building packs...")
    
    for pack in packs:
        print("\u001b[30;1mPack: {}\u001b[0m".format(pack))
        os.chdir(pack)

        with open('title.txt', 'r') as titlefile:
            title = titlefile.read()

        try: 
            file = zipfile.ZipFile(
                '../../release/{}.wastickers'.format(title), 
                'w', zipfile.ZIP_DEFLATED)

            for item in [item for item in os.listdir() if not item.startswith(".")]: 
                file.write(item)
            file.close()
            os.chdir("..")
        except Exception as e:
            print(e)
            print("Could not build pack")

    print("Packs have been built.")

if __name__ == "__main__":
    build()
