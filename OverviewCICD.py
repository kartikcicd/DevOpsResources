# CI/CD Fundamentals
# 1. CI (Continuous Integration): Automaticallt build and test code whenever any changes are made and pushed 
# inside a central repo (Git, Bitbucket, etc). 
# This helps to detect bugs and issues early in the development cycle. (Dev)
# 2. CD (Continuous Delivery): Automatically prepare validated for release. (QA, Staging, etc.) (Pre-Release)
# 3. CD (Continuous Deployment): Automatically release validated code to production. (Production)

# Dev - CI, QA - CD, Staging - CD, Production - CD (Deployment)
# Build -> Push -> Validate -> Deploy

# DevOps Lifecycle
# 1. Source Code Management (SCM): Version control system to manage code changes (Git, GitHub, GitLab, SVN, etc.)
#  (Local Repo (Locally Inside the system) -> Central Repo (Cloud Repo (GitHub, GitLab, Bitbucket, etc.))) (Azure Repos)
# 2. Build and Compile: Convert source code into executable code (Maven, Gradle, Ant, npm, etc.) (GitHub Copilot)
# 3. Automated Testing: Run automated tests to validate code changes (JUnit, SonarQube, Automated Security Scans, etc.)
# 4. Package and Publish (Containerization): Package the application into a deployable format (Docker, JAR, WAR, etc.) 
# and publish to a repository (Nexus, Artifactory, Docker Hub, etc.) [Containerization Tools: Docker, Podman, etc.] and 
# [Orchestration Tools: Kubernetes, OpenShift, etc.]
# 5. Deployment: Deploy the application to various environments (QA, Staging, Production) (Kubernetes, OpenShift, Ansible, 
# Helm, Argo CD, etc.)
# 6. Monintoring and Logging: Monitor the application and infrastructure for performance, availability, and errors (Prometheus, Grafana, ELK Stack, etc.) 
# [Azure Monitoring Services, AWS Cloudwatch, GCP Stackdriver, etc.] {Logs, Failure Analysis, Optimization and Recommendations, etc.}
# (ChatGpt)

# Watch
# N Components of watch (Source Code Management) -> 
# Assemble all components (Build and Compile Stage) ->
# Test the watch mechanism (Check All Components) (Automated Testing) -> 
# Package the watch (Pacakging) -> 
# Give Watch to their employees to test and Monitor -> (Release (QA, UAT, Staging, etc.)) ->
# Ship to the customers (Deploy)

# Jenkins CI/CD Pipeline
# 1. Jenkins is an open-source automation server used to build, test and deploy application through CI/CD Pipelines defined in Jenkinsfile (Declarative or Scripted Pipeline).
# 2. Jenkins can deploy via Virtual Machines, Containers or Serverless Functions. (VMs - AWS EC2, Azure VM, GCP Compute Engine, Containers - Docker, Kubernetes, Serverless Functions - AWS Lambda, Azure Functions, GCP Cloud Functions)

# - Jenkins Controller and agents
# - Jenkins Controller: Manages the overall Jenkins environment, schedules jobs, and distributes tasks to agents.
# - Jenkins Agents: Execute the tasks assigned by the controller, running jobs and reporting results back

# Master Slave Architecture (Jenkins Controller and Agents)

# Freestyle jobs vs Pipeline jobs
# Freestyle jobs: Simple, single-task jobs with limited flexibility and scalability. (Good for small projects or simple tasks)
# Pipeline jobs: Complex, multi-stage jobs that can be version-controlled and easily maintained. (Good for large projects or complex workflows)

# GitHub Actions CI/CD Pipeline
# - Workflows, events, jobs, steps and runners
# - push, pull_request, schedule, workflow_dispatch, repository_dispatch, issue_comment, create, delete, release, etc.
# - Github hosted runners and Self hosted runners
    # (Runners: GitHub-hosted runners are managed by GitHub and run on virtual machines in the cloud, 
    # while self-hosted runners are managed by the user and can run on their own infrastructure.)

# GitLab CI/CD Pipeline
# It defines pipelines in a .gitlab-ci.yml file, which is stored in the root of the repository. 
# The pipeline consists of jobs, stages, and scripts that define the CI/CD process. 
# GitLab CI/CD supports various runners, including shared runners provided by GitLab (Gitlab hosted runners) and custom runners set up by users (self hosted runners).
# - Pipeline stages and jobs
# - Variable and secrets management (Protected variables, masked variables, secret variables, etc.)
# - GitLab CI/CD supports various deployment strategies, including rolling updates, blue-green deployments, and canary releases.
# - Artifacts and Caching

# (DevSecOps) and AIOps

# Automated Testing in CI/CD
# Unit Testing: Test an Individual function or method in isolation (JUnit, NUnit, pytest, etc.)
# Integration Testing: Test the interaction between multiple components or modules (TestContainers, etc.)
# Code Quality: Identify bugs and issues in the codebase (SonarQube, ESLint, Pylint, etc.)
# Security Testing: Detect vulnerabilities and security issues in the codebase (Trivy, SAST etc.)
# Container Scanning: Scan container images for vulnerabilities and security issues (Trivy, Clair, Anchore, etc.)
# End-to-End Testing: Test the entire application flow from start to finish (Selenium, Cypress, Playwright, etc.)

# AI Assisted CI/CD Automation
# AI can assist in various aspects of CI/CD automation, including:
# 1. Code Analysis and Review: AI can analyze code changes, identify potential issues, and provide suggestions for improvements. (GitHub Copilot, etc.)
# 2. Test Generation and Optimization: AI can generate test cases, optimize test coverage, and prioritize tests based on code changes. (Diffblue Cover, etc.)
# 3. AI-Generated yaml and pipeline code: Generate initial pipeline code like jenkinsfile, Github action workflow, Gitlab CI/CD pipeline code, etc. (LLM Models, AntiGravity, CoPilot, Claude, etc.)
# 4. AI Powered failure analysis: Summarize the failure logs and provide recommendations to fix the issues. (LLM Models, AntiGravity, CoPilot, Claude, etc.)

# CI/CD Pipeline as Code - Jenkins
# Pre-requisites:
# 1. Install Docker Desktop
# 2. Git Installed and configured 
# 3. GitHub Account and Repository created

# Jenkins -> GitHub Actions -> GitLab CI/CD
# Automated Pipelines testing
# Yaml Generation & Optimization
