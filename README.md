# 🚀 GitMaster Pro - Ultimate GitHub Automation Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20Mac-success?style=for-the-badge&logo=linux)
![Status](https://img.shields.io/badge/Status-Stable%20v4.0-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

> **"Upload code to GitHub at the speed of thought."** ⚡

**GitMaster Pro** is an advanced CLI automation tool designed to eliminate the repetitive commands of Git. It initializes, creates repositories, analyzes your code structure, generates descriptions, and pushes your code—all in a single click. **Zero crashes. 100% Efficiency.**

---

## 🌟 Key Features (Ultrasonic Edition)

* **🛡️ Crash-Proof Core:** Built with advanced `try-catch` mechanisms and `shutil` file handling. It never crashes, even if the internet fails or files are locked.
* **🧠 A.I. Auto-Analysis:** Automatically scans your project folder, detects languages (Python, JS, HTML, etc.), and writes a smart description for your repository.
* **🌍 Cross-Platform Supremacy:** Works flawlessly on **Windows, Linux (Kali/Ubuntu), and macOS**. Handles path separators (`/` vs `\`) automatically.
* **🎯 Target Locking (`-t`):** Upload any folder from anywhere on your disk without moving the script.
* **🎨 Beautiful UI:** Features a hacker-style banner, color-coded logs (Green for Success, Red for Error), and live status updates.

---

## 📸 Preview

```text
    ██████╗ ██╗████████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
   ██╔════╝ ██║╚══██╔══╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
   ██║  ███╗██║   ██║   ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
   ██║   ██║██║   ██║   ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
   ╚██████╔╝██║   ██║   ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
    ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                 [v4.0 - OS Stable Edition]
    
    [INFO] Authenticated as: vishal8736
    [INFO] Analyzing directory content...
    [INFO] Auto-Description: Project containing 15 files. Tech Stack: Python, HTML.
    
    [?] Enter Repository Name: my-awesome-project
    [?] Private Repo? (y/n): n
    
    [SUCCESS] Repository created successfully!
    [SUCCESS] Mission Accomplished! 🚀

🛠️ Installation
1. Clone the Tool:
git clone [https://github.com/vishal8736/gitmaster.git](https://github.com/vishal8736/gitmaster.git)
cd gitmaster
2. Install Requirements:
You need requests and colorama for the UI and API calls.

pip install requests colorama
3. Setup Token:
Open gitmaster.py in any text editor.
Find the line: GITHUB_TOKEN = "YOUR_TOKEN_HERE"
Replace it with your classic Personal Access Token (PAT) from GitHub Settings.

🚀 Usage
1. Basic Usage (Current Folder)
To upload the files in the directory where the script is located:

2. Advanced Usage (Target Specific Folder)
To upload a specific project folder located somewhere else on your computer:

python gitmaster.py -t "/path/to/your/project"

Windows Example: python gitmaster.py -t "C:\Users\Vishal\Desktop\MyWeb"
Linux Example: python gitmaster.py -t "/home/kali/tools/scan-tool"

⚙️ How It Works
Checks Environment: Verifies Internet, Git installation, and OS type.
Scans Code: Looks inside your target folder to count files and identify programming languages.
Creates Repo: Uses GitHub API to create a new repository instantly.
Git Magic:
git init
git add .
git commit (with auto message)
git remote add
git push
Success: Returns the link to your new live repository.
👨‍💻 Developer Info
<div align="center">
Developer Contact GitHub

🌸 Vishal ❤️ Subhi 🌸

 📧 vishalsharma852863@gmail.com github.com/vishal8736

</div>
<p align="center">
Made with ❤️ and Python

<i>Don't just code, dominate the repo.</i>
</p>
