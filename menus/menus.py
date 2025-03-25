import os
from modulos import downloader


def exibir_menu(titulo, opcoes):
    """Função para exibir o menu com opções."""
    os.system("cls" if os.name == "nt" else "clear")
    
    print("=" * 50)
    print(titulo)
    print("=" * 50)

    for chave, opcao in opcoes.items():
        print(f"{chave}️⃣  {opcao[0]}")
    
    print("\n" + "=" * 50)

def menu_navegadores():
    opcoes_navegadores = {
        "1": ("Google Chrome", "https://dl.google.com/dl/chrome/install/googlechromestandaloneenterprise64.msi"),
        "2": ("Mozilla Firefox", "https://download-installer.cdn.mozilla.net/pub/firefox/releases/123.0.1/win64/pt-BR/Firefox Setup 123.0.1.msi"),
        "3": ("Microsoft Edge", "https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/950e5559-bb85-4d79-98bb-847b22c3700e/MicrosoftEdgeEnterpriseX64.msi"),
        "4": ("Opera", "https://download5.operacdn.com/ftp/pub/opera/desktop/117.0.5408.154/win/Opera_117.0.5408.154_Setup_x64.exe"),
        "5": ("Voltar", None)
    }

    while True:
        exibir_menu("Escolha seu Navegador", opcoes_navegadores)
        escolha = input("👉 Digite o número correspondente: ")

        if escolha == "5":
            break  # Volta ao menu principal

        if escolha in opcoes_navegadores:
            nome, link = opcoes_navegadores[escolha]
            print(f"\n✅ Você escolheu {nome}. Iniciando download...")
            print(f"🔗 Link de download: {link}\n")
            downloader.download_arquivo(link, "downloads/navegadores")
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

        input("Pressione ENTER para continuar...")

def menu_sdk():
    opcoes_sdk = {
        "1": ("Node.js (22.14)", "https://nodejs.org/dist/v22.14.0/node-v22.14.0-x64.msi"),
        "2": ("Oracle JDK (JDK 24)", "https://download.oracle.com/java/24/latest/jdk-24_windows-x64_bin.exe"),
        "3": ("Open JDK (JDK 24)", "https://download.java.net/java/GA/jdk24/1f9ff9062db4449d8ca828c504ffae90/36/GPL/openjdk-24_windows-x64_bin.zip"),
        "4": (".NET SDK (.NET 8)", "https://download.visualstudio.microsoft.com/download/pr/6f043b39-b3d2-4f0a-92bd-99408739c98d/fa16213ea5d6464fa9138142ea1a3446/dotnet-sdk-8.0.407-win-x64.exe"),
        "5": ("Voltar", None)
    }

    while True:
        exibir_menu("Escolha o Ambiente de Desenvolvimento", opcoes_sdk)
        escolha = input("👉 Digite o número correspondente: ")

        if escolha == "5":
            break  # Volta ao menu principal

        if escolha in opcoes_sdk:
            nome, link = opcoes_sdk[escolha]
            print(f"\n✅ Você escolheu {nome}. Iniciando download...")
            print(f"🔗 Link de download: {link}\n")
            downloader.download_arquivo(link, "downloads/sdk")
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

        input("Pressione ENTER para continuar...")

def menu_ides():
    opcoes_ides = {
        "1": ("Visual Studio Code", "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64"),
        "2": ("IntelliJ IDEA", "https://download-cdn.jetbrains.com/idea/ideaIU-2024.3.5.exe"),
        "3": ("Eclipse", "https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2025-03/R/eclipse-inst-jre-win64.exe&mirror_id=1"),
        "4": ("PyCharm Community", "https://download-cdn.jetbrains.com/python/pycharm-community-2024.3.5.exe"),
        "5": ("NetBeans", "https://dlcdn.apache.org/netbeans/netbeans-installers/25/Apache-NetBeans-25-bin-windows-x64.exe"),
        "6": ("Notepad++", "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.7.7/npp.8.7.7.Installer.x64.exe"),
        "7": ("Git for Windows", "https://github.com/git-for-windows/git/releases/download/v2.49.0.windows.1/Git-2.49.0-64-bit.exe"),
        "8": ("GitHub Desktop", "https://desktop.githubusercontent.com/releases/3.4.18-19c76e1d/GitHubDesktopSetup-x64.exe"),
        "9": ("Voltar", None)
    }

    while True:
        exibir_menu("Escolha sua IDE (Ambiente de Desenvolvimento)", opcoes_ides)
        escolha = input("👉 Digite o número correspondente: ")

        if escolha == "9":
            break  # Volta ao menu principal

        if escolha in opcoes_ides:
            nome, link = opcoes_ides[escolha]
            print(f"\n✅ Você escolheu {nome}. Iniciando download...")
            print(f"🔗 Link de download: {link}\n")
            downloader.download_arquivo(link, "downloads/ides")
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

        input("Pressione ENTER para continuar...")

def menu_banco_de_dados():
    opcoes_bancos = {
        "1": ("MySQL (8.0)", "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.41.0.msi"),
        "2": ("MariaDB (11.4)", "https://archive.mariadb.org//mariadb-11.4.5/winx64-packages/mariadb-11.4.5-winx64.msi"),
        "3": ("MongoDB", "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-8.0.6-signed.msi"),
        "4": ("Voltar", None)
    }

    while True:
        exibir_menu("Escolha o Banco de Dados", opcoes_bancos)
        escolha = input("👉 Digite o número correspondente: ")

        if escolha == "4":
            break  # Volta ao menu principal

        if escolha in opcoes_bancos:
            nome, link = opcoes_bancos[escolha]
            print(f"\n✅ Você escolheu {nome}. Iniciando download...")
            print(f"🔗 Link de download: {link}\n")
            downloader.download_arquivo(link, "downloads/bancos_de_dados")
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

        input("Pressione ENTER para continuar...")

def menu_iso():
    opcoes_os = {
        "1": ("Windows 11 (Media Creator Tool)", "https://software-static.download.prss.microsoft.com/dbazure/888969d5-f34g-4e03-ac9d-1f9786c66749/mediacreationtool.exe"),
        "2": ("Ubuntu (24.04.2 LTS)", "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso"),
        "3": ("Ubuntu (24.10)", "https://releases.ubuntu.com/24.10/ubuntu-24.10-desktop-amd64.iso"),
        "4": ("Debian 12 (Full install)", "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.10.0-amd64-DVD-1.iso"),
        "5": ("Fedora 41", "https://download.fedoraproject.org/pub/fedora/linux/releases/41/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-41-1.4.iso"),
        "5": ("OpenSuse (Tumbleweed)", "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso"),
        "6": ("Rufus", "https://github.com/pbatard/rufus/releases/download/v4.6/rufus-4.6.exe"),
        "7": ("Voltar", None)
    }

    while True:
        exibir_menu("Escolha o Banco de Dados", opcoes_os)
        escolha = input("👉 Digite o número correspondente: ")

        if escolha == "7":
            break  # Volta ao menu principal

        if escolha in opcoes_os:
            nome, link = opcoes_os[escolha]
            print(f"\n✅ Você escolheu {nome}. Iniciando download...")
            print(f"🔗 Link de download: {link}\n")
            downloader.download_arquivo(link, "downloads/iso")
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

        input("Pressione ENTER para continuar...")
