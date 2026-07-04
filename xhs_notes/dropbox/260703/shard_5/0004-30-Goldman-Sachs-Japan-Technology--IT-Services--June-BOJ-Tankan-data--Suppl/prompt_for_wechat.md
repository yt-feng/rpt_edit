你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Japan Technology: IT Services: June BOJ Tankan data: Supply/demand tightness eases slightly, gap may widen in margin improvement on AI

The Bank of Japan (BOJ) announced detailed data (software fixed investment, DIs) by industry from the June 2026 Tankan survey at 08:50 JST on July 2 (the summary was released on July 1). FY26 (FY3/27) software investment plans (all industries, including financials) were revised up sharply to +12.4% yoy (+5.3 pp from the March survey), led by manufacturers, and the favorable demand environment is expected to continue, centered on modernization. At present, demand is beginning to emerge for consulting, network building, and cybersecurity, driven by growing corporate appetite for AI adoption, and we believe this trend could accelerate going forward. Furthermore, excluding quarterly fluctuations, the trends of engineer shortages and rising unit prices generally remain unchanged, based on the DIs. However, we expect the effects of AI-driven development to gradually become apparent at some major system integrators going forward, which we think could have a slight impact on supply/demand trends in the industry. From the perspective of AI-related businesses and AI-driven development, we highlight Buy-rated NEC, Baycurrent, NOM Institute (NRI), and Fujitsu. However, for Fujitsu and NEC, we note the need to watch the impact of higher memory prices (Fujitsu has a higher sales mix of related products based on FY3/26 results).

Chikai Tanaka, CFA
+81(3)4587-9840 |
chikai.tanaka@gs.com
GS Japan Co., Ltd.

Yuki Sato
+81(3)4587-8536 | yuki.z.sato@gs.com
GS Japan Co., Ltd.

## Dls

The June 2026 employment conditions DI (all enterprises; excessive - insufficient, %) for the information services industry was -41 (+9 qoq), with the figure improving mainly for mid-sized and SMEs. However, the DI for large enterprises (major system integrators) was close to its average over the past year, indicating no change in the situation, with supply/demand remaining tight. Also, reflecting the tight supply/demand, both the output (sales) price DI (rise - fall, %) and input price DI (rise - fall, %) remain at high levels, and the outlook DIs for September suggest both will rise further. Overall, excluding quarterly fluctuations, the trends of engineer shortages and rising unit prices remains unchanged. However, we expect the effects of AI-driven development to gradually become apparent at some major system integrators going forward, which we think will have a slight impact on supply/demand trends in the industry. Our impression is that Fujitsu in particular is leading these initiatives, followed by NRI and NEC. With the exception of these few companies, efforts toward AI-driven development across the industry as a whole are still slow. In Japan, where the working population is declining, this is not yet expected to have a significant enough impact to fundamentally resolve the current shortage of engineers. However, depending on the progress of these efforts, a significant

disparity in the pace of productivity improvements could emerge among companies.

## Software investment

The BOJ released a detailed breakdown of software investment plans by industry. FY26 (FY3/27) software investment plans (all industries, including financials) call for growth of +12.4% yoy (+5.3 pp from the March survey), including +21.0% yoy for manufacturers (+10.7 pp), +9.6% yoy for non-manufacturers (+4.7 pp), and +9.5% yoy for financials (+1.5 pp). The plans were thus revised up considerably, led by manufacturers. When the initial plans were announced, market sentiment had worsened due to factors such as rising tensions in the Middle East, but the easing of this situation likely led to the upward revisions. By subsector, growth (in value terms) on a yoy basis is expected to be driven by machinery, electrical machinery, motor vehicles, retailing, transport & postal services, telecommunications, information services, and banks. While modernization continues to drive investment expansion, demand is beginning to emerge at present for consulting, network building, and cybersecurity, driven by growing corporate appetite for AI adoption, and we believe this trend could accelerate going forward.

Exhibit 1: BOJ Tankan: Information services business conditions DI, employment conditions DI, and output price DI (June 2026 survey)

