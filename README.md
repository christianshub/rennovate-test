# Renovate

Minimal setup as a POC.

## Token setup

For renovate to access repositories public and private, a Github token is needed.

Generate a token (assuming you are using GitHub in this guide) at <https://github.com/settings/tokens>


### Windows

1. Use your token as an environment variable:

    ```ps1
    $env:GITHUB_TOKEN="<your-token>"
    # verify:
    echo $env:GITHUB_TOKEN
    ```

1. Confirm the validity of the token by running:

    ```ps1
    $headers = @{
        "Authorization" = "token $env:GITHUB_TOKEN"
    }
    Invoke-WebRequest -Uri "https://api.github.com/user" -Headers $headers
    ```

### Linux (Ubuntu)

1. Use your token as an environment variable:

    ```bash
    export GITHUB_TOKEN="<your-token>"
    ```

    Or add it to your .bashrc/.zshrc:

    ```bash
    echo 'export GITHUB_TOKEN="<your-token>"' >> ~/.zshrc # or ~/.bashrc
    source ~/.zshrc
    ```

1. Confirm the validity of the token by running:
                
    ```bash
    curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
    ```

## Install renovate

### Windows
    
1. Ensure nodejs and npm are installed

1. Install nvm from <https://github.com/coreybutler/nvm-windows/releases> (you may need to restart after install)

1. Install nodejs: 

    ```ps1
    nvm install node
    nvm install latest
    nvm use latest
    ```

1. Install renovate: `npm install -g renovate`

### Linux (Ubuntu)

1. Install nvm, npm and renovate:

    ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash # (bump the version)
    nvm install node
    npm install -g renovate
    ```
    
## Run renovate

### Windows

```ps1
renovate --token $env:GITHUB_TOKEN --platform=github christianshub/renovate-test
```

### Linux (Ubuntu)

```bash
renovate --token $GITHUB_TOKEN --platform=github christianshub/renovate-test
```

> Note you can also you docker for this: `docker run --rm -e GITHUB_TOKEN=$GITHUB_TOKEN renovate/renovate:37 --platform=github christianshub/renovate-test`

## Debug

To obtain debug information, set a `LOG_LEVEL` environment variable to `debug` and run renovate again:

```
export LOG_LEVEL=debug
```

You can also dry run:

```bash
renovate --token $GITHUB_TOKEN --dry-run=true --platform=github christianshub/renovate-test 
```
