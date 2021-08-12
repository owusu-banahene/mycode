#!/usr/bin/env python3
import os
os.system("git add .")
os.system("git commit -m"+input("commit message:").strip())
os.system("git push origin main")
