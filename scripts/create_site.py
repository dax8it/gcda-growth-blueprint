from pathlib import Path
import shutil, subprocess, math, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

root = Path('/Users/Shared/GITHUB/gcda-growth-blueprint')
gcda_repo = Path('/Users/Shared/GITHUB/gcda_audit/gcdadance')
assets_src_tmp = Path('/Users/Shared/GITHUB/gcda-growth-blueprint-assets')
site = root / 'site'
assets = site / 'assets'
media = site / 'media'
briefs = site / 'briefs'
for d in [assets, media, briefs, root/'scripts']:
    d.mkdir(parents=True, exist_ok=True)

# Curated GCDA visual proof assets from current site repo.
image_candidates = [
    gcda_repo/'public/images/hero/CNO05006.jpg',
    gcda_repo/'public/images/sections/classes/CNO04471.jpg',
    gcda_repo/'public/images/sections/classes/CNO04507.jpg',
    gcda_repo/'public/images/sections/classes/CNO04816.jpg',
    gcda_repo/'public/images/sections/studio/gallery/CNO03983.jpg',
    gcda_repo/'public/images/sections/studio/gallery/CNO04167.jpg',
]
for idx, src in enumerate(image_candidates, 1):
    if src.exists():
        out = assets / f'gcda-proof-{idx:02d}.jpg'
        im = Image.open(src).convert('RGB')
        im.thumbnail((1800, 1200), Image.Resampling.LANCZOS)
        im.save(out, quality=82, optimize=True)

