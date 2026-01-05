import os
import sys
import subprocess
import requests
import argparse
import shutil
import platform
import stat
from collections import Counter
from colorama import Fore, Style, init

# --- INITIALIZATION ---
init(autoreset=True)

# --- CONFIGURATION ---
# SECURITY UPDATE: Token ab hardcode nahi hoga.
GITHUB_API_URL = "https://api.github.com/user/repos"
USER_API_URL = "https://api.github.com/user"

# --- UI COLORS ---
INFO = f"{Fore.CYAN}[INFO]{Style.RESET_ALL}"
PROCESS = f"{Fore.YELLOW}[...]{Style.RESET_ALL}"
SUCCESS = f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}"
ERROR = f"{Fore.RED}[ERROR]{Style.RESET_ALL}"
INPUT_MARK = f"{Fore.MAGENTA}[INPUT]{Style.RESET_ALL}"
RESET = Style.RESET_ALL

# Global variable for token
CURRENT_TOKEN = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_screen()
    print(Fore.GREEN + """
    ██████╗ ██╗████████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
   ██╔════╝ ██║╚══██╔══╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
   ██║  ███╗██║   ██║   ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
   ██║   ██║██║   ██║   ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
   ╚██████╔╝██║   ██║   ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
    ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                 [v4.1 - Secure Edition]
    """ + RESET)
    print(Fore.WHITE + "    ----------------------------------------------------------")
    print(f"    {Fore.MAGENTA}System    : {Fore.YELLOW}{platform.system()} {platform.release()}{RESET}")
    print(f"    {Fore.MAGENTA}Dev Name  : {Fore.YELLOW}🌸 Vishal ❤️ Subhi 🌸{RESET}")
    print(Fore.WHITE + "    ----------------------------------------------------------\n")

# --- UTILITY FUNCTIONS ---