<table><tr><td rowspan="2" colspan="2">Information Services DI</td><td colspan="4">2022</td><td colspan="4">2023</td><td colspan="4">2024</td><td colspan="4">2025</td><td colspan="3">2026</td></tr><tr><td>1-3</td><td>4-6</td><td>7-9</td><td>10-12</td><td>1-3</td><td>4-6</td><td>7-9</td><td>10-12</td><td>1-3</td><td>4-6</td><td>7-9</td><td>10-12</td><td>1-3</td><td>4-6</td><td>7-9</td><td>10-12</td><td>1-3</td><td>4-6</td><td>7-9</td></tr><tr><td colspan="21">Business Conditions (Diffusion index of &quot;Favorable&quot; minus &quot;Unfavorable&quot;)</td></tr><tr><td>Information services</td><td>F</td><td>14</td><td>21</td><td>24</td><td>25</td><td>26</td><td>28</td><td>29</td><td>28</td><td>31</td><td>36</td><td>37</td><td>34</td><td>34</td><td>37</td><td>33</td><td>36</td><td>36</td><td>32</td><td>31</td></tr><tr><td>All Enterprises</td><td>A</td><td>28</td><td>30</td><td>31</td><td>28</td><td>34</td><td>33</td><td>31</td><td>37</td><td>41</td><td>40</td><td>39</td><td>41</td><td>40</td><td>39</td><td>42</td><td>41</td><td>44</td><td>38</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>25</td><td>29</td><td>34</td><td>34</td><td>36</td><td>39</td><td>41</td><td>38</td><td>40</td><td>47</td><td>51</td><td>47</td><td>45</td><td>47</td><td>42</td><td>46</td><td>47</td><td>45</td><td>39</td></tr><tr><td>Large Enterprises</td><td>A</td><td>38</td><td>37</td><td>36</td><td>40</td><td>42</td><td>45</td><td>42</td><td>43</td><td>54</td><td>54</td><td>53</td><td>53</td><td>46</td><td>51</td><td>55</td><td>51</td><td>52</td><td>52</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>10</td><td>20</td><td>21</td><td>25</td><td>31</td><td>34</td><td>34</td><td>28</td><td>33</td><td>35</td><td>36</td><td>35</td><td>36</td><td>37</td><td>34</td><td>36</td><td>37</td><td>38</td><td>37</td></tr><tr><td>Medium-sized Enterprises</td><td>A</td><td>26</td><td>29</td><td>31</td><td>27</td><td>40</td><td>36</td><td>31</td><td>40</td><td>37</td><td>37</td><td>35</td><td>40</td><td>45</td><td>43</td><td>45</td><td>47</td><td>51</td><td>46</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>9</td><td>17</td><td>21</td><td>19</td><td>15</td><td>12</td><td>14</td><td>17</td><td>21</td><td>29</td><td>29</td><td>24</td><td>23</td><td>27</td><td>25</td><td>28</td><td>24</td><td>20</td><td>19</td></tr><tr><td>Small Enterprises</td><td>A</td><td>24</td><td>26</td><td>27</td><td>21</td><td>21</td><td>20</td><td>23</td><td>29</td><td>35</td><td>33</td><td>31</td><td>33</td><td>30</td><td>26</td><td>28</td><td>26</td><td>33</td><td>21</td><td>-</td></tr><tr><td colspan="21">Employment Conditions (Diffusion index of &quot;Excessive employment&quot; minus &quot;Insufficient employment&quot;)</td></tr><tr><td>Information services</td><td>F</td><td>-38</td><td>-38</td><td>-44</td><td>-42</td><td>-46</td><td>-50</td><td>-50</td><td>-53</td><td>-50</td><td>-51</td><td>-54</td><td>-53</td><td>-56</td><td>-52</td><td>-53</td><td>-53</td><td>-56</td><td>-48</td><td>-42</td></tr><tr><td>All Enterprises</td><td>A</td><td>-37</td><td>-43</td><td>-42</td><td>-46</td><td>-48</td><td>-45</td><td>-49</td><td>-49</td><td>-48</td><td>-49</td><td>-49</td><td>-52</td><td>-49</td><td>-51</td><td>-51</td><td>-53</td><td>-50</td><td>-41</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>-25</td><td>-27</td><td>-27</td><td>-27</td><td>-29</td><td>-28</td><td>-30</td><td>-36</td><td>-39</td><td>-35</td><td>-33</td><td>-37</td><td>-38</td><td>-35</td><td>-39</td><td>-39</td><td>-39</td><td>-40</td><td>-34</td></tr><tr><td>Large Enterprises</td><td>A</td><td>-25</td><td>-27</td><td>-27</td><td>-27</td><td>-33</td><td>-32</td><td>-36</td><td>-37</td><td>-33</td><td>-35</td><td>-37</td><td>-38</td><td>-33</td><td>-39</td><td>-36</td><td>-38</td><td>-43</td><td>-38</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>-42</td><td>-43</td><td>-49</td><td>-48</td><td>-53</td><td>-64</td><td>-57</td><td>-58</td><td>-54</td><td>-58</td><td>-64</td><td>-59</td><td>-63</td><td>-59</td><td>-60</td><td>-62</td><td>-66</td><td>-56</td><td>-48</td></tr><tr><td>Medium-sized Enterprises</td><td>A</td><td>-42</td><td>-49</td><td>-48</td><td>-50</td><td>-52</td><td>-51</td><td>-55</td><td>-53</td><td>-56</td><td>-59</td><td>-58</td><td>-59</td><td>-55</td><td>-56</td><td>-60</td><td>-61</td><td>-56</td><td>-46</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>-42</td><td>-41</td><td>-50</td><td>-46</td><td>-50</td><td>-52</td><td>-54</td><td>-59</td><td>-53</td><td>-54</td><td>-57</td><td>-57</td><td>-61</td><td>-56</td><td>-56</td><td>-54</td><td>-56</td><td>-46</td><td>-40</td></tr><tr><td>Small Enterprises</td><td>A</td><td>-41</td><td>-46</td><td>-47</td><td>-53</td><td>-53</td><td>-48</td><td>-53</td><td>-53</td><td>-48</td><td>-48</td><td>-47</td><td>-54</td><td>-55</td><td>-53</td><td>-50</td><td>-54</td><td>-48</td><td>-39</td><td>-</td></tr><tr><td colspan="21">Change in Output Prices (Diffusion index of &quot;Rise&quot; minus &quot;Fall&quot;)</td></tr><tr><td>Information services</td><td>F</td><td>-2</td><td>1</td><td>2</td><td>6</td><td>8</td><td>17</td><td>16</td><td>16</td><td>17</td><td>22</td><td>23</td><td>24</td><td>24</td><td>29</td><td>26</td><td>29</td><td>29</td><td>33</td><td>33</td></tr><tr><td>All Enterprises</td><td>A</td><td>0</td><td>0</td><td>5</td><td>3</td><td>9</td><td>11</td><td>14</td><td>14</td><td>20</td><td>24</td><td>26</td><td>26</td><td>26</td><td>29</td><td>23</td><td>24</td><td>29</td><td>28</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>4</td><td>6</td><td>12</td><td>15</td><td>21</td><td>30</td><td>31</td><td>27</td><td>33</td><td>40</td><td>35</td><td>38</td><td>36</td><td>42</td><td>37</td><td>40</td><td>40</td><td>43</td><td>37</td></tr><tr><td>Large Enterprises</td><td>A</td><td>8</td><td>6</td><td>13</td><td>13</td><td>19</td><td>24</td><td>27</td><td>31</td><td>33</td><td>35</td><td>40</td><td>38</td><td>38</td><td>40</td><td>33</td><td>36</td><td>41</td><td>39</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>-5</td><td>-1</td><td>0</td><td>3</td><td>5</td><td>17</td><td>13</td><td>14</td><td>15</td><td>22</td><td>26</td><td>25</td><td>26</td><td>32</td><td>30</td><td>31</td><td>31</td><td>39</td><td>39</td></tr><tr><td>Medium-sized Enterprises</td><td>A</td><td>-3</td><td>-4</td><td>3</td><td>2</td><td>4</td><td>5</td><td>11</td><td>10</td><td>15</td><td>24</td><td>26</td><td>24</td><td>24</td><td>30</td><td>22</td><td>22</td><td>29</td><td>32</td><td>-</td></tr><tr><td>Information services</td><td>F</td><td>-3</td><td>0</td><td>-2</td><td>3</td><td>2</td><td>8</td><td>9</td><td>9</td><td>8</td><td>9</td><td>12</td><td>13</td><td>14</td><td>18</td><td>14</td><td>20</td><td>18</td><td>21</td><td>25</td></tr><tr><td>Small Enterprises</td><td>A</td><td>-3</td><td>0</td><td>3</td><td>-1</td><td>7</td><td>7</td><td>9</td><td>7</td><td>16</td><td>16</td><td>15</td><td>20</td><td>19</td><td>20</td><td>17</td><td>16</td><td>23</td><td>18</td><td>-</td></tr></table>

