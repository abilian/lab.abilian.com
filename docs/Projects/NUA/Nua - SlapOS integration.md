
#public #nua #cloud #slapos

## Goal

- Port a fair number (up to 100, at the end of the project) of applications, including Abilian's own (some open source, some not) to SlapOS/Rapid.Space by using (and extending) the Nua build tools and runtime services.
- Allow developers to easily port application from Heroku / Render / Railsway / etc. to SlapOS/Rapid.Space using the paradigms they are familiar with.

## Initial ideas

Notes: these need to be discussed first with JPS to check applicability and usefulness.

The idea is to start from the simple possible integration, and move towards more "intimate" integrations.

- If SlapOS can support Docker → use SlapOS as a Docker host. Use `nua-build` and `nua-orchestator` mostly as-is (but start leveraging the SlapOS APIs when useful).
- If SlapOS can support QEMU → use SlapOS as a QEMU host.  Modify `nua-build` and `nua-orchestrator` to use QEMU as image container.
- Use the Nua build engine (i.e. `nua-build`) to generate the config files for SlapOS for any Nua application, and then build the apps using SlapOS (Nua configs will need to be adapted, but we will try to mimimize disruption).
- Port to SlapOS the services allowing developers to publish an app to SlapOS/Rapid.Space by simply running a `git push` or a `nua deploy` (similar to the approach pionneered by Heroku, Clever, etc.)
- Leverage some or all of the specific services provided by SlapOS / Rapid.Space (e.g. CDN, monitoring, testing. What else?).
- Make Nua multi-servers / multi-datacenters enabled thanks to SlapOS / Rapid.Space.
- Some of Abilian's own applications will need to be updated / made "cloud native".

## List of applications

### Currently

- Galene
- Etherpad
- Hedgedoc
- Ackee
- Dolibarr

## Coming soon (or later)

- Abilian SBE, Abilian CRM, Lab&Co, JNOV.
- All customer-specific applications currently operated by Abilian.
- Wordpress, Ghost, Drupal, Plone...
- Redmine, Gitlab, Git(whatever)...
- Nextcloud...
- OnlyOffice, Collabora Online...
- Ethercalc, Cryptpad...
- Big Blue Button, Jitsi...
- Mattermost, Rocket.chat, Element...
- SuiteCRM...
- Matomo, Shynet...
- Mediawiki, XWiki, MoinMoin, Dokuwiki...
- Discourse, PphBB...
- Magento, Prestashop...
- Jenkins, Buildbot...
- Airflow, Prefect...
- Mastodon & fediverse apps
- Mailman, Sympa...

See also [[00 Apps]]

(NB: Not a contractual list.)

## Infrastructure

Open question: should infrastructure software (databases, message brokers, observability tools, other middleware...) be provided (and managed) by SlapOS directly or by Nua (in which case, as OCI containers) ?