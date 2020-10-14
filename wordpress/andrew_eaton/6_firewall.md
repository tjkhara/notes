# firewall

Check if it is installed:

    sudo ufw status verbose

If not, then install:

    sudo apt-get install ufw

Setup default:

    sudo ufw default deny incoming

    sudo ufw default allow outgoing

Adding custom rules:

    sudo ufw allow ssh && sudo ufw allow http && sudo ufw allow https

Enable it:

    sudo ufw enable

Check status:

    sudo ufw status