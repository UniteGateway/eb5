/* GoEB5 shared script — every feature runs only if its section exists on the page.
   window.goInit() is re-run by the single-page preview router after each page swap. */
window.goInit=function(){
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const fmt=n=>'$'+n.toLocaleString('en-US');

/* countdown to the 1 Jan 2027 inflation adjustment (US Eastern) */
const cd=$('#cd');
if(cd){clearInterval(window._cdI);const end=new Date('2027-01-01T00:00:00-05:00');const tick=()=>{const d=Math.max(0,end-new Date());cd.innerHTML=`<div>${Math.floor(d/864e5)}<small>days</small></div><div>${Math.floor(d/36e5)%24}<small>hours</small></div><div>${Math.floor(d/6e4)%60}<small>min</small></div>`};tick();window._cdI=setInterval(tick,30000)}

/* projects */
const P=[
 {t:'solar',img:'p1',feat:1,n:'Unite Texas Solar — McAllen Area',loc:'112-acre site, Hidalgo County area, Texas',cat:'Under evaluation',min:0,jobs:0,raise:0,funded:0,open:2,href:'texas-solar.html',d:'Proposed solar development with potential battery storage, promoted by Unite Group Inc., USA with local partner 112 Citrus LLC. EB-5 structuring under evaluation.'},
 {t:'solar',img:'p2',n:'Arizona Community Solar Portfolio',loc:'Pinal County, Arizona',cat:'Rural TEA',min:800000,jobs:310,raise:18,funded:41,open:1,d:'Twelve distributed solar sites serving schools, farms and municipal buildings under 20-year contracts.'},
 {t:'solar',img:'p3',n:'Nevada Solar Park & BESS 120 MW',loc:'Nye County, Nevada',cat:'Rural TEA',min:800000,jobs:560,raise:40,funded:100,open:0,d:'Utility-scale solar with 4-hour storage. Fully subscribed; shown for track record.'},
 {t:'infra',img:'p4',n:'South Texas Freight Rail Corridor',loc:'Rio Grande Valley, Texas',cat:'Infrastructure set-aside',min:800000,jobs:380,raise:30,funded:35,open:1,d:'Public-private short-line rail upgrade and cross-border freight terminal sponsored by a regional transport authority.'},
 {t:'infra',img:'p5',n:'Gulf Coast Logistics & Rail Hub',loc:'Houston, Texas',cat:'High-unemployment TEA',min:800000,jobs:640,raise:45,funded:58,open:1,d:'Intermodal rail yard, cold-chain warehouses and truck terminal next to the port corridor.'},
 {t:'infra',img:'p6',n:'EV Charging Corridor I-10',loc:'Texas · New Mexico · Arizona',cat:'Infrastructure set-aside',min:800000,jobs:290,raise:20,funded:22,open:1,d:'Fast-charging hubs with on-site solar canopies along a 1,200-mile interstate corridor.'}];
const pg=$('#pgrid');
if(pg){let pf='all';
 const card=p=>{const tag=`<span class="tag ${p.t=='solar'?'s':'i'}">${p.t=='solar'?'Solar':'Infrastructure'}</span>`;
  const nums=p.open==2?`<div class="kv"><div><b>112 acres</b>Proposed site</div><div><b>Texas</b>Location</div><div><b>EB-5</b>Pathway</div></div><span class="note">Feasibility and EB-5 eligibility being verified</span>`:`<div class="kv"><div><b>${fmt(p.min)}</b>Minimum</div><div><b>${p.jobs}</b>Est. jobs</div><div><b>$${p.raise}M</b>EB-5 raise</div></div><div><div class="bar"><i style="width:${p.funded}%"></i></div><span class="note">${p.funded}% subscribed${p.open?'':' · closed'}</span></div>`;
  const btn=p.open==2?`<a class="btn navy" href="${p.href}">Explore project</a>`:`<a class="btn ${p.open?'':'ghost'}" href="contact.html" data-pn="${p.n}">${p.open?'Request brochure':'View case study'}</a>`;
  return `<article class="proj"><div class="pimg"><img src="img/${p.img}.jpg" alt="${p.n}">${tag}</div><div class="in"><div><span class="tag">${p.cat}</span>${p.feat?'<span class="gold" style="font-size:11px;padding:3px 10px">Featured · Unite</span>':''}</div><h3 style="margin:0">${p.n}</h3><span class="note">${p.loc}</span><p style="margin:0;font-size:15px">${p.d}</p>${nums}${btn}</div></article>`};
 const lim=+(pg.dataset.limit||0);
 const render=()=>{const L=P.filter(p=>pf=='all'||(pf=='open'?p.open:p.t==pf));pg.innerHTML=(lim?L.slice(0,lim):L).map(card).join('')||'<p>No projects in this view.</p>'};
 $$('[data-f]').forEach(b=>b.onclick=()=>{pf=b.dataset.f;$$('[data-f]').forEach(x=>x.setAttribute('aria-pressed',x==b));render()});
 pg.addEventListener('click',e=>{const a=e.target.closest('[data-pn]');if(a){try{sessionStorage.setItem('goeb5project',a.dataset.pn)}catch(_){}}});
 render()}

/* countries — every ISO country with its flag */
const R={'Asia':'AF AM AZ BH BD BT BN KH CN CY GE HK IN ID IR IQ IL JP JO KZ KW KG LA LB MO MY MV MN MM NP KP OM PK PS PH QA SA SG KR LK SY TW TJ TH TL TR TM AE UZ VN YE','Europe':'AL AD AT BY BE BA BG HR CZ DK EE FI FR DE GR HU IS IE IT XK LV LI LT LU MT MD MC ME NL MK NO PL PT RO RU SM RS SK SI ES SE CH UA GB VA','Africa':'DZ AO BJ BW BF BI CV CM CF TD KM CG CD CI DJ EG GQ ER SZ ET GA GM GH GN GW KE LS LR LY MG MW ML MR MU MA MZ NA NE NG RW ST SN SC SL SO ZA SS SD TZ TG TN UG ZM ZW','Americas':'AG AR BS BB BZ BO BR CA CL CO CR CU DM DO EC SV GD GT GY HT HN JM MX NI PA PY PE PR KN LC VC SR TT US UY VE','Oceania':'AU FJ KI MH FM NR NZ PW PG WS SB TO TV VU'};
let dn;try{dn=new Intl.DisplayNames(['en'],{type:'region'})}catch(e){dn={of:c=>c}}
const flag=c=>c.replace(/./g,ch=>String.fromCodePoint(127397+ch.charCodeAt(0)));
const C=Object.entries(R).flatMap(([r,s])=>s.split(' ').map(c=>({c,r,n:c=='XK'?'Kosovo':dn.of(c)}))).sort((a,b)=>a.n.localeCompare(b.n));
$$('select.country').forEach(s=>{s.innerHTML=C.map(x=>`<option value="${x.c}">${flag(x.c)} ${x.n}</option>`).join('');s.value='IN'});
const fl=$('#flags');
if(fl){const note={IN:'Unreserved EB-5 is backlogged for India, but rural, high-unemployment and infrastructure set-aside visas are currently available. H-1B and F-1 holders in the US may file I-485 concurrently.',CN:'Mainland-China-born investors face a long unreserved backlog; set-aside categories are currently available.',VN:'Vietnam-born investors should check the monthly Visa Bulletin; set-aside categories offer a faster route.',US:'US citizens are not eligible, but we work with US-based families sponsoring relatives abroad.'};
 let reg='All',sel='IN';
 $('#regions').innerHTML=['All',...Object.keys(R)].map(r=>`<button data-r="${r}" aria-pressed="${r=='All'}">${r}</button>`).join('');
 const render=()=>{const q=$('#csearch').value.trim().toLowerCase();const L=C.filter(x=>(reg=='All'||x.r==reg)&&(!q||x.n.toLowerCase().includes(q)));fl.innerHTML=L.map(x=>`<button data-c="${x.c}" aria-pressed="${x.c==sel}"><span class="f">${flag(x.c)}</span>${x.n}</button>`).join('')||'<p>No country matches.</p>'};
 const show=c=>{sel=c;const x=C.find(y=>y.c==c);$('#cinfo').innerHTML=`<span class="f">${flag(c)}</span><div><h3 style="margin:0 0 4px">${x.n}</h3><span class="note">${note[c]||`Investors from ${x.n} can apply for EB-5 at the current minimums. Visa numbers for ${x.n}-born applicants are generally current; we help prepare source-of-funds evidence and consular processing at the nearest US embassy.`}</span></div>`;$$('select.country').forEach(s=>s.value=c);render()};
 $('#regions').onclick=e=>{const b=e.target.closest('[data-r]');if(!b)return;reg=b.dataset.r;$$('[data-r]').forEach(x=>x.setAttribute('aria-pressed',x==b));render()};
 fl.onclick=e=>{const b=e.target.closest('[data-c]');if(b)show(b.dataset.c)};
 $('#csearch').oninput=render;render()}

/* cost calculator */
if($('#amt')){const calc=()=>{const a=+$('#amt').value,ad=+$('#adm').value||0,l=+$('#leg').value||0,fx=+$('#fx').value||0,f=+$('#fam').value;const t=a+ad+l;$('#tUSD').textContent=fmt(t)+' · '+fmt(a)+' at-risk capital';$('#tINR').textContent='₹'+Math.round(t*fx/1e5).toLocaleString('en-IN')+' lakh';const y=Math.ceil(t/(250000*f));$('#lrs').textContent=`With ${f} family member${f>1?'s':''} remitting under LRS, about ${y} financial year${y>1?'s':''} needed at $250,000 each.`;try{localStorage.setItem('goeb5calc',JSON.stringify({fx,ad,l}))}catch(e){}};
 try{const s=JSON.parse(localStorage.getItem('goeb5calc'));if(s){$('#fx').value=s.fx;$('#adm').value=s.ad;$('#leg').value=s.l}}catch(e){}
 ['amt','adm','leg','fx','fam'].forEach(id=>$('#'+id).addEventListener('input',calc));calc()}

/* eligibility check */
const qz=$('#quiz');
if(qz){const Q=['Are you 18 or older?','Can you invest at least $800,000 plus fees?','Can you document the lawful source of these funds?','Are you free of serious criminal or immigration-fraud history?','Do you accept that the capital is at risk for several years?'];const A=Array(Q.length).fill(null);
 qz.innerHTML=Q.map((q,i)=>`<div class="q"><span>${q}</span><div class="yn"><button type="button" data-q="${i}" data-v="1" aria-pressed="false">Yes</button><button type="button" data-q="${i}" data-v="0" aria-pressed="false">No</button></div></div>`).join('');
 qz.onclick=e=>{const b=e.target.closest('[data-q]');if(!b)return;A[+b.dataset.q]=+b.dataset.v;b.parentNode.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x==b));const done=A.filter(x=>x!==null).length,yes=A.filter(x=>x===1).length;
  $('#qres').innerHTML=done<Q.length?`${done} of ${Q.length} answered.`:yes==Q.length?'<strong style="color:var(--ok)">You look like a strong EB-5 candidate.</strong> <a href="contact.html">Book a consultation</a> to match a project and start your source-of-funds file.':A[2]===0?'<strong>Source of funds is the key hurdle.</strong> Gifts, property sales and loans can all qualify with the right paperwork — talk to us.':'<strong>Some points need review.</strong> An advisor can tell you whether they can be resolved before you file.'}}

