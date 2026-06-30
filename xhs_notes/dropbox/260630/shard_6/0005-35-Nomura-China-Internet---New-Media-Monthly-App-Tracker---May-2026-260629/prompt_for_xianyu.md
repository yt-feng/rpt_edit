你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# China Internet & New Media

EQUITY: INTERNET & NEW MEDIA

## Monthly App Tracker – May 2026

## China's Instagram, Xiaohongshu, registers first-ever decline in time spent

MAS rose 1.2% y-y and total monthly time spent increased 10.1% y-y in May
Monthly active smartphone (MAS) users in China rose 1.2% y-y to 1.28bn in May 2026. China's MAS has remained stable in recent months. Total monthly time spent (MTS) grew 10.1% y-y in May, largely on par with the 10.3% y-y growth in April 2026.

## Ecommerce apps showed lukewarm growth despite 618 promotions

The MTS of Taobao app [owned by Alibaba (BABA US, Buy)] and JD (JD US, Buy) app rebounded by 17% and 19% sequentially, respectively, in May, driven by 618 promotions (which started in mid-May). But the y-y trend looks lackluster – Taobao’s MTS in May rose only 7% y-y, while JD’s declined 10% from a high base a year ago when it launched the food delivery business followed by substantial investment in user acquisition. In terms of DAU (daily active users), Taobao recorded modest 1% y-y growth, while JD’s declined 3% y-y. For PDD (PDD US, Neutral), MTS rose 13% y-y and 3% m-m – PDD business is not as prone to 618 promotions as the platform has a low-price strategy throughout the year.

The weakness in the China ecommerce market will likely be reflected in soft ecommerce sales for the June quarter to be reported by our covered ecommerce platforms. NOM projects an 8% decline in customer management revenue (CMR) for Alibaba and a 7% decline in JDR's revenue in the June quarter. Please see our BABA preview note for more detailed discussions.

## Weakening user engagement with the travel-booking apps

The user engagement of the travel sector deteriorated further into May. The MTS of Trip.com's (TCOM US, Neutral) two China apps Ctrip and Qunar in May fell 19% and 14% y-y, respectively, weighed down by 9% and 13% declines of DAU. Fliggy (owned by BABA) saw a bigger 15% y-y decline, mainly due to an 11% drop of DAU. Even the state-backed ticketing app Umetrip (unlisted) was not immune to this weakness, reversing the growth trend of previous months and ending May with flat year-over-year MTS. We believe the hikes in air fuel surcharge likely resulted in the weakness.

## Xiaohongshu registers the first-ever decline in time spent

According to Questmobile, the MTS of Xiaohongshu (XHS, unlisted) declined 1% y-y, the first-ever decline since we began tracking its app in 2020. The decline was a combined result of 3% growth of DAU and a 4% drop of average daily time spent per DAU (DTSD) We think XHS is likely experiencing the same “AI headwind” as other information portals like search – users are increasingly switching to AI chatbots for information and knowledge discovery which poses a threat to the core value proposition offered by XHS. XHS has secured an exclusive online streaming right for the FIFA World Cup 2026 in China, which we believe is likely aimed at broadening its demographic reach and further drive the user growth. Based on Questmobile, the DAU of XHS reached 122mn in May 2026, up 3% y-y.

## DeepSeek returned to second position in native AI chatbot field

According to Questmobile, Doubao (owned by Bytedance) appeared to have further widened its lead in the crowded field of AI chatbots with DAU growth of 5% m-m and 3.6x y-y, reaching 158mn. Following the successful release of DeepSeek - V4 models in late April, DeepSeek's consumer app climbed to the second position with DAU standing at 30.5mn, up by 6% m-m, surpassing Qwen app (owned by BABA) at 27.9mn (down 5% m-m but up 76.6x from a low base a year ago). Additionally, Ant's AI assistant, Afu, saw impressive user growth with DAU rising 11% m-m to 5.1mn, likely driven by the launch of a free consultation service that interprets users' medical checkup reports.

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK

Jialong.shi@NOM.com

+852 2252 1409

## Rachel Guo - NIHK

rachel.guo@NOM.com

+852 2252 1400

## Overview of leading Chinese apps

Much of the traffic flow in May 2026 was dominated by apps owned by Bytedance, Tencent (700 HK, Buy), Baidu (BIDU US, Buy), and Alibaba. In particular, Bytedance's apps took five spots among the Top-20 in terms of both monthly active users (MAU) and time spent share in May, according to QuestMobile. Tencent's WeChat alone recorded an 19.0% share in terms of time spent by Chinese mobile users, leading the next two apps – Douyin and Douyin Lite (both unlisted, owned by Bytedance) – with 18.7% and 6.3% time-spent share, respectively.

Fig. 1: Top-20 apps in China, by MAU and time spent – May

<table><tr><td colspan="5">Top 20 Apps in MAU: MAUs change and penetration</td></tr><tr><td>App Name</td><td>Rank M-M chg</td><td>Penetration</td><td>Penetration Y-Y</td><td>Penetration M-M</td></tr><tr><td>WeChat</td><td>-</td><td>90.1%</td><td>2.8ppt</td><td>0.9ppt</td></tr><tr><td>Douyin</td><td>-</td><td>80.4%</td><td>8.7ppt</td><td>1.0ppt</td></tr><tr><td>Taobao</td><td>-</td><td>77.1%</td><td>-0.4ppt</td><td>2.1ppt</td></tr><tr><td>Alipay</td><td>-</td><td>73.6%</td><td>0.3ppt</td><td>0.5ppt</td></tr><tr><td>Amap</td><td>-</td><td>72.4%</td><td>0.5ppt</td><td>1.0ppt</td></tr><tr><td>Pinduoduo</td><td>-</td><td>55.8%</td><td>0.7ppt</td><td>-0.4ppt</td></tr><tr><td>Sogou Keyboard</td><td>-</td><td>54.4%</td><td>4.4ppt</td><td>-0.1ppt</td></tr><tr><td>JD</td><td>↑</td><td>50.7%</td><td>1.5ppt</td><td>3.3ppt</td></tr><tr><td>Baidu</td><td>↓</td><td>50.7%</td><td>-5.3ppt</td><td>-0.1ppt</td></tr><tr><td>QQ</td><td>↓</td><td>49.4%</td><td>-0.8ppt</td><td>0.9ppt</td></tr><tr><td>Baidu Maps</td><td>-</td><td>44.8%</td><td>-2.1ppt</td><td>0.9ppt</td></tr><tr><td>Meituan</td><td>-</td><td>40.9%</td><td>0.7ppt</td><td>0.5ppt</td></tr><tr><td>Weibo</td><td>↑</td><td>38.7%</td><td>-0.3ppt</td><td>1.5ppt</td></tr><tr><td>Baidu Keyboard</td><td>↓</td><td>38.7%</td><td>-0.8ppt</td><td>0.3ppt</td></tr><tr><td>Kuaishou</td><td>-</td><td>35.3%</td><td>-1.2ppt</td><td>0.1ppt</td></tr><tr><td>Toutiao</td><td>-</td><td>29.9%</td><td>-1.0ppt</td><td>0.4ppt</td></tr><tr><td>Doubao</td><td>-</td><td>28.9%</td><td>18.5ppt</td><td>0.8ppt</td></tr><tr><td>Red Fruit Free Short Dram</td><td>↑</td><td>27.9%</td><td>12.1ppt</td><td>1.7ppt</td></tr><tr><td>QQ Browser</td><td>↓</td><td>26.8%</td><td>-6.8ppt</td><td>-0.9ppt</td></tr><tr><td>Douyin Lite</td><td>-</td><td>26.0%</td><td>3.5ppt</td><td>0.1ppt</td></tr></table>

Source: QuestMobile, NOM