# Docs / creative briefs.
brief_docs = {
'creative-brief.md': '''# GCDA Growth Blueprint — Creative Brief

## Project
A client-facing growth blueprint microsite and explainer video for Gulf Coast Dance Alliance, translating the SEO/UX/social audit into a clear action plan.

## Core problem
GCDA is not primarily missing brand polish. It was losing parent demand because the conversion path and proof layer needed repair: the contact form path had to be restored, the class finder needs a stable fallback, the homepage must speak directly to parents, and local schema/social proof/review systems need to become measurable growth assets.

## Strategic thesis
Before paid ads, repair the organic engine in under three days, then shift into growth: make the site easier to use, make GCDA easier to trust, make each program easier to find in Google, turn social into local proof, and measure weekly before scaling.

## Audience
Primary: parents of children and teens in Spanish Fort / Eastern Shore evaluating dance programs. Secondary: current GCDA families who can produce reviews, referrals, and proof. Tertiary: schools, preschools, PTAs, community calendars, family blogs, and local partners.

## Message
GCDA already has the ingredients: real students, faculty, location, and community. The growth work is to make those signals visible, measurable, and easy to act on.

## Tone
Warm, direct, parent-first, confident, operational. Avoid agency fluff.

## Visual direction
Blend Stripe-style clarity/control-panel precision with Airbnb-style warmth and human proof. Use blush, deep plum, warm ivory, and strong contrast. Photography should feel like evidence, not decoration.

## Primary future-site CTA
Book a Trial Class / Find Your Child’s Class.
''',
'website-redesign-brief.md': '''# Website Redesign Brief — GCDA Parent-First Site

## Goal
Turn gcdadance.com from a polished brochure into a parent conversion engine.

## Required fixes
1. Day 1: Contact form must render, submit through Netlify Forms, and notify info@gcdadance.com plus Carlos via a second notification.
2. Day 2: Class finder must render real classes or a stable fallback schedule path.
3. Day 2: Homepage H1 must include audience + service + location.
4. Day 2: Add trial-class CTA above the fold.
5. Day 3: Add LocalBusiness/DanceSchool JSON-LD.
6. Day 3: Add social links and proof section.
7. Day 3: Redirect old indexed posts and verify analytics/search tracking.
8. Growth phase: Add program pages, a New Family Guide, and optional voice chat agent once source content is verified.

## New IA
Home, Classes, Preschool/Tiny Dancers, Ballet, Hip-Hop, Acro/Tumbling, Tap + Jazz, Competitive Company, Summer/Seasonal Registration, New Family Guide, Faculty, Policies + FAQ, Contact / Trial Class.

## Above-fold copy direction
H1: Dance Classes for Kids & Teens in Spanish Fort
Subhead: Ballet, tap, jazz, hip-hop, acro, modern and competitive training for Eastern Shore families.
CTA 1: Find Your Child’s Class
CTA 2: Book a Trial Class

## Trust modules
Parent reviews, teacher credentials, years/community proof, real class photos/video, competition/recital highlights, beginner-friendly promise, age-appropriate instruction.
''',
'explainer-video-brief.md': '''# Explainer Video Brief — “Stop Losing the Families Already Looking”

## Format
60–75 second narrated explainer, 16:9, embedded on the growth blueprint site.

## Narrative arc
1. The problem is not awareness alone — it is conversion leakage.
2. The contact form is now repaired; the remaining core site fixes should finish inside three days.
3. Day two: make the class finder and parent path clear.
4. Day three: fix entity signals, redirects, analytics, and QA.
5. Then build organic demand capture pages.
6. Turn social into proof.
7. Add a voice chat agent only after verified school, schedule, teacher, location, hours, and policy content is ready.
8. 90-day outcome: easier to find, easier to trust, easier to join.

## Visual language
Control-room dashboard panels, parent journey funnel, red/amber/green repair states, three-day fix sprint, 30/60/90 growth timeline, optional voice-agent layer, warm dance photography as proof layer, subtle motion.

## Script
GCDA's site repair should not take ninety days. The core website fixes happen in the first three days. Day one: the contact form renders, Netlify detects it, and every submission routes to info at GCDA Dance with Carlos copied through a second notification. Day two: the class finder gets a stable path, with either live classes or a clear fallback schedule, so parents can find the right fit without waiting on a spinner. Day three: the homepage, schema, redirects, social links, analytics, and production QA are tightened, so the site is measurable and ready for growth. After that, the thirty, sixty, and ninety day plan becomes true growth work: programme pages, Google Business Profile improvements, parent reviews, social proof, local partnerships, and a New Family Guide. A voice chat agent can help once the schedule, teachers, hours, location, and policy answers are locked to verified content. Used correctly, it reduces parent friction, answers after-hours questions, and captures more trial class intent. If the source data is not reliable, we leave it out until it is.
''',
'growth-plan-30-60-90.md': '''# GCDA 30/60/90 Organic Growth Plan

## Immediate — first 3 days

### Day 1 — contact capture
Contact form renders on `/contact` and homepage, Netlify Forms detects the hidden mirror form, submissions include routing metadata, and notifications go to info@gcdadance.com with Carlos copied through a second notification. Verify form detection, production DOM, and Netlify form registry before calling it done.

### Day 2 — parent path
Fix the class finder/listing surface or add a stable fallback schedule path, add trial-class CTA language, and rewrite the homepage hero for parents and Google: `Dance Classes for Kids & Teens in Spanish Fort`.

### Day 3 — trust, tracking, and QA
Add LocalBusiness/DanceSchool schema, social sameAs links, `/company-team` sitemap inclusion, old indexed URL redirects, Search Console/GA4/GBP measurement checks, and production QA.

## 30 days — local foundation
Build current enrollment/seasonal landing page, publish parent FAQ content, start 3x/week organic social cadence, add program-page briefs and first two high-intent pages, and start the review sprint.

## 60 days — demand capture
Publish pages for preschool dance, ballet, hip-hop, acro/tumbling, competitive company; add truthful Eastern Shore/Daphne/Fairhope service-area content; build local backlinks through schools, preschools, PTAs, community calendars, and family blogs.

## 90 days — scale authority
Launch New Family Guide, build reusable photo/video/testimonial proof library, run monthly open-house/trial-class events, review weekly data and double down on pages/topics producing impressions, clicks, calls, or registrations.

## Optional voice chat agent — after content lock
An ElevenLabs voice chat agent is worth testing after schedule, teacher, location, hours, tuition/policy, and class-fit answers are verified in a knowledge base. Growth upside: answer after-hours parent questions, reduce decision friction, capture trial-class intent, and route complex questions to the contact form or staff. Guardrail: do not launch it if the source data is stale or if it invents schedule/pricing answers.
'''
}
for name, content in brief_docs.items():
    (briefs/name).write_text(content)

# Narration from previous ElevenLabs TTS call.
narration_src = assets_src_tmp / 'gcda-growth-explainer-narration.mp3'
narration_dst = media / 'gcda-growth-explainer-narration.mp3'
if narration_src.exists():
    shutil.copy2(narration_src, narration_dst)

# Deterministic MP4 explainer render.
W,H,fps = 1920,1080,24
try:
    dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1', str(narration_dst)], text=True).strip())
except Exception:
    dur = 72.0
