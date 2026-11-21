import { createHash } from "node:crypto";
const sites=[
  ["Portfolio","https://lamberthrumpaidus.netlify.app/"],
  ["3D-Portfolio","https://3d-lamberthrumpaidus.netlify.app/"],
  ["Rubaka","https://rubaka.netlify.app/"],
  ["Arcade_Collection_Game","https://arcadecollectiongame.netlify.app/"],
  ["Omni_Science","https://omn1sc1ence.netlify.app/"]
];
let failures=0;
let expectedHash="";
for(const [name,url] of sites){
  try{
    const res=await fetch(url,{signal:AbortSignal.timeout(20000),headers:{"Cache-Control":"no-cache"}});
    if(!res.ok)throw new Error("HTML HTTP "+res.status);
    const html=await res.text();
    const match=html.match(/<img\b[^>]*\bsrc=["']([^"']*lr-credit-logo-v2(?:-[a-f0-9]+)?\.png(?:\?[^"']*)?)["']/i);
    if(!match)throw new Error("Rendered HTML does not reference corrected PNG");
    const assetUrl=new URL(match[1],url).href;
    const img=await fetch(assetUrl,{signal:AbortSignal.timeout(20000)});
    if(!img.ok)throw new Error("PNG HTTP "+img.status+" at "+assetUrl);
    const data=Buffer.from(await img.arrayBuffer());
    if(!data.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])))throw new Error("Asset is not a valid PNG");
    const width=data.readUInt32BE(16),height=data.readUInt32BE(20);
    if(width<600||height<300||data.length<50000)throw new Error("Degraded logo asset "+width+"x"+height+" "+data.length+" bytes");
    const sha=createHash("sha256").update(data).digest("hex");
    if(expectedHash && expectedHash!==sha)throw new Error("Logo bytes differ across sites");
    expectedHash=sha;
    console.log("LIVE_ASSET_PASS "+name+" "+width+"x"+height+" "+data.length+" bytes at "+assetUrl);
  }catch(e){failures++;console.error("LIVE_ASSET_FAIL "+name+" "+e.message);}
}
if(failures)process.exitCode=1;
else console.log("ALL 5 NETLIFY SITES DELIVER THE IDENTICAL VERIFIED PNG IMAGE");