<table><tr><td colspan="5">Time spent share for top 20 Chinese mobile apps in May</td></tr><tr><td>App Name</td><td>Rank M-M chg</td><td>Time spent share</td><td>Time spent share Y-Y</td><td>Time spent share M-M</td></tr><tr><td>WeChat</td><td>-</td><td>19.0%</td><td>-1.5ppt</td><td>-0.4ppt</td></tr><tr><td>Douyin</td><td>-</td><td>18.7%</td><td>2.6ppt</td><td>0.6ppt</td></tr><tr><td>Douyin Lite</td><td>-</td><td>6.3%</td><td>1.2ppt</td><td>0.1ppt</td></tr><tr><td>Red Fruit Free Short Drama</td><td></td><td>4.0%</td><td>2.1ppt</td><td>0.3ppt</td></tr><tr><td>Kuaishou</td><td></td><td>3.9%</td><td>-0.9ppt</td><td>0.0ppt</td></tr><tr><td>Sogou Keyboard</td><td>-</td><td>3.1%</td><td>-0.1ppt</td><td>-0.1ppt</td></tr><tr><td>Toutiao</td><td>-</td><td>2.8%</td><td>-0.4ppt</td><td>-0.1ppt</td></tr><tr><td>Pinduoduo</td><td>-</td><td>2.3%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>rednote</td><td>-</td><td>2.2%</td><td>-0.3ppt</td><td>0.0ppt</td></tr><tr><td>Kuaishou Express</td><td>-</td><td>2.2%</td><td>-0.4ppt</td><td>0.0ppt</td></tr><tr><td>Baidu Keyboard</td><td>-</td><td>2.1%</td><td>-0.3ppt</td><td>0.1ppt</td></tr><tr><td>Weibo</td><td>-</td><td>2.0%</td><td>-0.3ppt</td><td>0.0ppt</td></tr><tr><td>Fanqie Free Novels</td><td>-</td><td>1.9%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Taobao</td><td>-</td><td>1.9%</td><td>-0.1ppt</td><td>0.2ppt</td></tr><tr><td>Bilibili</td><td>-</td><td>1.7%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Sina News</td><td>-</td><td>1.5%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Baidu</td><td>-</td><td>1.5%</td><td>-0.6ppt</td><td>0.0ppt</td></tr><tr><td>Honour of Kings</td><td>-</td><td>1.3%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Alipay</td><td>-</td><td>1.2%</td><td>0.1ppt</td><td>0.0ppt</td></tr><tr><td>Tencent News</td><td>-</td><td>1.1%</td><td>0.0ppt</td><td>0.0ppt</td></tr></table>

Among the Top-50 apps, which accounted for \~93% of the total mobile time spent in China during May, we note that the Bytedance camp gained time-spent share on a y-y basis, which rose from 32.6% in May 2025 to 39.2% in May 2026, surpassing Tencent camp's 29.8%. Sequentially, Bytedance's time-spent share was up 0.8pp m-m.

Fig. 2: Time-spent share of various internet camps among the Top-50 apps in China

<table><tr><td></td><td>Tencent</td><td>Bytedance</td><td>Baidu</td><td>Alibaba</td><td>Sina</td><td>Others</td></tr><tr><td>May-26</td><td>29.8%</td><td>39.2%</td><td>4.9%</td><td>5.6%</td><td>3.7%</td><td>16.7%</td></tr><tr><td>Apr-26</td><td>30.8%</td><td>38.3%</td><td>5.0%</td><td>5.4%</td><td>3.8%</td><td>16.7%</td></tr><tr><td>May-25</td><td>31.9%</td><td>32.6%</td><td>6.3%</td><td>6.2%</td><td>4.1%</td><td>18.9%</td></tr></table>

Source: QuestMobile, NOM

## Long-form vs short-form dramas

Long-form video apps remained weak in May. The MTS of Tencent Video (owned by Tencent) recorded a 31% y-y decline in May, dragged by a 22% decline in DAU and an 11% decline in DTSD. Youku (owned by BABA)/Mango TV (300413 CH, Not rated)/iQIYI (IQ US, Neutral) recorded 36%/5%/6% y-y declines in total time spent, mainly dragged by 28%/10%/12% declines in DAU.