Based on new definitions from Jan-Mar 2026

Exhibit 2: BOJ Tankan: Software investment plans (June 2026 survey)

<table><tr><td>YoY (%)</td><td>Actual FY20</td><td>Actual FY21</td><td>Actual FY22</td><td>Actual FY23</td><td>Actual FY24</td><td>Actual FY25</td><td>Jun survey Forecast FY26</td><td>Jun survey Revision rate FY26</td></tr><tr><td>All industries including Financial institutions</td><td>-7.4</td><td>5.4</td><td>14.5</td><td>12.2</td><td>3.7</td><td>8.9</td><td>12.4</td><td>5.3</td></tr><tr><td>Financial institutions</td><td>-10.2</td><td>1.0</td><td>21.0</td><td>17.8</td><td>2.7</td><td>12.3</td><td>9.5</td><td>1.5</td></tr><tr><td>Banks</td><td>-11.9</td><td>1.8</td><td>21.2</td><td>20.8</td><td>14.7</td><td>7.9</td><td>19.8</td><td>2.6</td></tr><tr><td>Financial institutions for cooperative organizations</td><td>-22.1</td><td>10.1</td><td>50.7</td><td>19.9</td><td>4.3</td><td>-1.8</td><td>12.0</td><td>13.1</td></tr><tr><td>Financial products transaction dealers</td><td>2.1</td><td>-3.7</td><td>29.3</td><td>6.6</td><td>-5.2</td><td>17.6</td><td>-3.3</td><td>-7.6</td></tr><tr><td>Insurance companies</td><td>-0.7</td><td>-0.9</td><td>20.4</td><td>15.2</td><td>-5.3</td><td>20.8</td><td>2.7</td><td>-1.0</td></tr><tr><td>Non-deposit money corporations</td><td>-34.0</td><td>11.0</td><td>13.3</td><td>30.7</td><td>1.8</td><td>4.2</td><td>4.2</td><td>10.0</td></tr><tr><td>All industries</td><td>-6.2</td><td>7.6</td><td>11.5</td><td>10.0</td><td>4.2</td><td>7.5</td><td>13.5</td><td>6.8</td></tr><tr><td>Manufacturing</td><td>-5.9</td><td>9.7</td><td>16.2</td><td>11.3</td><td>7.2</td><td>5.1</td><td>21.0</td><td>10.7</td></tr><tr><td>Textiles</td><td>-7.9</td><td>17.7</td><td>39.1</td><td>-9.4</td><td>-10.3</td><td>26.0</td><td>44.8</td><td>6.7</td></tr><tr><td>Lumber &amp; Wood products</td><td>-24.2</td><td>16.3</td><td>28.9</td><td>10.2</td><td>22.8</td><td>-6.2</td><td>38.5</td><td>19.7</td></tr><tr><td>Pulp &amp; Paper</td><td>-15.9</td><td>-27.3</td><td>44.6</td><td>7.7</td><td>-31.4</td><td>43.6</td><td>27.6</td><td>9.3</td></tr><tr><td>Chemicals</td><td>-1.7</td><td>-1.3</td><td>15.9</td><td>4.3</td><td>11.5</td><td>2.9</td><td>6.2</td><td>1.3</td></tr><tr><td>Petroleum &amp; Coal products</td><td>-19.8</td><td>70.2</td><td>8.0</td><td>19.3</td><td>45.8</td><td>9.7</td><td>109.1</td><td>99.8</td></tr><tr><td>Ceramics, Stone &amp; Clay</td><td>15.7</td><td>19.3</td><td>-10.9</td><td>11.7</td><td>-7.7</td><td>36.1</td><td>11.1</td><td>-1.4</td></tr><tr><td>Iron &amp; Steel</td><td>-0.5</td><td>91.4</td><td>-3.2</td><td>-3.8</td><td>17.9</td><td>0.7</td><td>0.1</td><td>-2.5</td></tr><tr><td>Nonferrous metals</td><td>-1.0</td><td>-10.2</td><td>31.1</td><td>-22.4</td><td>-7.2</td><td>4..9</td><td>25.5</td><td>-7.9</td></tr><tr><td>Food &amp; Beverages</td><td>-8.9</td><td>-2.8</td><td>8.0</td><td>29.4</td><td>0.9</td><td>-2.2</td><td>204.5</td><td>183.9</td></tr><tr><td>Processed metals</td><td>-37.1</td><td>30.0</td><td>7.8</td><td>42.3</td><td>-9.7</td><td>-3.2</td><td>31.9</td><td>-0.2</td></tr><tr><td>General-purpose, Production &amp;Business oriented machinery</td><td>-8.6</td><td>13.3</td><td>16.4</td><td>12.6</td><td>15.1</td><td>9.3</td><td>9.3</td><td>4.3</td></tr><tr><td>General-purpose machinery</td><td>-12.6</td><td>18.0</td><td>-0.1</td><td>26.9</td><td>4.0</td><td>3.0</td><td>8.0</td><td>-4.4</td></tr><tr><td>Production machinery</td><td>-5.4</td><td>5.6</td><td>21.1</td><td>11.0</td><td>22.4</td><td>4.8</td><td>6.1</td><td>1.1</td></tr><tr><td>Business oriented machinery</td><td>-9.8</td><td>18.8</td><td>21.3</td><td>5.0</td><td>12.9</td><td>23.8</td><td>15.9</td><td>17.2</td></tr><tr><td>Electrical machinery</td><td>-3.3</td><td>6.7</td><td>14.9</td><td>11.3</td><td>3.3</td><td>-5.1</td><td>7.3</td><td>-11.5</td></tr><tr><td>Transportation machinery</td><td>-6.1</td><td>3.8</td><td>40.9</td><td>20.5</td><td>7.6</td><td>11.2</td><td>12.2</td><td>4.7</td></tr><tr><td>Shipbuilding, Heavy machinery &amp; Other transportation machinery</td><td>4.2</td><td>-14.7</td><td>41.5</td><td>3.2</td><td>1.8</td><td>39.3</td><td>10.7</td><td>1.5</td></tr><tr><td>Motor vehicles</td><td>-7.4</td><td>6.6</td><td>40.8</td><td>22.1</td><td>8.1</td><td>9.1</td><td>12.4</td><td>5.0</td></tr><tr><td>Other manufacturing</td><td>-6.4</td><td>11.2</td><td>2.4</td><td>5.7</td><td>11.0</td><td>26.3</td><td>1.6</td><td>15.8</td></tr><tr><td>Basic materials</td><td>-2.3</td><td>15.2</td><td>11.6</td><td>0.7</td><td>7.8</td><td>5.8</td><td>10.9</td><td>2.3</td></tr><tr><td>Processing</td><td>-7.0</td><td>7.7</td><td>18.1</td><td>15.1</td><td>7.0</td><td>4.9</td><td>24.1</td><td>13.2</td></tr><tr><td>Nonmanufacturing</td><td>-6.4</td><td>6.4</td><td>9.1</td><td>9.3</td><td>2.7</td><td>8.8</td><td>9.6</td><td>4.7</td></tr><tr><td>Construction</td><td>1.8</td><td>30.9</td><td>2.4</td><td>16.8</td><td>3.0</td><td>6.2</td><td>13.1</td><td>9.2</td></tr><tr><td>Real estate, Goods rental &amp; Leasing</td><td>-40.2</td><td>6.5</td><td>13.2</td><td>18.8</td><td>4.0</td><td>12.0</td><td>11.8</td><td>-3.2</td></tr><tr><td>Real estate</td><td>3.2</td><td>-2.1</td><td>35.9</td><td>8.4</td><td>-6.0</td><td>27.7</td><td>12.3</td><td>2.4</td></tr><tr><td>Goods rental &amp; Leasing</td><td>-63.6</td><td>24.8</td><td>-24.7</td><td>48.6</td><td>24.8</td><td>-9.4</td><td>10.9</td><td>-12.7</td></tr><tr><td>Wholesaling &amp; Retailing</td><td>-2.1</td><td>10.6</td><td>28.9</td><td>5.6</td><td>-6.5</td><td>6.1</td><td>4.0</td><td>1.2</td></tr><tr><td>Wholesaling</td><td>-4.5</td><td>5.6</td><td>34.7</td><td>4.5</td><td>-8.9</td><td>7.6</td><td>-6.4</td><td>2.9</td></tr><tr><td>Retailing</td><td>2.2</td><td>18.2</td><td>20.7</td><td>7.3</td><td>-3.0</td><td>3.7</td><td>20.2</td><td>-0.7</td></tr><tr><td>Transport &amp; Postal activities</td><td>-20.4</td><td>20.9</td><td>21.7</td><td>7.7</td><td>3.3</td><td>44.0</td><td>10.9</td><td>16.1</td></tr><tr><td>Information communication</td><td>1.3</td><td>5.0</td><td>-1.2</td><td>10.1</td><td>2.8</td><td>2.1</td><td>7.3</td><td>2.2</td></tr><tr><td>Communications</td><td>-8.9</td><td>5.8</td><td>16.3</td><td>4.1</td><td>11.3</td><td>16.6</td><td>10.4</td><td>13.1</td></tr><tr><td>Information services</td><td>13.2</td><td>10.7</td><td>-14.0</td><td>4.8</td><td>-9.3</td><td>-7.6</td><td>7.0</td><td>-2.6</td></tr><tr><td>Other information communication</td><td>0.7</td><td>-23.4</td><td>-4.2</td><td>31.4</td><td>10.2</td><td>-10.9</td><td>-1.6</td><td>-15.5</td></tr><tr><td>Electric &amp; Gas utilities</td><td>-13.6</td><td>-24.1</td><td>-7.7</td><td>13.4</td><td>29.4</td><td>14.8</td><td>11.4</td><td>16.0</td></tr><tr><td>Services for businesses</td><td>-10.3</td><td>18.3</td><td>9.8</td><td>-1.3</td><td>9.0</td><td>9.4</td><td>27.3</td><td>4.2</td></tr><tr><td>Services for individuals</td><td>-17.5</td><td>-2.8</td><td>11.0</td><td>27.2</td><td>3.7</td><td>3.4</td><td>6.8</td><td>6.0</td></tr><tr><td>Accommodations,Eating &amp; Drinking services</td><td>-31.5</td><td>4.1</td><td>53.0</td><td>-5.9</td><td>18.7</td><td>-17.1</td><td>38.5</td><td>-7.5</td></tr><tr><td>Mining &amp; Quarrying of stone and gravel</td><td>63.9</td><td>-11.7</td><td>18.1</td><td>-0.5</td><td>-5.6</td

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
