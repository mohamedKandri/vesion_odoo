import {patch} from "@web/core/utils/patch";
import {AppsMenu} from "@web_responsive/components/apps_menu/apps_menu.esm";
import {session} from "@web/session";

patch(AppsMenu.prototype, {
    get startupBranding() {
        return session.startup_branding || {};
    },
});