scenes = [
('3-day site repair','Fix the conversion path before asking growth channels to work harder.',['Day 1: contact capture','Day 2: class path','Day 3: trust + QA'],'hero'),
('Day 1: contact form fixed','Netlify detects the form and submissions route to the right people.',['info@gcdadance.com','Carlos copied','Production verified'],'issues'),
('Day 2: parent path','Parents need classes, age fit, schedule clarity, and a low-friction next step.',['Stable class finder','Fallback schedule path','Book a trial class'],'homepage'),
('Day 3: trust + tracking','Make Google and parents understand GCDA clearly.',['DanceSchool schema','Redirects + sitemap','Analytics + GBP QA'],'seo'),
('Then growth starts','Use the repaired site to capture real demand.',['Preschool dance','Ballet / Hip-hop / Acro','Competitive company'],'pages'),
('Social becomes proof','Instagram, Facebook, and TikTok should show the studio in motion — not random updates.',['Teacher moments','Student growth','Parent answers'],'social'),
('Voice agent: later','Useful only after verified school, schedule, teacher, hours, location, and policy content is locked.',['Answer after-hours questions','Capture trial intent','Route to staff/forms'],'voice'),
('90-day outcome','GCDA becomes easier to find, easier to trust, and easier to join.',['More inquiries','More trial classes','More students'],'outcome'),
]
scene_dur = dur / len(scenes)
frames_dir = root / '.render-frames'
if frames_dir.exists(): shutil.rmtree(frames_dir)
frames_dir.mkdir(parents=True)

def font(size, bold=False):
    for c in ['/System/Library/Fonts/Supplemental/Avenir Next.ttc','/System/Library/Fonts/Supplemental/Arial.ttf','/Library/Fonts/Arial.ttf']:
        if Path(c).exists():
            try: return ImageFont.truetype(c, size=size, index=1 if bold and c.endswith('.ttc') else 0)
            except Exception: pass
    return ImageFont.load_default()
F_display=font(86, True); F_h1=font(64, True); F_h2=font(42, True); F_body=font(34); F_small=font(26); F_micro=font(20)

def draw_bg():
    im = Image.new('RGB',(W,H),'#fbf7f1'); px=im.load()
    c1=(255,248,240); c2=(245,226,236); c3=(31,21,51)
    for y in range(0,H,2):
      for x in range(0,W,2):
        u=x/W; v=y/H
        r=int(c1[0]*(1-v)+c2[0]*v+18*u*(1-v)); g=int(c1[1]*(1-v)+c2[1]*v); b=int(c1[2]*(1-v)+c2[2]*v+25*u)
        if x>W*.58 and y<H*.42:
            k=((x-W*.58)/(W*.42))*((H*.42-y)/(H*.42)); r=int(r*(1-k*.55)+c3[0]*(k*.55)); g=int(g*(1-k*.55)+c3[1]*(k*.55)); b=int(b*(1-k*.55)+c3[2]*(k*.55))
        for yy in (y,y+1):
          for xx in (x,x+1):
            if xx<W and yy<H: px[xx,yy]=(r,g,b)
    return im.filter(ImageFilter.GaussianBlur(.6))
BG=draw_bg()

def wrap(draw,text,fnt,max_w):
    words=text.split(); lines=[]; line=''
    for word in words:
        test=(line+' '+word).strip()
        if draw.textbbox((0,0),test,font=fnt)[2]<=max_w or not line: line=test
        else: lines.append(line); line=word
    if line: lines.append(line)
    return lines

def text(draw,xy,s,fnt,fill,max_w=None,gap=8):
    x,y=xy
    if max_w:
        for line in wrap(draw,s,fnt,max_w):
            draw.text((x,y),line,font=fnt,fill=fill); y += draw.textbbox((0,0),line,font=fnt)[3]+gap
        return y
    draw.text((x,y),s,font=fnt,fill=fill); return y+draw.textbbox((0,0),s,font=fnt)[3]

def rr(draw,box,r,fill,outline=None,w=1): draw.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=w)
proof_imgs=[]
for f in sorted(assets.glob('gcda-proof-*.jpg'))[:4]:
    try: proof_imgs.append(Image.open(f).convert('RGB'))
    except Exception: pass

