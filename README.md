📝 Git Workflow Guide for the Project

This document outlines how to work with Git during sprints to improve team coordination and avoid code conflicts.

🗂 Branch Structure:

main: Stable and production-ready code.

develop: Integration branch for collecting changes during the sprint.

feature/*: Branches created from develop for individual features.

🚀 Workflow for Each Sprint:

✅ Starting the Sprint:

Update the develop branch:Make sure develop is up to date with main before starting work:
git checkout develop
git pull origin main
git push origin develop
Create a feature branch for each task:Create a new branch from develop for your feature:
git checkout develop
git pull origin develop  # Get the latest changes
git checkout -b feature/feature-name
🛠 Working on the Feature:

After making the necessary changes:
git add .
git commit -m "Add [feature-name]"
git push origin feature/feature-name
🔄 Opening and Reviewing a Pull Request:

Create a PR:Open a pull request from your feature branch to develop in GitHub.

Resolve conflicts if necessary:If there are conflicts, resolve them as follows:
git checkout feature/feature-name
git fetch origin
git pull origin develop  # Sync with the latest changes
git add .
git commit -m "Resolve merge conflicts"
git push origin feature/feature-name
Review and approval:

Have at least one team member review the code.

Once approved, the PR can be merged.

🏁 Ending the Sprint:

When all features are merged into develop and tests pass:
git checkout main
git pull origin develop
git push origin main
The final version is now ready for release.

✅ Branching Rules Suggestions:

Direct pushes to main and develop should be prohibited.

Require at least one code review before merging a PR.

Enable automated tests on PRs.

Use Squash and Merge to keep the commit history clean.

🧭 Workflow Overview:
main <--- develop <--- feature/login
                     <--- feature/profile
                     <--- feature/dashboard
At the end of each sprint:
develop ---> main ✅
By following this workflow, the team can collaborate efficiently without conflicts. 🚀