/* consultation slot picker */
const sl=$('#slots');
if(sl){const di=$('#bdate');const t=new Date();t.setDate(t.getDate()+1);di.min=t.toISOString().slice(0,10);di.value=di.min;
 const S=['10:00','11:00','12:00','14:30','15:30','16:30','18:00'];sl.innerHTML=S.map(s=>`<button type="button" data-s="${s}" aria-pressed="false">${s} IST</button>`).join('');
 sl.onclick=e=>{const b=e.target.closest('[data-s]');if(!b)return;$$('[data-s]').forEach(x=>x.setAttribute('aria-pressed',x==b));$('#btime').value=b.dataset.s}}

/* forms — validated in the page; no data leaves the browser until a backend is connected */
try{const p=sessionStorage.getItem('goeb5project');if(p&&$('#m'))$('#m').value='I would like the brochure for '+p+'.'}catch(e){}
$$('form[data-form]').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const ok=f.querySelector('.ok');ok.style.display='block';
 const miss=[...f.querySelectorAll('[required]')].find(i=>i.type=='checkbox'?!i.checked:!i.value.trim());
 const em=f.querySelector('input[type=email]');
 if(miss){ok.style.color='var(--acc)';ok.textContent='Please complete: '+(f.querySelector(`label[for="${miss.id}"]`)?.textContent.trim()||'required fields')+'.';miss.focus();return}
 if(em&&!/^\S+@\S+\.\S+$/.test(em.value)){ok.style.color='var(--acc)';ok.textContent='Please enter a valid email.';return}
 if(f.querySelector('#btime')&&!f.querySelector('#btime').value){ok.style.color='var(--acc)';ok.textContent='Please choose a time slot.';return}
 ok.style.color='';ok.textContent=f.dataset.form+' received. This preview does not send data yet — connect the form to your CRM or email before going live.'}));