total_frames = int(math.ceil(dur*fps))
for n in range(total_frames):
    t=n/fps; si=min(len(scenes)-1,int(t/scene_dur)); local=(t-si*scene_dur)/scene_dur
    title,subtitle,bullets,kind=scenes[si]
    im=BG.copy().convert('RGBA'); draw=ImageDraw.Draw(im)
    for j,(cx,cy,col) in enumerate([(1550,180,'#ff5b8c'),(1700,360,'#7c3aed'),(1350,890,'#f5b041')]):
        r=int(90+28*math.sin(t*.8+j)); overlay=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(overlay)
        od.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col+'55'); im=Image.alpha_composite(im,overlay.filter(ImageFilter.GaussianBlur(28))); draw=ImageDraw.Draw(im)
    draw.text((92,60),'GCDA / ORGANIC GROWTH SYSTEM',font=F_micro,fill='#7b5065'); rr(draw,(92,93,410,99),3,'#ff4f85')
    x=int(92+(1-min(1,local*2))*-40)
    text(draw,(x,150),title,F_display,'#23142e',920,10); text(draw,(x,360),subtitle,F_h2,'#5f4b62',830,10)
    for i,b in enumerate(bullets):
        yy=590+i*112; alpha=min(1,max(0,(local-.12*i)*2.4)); overlay=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(overlay)
        od.rounded_rectangle((x,yy,x+760,yy+82),radius=24,fill=(255,255,255,int(235*alpha)),outline=(233,213,226,int(255*alpha)),width=2)
        od.ellipse((x+24,yy+24,x+58,yy+58),fill=(255,79,133,int(255*alpha))); od.text((x+82,yy+22),b,font=F_small,fill=(43,27,51,int(255*alpha)))
        im=Image.alpha_composite(im,overlay); draw=ImageDraw.Draw(im)
    rr(draw,(1060,150,1810,910),36,'#ffffffdd','#ead6e2',2)
    if kind in ['hero','homepage','outcome'] and proof_imgs:
        for idx,img in enumerate(proof_imgs[:3]):
            crop=img.copy(); crop.thumbnail((430,320),Image.Resampling.LANCZOS); tile=Image.new('RGB',(430,300),'#eee'); tile.paste(crop,((430-crop.width)//2,(300-crop.height)//2))
            mask=Image.new('L',(430,300),0); md=ImageDraw.Draw(mask); md.rounded_rectangle((0,0,430,300),30,fill=255)
            im.paste(tile.convert('RGBA'),(1120+(idx%2)*260,230+idx*140),mask)
        draw=ImageDraw.Draw(im); text(draw,(1120,700),'Proof must feel alive — class energy, parent trust, and a clear trial path.',F_body,'#24152e',610)
    elif kind=='issues':
        y=235
        for a,b,c in [('CONTACT FORM','0 forms visible','#e11d48'),('CLASS FINDER','stuck loading','#f97316'),('TRIAL CTA','missing','#f59e0b')]:
            rr(draw,(1120,y,1750,y+130),24,'#fff7f7','#f4cdd8',2); draw.text((1155,y+26),a,font=F_micro,fill='#7b5065'); draw.text((1155,y+58),b,font=F_h2,fill=c); y+=165
    elif kind=='seo':
        center=(1435,525); radius=240; draw.ellipse((center[0]-radius,center[1]-radius,center[0]+radius,center[1]+radius),outline='#ead6e2',width=10)
        for ang,label in [(0,'Schema'),(72,'GBP'),(144,'Reviews'),(216,'Social'),(288,'Pages')]:
            a=math.radians(ang+t*5); px=center[0]+math.cos(a)*radius; py=center[1]+math.sin(a)*radius
            draw.ellipse((px-58,py-58,px+58,py+58),fill='#3b2144'); draw.text((px-42,py-10),label,font=F_micro,fill='white')
        draw.text((1325,500),'LOCAL\nENTITY',font=F_h2,fill='#24152e')
    elif kind=='pages':
        y=230
        for name,color in [('Preschool dance','#ff4f85'),('Ballet','#7c3aed'),('Hip-hop','#1f8a70'),('Acro / Tumbling','#f59e0b'),('Company team','#24152e')]:
            rr(draw,(1130,y,1740,y+72),18,'#fbf7f1','#ead6e2',2); draw.rectangle((1130,y,1138,y+72),fill=color); draw.text((1160,y+20),name,font=F_small,fill='#24152e'); y+=88
    elif kind=='social':
        for i,(name,val,color) in enumerate([('Instagram','1,728 followers','#e11d48'),('Facebook','category cleanup','#2563eb'),('TikTok','112 followers / 31 videos','#111827')]):
            y=250+i*160; rr(draw,(1130,y,1745,y+115),28,'#ffffff','#ead6e2',2); draw.ellipse((1160,y+32,1210,y+82),fill=color); draw.text((1235,y+24),name,font=F_h2,fill='#24152e'); draw.text((1235,y+70),val,font=F_small,fill='#6b5568')
    elif kind=='voice':
        y=245
        for name,val,color in [('Verified KB','schedule + teachers + policies','#7c3aed'),('Voice Q&A','after-hours parent help','#ff4f85'),('Lead capture','trial-class intent','#1f8a70')]:
            rr(draw,(1130,y,1745,y+115),28,'#ffffff','#ead6e2',2); draw.ellipse((1160,y+32,1210,y+82),fill=color); draw.text((1235,y+24),name,font=F_h2,fill='#24152e'); draw.text((1235,y+70),val,font=F_small,fill='#6b5568'); y+=160
    elif kind=='timeline':
        xs=[1190,1435,1680]; draw.line((1190,520,1680,520),fill='#ead6e2',width=10)
        for i,(lab,sub,col) in enumerate([('30','repair','#ff4f85'),('60','capture','#7c3aed'),('90','scale','#1f8a70')]):
            x0=xs[i]; draw.ellipse((x0-78,442,x0+78,598),fill=col); draw.text((x0-38,470),lab,font=F_h1,fill='white'); draw.text((x0-52,620),sub,font=F_small,fill='#24152e')
    prog=t/dur; rr(draw,(92,1008,1828,1028),10,'#ead6e2'); rr(draw,(92,1008,92+int(1736*prog),1028),10,'#ff4f85')
    im.convert('RGB').save(frames_dir/f'frame_{n:05d}.jpg',quality=90)

video_final=media/'gcda-growth-explainer.mp4'; poster=media/'gcda-growth-explainer-poster.jpg'; video_tmp=media/'gcda-growth-explainer.tmp.mp4'
cmd=['ffmpeg','-y','-framerate',str(fps),'-i',str(frames_dir/'frame_%05d.jpg')]
if narration_dst.exists(): cmd += ['-i',str(narration_dst),'-c:a','aac','-b:a','160k']
cmd += ['-c:v','libx264','-pix_fmt','yuv420p','-r',str(fps),'-shortest',str(video_tmp)]
subprocess.check_call(cmd)
subprocess.check_call(['ffmpeg','-y','-i',str(video_tmp),'-c','copy','-movflags','+faststart',str(video_final)])
subprocess.check_call(['ffmpeg','-y','-i',str(video_final),'-ss','00:00:03','-vframes','1',str(poster)])
shutil.rmtree(frames_dir); video_tmp.unlink(missing_ok=True)

imgs=sorted(assets.glob('gcda-proof-*.jpg')); hero_img=imgs[0].name if imgs else ''
photo_strip=''.join(f'<img src="/assets/{p.name}" alt="GCDA studio proof image">' for p in imgs[:3])
css=r''':root{--ink:#24152e;--muted:#6d5b6b;--paper:#fffaf4;--soft:#f6e9ef;--rose:#ff4f85;--plum:#3b2144;--violet:#7c3aed;--green:#1f8a70;--amber:#f5a524;--line:#ead6e2;--card:#ffffff;--shadow:rgba(66,38,82,.18) 0 24px 70px -28px,rgba(0,0,0,.08) 0 10px 24px -16px}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:'DM Sans',system-ui,-apple-system,Segoe UI,sans-serif;color:var(--ink);background:radial-gradient(circle at top right,#f1dbe8 0,#fffaf4 36%,#fbf4eb 100%);line-height:1.45}.nav{position:sticky;top:0;z-index:50;background:rgba(255,250,244,.83);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}.nav-inner{max-width:1180px;margin:auto;display:flex;align-items:center;justify-content:space-between;padding:16px 22px}.brand{font-weight:900;letter-spacing:-.04em}.brand span{color:var(--rose)}.nav a{color:var(--ink);text-decoration:none;font-size:14px;font-weight:700;margin-left:18px}.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;padding:13px 20px;font-weight:900;text-decoration:none;border:1px solid transparent;transition:.2s}.btn.primary{background:var(--ink);color:white;box-shadow:var(--shadow)}.btn.rose{background:var(--rose);color:white}.btn.ghost{background:white;color:var(--ink);border-color:var(--line)}.hero{max-width:1180px;margin:auto;padding:84px 22px 56px;display:grid;grid-template-columns:1.06fr .94fr;gap:48px;align-items:center}.eyebrow{color:var(--rose);font-weight:900;letter-spacing:.13em;text-transform:uppercase;font-size:12px}.hero h1{font-size:clamp(48px,7vw,92px);letter-spacing:-.075em;line-height:.92;margin:14px 0 22px}.hero p{font-size:22px;color:var(--muted);max-width:720px}.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}.dashboard{background:rgba(255,255,255,.7);border:1px solid var(--line);border-radius:34px;padding:18px;box-shadow:var(--shadow);position:relative;overflow:hidden}.dash-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.metric{background:white;border:1px solid var(--line);border-radius:24px;padding:18px;min-height:132px}.metric b{font-size:36px;letter-spacing:-.05em;display:block}.metric small{color:var(--muted);font-weight:800}.metric.danger{background:#fff4f6}.metric.good{background:#effaf5}.wide{grid-column:1/-1}.photo-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px}.photo-strip img{width:100%;height:142px;object-fit:cover;border-radius:20px}.section{max-width:1180px;margin:auto;padding:70px 22px}.section h2{font-size:clamp(34px,4vw,58px);letter-spacing:-.055em;line-height:1;margin:0 0 18px}.section-lede{font-size:20px;color:var(--muted);max-width:850px}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:28px}.card{background:rgba(255,255,255,.82);border:1px solid var(--line);border-radius:28px;padding:24px;box-shadow:var(--shadow)}.card h3{font-size:24px;letter-spacing:-.035em;margin:0 0 10px}.tag{display:inline-flex;border-radius:999px;background:var(--soft);padding:7px 11px;font-size:12px;font-weight:900;color:var(--plum);margin-bottom:14px}.video-wrap{background:#130c19;color:white;border-radius:38px;padding:28px;box-shadow:var(--shadow);display:grid;grid-template-columns:1.2fr .8fr;gap:28px;align-items:center}.video-wrap video{width:100%;border-radius:26px;box-shadow:0 22px 80px rgba(0,0,0,.4);background:#000}.video-wrap h2,.video-wrap p{color:white}.video-wrap p{opacity:.78}.timeline{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}.time{background:white;border:1px solid var(--line);border-radius:30px;padding:24px;position:relative;overflow:hidden}.time:before{content:attr(data-day);position:absolute;right:16px;top:6px;font-size:78px;font-weight:900;letter-spacing:-.08em;color:#f5dbe6}.time>*{position:relative}.brief-list{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:28px}.brief{background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px;text-decoration:none;color:var(--ink);box-shadow:var(--shadow)}.table{width:100%;border-collapse:collapse;background:white;border-radius:24px;overflow:hidden;box-shadow:var(--shadow);margin-top:28px}.table th,.table td{text-align:left;border-bottom:1px solid var(--line);padding:16px;vertical-align:top}.table th{background:#2b1834;color:white}.footer{padding:60px 22px;text-align:center;color:var(--muted);border-top:1px solid var(--line);background:#fffaf4}.socials a{margin:0 8px;color:var(--plum);font-weight:900}.quote{font-size:30px;letter-spacing:-.035em;line-height:1.18;background:var(--ink);color:white;border-radius:34px;padding:34px;margin-top:30px}.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}.mock{background:white;border:1px solid var(--line);border-radius:32px;padding:22px;box-shadow:var(--shadow)}.mock img{width:100%;height:310px;object-fit:cover;border-radius:24px}.check li{margin:10px 0}.check li::marker{color:var(--rose)}@media(max-width:880px){.hero,.video-wrap,.two{grid-template-columns:1fr}.cards,.timeline,.brief-list{grid-template-columns:1fr}.nav .links{display:none}.hero{padding-top:54px}.photo-strip img{height:108px}}'''
index=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GCDA Growth Blueprint | SEO + Enrollment Plan</title><meta name="description" content="A client-facing organic growth, SEO, social, and website conversion blueprint for Gulf Coast Dance Alliance."><meta property="og:title" content="GCDA Growth Blueprint"><meta property="og:description" content="Three-day site repair sprint, SEO plan, social proof engine, creative briefs, voice-agent option, and 30/60/90 growth roadmap."><meta property="og:image" content="/media/gcda-growth-explainer-poster.jpg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet"><link rel="stylesheet" href="/styles.css"></head><body><nav class="nav"><div class="nav-inner"><a class="brand" href="#top">GCDA<span>Growth</span></a><div class="links"><a href="#audit">Audit</a><a href="#video">Video</a><a href="#plan">Roadmap</a><a href="#voice-agent">Voice agent</a><a href="#briefs">Briefs</a><a href="https://gcdadance.com">Live Site</a></div><a class="btn rose" href="#immediate">Start fixes</a></div></nav><header class="hero" id="top"><div><div class="eyebrow">Organic enrollment system / no ads first</div><h1>Make GCDA easier to find, trust, and join.</h1><p>A public-facing growth blueprint translating the audit into a website redesign direction, SEO sprint, social proof engine, and 90-day enrollment plan for Spanish Fort and Eastern Shore families.</p><div class="hero-actions"><a class="btn primary" href="#immediate">View immediate fixes</a><a class="btn ghost" href="#video">Play explainer</a></div></div><aside class="dashboard"><div class="dash-grid"><div class="metric good"><small>Day 1 fixed</small><b>Form</b><span>Netlify contact capture restored and production verified</span></div><div class="metric danger"><small>Day 2 focus</small><b>Classes</b><span>finder/fallback schedule path is the next core fix</span></div><div class="metric good"><small>Exact local intent</small><b>#1</b><span>directional snapshot for dance studio Spanish Fort AL</span></div><div class="metric"><small>Core fix window</small><b>3</b><span>days for site repair before growth execution</span></div><div class="metric wide"><small>Thesis</small><b>Repair before ads.</b><span>The studio needs exposure, but first it needs a working path from parent curiosity to inquiry/trial/register.</span></div></div><div class="photo-strip">{photo_strip}</div></aside></header><section class="section" id="audit"><div class="eyebrow">What the audit says</div><h2>The problem is not just ranking. It is conversion reality.</h2><p class="section-lede">The site has a stronger modern visual baseline than several competitors, but the parent journey has broken surfaces and missing proof. We fix those first, then build the organic demand engine.</p><div class="cards"><article class="card"><span class="tag">Critical</span><h3>Contact path broken</h3><p>The live contact page showed no visible form after hydration. That means parents are forced to call or email manually.</p></article><article class="card"><span class="tag">Critical</span><h3>Class discovery blocked</h3><p>The classes page stayed on “Loading class finder…”. Families need age, style, day, time, and availability before they register.</p></article><article class="card"><span class="tag">High ROI</span><h3>Trust layer too thin</h3><p>Generic testimonials and “stay tuned” cards do not compete with studios showing reviews, awards, student proof, and parent confidence.</p></article></div><div class="quote">“GCDA does not need to buy attention first. It needs to stop losing the families already looking.”</div></section><section class="section" id="immediate"><div class="eyebrow">First 3 days</div><h2>Immediate fixes before the growth plan starts.</h2><div class="two"><div class="mock"><img src="/assets/{hero_img}" alt="GCDA proof"><h3>Future homepage direction</h3><p><strong>H1:</strong> Dance Classes for Kids & Teens in Spanish Fort</p><p><strong>CTA:</strong> Find Your Child’s Class / Book a Trial Class</p></div><div class="mock"><ul class="check"><li><strong>Day 1:</strong> contact form rendering, Netlify detection, info@gcdadance.com notification, and Carlos copy notification.</li><li><strong>Day 2:</strong> class finder repair or stable fallback schedule path, trial-class CTA, and parent-first hero copy.</li><li><strong>Day 3:</strong> schema, sitemap, redirects, social links, analytics/GBP checks, and production QA.</li><li><strong>After Day 3:</strong> review sprint, program pages, local partnerships, and social proof cadence.</li></ul></div></div></section><section class="section" id="video"><div class="video-wrap"><video controls preload="metadata" poster="/media/gcda-growth-explainer-poster.jpg"><source src="/media/gcda-growth-explainer.mp4" type="video/mp4"></video><div><div class="eyebrow">Narrated explainer</div><h2>From audit to enrollment engine.</h2><p>Press play for the updated British-female narrated version of the strategy. It frames the three-day site repair sprint, local SEO foundation, social proof engine, optional voice-agent layer, and 90-day growth plan in a client-friendly format.</p><a class="btn rose" href="/media/gcda-growth-explainer.mp4">Download MP4</a></div></div></section><section class="section" id="plan"><div class="eyebrow">Roadmap</div><h2>3-day repair, then 30 / 60 / 90 day growth.</h2><div class="timeline"><article class="time" data-day="1"><h3>Day 1: Contact capture</h3><p>Contact form renders, Netlify Forms detects it, submissions include routing metadata, and email notifications go to info@gcdadance.com with carlos@gcdadance.com copied through a second notification.</p></article><article class="time" data-day="2"><h3>Day 2: Class path</h3><p>Fix class finder/listing behavior or add a stable official schedule fallback, then make the hero and CTA speak directly to parents looking for kids and teens dance classes in Spanish Fort.</p></article><article class="time" data-day="3"><h3>Day 3: Trust + QA</h3><p>Add schema, sitemap/redirect cleanup, social links, measurement checks, and production QA so the site is ready for ongoing growth work.</p></article><article class="time" data-day="30"><h3>30 days: Local foundation</h3><p>Publish current enrollment/seasonal landing page, parent FAQ content, social cadence, first program pages, GBP cleanup, and review sprint.</p></article><article class="time" data-day="60"><h3>60 days: Demand capture</h3><p>Publish preschool, ballet, hip-hop, acro, company, seasonal, FAQ, and truthful Eastern Shore service-area pages.</p></article><article class="time" data-day="90"><h3>90 days: Scale proof</h3><p>Launch New Family Guide, build photo/video/review library, monthly trial/open-house events, partner links, and weekly ranking/conversion review.</p></article></div><table class="table"><tr><th>Track</th><th>What changes</th><th>Validation</th></tr><tr><td>Site repair</td><td>Form, class path, parent hero, schema, redirects, tracking.</td><td>Browser DOM, Netlify form registry, class clicks, mobile QA, analytics readback.</td></tr><tr><td>SEO</td><td>Program pages, local service-area content, GBP, reviews, backlinks.</td><td>GSC impressions/clicks, indexed pages, local rankings.</td></tr><tr><td>Social</td><td>Canonical profiles, proof cadence, studio-in-motion content.</td><td>Profile clicks, saves, shares, inquiries with UTM links.</td></tr><tr><td>Voice agent</td><td>Only after verified KB: schedules, teachers, policies, location, hours, and CTAs.</td><td>Prompt/KB readback, domain/widget QA, no hallucinated pricing/schedule answers.</td></tr></table></section><section class="section" id="voice-agent"><div class="eyebrow">Future enhancement</div><h2>ElevenLabs voice chat agent: possible, but only after content lock.</h2><div class="two"><article class="mock"><h3>How it helps growth</h3><ul class="check"><li>Answers after-hours parent questions about schedule, teachers, location, hours, policies, and class fit.</li><li>Reduces friction for parents who prefer talking over reading.</li><li>Captures trial-class intent and routes complex questions to the contact form or staff.</li><li>Creates a premium, helpful experience without requiring immediate staff response.</li></ul></article><article class="mock"><h3>Launch guardrails</h3><ul class="check"><li>Use a verified knowledge base only: schedule, teacher bios, location, hours, tuition/policy language, and FAQs.</li><li>No invented pricing, availability, or enrollment promises.</li><li>Clear AI disclosure and fallback CTAs: call, email, or contact form.</li><li>Ship after the three-day site repair and content QA, not before.</li></ul></article></div></div></section><section class="section" id="briefs"><div class="eyebrow">Creative briefs</div><h2>Strategy artifacts, ready to hand to designers, writers, and implementers.</h2><p class="section-lede">The site includes the actual working briefs as markdown files so the plan does not stay trapped in chat.</p><div class="brief-list"><a class="brief" href="/briefs/creative-brief.md"><h3>Creative Brief</h3><p>Positioning, audience, tone, and visual direction.</p></a><a class="brief" href="/briefs/website-redesign-brief.md"><h3>Website Redesign Brief</h3><p>Parent-first IA, required modules, and homepage copy direction.</p></a><a class="brief" href="/briefs/explainer-video-brief.md"><h3>Explainer Video Brief</h3><p>Script, scene arc, and motion language.</p></a><a class="brief" href="/briefs/growth-plan-30-60-90.md"><h3>30/60/90 Growth Plan</h3><p>Execution roadmap for organic enrollment growth.</p></a></div></section><footer class="footer"><p><strong>GCDA Growth Blueprint</strong> — strategy microsite for Gulf Coast Dance Alliance. Built from live audit evidence; measurement access still required for quantified trend attribution.</p><p class="socials"><a href="https://www.instagram.com/gcdadance">Instagram</a><a href="https://www.facebook.com/gcdadance">Facebook</a><a href="https://www.tiktok.com/@gcdadance_">TikTok</a><a href="https://gcdadance.com">gcdadance.com</a></p></footer><script>document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{{const el=document.querySelector(a.getAttribute('href'));if(el){{e.preventDefault();el.scrollIntoView({{behavior:'smooth'}})}}}}));</script></body></html>'''
(site/'styles.css').write_text(css); (site/'index.html').write_text(index); (site/'robots.txt').write_text('User-agent: *\nAllow: /\n')
(root/'netlify.toml').write_text('[build]\n  publish = "site"\n\n[[headers]]\n  for = "/media/*.mp4"\n  [headers.values]\n    Content-Type = "video/mp4"\n    Cache-Control = "public, max-age=31536000, immutable"\n\n[[headers]]\n  for = "/*"\n  [headers.values]\n    X-Content-Type-Options = "nosniff"\n    Referrer-Policy = "strict-origin-when-cross-origin"\n')
(root/'README.md').write_text('# GCDA Growth Blueprint\n\nClient-facing organic growth microsite for Gulf Coast Dance Alliance. Includes SEO/UX/social audit narrative, three-day site-repair sprint, 30/60/90 growth plan, ElevenLabs voice-agent option, creative briefs, and British-female narrated explainer video.\n\n## Live URLs\n\n- Production: https://gcda-growth-blueprint.netlify.app\n- GitHub: https://github.com/dax8it/gcda-growth-blueprint\n\n## Local preview\n\n```bash\npython3 -m http.server 4173 -d site\n```\n\nNetlify publish directory: `site`.\n')
(root/'.gitignore').write_text('.DS_Store\n.render-frames/\nnode_modules/\n.netlify/\n__pycache__/\n*.pyc\n')
meta=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size','-of','json',str(video_final)], text=True)
print('root',root); print('assets',[p.name for p in assets.glob('*')]); print('video',meta); print('poster',poster.exists(),poster.stat().st_size)