The dominant short-form drama app – Red Fruit Free Short Drama – kept its strong growth trend with an MTS increase of 134%, backed by 110% growth in DAU and 11% growth in DTSD.

Fig. 3: DAUs of long-form vs short-form dramas apps  
![](images/56a4bfee30f554a010dce77923f16d901570f7cbfdb4a30a5df8ba84764b090f.jpg)  
Source: QuestMobile, NOM

Fig. 4: Average daily time spent per user  
![](images/8842a3e77785ab32dacdc6e6e204a36d61f0443e5e3e78d9b54156d7555dc8e9.jpg)  
Source: QuestMobile, NOM

## Short video

In May, Douyin maintained its solid growth momentum in terms of MTS, at 28% y-y, mainly driven by 21% growth in DAU. Total time spent for Bilibili (BILI US, Neutral) recorded 10% y-y growth in May, driven by 4% y-y growth in DAU and 6% growth in DTSD. However, Kuaishou (1024 HK, Neutral) continued its relatively soft performance, with a decline of 11% y-y in MTS, mainly dragged by an 11% y-y decline in DTSD.

Fig. 5: DAUs of short video apps  
![](images/59bc899640c2317c4ae0d7fb9c5607c9489db75abd49eb5e4b404c70c8cfbdb4.jpg)  
Source: QuestMobile, NOM

Fig. 6: Average daily time spent per user  
![](images/d26bdc28f2bf2f63508e7e8c9101b761d1dbdc2bf3aee0bf5c590bc73661cabf.jpg)  
Source: QuestMobile, NOM

## Online reading

The MTS of the free reading app leader Tomato Free Novels (unlisted; owned by ByteDance) maintained its solid growth momentum, up 12% y-y in May, driven by increases of 11% y-y in DAU. Another free reading app, Qimao Free Novels (unlisted), recorded a 41% y-y decline in total time spent, dragged by 28% and 17% y-y declines in DAU and DTSD, respectively.

Paid reading apps owned by China Literature (772 HK, Buy), i.e., Qidian reading and QQ reading, recorded respective declines of 11% and 8% on a y-y basis in DAU during the month, while their DTSDs were down by 11% and 9% y-y, respectively.

Fig. 7: DAU of online reading platforms  
![](images/8d8772dcf1953ddc141c122680fca09892b70e76792033612e6180fbada48778.jpg)  
Source: QuestMobile, NOM

Fig. 8: Average daily time spent per DAU of online reading platforms  
![](images/c1e647b45c6b690777d76764fc57bc04ff7fb900e3427e426045cc2bb701f521.jpg)  
Source: QuestMobile, NOM

## Live broadcasting

Live broadcasting show apps maintained their y-y downward trend in MTS in May. The DAU of Momo (MOMO US, Not rated) and YY (owned by Baidu) declined by 11% and 5% y-y, respectively. In terms of DTSD, Momo was up 2% y-y, while YY recorded a 14% y-y decline during the month.

Fig. 9: DAUs of live broadcasting show apps  
![](images/2172da0a29d49ece751d79e50e260d84a34bc4ff83ba2e7061d77b8a7d6d2e4a.jpg)  
Source: QuestMobile, NOM

Fig. 10: Average daily time spent per user  
![](images/4a786d75d5865701fefa2310f87d5b7cbdd2127e45dc9556f6064d199ab141bc.jpg)  
Source: QuestMobile, NOM

For game live broadcasting apps, the MTS for Huya (HUYA US, Not rated) recorded a 14% decline in May, mainly dragged by a 15% y-y decline in DAU. The MTS for Douyu (DOYU US, Not rated) recovered to 1% y-y growth in May, driven by 12% y-y growth in DTSD, offsetting 10% y-y decline in DAU.

