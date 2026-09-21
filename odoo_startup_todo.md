# Odoo Community Startup Build: To-Do List

## Open decisions
- [x] Target Odoo version: **19** (Community)
- [ ] Target country/localization (drives payroll, tax rules, fiscal reports)
- [x] Verify OCA 19.0 branch availability for key repos — done 2026-09-21, see table below

## Core layer
- [x] `startup_base`: company settings, branding, default config — built 2026-09-21 (res.company color/tagline fields + Settings UI)
- [ ] `startup_security`: roles, access groups, record rules
- [ ] `startup_automation`: automated actions, scheduled jobs, notifications
- [ ] `startup_dashboard`: KPI dashboards (sales, finance, HR, projects)
- [ ] `startup_reports`: branded PDF templates (invoice, quote, PO, payslip)
- [ ] `startup_seed`: one-click loader (sample data, chart of accounts, templates)
- [ ] `startup_onboarding`: setup wizard to enable modules and config
- [ ] `startup_audit`: audit log and change tracking
- [ ] `startup_api`: REST API and integration hooks
- [x] `startup_home_menu`: full-screen app grid, live search, keyboard navigation, recents/favorites — built 2026-09-21 (wraps OCA `web_responsive`)
- [ ] `startup_theme`: colors, fonts, login page, navbar, backgrounds, icon set (`web_icon` on every root menu), driven by company settings — **in progress 2026-09-21**: app-grid background + wordmark/tagline done (company primary/secondary color, dynamic via session_info); login page, navbar, and per-app `web_icon` still open

## Enterprise replacements
- [ ] `startup_accounting`: bank reconciliation, financial reports, assets, budgets
- [ ] `startup_payroll`: salary rules, payslips, contributions, local tax rules
- [ ] `startup_helpdesk`: tickets, SLAs, teams, portal
- [ ] `startup_documents`: workspace, tags, access rights
- [ ] `startup_knowledge`: internal wiki and articles
- [ ] `startup_approvals`: generic approval engine other modules hook into
- [ ] `startup_sign`: e-signature requests and templates
- [ ] `startup_subscriptions`: recurring contracts and invoicing
- [ ] `startup_planning`: shift and resource planning
- [ ] `startup_field_service`: on-site tasks, worksheets, mobile use
- [ ] `startup_barcode`: scanning for inventory operations
- [ ] `startup_appraisals`: employee reviews and goals
- [ ] `startup_marketing_automation`: campaign workflows and triggers
- [ ] `startup_expenses`: expense reports and reimbursements (check version first)

## Optional
- [ ] `startup_vertical_*`: per-specialty modules (retail, services, logistics, ...)

## Standard Community apps to install
- [ ] **Finance:** Invoicing, Payment Providers
- [ ] **Sales:** CRM, Sales, Contacts
- [ ] **Operations:** Purchase, Inventory, Project, Timesheets, Manufacturing, Maintenance, Fleet
- [ ] **People:** Employees, Recruitment, Time Off, Attendance, Lunch
- [ ] **Business:** Website, eCommerce, Email Marketing, Discuss, Calendar, Live Chat, Surveys, eLearning
- [ ] **Tools:** Point of Sale

## OCA modules to evaluate before building from scratch
Checked against GitHub 19.0 branches on 2026-09-21 (module count = 18.0 vs 19.0, rough maturity proxy).

| Repo | 18.0 | 19.0 | Verdict for `startup_*` |
|---|---|---|---|
| `web` (incl. `web_responsive`) | 67 | 37 | `web_responsive` **is ported** — use as base for `startup_home_menu` |
| `account-financial-tools` | 43 | 24 | ~55% ported, no reconciliation/statement-import module yet — check individually for `startup_accounting` |
| `helpdesk` | 35 | 17 | ~50% ported — check individually for `startup_helpdesk` |
| `server-ux` (tier validation) | 38 | 18 | `base_tier_validation` **not yet in 19.0** — build `startup_approvals` custom, revisit OCA later |
| `dms` (documents) | 9 | 3 | thin (~33%) — build `startup_documents` mostly custom for now |
| `knowledge` | 17 | 11 | ~65% ported — worth checking for `startup_knowledge` |
| `hr` | 33 | 13 | ~40% ported |
| `hr-expense` | 13 | 1 | barely started — build `startup_expenses` custom, don't wait |
| `field-service` | 41 | 36 | ~88% ported — good OCA candidate for `startup_field_service` |
| `sign` | 5 | 3 | ~60% ported |
| `e-commerce` | 45 | 47 | fully ported |
| `server-tools` | 59 | 31 | ~55% ported |

Re-check this table periodically — OCA ports fill in over time after an Odoo release.

## Notes
- Do not reuse `web_enterprise` code (OEEL license).
- Every module needs `static/description/icon.png` so the app grid has no placeholder cubes.