/* gallery lightbox */
const lb=$('#lb');
if(lb){$$('.gal button').forEach(b=>b.onclick=()=>{lb.querySelector('img').src=b.querySelector('img').src;lb.querySelector('img').alt=b.querySelector('img').alt;lb.querySelector('p').textContent=b.querySelector('span').textContent;lb.classList.add('on');lb.querySelector('.x').focus()});
 const close=()=>lb.classList.remove('on');lb.querySelector('.x').onclick=close;lb.onclick=e=>{if(e.target==lb)close()};document.onkeydown=e=>{if(e.key=='Escape')close()}}
};
{const m=document.querySelector('.menu'),l=document.getElementById('links');if(m&&l)m.onclick=()=>{const o=l.classList.toggle('open');m.setAttribute('aria-expanded',o);m.textContent=o?'Close':'Menu'}}

/* social share links (work without accounts); profile links come from SOCIAL below */
window.SOCIAL={facebook:'',instagram:'',linkedin:'',x:'',youtube:'',whatsapp:''}; /* paste profile URLs here when ready */
{const u=encodeURIComponent('https://goeb5.in'),t=encodeURIComponent('GoEB5 — US green card through EB-5 investment in solar and infrastructure');
 const share={facebook:`https://www.facebook.com/sharer/sharer.php?u=${u}`,linkedin:`https://www.linkedin.com/sharing/share-offsite/?url=${u}`,x:`https://twitter.com/intent/tweet?url=${u}&text=${t}`,whatsapp:`https://wa.me/?text=${t}%20${u}`,telegram:`https://t.me/share/url?url=${u}&text=${t}`,email:`mailto:?subject=${t}&body=${u}`};
 window.goSocial=()=>{document.querySelectorAll('[data-share]').forEach(a=>{a.href=share[a.dataset.share]});document.querySelectorAll('[data-follow]').forEach(a=>{const v=window.SOCIAL[a.dataset.follow];if(v){a.href=v;a.removeAttribute('data-spa')}})};}
if(!window.GO_SPA){goInit();goSocial()}
