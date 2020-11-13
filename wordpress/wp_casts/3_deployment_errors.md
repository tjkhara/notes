# Errors

------------------------------------------------------------------------------------

Error: the required `letsencrypt_contact_emails` variable is not defined.

Please define it in `groups_vars/all/main.yml` with at least one email:

  letsencrypt_contact_emails:
    - changeme@example.com

The contact email is used by Let's Encrypt to send expiry notices when a
certificate is coming up for renewal.

See https://letsencrypt.org/docs/expiration-emails/ for more information.

Since Trellis attempts to renew certificates after 60 days (30 days before
renewal), getting an expiry notice email means something has gone wrong
giving you enough notice to fix the problem.
fatal: [139.59.82.151]: FAILED! => {"changed": false}

------------------------------------------------------------------------------------