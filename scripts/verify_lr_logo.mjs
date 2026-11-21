// ALL Create by LamberthRumpaidus
import { chromium } from "playwright";
import fs from "node:fs";
import http from "node:http";
import path from "node:path";

const projects = [
  { name:"lamberthrumpaidus", profile:true, selector:"#creator-logo" },
  { name:"Portfolio", selector:".brand-logo-img" },
  { name:"3D-Portfolio", selector:".lr-cyber-footer-mark img" },
  { name:"LANDLORD", selector:".lr-settings-mark img" },
  { name:"Rubaka", selector:".lr-rubaka-credit img" },
  { name:"Arcade_Collection_Game", selector:".global-footer .lr-monogram" },
  { name:"Omni_Science", selector:"footer .lr-monogram" },
  { name:"pixelpay", selector:".identity .lr-monogram" }
];
const root=path.resolve("sites");
const types={".html":"text/html; charset=utf-8",".js":"text/javascript; charset=utf-8",".css":"text/css; charset=utf-8",".svg":"image/svg+xml",".png":"image/png",".jpg":"image/jpeg",".woff":"font/woff",".woff2":"font/woff2",".json":"application/json",".glb":"model/gltf-binary"};
function serve(dir) {
  return http.createServer((req,res)=>{
    let pathName;
    try {pathName=decodeURIComponent(new URL(req.url,"http://localhost").pathname);}catch{res.writeHead(400).end();return;}
    const full=path.resolve(dir,"."+pathName);
    if(full!==dir&&!full.startsWith(dir+path.sep)){res.writeHead(403).end();return;}
    const file=fs.existsSync(full)&&fs.statSync(full).isDirectory()?path.join(full,"index.html"):full;
    if(!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404).end();return;}
    res.writeHead(200,{"content-type":types[path.extname(file).toLowerCase()]||"application/octet-stream"});
    fs.createReadStream(file).pipe(res);
  });
}
function assert(condition,message){if(!condition)throw new Error(message);}
const browser=await chromium.launch({headless:true,args:["--enable-webgl","--use-gl=angle","--use-angle=swiftshader","--disable-dev-shm-usage"]});
let failed=0;
for(const spec of projects){
  const dir=path.join(root,spec.name,spec.name==="3D-Portfolio"?"dist":"");
  if(spec.profile){
    fs.writeFileSync(path.join(dir,"__brand_check.html"),'<!doctype html><html><body style="background:#0b1424;display:grid;place-items:center;min-height:100vh;margin:0"><img id="creator-logo" src="./assets/lr-logo-v2.png" width="340" height="186" style="object-fit:contain" alt="L/R"></body></html>');
  }
  const server=serve(dir);
  await new Promise(resolve=>server.listen(0,"127.0.0.1",resolve));
  const page=await browser.newPage({viewport:{width:1280,height:800}});
  try{
    const url="http://127.0.0.1:"+server.address().port+(spec.profile?"/__brand_check.html":"/");
    await page.goto(url,{waitUntil:"domcontentloaded",timeout:45000});
    const logo=page.locator(spec.selector).first();
    await logo.waitFor({state:"attached",timeout:15000});
    const img=await logo.evaluate(async el=>{
      el.loading="eager";
      const image=new Image();
      image.src=el.currentSrc||el.src;
      await Promise.race([
        image.decode(),
        new Promise((_,reject)=>setTimeout(()=>reject(new Error("Logo image failed to decode within 12 seconds")),12000))
      ]);
      const width=image.naturalWidth,height=image.naturalHeight;
      const canvas=document.createElement("canvas");
      canvas.width=width;canvas.height=height;
      const ctx=canvas.getContext("2d",{willReadFrequently:true});
      ctx.drawImage(image,0,0);
      const pixels=ctx.getImageData(0,0,width,height).data;
      let above=0,below=0,lowerRows=0;
      for(let y=0;y<height;y++)for(let x=0;x<width;x++){
        const a=pixels[(y*width+x)*4+3];
        if(a>170){
          if(y<height*.25)above++;
          if(y>=height*.75)below++;
          if(y>=height*.65)lowerRows++;
        }
      }
      const rect=el.getBoundingClientRect();
      return{src:el.getAttribute("src"),width,height,above,below,lowerRows,rect:{width:rect.width,height:rect.height}};
    });
    assert(img.width>=600&&img.height>=300,spec.name+" used a small or truncated logo "+JSON.stringify(img));
    assert(img.below>img.width*img.height*.04,spec.name+" logo is visibly truncated in lower quarter");
    assert(img.above>img.width*img.height*.04,spec.name+" logo is missing upper quarter");
    assert(img.src.includes("lr-logo-v2")||img.src.includes("lr-credit-logo-v2"),spec.name+" references obsolete SVG");
    if(spec.name!=="LANDLORD")assert(img.rect.width>=24&&img.rect.height>=16,spec.name+" logo bounding box collapsed");
    if(!spec.profile&&spec.name!=="Portfolio"){
      const app=await page.locator('img[src*="app-logo.svg"], img[src*="app-logo-"]').count();
      if(spec.name!=="LANDLORD")assert(app>=1,spec.name+" lacks independent application logo");
    }
    await page.setViewportSize({width:390,height:844});
    await page.waitForTimeout(100);
    const mobile=await logo.evaluate(el=>{const r=el.getBoundingClientRect();return {width:r.width,height:r.height};});
    if(spec.name!=="LANDLORD")assert(mobile.width>=16&&mobile.height>=12,spec.name+" creator logo is collapsed on mobile");
    console.log("PASS "+spec.name+" | "+img.width+"x"+img.height+" PNG | lower quarter "+Math.round(img.below/(img.width*img.height)*100)+"% of canvas | mobile "+Math.round(mobile.width)+"x"+Math.round(mobile.height));
  }catch(e){failed++;console.error("FAIL "+spec.name+" "+e.message);}
  finally{await page.close();await new Promise(resolve=>server.close(resolve));}
}
await browser.close();
if(failed){console.error("LR visual checks FAILED: "+failed+" of "+projects.length);process.exitCode=1;}
else{console.log("ALL 8 LR brand visual checks PASSED.");}