Fig. 11: DAUs of game live broadcasting apps  
![](images/0aeea14e3f6284680c29dd2e961f92b816a3db3e7be8d61c6bc7423144405533.jpg)  
Source: QuestMobile, NOM

Fig. 12: Average daily time spent per user  
![](images/fe0dba7041a92f035f0bd93edfa4b8a8de8ffc6c82d4b43a238c599ecbae344d.jpg)  
Source: QuestMobile, NOM

## Music

The y-y decline in DAU continued for most part of the music universe, except for Soda Music and Tomato Music (both owned by ByteDance), which recorded 79% and 57% y-y growth in May. The DAU of NetEase Cloud Music (9899 HK, Not rated) recorded flat y-y in May. QQ Music/Kugou Music/Kuwo Music [owned by TME (TME US, Buy)] decreased 4%/12%/13% y-y in terms of DAU in May (as shown in Fig. 13).

Tencent Karaoke maintained its y-y downward trend in MTS, with a 23% y-y decline, mainly dragged by a 27% y-y drop in DAU, offsetting 7% y-y growth in DTSD in May (as shown in Fig. 14).

Fig. 13: DAUs of music streaming apps  
![](images/511ea079eaf4e4c8f6276031d3369e233fb87513517f26cab848fe3663d995a1.jpg)  
Source: QuestMobile, NOM

Fig. 14: DAUs of online karaoke app  
![](images/66ff2696228da91c22769d4c86dda58f85980a899f717122c60d66dc609e49a4.jpg)  
Source: QuestMobile, NOM

## Social

The MTS of Xiaohongshu (unlisted) saw 1% y-y decline for the first time in May, dragged by a 4% y-y decline in DTSD, offsetting 3% growth in DAU. The MTS of Weibo (WB US, Neutral) declined 3% y-y in May, dragged by 2%/1% decline in DTSD and DAU, respectively. Within Tencent's social ecosystem, QQ maintained its downward trend in MTS, with a 3% y-y decline, while WeChat recorded 2% y-y growth in terms of total time spent in May.

Fig. 15: DAUs of social apps  
![](images/e519e4e6b7019442429212b0fca2231feefb51dd1f0fbb7b5950939713cefef4.jpg)  
Source: QuestMobile, NOM

Fig. 16: Average daily time spent per user  
![](images/468733dcf43e397497a625fe3fb56e5528018710958db0265eef09c6fb93aa87.jpg)  
Source: QuestMobile, NOM

## Office apps

Within the office apps vertical, the DAU of Feishu (owned by Bytedance) and Wecom (owned by Tencent) recorded 45% y-y and 9% y-y growth, respectively, in May, while Ding Talk (owned by BABA) declined by 1% y-y. However, Ding Talk owned the largest DAU base at \~80mn, which was 1.1x and 9.0x that of Wecom and Feishu, respectively. For Feishu, the DTSD was at 14.2 minutes (flat y-y), followed by Wecom's 11.9 minutes (up 3% y-y) and DingTalk's 9.7 minutes (down 2% y-y), as per QuestMobile data.

Fig. 17: DAUs of office business apps  
![](images/6926c3302b481292d00f2add752ec7e68ac62765e8ddfa5563afdf1a2a03050a.jpg)  
Source: QuestMobile, NOM

Fig. 18: Average daily time spent per user  
![](images/2b650dea913b770968d91db1d647bc7592ebc150fe578590a925457fbc5293a9.jpg)  
Source: QuestMobile, NOM

## Search

The Baidu app, despite being a dominant search engine in China, witnessed a 21% y-y decline in MTS during the month, dragged by a 21% y-y decline in DAU.

![](images/3b9675231644f5adb1128be715d913b05c15772a42b0580a18efac13d013dcd4.jpg)  
Source: QuestMobile, NOM

![](images/89be202fb98af60c72609404828dcb6206bf131086ce84085fb97d69db534173.jpg)  
Source: QuestMobile, NOM

## AI tools

The DAU o

[中间内容因长度限制已省略]

ubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
