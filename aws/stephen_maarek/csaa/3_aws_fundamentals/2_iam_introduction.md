# iam introduction

IAM - identity and access management

- Users
- Group
- Roles

Root account. The account with which we create our aws account.

Policies are written in JSON.

User - is a physical person.

Groups - users can be grouped together.

Usually by function or by team.

Groups contain users.

Roles - internal usage within aws and give these to machines.

Policies - are json documents that define what users, groups, and roles can and cannot do.

MFA can be used for root and users.

IAM has predefined managed policies.

It is best to give users and roles the minimal permissions they need to get the job done.

Don't overpower any user or application.

---

IAM Federation - for big enterprises.

Users of big enterprises can login to aws using their own login.

Identity federation uses the SAML standard.

---

## IAM 101

One IAM user per physical person.

One IAM role per application.

IAM credentials should never be shared.

Never write IAM credentials in code.

Never use the root account except for setup.
