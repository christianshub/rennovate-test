# Renovate

Small POC

## Install renovate

1. Ensure nodejs and npm are installed

    ```bash
    # Install nvm
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    nvm install node
    npm install -g renovate
    ```

## Token setup

1. Generate a token (assuming you are using GitHub in this guide) at
   <https://github.com/settings/tokens>

1. Add or export your token:

    ```bash
    export GITHUB_TOKEN="<your-token>"
    ```
    
    Or add it to your .bashrc/.zshrc:

    ```bash
    echo 'export GITHUB_TOKEN="<your-token>"' >> ~/.zshrc # or ~/.bashrc
    source ~/.zshrc
    ```

## Run renovate

To run renovate against a repo do:

    ```bash
    renovate --token $GITHUB_TOKEN ---platform=github christianshub/renovate-demo
    ```