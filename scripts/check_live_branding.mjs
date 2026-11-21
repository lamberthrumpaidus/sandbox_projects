const sites = [
 ["Portfolio","https://lamberthrumpaidus.netlify.app/"],
 ["3D-Portfolio","https://3d-lamberthrumpaidus.netlify.app/"],
 ["Rubaka","https://rubaka.netlify.app/"],
 ["Arcade_Collection_Game","https://arcadecollectiongame.netlify.app/"],
 ["Omni_Science","https://omn1sc1ence.netlify.app/"]
];
let updated=0,stale=0,unavailable=0;
for(const [name,url] of sites){
 try{
  const response=await fetch(url,{signal:AbortSignal.timeout(18000),redirect:"follow",headers:{"cache-control":"no-cache","user-agent":"GitHubActions-LR-brand-validation"}});
  const html=await response.text();
  if(!response.ok||!html.includes("<html")){unavailable++;console.log("LIVE_UNAVAILABLE "+name+" HTTP "+response.status);continue;}
  const re=/lr-credit-logo-v2(?:-[a-f0-9]+)?\.png/g;
  if(!re.test(html)){stale++;console.log("LIVE_STALE "+name+" no repaired logo in fetched HTML");continue;}
  updated++;
  console.log("LIVE_UPDATED "+name+" new full logo reference is deployed");
 }catch(e){unavailable++;console.log("LIVE_UNAVAILABLE "+name+" "+e.message);}
}
console.log("LIVE_SUMMARY updated="+updated+" stale="+stale+" unavailable="+unavailable+" (known domains only; not proof of visual rendering)");
