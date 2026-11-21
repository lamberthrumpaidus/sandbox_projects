// ALL Create by LamberthRumpaidus
import { chromium } from "playwright";
import fs from "node:fs";
import http from "node:http";
import path from "node:path";

const projects = ["Rubaka", "Arcade_Collection_Game", "Omni_Science", "pixelpay", "3D-Portfolio"];
const assert = (pass, text) => { if (!pass) throw new Error(text); };
const root = path.resolve("sites");
const contentTypes = new Map([
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".png", "image/png"],
  [".webp", "image/webp"],
  [".jpg", "image/jpeg"],
  [".jpeg", "image/jpeg"],
  [".woff", "font/woff"],
  [".woff2", "font/woff2"],
  [".json", "application/json"],
  [".wasm", "application/wasm"],
  [".glb", "model/gltf-binary"],
  [".mp3", "audio/mpeg"],
  [".wav", "audio/wav"]
]);

function serve(directory) {
  return http.createServer((req, res) => {
    const loc = decodeURIComponent(new URL(req.url || "/", "http://localhost").pathname);
    const filename = path.resolve(directory, "." + loc);
    if (!(filename === directory || filename.startsWith(directory + path.sep))) {
      res.writeHead(403); res.end(); return;
    }
    const file = fs.existsSync(filename) && fs.statSync(filename).isDirectory() ?
      path.join(filename, "index.html") : filename;
    if (!fs.existsSync(file) || !fs.statSync(file).isFile()) {
      res.writeHead(404); res.end(); return;
    }
    res.writeHead(200, {"content-type":contentTypes.get(path.extname(file).toLowerCase()) || "application/octet-stream"});
    fs.createReadStream(file).pipe(res);
  });
}

const browser = await chromium.launch({
  headless:true,
  args:["--enable-webgl","--use-gl=angle","--use-angle=swiftshader","--disable-dev-shm-usage"]
});
let failures = [];
for (const project of projects) {
  const directory = path.join(root, project, project === "3D-Portfolio" ? "dist" : "");
  const server = serve(directory);
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  const port = server.address().port;
  const url = "http://127.0.0.1:" + port;
  const context = await browser.newContext({viewport:{width:1280,height:800},reducedMotion:"reduce"});
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  try {
    await page.goto(url, {waitUntil:"domcontentloaded",timeout:35000});
    await page.locator("img[src*='app-logo']").first().waitFor({state:"attached",timeout:12000});
    const logos = await page.locator("img[src*='app-logo']").count();
    const credits = await page.locator("img[src*='lr-credit-logo-v2']").count();
    assert(logos >= 1, project + ": missing dedicated app logo");
    assert(credits >= 1, project + ": missing creator credit logo");
    if (project === "Omni_Science") {
      await page.locator("#lab-search").waitFor({state:"visible"});
      await page.locator("#expr").fill("1+2");
      await page.locator("#btn-calc").click();
      await page.waitForTimeout(400);
      const result = await page.locator("#output-val").innerText();
      assert(result.trim() === "3", "Omni-Science calculation returned " + result);
      await page.locator("#lab-favorite").click();
      assert(await page.locator("#lab-favorite").getAttribute("aria-pressed") === "true", "Omni favorite failed");
    } else if (project === "pixelpay") {
      await page.locator("#pp-contrast").click();
      assert(await page.locator("#pp-contrast").getAttribute("aria-pressed") === "true", "PixelPay contrast toggle failed");
      await page.locator("#pp-faq-search").fill("top");
      assert(await page.locator("#faq details").count() > 0, "PixelPay FAQs missing");
    } else if (project === "Arcade_Collection_Game") {
      await page.locator("#arcade-search").fill("Tic Tac");
      assert(Number(await page.locator("#arcade-visible-count").innerText()) === 1, "Arcade filtering failed");
      await page.locator(".arcade-game-tile:not([hidden]) .btn-menu").first().click();
      assert(await page.locator("#tictactoe").evaluate(el => getComputedStyle(el).display !== "none"), "Arcade game switch failed");
      await page.evaluate(() => GameApp.switch("cocokkartu"));
      assert(await page.locator("#memory-board .memory-card").count() === 16, "Memory game missing cards");
      await page.locator("#memory-board .memory-card").first().click();
      assert(await page.locator("#memory-board .memory-card.flipped").count() === 1, "Memory game flip failed");
    } else if (project === "Rubaka") {
      await page.locator("#rb-help-toggle").click();
      assert(await page.locator("#rb-help").isVisible(), "Rubaka help failed to open");
      await page.locator("#rb-help-close").click();
      assert(await page.locator("#rb-help").isHidden(), "Rubaka help failed to close");
    } else if (project === "3D-Portfolio") {
      await page.locator("#pj-help").click();
      assert(await page.locator("#pj-shortcuts").evaluate(el => el.open), "3D shortcut dialog failed");
      await page.locator("#pj-shortcuts-close").click();
      assert(await page.locator("#pj-shortcuts").evaluate(el => !el.open), "3D shortcut dialog failed to close");
      await page.locator("#pj-motion").click();
      assert(await page.locator("#pj-motion").getAttribute("aria-pressed") === "true", "3D motion toggle failed");
    }
    await page.setViewportSize({width:390,height:844});
    await page.waitForTimeout(160);
    const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
    assert(overflow < 85, project + ": substantial horizontal overflow on mobile: " + overflow + "px");
    if (errors.length && project !== "3D-Portfolio") throw new Error("Unhandled JavaScript error: " + errors.slice(0,3).join(" | "));
    if (errors.length) console.log(project + " browser warnings/errors: " + errors.slice(0,3).join(" | "));
    console.log("PASS " + project + " — app/credit logos, interaction and mobile layout");
  } catch(error) {
    const msg=project + ": " + error.message + (errors.length?" | pageerror "+errors.slice(0,3).join(" | "):"");
    failures.push(msg);
    console.log("FAIL "+msg);
  } finally {
    await context.close();
    await new Promise(resolve => server.close(resolve));
  }
}
await browser.close();
if (failures.length) {
  console.error("Smoke checks failed: " + failures.length);
  process.exitCode=1;
} else {
  console.log("All 5 website smoke tests passed.");
}
