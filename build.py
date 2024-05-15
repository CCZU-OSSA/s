from pathlib import Path
from shutil import rmtree
from sys import platform
from typing import Dict

from colorama import Fore, Style, init
from yaml import Loader, load

if platform == "win32":
    init(wrap=True)

if __name__ != "__main__":
    print(f"{Fore.LIGHTRED_EX}😅 Don't import this file.{Style.RESET_ALL}")
    exit(0)

config = Path("config.yaml")
if not config.exists():
    print(f"{Fore.LIGHTRED_EX}😅 Can't find `config.yaml`{Style.RESET_ALL}")
    exit(1)
else:
    print(f"{Fore.LIGHTCYAN_EX}🤔 Loading `config.yaml`{Style.RESET_ALL}")

template = Path("template.html")
if not template.exists():
    print(f"{Fore.LIGHTRED_EX}😅 Can't find `template.html`{Style.RESET_ALL}")
    exit(1)
else:
    print(f"{Fore.LIGHTCYAN_EX}🤔 Loading `template.html`{Style.RESET_ALL}")
template_text = template.read_text()

build = Path("build")


if build.exists():
    rmtree(build)
    print(f"{Fore.LIGHTYELLOW_EX}💥 Remove `build` dir{Style.RESET_ALL}")
build.mkdir()
print(f"{Fore.LIGHTCYAN_EX}😋 Create `build` dir{Style.RESET_ALL}")


data: Dict[str, str] = load(config.read_text(), Loader)
length = len(data)
current = 1

for target, origin in data.items():
    print(
        Fore.LIGHTGREEN_EX + f"😋 Create `build/{target}.html ({current}/{length})`",
        Style.RESET_ALL,
    )
    target_path = Path(f"build/{target}.html")
    target_path.write_text(template_text.replace("${TARGET_URL}", origin))
    print(
        Fore.LIGHTGREEN_EX + f"😎 `build/{target}.html` OK",
        Style.RESET_ALL,
    )
    current += 1
print(
    Fore.LIGHTGREEN_EX + "🥰 Done!",
    Style.RESET_ALL,
)
