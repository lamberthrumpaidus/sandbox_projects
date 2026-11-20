/**
 * @author Lamberth Rumpaidus
 */
"use strict";

(async function adblockUtama() {
    while (!Spicetify?.Platform?.AdManagers) {
        await new Promise(r => setTimeout(r, 500));
    }

    const { Platform, CosmosAsync } = Spicetify;
    const statusAkun = Platform.UserAPI?._product_state || Platform.ProductStateAPI?.productStateApi;

    async function hajarIklan() {
        try {
            await statusAkun.putOverridesValues({
                pairs: { ads: "0", catalogue: "premium", product: "premium", type: "premium" }
            });

            const pengelola = Platform.AdManagers;
            if (pengelola) {
                if (pengelola.audio) await pengelola.audio.disable();
                if (pengelola.billboard) await pengelola.billboard.disable();
                if (pengelola.leaderboard) await pengelola.leaderboard.disableLeaderboard();
                if (pengelola.sponsoredPlaylist) await pengelola.sponsoredPlaylist.disable();
            }

            if (CosmosAsync) {
                await CosmosAsync.post("sp://ads/v1/testing/playtime", { value: -1e11 });
            }
        } catch (e) {}
    }

    const gaya = document.createElement("style");
    gaya.innerHTML = `
        .main-leaderboardComponent-container, .sponsor-container, .desktop-ad-track, 
        .main-topBar-UpgradeButton, div[data-testid*="hpto"], .ScclvBC0NsMgQLQC { 
            display: none !important; 
        }
    `;
    document.head.appendChild(gaya);

    await hajarIklan();
    statusAkun.subValues({ keys: ["ads", "product", "type"] }, hajarIklan);
    console.log("Adblock by Lamberth: Aktif Total");
})();