def get_token_securely():
    """Token ko secure tareeke se fetch karega"""
    # 1. Check Environment Variable
    token = os.environ.get("GITHUB_TOKEN")
    
    if token:
        return token
    
    # 2. If not in env, ask user
    print(f"{INFO} GitHub Token code me nahi mila (Security Best Practice).")
    print(f"{Fore.YELLOW}Tip: Baar baar enter karne se bachne ke liye: export GITHUB_TOKEN='your_token'{RESET}")
    token_input = input(f"{INPUT_MARK} Paste your GitHub Token here (hidden): ").strip()
    
    if not token_input:
        print(f"{ERROR} Token zaroori hai!")
        sys.exit(1)
        
    return token_input

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def check_git_installed():
    try:
        subprocess.run(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def check_internet():
    print(f"{PROCESS} Checking internet connection...")
    try:
        requests.get('https://github.com', timeout=5)
        print(f"{SUCCESS} Connection Established.")
        return True
    except requests.ConnectionError:
        print(f"{ERROR} Internet nahi chal raha hai.")
        return False

def get_username():
    headers = {"Authorization": f"token {CURRENT_TOKEN}"}
    try:
        response = requests.get(USER_API_URL, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()['login']
        elif response.status_code == 401:
            print(f"{ERROR} Token Invalid hai! Check karein ki token sahi copy kiya hai.")
            sys.exit(1)
        else:
            print(f"{ERROR} API Error: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"{ERROR} Network Error: {e}")
        sys.exit(1)

def analyze_directory(path):
    print(f"{PROCESS} Analyzing directory content...")
    extensions = []
    file_count = 0
    lang_map = {
        'py': 'Python', 'js': 'JavaScript', 'html': 'HTML', 'css': 'CSS',
        'java': 'Java', 'cpp': 'C++', 'c': 'C', 'php': 'PHP', 'ts': 'TypeScript', 'json': 'JSON'
    }

    try:
        for root, dirs, files in os.walk(path):
            if '.git' in dirs: dirs.remove('.git')
            for file in files:
                file_count += 1
                ext = file.split('.')[-1].lower() if '.' in file else 'file'
                if ext in lang_map: extensions.append(lang_map[ext])
        
        if file_count == 0: return "Empty Project"

        counter = Counter(extensions)
        top_langs = [lang for lang, count in counter.most_common(3)]
        langs_str = ", ".join(top_langs) if top_langs else "Mixed Files"
        
        desc = f"Project containing {file_count} files. Tech Stack: {langs_str}. Uploaded via GitMaster."
        print(f"{INFO} Auto-Description: {Fore.YELLOW}{desc}{RESET}")
        return desc
    except Exception as e:
        return "Project uploaded via GitMaster"

# --- CORE FUNCTIONS ---

def run_command(command, show_output=False):
    try:
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if show_output and process.stdout: print(f"{Fore.CYAN}  [LOG] {process.stdout.strip()}{RESET}")
        return (True, process.stdout.strip()) if process.returncode == 0 else (False, process.stderr.strip())
    except Exception as e:
        return False, str(e)

def create_repo(repo_name, is_private, description):
    headers = {"Authorization": f"token {CURRENT_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"name": repo_name, "private": is_private, "description": description}
    
    print(f"{PROCESS} Creating repository '{repo_name}'...")
    try:
        response = requests.post(GITHUB_API_URL, json=data, headers=headers, timeout=15)
        if response.status_code == 201:
            print(f"{SUCCESS} Repository created!")
            return True
        elif response.status_code == 422:
            print(f"{ERROR} Repository pehle se exist karta hai (Continuing...)")
            return True 
        else:
            print(f"{ERROR} Failed to create repo. Code: {response.status_code}")
            return False
    except Exception as e:
        print(f"{ERROR} Connection failed: {e}")
        return False

def push_code(repo_name, username, target_path):
    remote_url = f"https://{CURRENT_TOKEN}@github.com/{username}/{repo_name}.git"
    
    if not os.path.exists(target_path): return

    try:
        os.chdir(target_path)
    except PermissionError:
        print(f"{ERROR} Permission Denied!")
        return

    # Clean old .git to remove history of secrets
    git_folder = os.path.join(target_path, ".git")
    if os.path.exists(git_folder):
        print(f"{PROCESS} Cleaning old git config (Removing history)...")
        try:
            shutil.rmtree(git_folder, onerror=on_rm_error)
        except Exception: pass

    steps = [
        ("Initializing Git", "git init"),
        ("Adding Files", "git add ."),
        ("Committing", 'git commit -m "Secure Upload via GitMaster"'),
        ("Branching", "git branch -M main"),
        ("Linking Remote", f"git remote add origin {remote_url}"),
        ("Pushing Code", "git push -u origin main")
    ]

    for desc, cmd in steps:
        print(f"{PROCESS} {desc}...")
        success, output = run_command(cmd)
        
        if not success:
            if "remote origin already exists" in output:
                run_command(f"git remote set-url origin {remote_url}")
            elif "nothing to commit" in output:
                print(f"{INFO} Nothing to upload.")
            elif "identity unknown" in output.lower():
                run_command('git config user.email "vishalsharma852863@gmail.com"')
                run_command('git config user.name "Vishal Sharma"')
                run_command('git commit -m "Secure Upload"')
            else:
                print(f"{ERROR} Error: {output}")
                return
        else:
            print(f"{SUCCESS} {desc} Done.")

    print(f"\n{SUCCESS} {Fore.GREEN}SECURE UPLOAD COMPLETE! 🚀")
    print(f"{INFO} Link: https://github.com/{username}/{repo_name}")

def main():
    global CURRENT_TOKEN
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", default=".")
        args = parser.parse_args()
        target_path = os.path.abspath(args.target)

        banner()
        if not check_git_installed(): sys.exit(1)
        if not check_internet(): sys.exit(1)

        # SECURITY: Get Token dynamically
        CURRENT_TOKEN = get_token_securely()

        print(f"{PROCESS} Authenticating...")
        USERNAME = get_username()
        print(f"{SUCCESS} Authenticated as: {Fore.CYAN}{USERNAME}{RESET}")

        if not os.path.exists(target_path):
             print(f"{ERROR} Folder not found.")
             sys.exit(1)
             
        auto_desc = analyze_directory(target_path)

        print("-" * 50)
        repo_name = input(f"{INPUT_MARK} Enter Repository Name: ").strip()
        if not repo_name: sys.exit(1)
        vis_choice = input(f"{INPUT_MARK} Private Repo? (y/n): ").strip().lower()
        print("-" * 50)

        if create_repo(repo_name, vis_choice == 'y', auto_desc):
            push_code(repo_name, USERNAME, target_path)

    except KeyboardInterrupt:
        print(f"\n{ERROR} Stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
