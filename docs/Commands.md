# ╔══════════════════════════════════════════════════════╗
# ║   GIT BASH ENVIRONMENT SETUP (WINDOWS)               ║
# ╚══════════════════════════════════════════════════════╝

git clone <url>                 # Clone from remote

git init
python -m venv venv
source venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip freeze > requirements.txt
git add .  
git commit -m "initial commit"
git push -u origin main

# ╔══════════════════════════════════════════════════════╗
# ║   BASIC GIT COMMANDS                                 ║
# ╚══════════════════════════════════════════════════════╝
"""
git add .                    
git commit -m " "      
git push                     

# ╔══════════════════════════════════════════════════════╗
# ║   GIT BRANCH WORKFLOW                                ║
# ╚══════════════════════════════════════════════════════╝
"""
# Check current branch
git branch

# Create a new branch
git checkout -b title/branch_purpose
git checkout -b backend/complete_local_version

# Stage changes
git add .

# Commit changes
git commit -m "Descriptive commit message"

# Push branch to remote
git push -u origin title/branch_purpose
git push -u origin backend/complete_local_version

# Switch between branches
git checkout main
git checkout title/branch_purpose

# Merge branch into main
git checkout main
git pull                  # ensure main is up-to-date
git merge title/branch_purpose

# Delete branch (optional)
git branch -d title/branch_purpose        # local
git push origin --delete title/branch_purpose  # remote

# Useful commands
git status                      # View changes
git log --oneline               # Condensed history
git remote -v                   # Show remote URL
"""

# ╔══════════════════════════════════════════════════════╗
# ║   GIT: GO BACK TO OLD VERSIONS & PUSH TO GITHUB      ║
# ╚══════════════════════════════════════════════════════╝
"""
# Save current work
git status
git add .
git commit -m "Current working version"

# View commit history
git log --oneline

## ✅ Option A — Revert (Keep History, Create New Commit)
git revert <old_commit_hash>..HEAD
# Example:
git revert 8a61c0c8360841b8ef1a5f47f41854adc48f12d3..HEAD
git push

# Abort if stuck
git revert --abort

## 🔴 Option B — Reset (Full Move Back, No Conflicts)
git reset --hard <old_commit_hash>
git push --force

## Push project to GitHub
git init
git remote add origin https://github.com/AharonSegal/..
git add .
git commit -m "Initial Push"
git branch -M main          # Rename master → main
git push -u origin main

# If push fails due to remote changes
git pull origin main --rebase
git push -u origin main


# ╔══════════════════════════════════════════════════════╗
# ║   GIT LOGGING & VIEWING HISTORY                       ║
# ╚══════════════════════════════════════════════════════╝
"""
# View current branch status
git status

# View full commit history
git log

# View condensed history (one line per commit)
git log --oneline

# Show commits with graph
git log --oneline --graph --decorate --all

# View last N commits
git log -n 5

# View changes in a commit
git show <commit-hash>

# View differences in working directory
git diff

# View staged changes
git diff --cached

# Show remote repositories
git remote -v

# View detailed commit history for a file
git log -- <file-path>
"""
