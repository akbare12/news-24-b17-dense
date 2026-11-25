import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SANS='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SANSB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
CREAM=(250,246,236); INK=(20,20,22); RED=(178,34,34); NAVY=(24,48,84); GREEN=(34,120,60); BLUE=(30,90,160); ORANGE=(200,100,20); GREY=(110,110,110); LGREY=(228,224,214); GOLD=(176,132,30)
CHIPCOL={'CONFIRMED':GREEN,'OFFICIAL':BLUE,'REPORTED':(70,90,120),'CLAIM':ORANGE}
def wrap(d,t,f,w):
    lines=[]; cur=''
    for wd in t.split():
        s=(cur+' '+wd).strip()
        if d.textlength(s,font=f)<=w: cur=s
        else:
            if cur: lines.append(cur)
            cur=wd
    if cur: lines.append(cur)
    return lines
def chip(d,x,y,t,fs=8):
    f=F(SANSB,fs); w=int(d.textlength(t,font=f))+8
    d.rounded_rectangle([x,y,x+w,y+12],2,fill=CHIPCOL.get(t,(90,90,90))); d.text((x+4,y+1),t,font=f,fill='white'); return w
def scene(d,b,k):
    bx0,by0,bx1,by1=b; orig=d; tmp=Image.new('RGB',(300,100)); d=ImageDraw.Draw(tmp); x0,y0,x1,y1=0,0,300,100
    d.rectangle([0,0,299,99],fill=(226,236,244)); d.rectangle([0,0,299,99],outline=INK,width=1)
    cx=(x0+x1)//2; cy=(y0+y1)//2
    if k=='tower':
        d.rectangle([x0,y1-26,x1,y1],fill=(40,44,60)); d.rectangle([x0,y0+8,x1,y0+22],fill=(16,18,34))
        for i in range(7):
            bx=x0+8+i*((x1-x0-16)//7); bh=34+((i*13)%30); d.rectangle([bx,y1-26-bh,bx+16,y1-26],fill=(52,58,84))
        d.rectangle([cx-9,y0+18,cx+9,y1-26],fill=(24,28,52)); d.polygon([(cx-9,y0+18),(cx,y0+2),(cx+9,y0+18)],fill=(200,40,40))
        for yy in range(y0+24,y1-30,9):
            for xx in range(cx-6,cx+7,4): d.point((xx,yy),fill=(255,220,120))
        d.ellipse([x1-34,y0+6,x1-14,y0+26],fill=(255,214,90)); d.polygon([(x1-40,y0+30),(x1-22,y0+18),(x1-30,y0+34)],fill=(90,90,90)); d.ellipse([x1-52,y0+44,x1-40,y0+56],fill=(255,120,40)); d.ellipse([x1-46,y0+38,x1-34,y0+50],fill=(255,170,60))
    elif k=='party':
        d.rectangle([x0,y0+30,x1,y1],fill=(150,30,30)); d.rectangle([x0,y0+30,x1,y0+44],fill=(110,20,20)); d.polygon([(x0,y0+30),(cx,y0+4),(x1,y0+30)],fill=(178,34,34))
        for i in range(5):
            px=x0+14+i*((x1-x0-28)//5); d.rectangle([px,y0+52,px+10,y1-8],fill=(250,246,236))
        d.rectangle([cx-16,y0+58,cx+16,y1-8],fill=(60,10,10)); d.ellipse([cx-14,y0+14,cx+14,y0+42],fill=(255,214,90)); d.text((cx-4,y0+20),'*',font=F(SANSB,16),fill=(178,34,34))
        d.rectangle([x0,y1-8,x1,y1],fill=(60,60,60))
    elif k=='court':
        d.rectangle([x0,y1-14,x1,y1],fill=(120,120,110)); d.rectangle([x0+10,y0+34,x1-10,y0+44],fill=(200,200,190)); d.rectangle([x0+16,y0+44,x0+26,y1-14],fill=(180,180,170)); d.rectangle([x1-26,y0+44,x1-16,y1-14],fill=(180,180,170)); d.polygon([(x0+6,y0+34),(cx,y0+6),(x1-6,y0+34)],fill=(24,48,84))
        d.rectangle([cx-34,y0+52,cx+34,y0+72],fill=(24,48,84)); d.text((cx-30,y0+55),'HUAWEI',font=F(SANSB,11),fill='white'); d.rectangle([cx-40,y0+78,cx-6,y0+84],fill=(176,132,30)); d.rectangle([cx+6,y0+78,cx+40,y0+84],fill=(176,132,30)); d.line([cx,y0+72,cx,y0+78],fill=(176,132,30),width=3)
    elif k=='drones':
        d.rectangle([x0,y0,x1,y1],fill=(18,22,40)); d.ellipse([x1-30,y0+6,x1-12,y0+24],fill=(255,220,120))
        for i in range(5):
            bx=x0+10+i*((x1-x0-20)//5); bh=20+((i*17)%26); d.rectangle([bx,y1-bh,bx+14,y1],fill=(40,46,70))
        d.ellipse([cx-16,cy-26,cx+16,cy+6],fill=(255,120,40)); d.ellipse([cx-10,cy-18,cx+10,cy-2],fill=(255,180,60)); d.polygon([(cx-26,cy-8),(cx-14,cy-2),(cx-26,cy+4)],fill=(90,90,90)); d.ellipse([x0+16,y0+12,x0+24,y0+20],fill=(200,200,200)); d.ellipse([x0+34,y0+18,x0+42,y0+26],fill=(200,200,200))
    elif k=='trophy':
        d.rectangle([x0,y0,x1,y1],fill=(20,90,60)); d.ellipse([x0+8,y0+8,x0+34,y0+34],fill=(255,255,255)); d.ellipse([x1-34,y0+8,x1-8,y0+34],fill=(255,0,0)); d.ellipse([cx-14,y0+22,cx+14,y0+62],fill=(255,214,90)); d.rectangle([cx-16,y0+20,cx+16,y0+30],fill=(255,214,90)); d.rectangle([cx-4,y0+62,cx+4,y0+74],fill=(255,214,90)); d.rectangle([cx-16,y0+74,cx+16,y0+80],fill=(255,214,90)); d.text((cx-30,y1-16),'SEN 1-0 MAR',font=F(SANSB,9),fill='white')
    elif k=='ship':
        d.rectangle([x0,y0,x1,y1],fill=(190,220,235)); d.rectangle([x0,y0+40,x1,y0+52],fill=(120,170,200)); d.rectangle([cx-52,y0+30,cx+52,y0+52],fill=(178,34,34)); d.rectangle([cx-52,y0+30,cx+52,y0+38],fill=(120,40,40)); d.rectangle([cx-30,y0+16,cx-6,y0+30],fill=(240,240,240)); d.rectangle([cx+6,y0+16,cx+30,y0+30],fill=(240,240,240)); d.polygon([(x1-30,y0+8),(x1-16,y0+26),(x1-30,y0+26)],fill=(60,60,60)); d.ellipse([x0+10,y0+10,x0+22,y0+22],fill=(255,120,40))
    elif k=='chart':
        d.rectangle([x0,y0,x1,y1],fill=(250,246,236)); d.line([x0+10,y1-12,x1-8,y0+16],fill=GREEN,width=3); d.line([x0+10,y1-12,x1-8,y1-12],fill=INK,width=1); d.line([x0+10,y0+8,x0+10,y1-12],fill=INK,width=1); d.text((x0+12,y0+6),'50,018',font=F(SANSB,13),fill=GREEN); d.text((x1-58,y1-26),'DOW',font=F(SANSB,10),fill=INK)
    elif k=='data':
        d.rectangle([x0,y0,x1,y1],fill=(30,30,40)); 
        for i in range(4):
            rx=x0+8+i*((x1-x0-16)//4); d.rectangle([rx,y0+10,rx+20,y1-8],fill=(50,55,75)); d.rectangle([rx+3,y0+14,rx+17,y0+20],fill=(255,60,60)); d.rectangle([rx+3,y0+24,rx+17,y0+28],fill=(255,60,60))
        d.text((cx-26,y1-16),'CODE RED',font=F(SANSB,9),fill=(255,80,80))
    elif k=='heli':
        d.rectangle([x0,y0,x1,y1],fill=(200,215,225)); d.polygon([(x0+6,y0+34),(x1-6,y0+34),(x1-6,y0+22),(x0+30,y0+22)],fill=(90,90,90)); d.ellipse([x0+8,y0+34,x0+40,y0+52],fill=(60,90,60)); d.rectangle([x0+44,y0+40,x0+70,y0+48],fill=(60,90,60)); d.line([x0+30,y0+18,x1-10,y0+18],fill=INK,width=2); d.polygon([(x0+8,y1-6),(x0+30,y0+56),(x0+44,y1-6)],fill=(120,110,90)); d.polygon([(x1-44,y1-6),(x1-22,y0+56),(x1-8,y1-6)],fill=(120,110,90))
    elif k=='market':
        d.rectangle([x0,y0,x1,y1],fill=(240,230,200)); d.rectangle([x0+8,y0+30,x1-8,y0+44],fill=(178,34,34)); d.rectangle([x0+8,y0+44,x1-8,y1-8],fill=(250,246,236)); d.rectangle([cx-24,y0+50,cx+24,y1-8],fill=(120,140,170)); d.text((cx-20,y0+56),'25',font=F(SANSB,12),fill='white')
    elif k=='desert':
        d.rectangle([x0,y0,x1,y1],fill=(235,205,150)); d.ellipse([x1-28,y0+6,x1-10,y0+24],fill=(255,200,80)); d.polygon([(x0,y1),(x0+50,y0+40),(x1,y1)],fill=(200,160,100)); d.polygon([(x0+40,y1),(x0+90,y0+52),(x1-10,y1)],fill=(180,140,85)); d.text((cx-22,y0+10),'60 km',font=F(SANSB,11),fill=INK)
    elif k=='bus':
        d.rectangle([x0,y0,x1,y1],fill=(210,220,230)); d.rectangle([x0+8,y0+22,x1-8,y0+50],fill=(240,200,60)); d.rectangle([x0+12,y0+28,x0+30,y0+40],fill=(180,220,240)); d.rectangle([x0+34,y0+28,x0+52,y0+40],fill=(180,220,240)); d.ellipse([x0+16,y0+50,x0+28,y0+60],fill=INK); d.ellipse([x1-28,y0+50,x1-16,y0+60],fill=INK); d.text((cx-14,y0+4),'25',font=F(SANSB,11),fill=RED)
    else:
        d.rectangle([x0,y0,x1,y1],fill=(16,20,44))
        for i in range(40): d.point((x0+4+(i*13)%(x1-x0-8),y0+4+(i*7)%(y1-y0-8)),fill='white')
        d.polygon([(cx-4,y1-8),(cx+4,y1-8),(cx+2,y0+22),(cx-2,y0+22)],fill=(240,240,240)); d.polygon([(cx-16,y0+22),(cx+16,y0+22),(cx,y0+6)],fill=(255,80,60)); d.ellipse([cx-22,y0+30,cx+22,y0+52],fill=(200,200,210))
    orig._image.paste(tmp.resize((bx1-bx0,by1-by0)),(bx0,by0))
HERO=[('1 RIYADH','MIDDLE EAST','CONFIRMED',"Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, for the second time in a week. 11 hurt: 2 Saudis, 2 Indians, 3 Nepalis, 4 Egyptians.",'Saudi officials · AP','tower'),('2 SHANGHAI','ASIA','OFFICIAL','China probes Shanghai party chief Chen Jining',"Chen Jining, 62, is probed for 'serious violations'. He is the 4th Politburo member to fall in a probe this year.",'CCDI','party'),('3 NEW YORK','US / TECH','CONFIRMED','Huawei guilty on 10 of 12 counts','A US federal jury found Huawei guilty of trade-secret theft and bank fraud, but cleared it of racketeering. Sentencing Sep 2027; Huawei appeals.','US court','court')]
CARDS=[('4 ZAPORIZHZHIA','EUROPE / WAR','REPORTED','Russian attacks kill 9 across Ukraine in a day','9 killed and 81 hurt as Russia launches 96 drones; Kyiv says 73 were shot down or jammed.','Ukraine officials','drones'),('5 CAS','AFRICA / SPORT','OFFICIAL','CAS hands Senegal back the AFCON title','Morocco forfeit 3-0, so Senegal win 1-0 and take the Africa Cup back.','CAS','trophy'),('6 HORMUZ','MIDDLE EAST','REPORTED','IRGC attacks container ship in Hormuz','A container ship was attacked at 18:58 UTC; its navigation was disabled near Khasab, Oman.','UKMTO','ship'),('7 NEW YORK','WORLD / MARKETS','CONFIRMED','Dow closes above 50,000 for the first time','The Dow closed at 50,018. Taiex jumped 8.99% to a record 40,122 as the Nasdaq slid 1.5%.','Market close','chart'),('8 REDMOND','WORLD / TECH','REPORTED',"Microsoft declares 'Code Red' after historic outage",'After a 24-hour outage, Microsoft targets full recovery within 1 hour with 5 workstreams.','Reuters','data'),('9 ESKISEHIR','EUROPE','REPORTED','Turkish military helicopter crash kills 5','An AS-532 military helicopter crashed in Eskisehir at 19:52 UTC, killing all 5 aboard.','Turkish officials','heli'),('10 CARTAGENA','AMERICAS','REPORTED','Supermarket hostages: 25 held in Cartagena','25 hostages were held in a Cartagena supermarket; 5 elderly women were freed.','Colombian officials','market'),('11 ADEN','MIDDLE EAST','REPORTED','Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden in Yemen at 16:51 UTC.','Wires','desert'),('12 LAHJ','MIDDLE EAST','REPORTED','Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes hit a bus and truck in Wadi Maabaq, Lahj: 25 killed or missing, 6 hurt.','Yemeni officials','bus'),('13 JIUQUAN','WORLD / SPACE','OFFICIAL','China names first foreign astronaut for Tiangong','Shenzhou-24 crew: Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan. Launch Wed 25 Nov.','CMSA','rocket')]
ALSO=[('14','Ankara','Haftar visits Turkey first time','REP'),('15','London','UK sanctions Houthis + 4 officials','OFF'),('16','Villavicencio','Car bomb injures 23','REP'),('17','Gaza','Israel kills Hamas security chief','REP'),('18','Baghdad','Iraq takes control of Kurdish oil','OFF'),('19','Gaza','Meningitis alert, 272 cases in Oct','OFF'),('20','DR Congo','Missing Cessna 208, rebels claim hit','CLA'),('21','Hanoi','Hot-pot blast kills at least 6','REP'),('22','Gulf of Finland','Ukraine hits ship Sparta II','REP'),('23','Kuala Lumpur','Malaysia to return migrants','OFF'),('24','Ulleungdo','S. Korea shelter order, jets in ADIZ','OFF'),('25','Dhaka','Hasina plans return on 16 Dec','REP'),('26','The Hague','14 nations back ICJ Myanmar ruling','REP'),('27','Jakarta','Indonesia names 2 VP candidates','OFF'),('28','Beijing','China sentences official Ma to death','OFF'),('29','Brussels','NATO vows defence vs space threat','OFF'),('30','Mexico City','US drone aided El Chapo capture','REP'),('31','San Salvador','Bukele names 3 soldiers killed','OFF'),('32','Ottawa','Pentagon rebukes Canada, 41.9% ready','REP'),('33','Washington','US adds Megaspeed to blacklist','OFF'),('34','Kyiv','Zelensky urges talks soon','REP'),('35','Ras Al Khaimah','Bus-truck crash kills 13','REP'),('36','London','England record 5,258 heat deaths','OFF'),('37','Kourou','Ariane 6 lofts 36 Amazon satellites','OFF'),('38','Cikande','Factory-fire toll rises to 26','REP')]
UTC=[('02:15','NATO vows space defence'),('08:16','Hanoi blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
NUMS=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow close'),('+8.99%','Taiex record'),('25','killed/missing, Yemen'),('26','Cikande fire toll'),('10/12','Huawei counts guilty'),('96','drones at Ukraine')]
REGS=[('Europe',9,RED),('Middle East',8,(200,120,30)),('Asia',8,NAVY),('Africa',2,GREEN),('Americas',7,(120,60,120)),('World / Space',4,GREY)]

NA=[(-168,66),(-140,70),(-125,71),(-110,68),(-95,69),(-85,66),(-80,73),(-65,60),(-55,52),(-60,47),(-70,42),(-75,35),(-80,26),(-85,20),(-90,15),(-95,16),(-100,20),(-105,23),(-110,28),(-117,33),(-125,40),(-125,48),(-135,58),(-155,60),(-168,66)]
SA=[(-80,10),(-70,12),(-60,8),(-52,5),(-50,0),(-40,-5),(-35,-8),(-40,-20),(-48,-28),(-55,-35),(-65,-41),(-70,-50),(-73,-53),(-70,-30),(-72,-20),(-77,-12),(-80,-3),(-80,10)]
AF=[(-17,15),(-10,30),(0,36),(10,37),(20,32),(32,31),(35,28),(43,12),(51,11),(48,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-27),(12,-18),(9,-2),(9,4),(-8,5),(-17,15)]
EU=[(-10,36),(-9,43),(-2,48),(0,50),(5,53),(8,57),(10,59),(18,56),(21,55),(28,59),(30,60),(25,65),(20,70),(15,70),(5,60),(-5,58),(-10,50),(-10,36)]
AS=[(30,60),(40,68),(60,69),(70,72),(90,75),(110,76),(130,72),(150,70),(170,66),(178,65),(162,60),(158,52),(142,50),(140,40),(130,35),(127,35),(122,31),(120,25),(110,20),(105,10),(100,8),(98,15),(95,16),(90,22),(85,20),(80,13),(77,8),(72,20),(66,25),(60,25),(55,26),(50,30),(45,29),(40,36),(35,36),(30,36),(30,42),(30,60)]
AU=[(114,-22),(114,-32),(124,-33),(130,-32),(137,-35),(140,-38),(147,-39),(150,-37),(153,-27),(146,-19),(142,-11),(136,-12),(132,-12),(126,-14),(122,-17),(114,-22)]
GL=[(-45,60),(-40,64),(-30,68),(-22,70),(-25,76),(-40,80),(-55,76),(-58,70),(-52,64),(-45,60)]
PINS=[(1,24.7,46.7,-14,-8),(2,31.2,121.5,0,0),(3,40.7,-74.0,14,-4),(4,47.8,35.2,0,0),(5,14.7,-17.4,0,0),(6,26.5,56.3,14,-12),(7,40.7,-74.0,-16,10),(8,47.6,-122.1,0,0),(9,39.8,30.5,-12,8),(10,10.4,-75.5,0,0),(11,12.8,45.0,16,12),(12,13.0,44.9,-16,10),(13,39.8,98.5,0,0)]
LEGEND=['1 Riyadh — PIF tower hit','2 Shanghai — Chen probed','3 New York — Huawei guilty','4 Zaporizhzhia — 9 killed','5 Dakar — Senegal AFCON title','6 Hormuz — ship attacked','7 New York — Dow 50,018','8 Redmond — Code Red','9 Eskisehir — heli crash, 5','10 Cartagena — 25 hostages','11 Aden — Houthis 60 km away','12 Lahj — Saudi strikes, 25','13 Jiuquan — Shenzhou-24 crew']
def main():
    im=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(im); M=16; x=M; w=W-2*M
    d.text((x,8),'THE WORLD ON ONE DAY',font=F(SANSB,11),fill=RED); d.text((x+560,8),'38 STORIES  ·  6 REGIONS  ·  13 PICTURES  ·  ALL FROM TUESDAY 24 NOVEMBER 2026',font=F(SANSB,10),fill=INK)
    d.text((x,24),'Tuesday 24 November 2026',font=F(SERIF,34),fill=INK)
    d.text((x,62),'Riyadh tower hit again.  Shanghai party chief probed.  Huawei guilty on 10 of 12 counts.',font=F(SERIF,13),fill=RED)
    d.line([x,82,x+w,82],fill=INK,width=2)
    bx=x; tot=sum(n for _,n,_ in REGS)
    for name,n,c in REGS:
        seg=int(w*n/tot); d.rectangle([bx,86,bx+seg,102],fill=c); d.text((bx+3,87),name+' '+str(n),font=F(SANSB,9),fill='white'); bx+=seg
    d.text((x,108),'THE DAY IN UTC',font=F(SANSB,10),fill=RED)
    ux=x
    for t,ev in UTC:
        d.text((ux,120),t,font=F(SANSB,10),fill=RED); d.text((ux,130),ev,font=F(SANS,8),fill=INK); ux+=w//7
    d.rectangle([x,146,x+w,182],outline=INK,width=1); nx=x+6
    for v,lab in NUMS:
        d.text((nx,148),v,font=F(SERIF,17),fill=RED); d.text((nx,168),lab,font=F(SANS,8),fill=INK); nx+=(w-12)//8
    hy=186; hw=(w-12)//3; hh=196
    for i,(kick,field,ch,hl,deck,src,kind) in enumerate(HERO):
        px=x+i*(hw+6); scene(d,(px,hy,px+hw,hy+88),kind)
        d.text((px,hy+92),kick+'  ·  '+field,font=F(SANSB,10),fill=RED); cw=chip(d,px,hy+107,ch); d.text((px+cw+6,hy+108),'('+src+')',font=F(SANS,8),fill=GREY)
        lines=wrap(d,hl,F(SANSB,13),hw)
        yy=hy+122
        for ln in lines[:2]: d.text((px,yy),ln,font=F(SANSB,13),fill=INK); yy+=15
        yy=hy+154
        for ln in wrap(d,deck,F(SANS,10),hw)[:3]: d.text((px,yy),ln,font=F(SANS,10),fill=(50,50,50)); yy+=11
    cy=hy+hh+8; cw2=(w-16)//5; chh=120
    for r in range(2):
        for c in range(5):
            i=r*5+c; city,field,ch,hl,deck,src,kind=CARDS[i]; px=x+c*(cw2+4); py=cy+r*(chh+6)
            d.rectangle([px,py,px+cw2,py+chh],outline=INK,width=1)
            scene(d,(px,py,px+cw2,py+52),kind)
            d.text((px+3,py+55),city+'  ·  '+field,font=F(SANSB,8),fill=RED)
            yy=py+66
            for ln in wrap(d,hl,F(SANSB,10),cw2-6)[:2]: d.text((px+3,yy),ln,font=F(SANSB,10),fill=INK); yy+=11
            for ln in wrap(d,deck,F(SANS,8),cw2-6)[:2]: d.text((px+3,yy),ln,font=F(SANS,8),fill=(50,50,50)); yy+=9
            chip(d,px+3,py+chh-14,ch,7)
    my=cy+2*(chh+6)+6; mh=150; mx0=x; mw2=624; my0=my
    d.text((x,my-2),'WHERE IT HAPPENED',font=F(SANSB,11),fill=RED)
    my+=14; mh-=14
    def proj(lon,lat): return (mx0+(lon+170)/360*mw2, my+(75-lat)/130*mh)
    d.rectangle([mx0,my,mx0+mw2,my+mh],fill=(210,228,240),outline=INK,width=1)
    for poly in [NA,SA,AF,AS,AU,GL,EU]:
        d.polygon([proj(lo,la) for lo,la in poly],fill=(140,180,120),outline=(60,90,60))
    for n,la,lo,dx,dy in PINS:
        px,py=proj(lo,la)
        if dx or dy: d.line([px,py,px+dx,py+dy],fill=RED,width=1)
        qx,qy=px+dx,py+dy; d.ellipse([qx-7,qy-7,qx+7,qy+7],fill=RED,outline='white',width=1); d.text((qx-3,qy-5),str(n),font=F(SANSB,8),fill='white')
    lx=mx0+mw2+10; d.text((lx,my),'PINNED STORIES',font=F(SANSB,11),fill=RED)
    for i,lg in enumerate(LEGEND): d.text((lx,my+16+i*9),lg,font=F(SANS,9),fill=INK)
    ay=my+mh+8; d.text((x,ay),'ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES',font=F(SANSB,11),fill=RED)
    ay+=16; colw=(w-16)//3
    for i,(n,city,hl,cc) in enumerate(ALSO):
        col=i//9; row=i%9; px=x+col*(colw+8); py=ay+row*12
        f=F(SANSB,7); d.rounded_rectangle([px,py,px+20,py+11],2,fill=CHIPCOL.get({'REP':'REPORTED','OFF':'OFFICIAL','CLA':'CLAIM'}[cc],GREY)); d.text((px+3,py+1),cc,font=f,fill='white')
        d.text((px+23,py),n+' '+city+': '+hl,font=F(SANS,8),fill=INK)
    dy=ay+9*12+6; d.rectangle([x,dy,x+w,dy+70],fill=(255,235,235),outline=RED,width=1)
    d.text((x+6,dy+4),'DATE CHECK',font=F(SANSB,11),fill=RED)
    dt="Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) · Nvidia Huang returns as CEO (Mon 23 Nov) · EU sanctions package 22 (Mon 23 Nov) · COP31 ends no deal (Sun 22 Nov) · corvette Merkury sinks (Sat 22 Nov) · El Chapo Isidro arrested (Fri 20 Nov) · Cikande factory fire starts (Sat 21 Nov) · Trump hush-money appeal verdict (Mon 23 Nov) · ATP Finals (Sun 22 Nov) · Las Vegas GP (Sat 21 Nov) · Peru quake M6.7 (Fri 20 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session picks VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns (16 Dec)."
    yy=dy+18
    for ln in wrap(d,dt,F(SANS,9),w-12): d.text((x+6,yy),ln,font=F(SANS,9),fill=INK); yy+=11
    fy=dy+74; d.text((x,fy),'Sources: dailysummaryof.com · Reuters · AP · UKMTO · CAS · CMSA · Focus Taiwan/CNA · UKHSA · WHO.',font=F(SANS,8),fill=GREY)
    d.text((x,fy+11),'Chips: CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side\'s claim. Scenes are drawn illustrations, not photographs.',font=F(SANS,8),fill=GREY)
    os.makedirs(os.path.dirname(OUT),exist_ok=True); im.save(OUT,optimize=True)
if __name__=='__main__': main()
