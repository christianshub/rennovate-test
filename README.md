# Renovate

Minimal setup as a POC.

## Token setup

For renovate to access repositories public and private, a Github token is needed.

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

1. Confirm the validity of the token by running:

```bash
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```
It should display details about the user that created the token:

```markdown
{
    "login": "<your-user-name>",
    "id": "2539",
    // left out for brevity
}
```

## Install renovate

1. Ensure nodejs and npm are installed

    * Windows
        1. Install nvm from
           <https://github.com/coreybutler/nvm-windows/releases> (you may need
           to restart after install)
        1. Install nodejs: 
            
            ```ps1
            nvm install node
            nvm install latestnvm use latest
            ```
        
        1. Install renovate: `npm install -g renovate`

    * Linux (Ubuntu)

        1. Install nvm: `curl -o-
           https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh |
           bash` (bump the version)
        1. Install node: `nvm install node`
        1. Install renovate: `npm install -g renovate`
        
## Run renovate

To run renovate against a repo do:

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