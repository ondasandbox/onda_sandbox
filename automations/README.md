# Onda Automations

This folder holds versioned automation definitions.

An automation should be defined in Git before it is enabled in a runtime such as Hermes cron. Runtime schedulers may create active jobs, but this folder is the durable source of truth for what those jobs are supposed to do.

Automation definitions should include:

- Name
- Schedule
- Owning skill
- Runtime prompt
- Delivery target
- Safety limits
- Test or validation command