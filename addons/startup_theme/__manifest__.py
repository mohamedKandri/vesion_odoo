{
    "name": "Startup Theme",
    "summary": "Company-branded, Enterprise-style look for the app grid home menu.",
    "version": "19.0.1.0.0",
    "category": "Hidden",
    "license": "LGPL-3",
    "author": "vesion",
    "depends": ["startup_home_menu"],
    "assets": {
        "web.assets_backend": [
            "startup_theme/static/src/webclient/apps_menu_branding/apps_menu_branding.js",
            "startup_theme/static/src/webclient/apps_menu_branding/apps_menu_branding.xml",
            "startup_theme/static/src/scss/apps_menu_theme.scss",
        ],
    },
    "installable": True,
    "application": False,
}
