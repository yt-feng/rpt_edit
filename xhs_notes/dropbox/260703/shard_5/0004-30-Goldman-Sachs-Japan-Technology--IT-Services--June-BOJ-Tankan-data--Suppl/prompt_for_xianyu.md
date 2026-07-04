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

<table><tr><td>YoY (%)</td><td>Actual FY20</td><td>Actual FY21</td><td>Actual FY22</td><td>Actual FY23</td><td>Actual FY24</td><td>Actual FY25</td><td>Jun survey Forecast FY26</td><td>Jun survey Revision rate FY26</td></tr><tr><td>All industries including Financial institutions</td><td>-7.4</td><td>5.4</td><td>14.5</td><td>12.2</td><td>3.7</td><td>8.9</td><td>12.4</td><td>5.3</td></tr><tr><td>Financial institutions</td><td>-10.2</td><td>1.0</td><td>21.0</td><td>17.8</td><td>2.7</td><td>12.3</td><td>9.5</td><td>1.5</td></tr><tr><td>Banks</td><td>-11.9</td><td>1.8</td><td>21.2</td><td>20.8</td><td>14.7</td><td>7.9</td><td>19.8</td><td>2.6</td></tr><tr><td>Financial institutions for cooperative organizations</td><td>-22.1</td><td>10.1</td><td>50.7</td><td>19.9</td><td>4.3</td><td>-1.8</td><td>12.0</td><td>13.1</td></tr><tr><td>Financial products transaction dealers</td><td>2.1</td><td>-3.7</td><td>29.3</td><td>6.6</td><td>-5.2</td><td>17.6</td><td>-3.3</td><td>-7.6</td></tr><tr><td>Insurance companies</td><td>-0.7</td><td>-0.9</td><td>20.4</td><td>15.2</td><td>-5.3</td><td>20.8</td><td>2.7</td><td>-1.0</td></tr><tr><td>Non-deposit money corporations</td><td>-34.0</td><td>11.0</td><td>13.3</td><td>30.7</td><td>1.8</td><td>4.2</td><td>4.2</td><td>10.0</td></tr><tr><td>All industries</td><td>-6.2</td><td>7.6</td><td>11.5</td><td>10.0</td><td>4.2</td><td>7.5</td><td>13.5</td><td>6.8</td></tr><tr><td>Manufacturing</td><td>-5.9</td><td>9.7</td><td>16.2</td><td>11.3</td><td>7.2</td><td>5.1</td><td>21.0</td><td>10.7</td></tr><tr><td>Textiles</td><td>-7.9</td><td>17.7</td><td>39.1</td><td>-9.4</td><td>-10.3</td><td>26.0</td><td>44.8</td><td>6.7</td></tr><tr><td>Lumber &amp; Wood products</td><td>-24.2</td><td>16.3</td><td>28.9</td><td>10.2</td><td>22.8</td><td>-6.2</td><td>38.5</td><td>19.7</td></tr><tr><td>Pulp &amp; Paper</td><td>-15.9</td><td>-27.3</td><td>44.6</td><td>7.7</td><td>-31.4</td><td>43.6</td><td>27.6</td><td>9.3</td></tr><tr><td>Chemicals</td><td>-1.7</td><td>-1.3</td><td>15.9</td><td>4.3</td><td>11.5</td><td>2.9</td><td>6.2</td><td>1.3</td></tr><tr><td>Petroleum &amp; Coal products</td><td>-19.8</td><td>70.2</td><td>8.0</td><td>19.3</td><td>45.8</td><td>9.7</td><td>109.1</td><td>99.8</td></tr><tr><td>Ceramics, Stone &amp; Clay</td><td>15.7</td><td>19.3</td><td>-10.9</td><td>11.7</td><td>-7.7</td><td>36.1</td><td>11.1</td><td>-1.4</td></tr><tr><td>Iron &amp; Steel</td><td>-0.5</td><td>91.4</td><td>-3.2</td><td>-3.8</td><td>17.9</td><td>0.7</td><td>0.1</td><td>-2.5</td></tr><tr><td>Nonferrous metals</td><td>-1.0</td><td>-10.2</td><td>31.1</td><td>-22.4</td><td>-7.2</td><td>4..9</td><td>25.5</td><td>-7.9</td></tr><tr><td>Food &amp; Beverages</td><td>-8.9</td><td>-2.8</td><td>8.0</td><td>29.4</td><td>0.9</td><td>-2.2</td><td>204.5</td><td>183.9</td></tr><tr><td>Processed metals</td><td>-37.1</td><td>30.0</td><td>7.8</td><td>42.3</td><td>-9.7</td><td>-3.2</td><td>31.9</td><td>-0.2</td></tr><tr><td>General-purpose, Production &amp;Business oriented machinery</td><td>-8.6</td><td>13.3</td><td>16.4</td><td>12.6</td><td>15.1</td><td>9.3</td><td>9.3</td><td>4.3</td></tr><tr><td>General-purpose machinery</td><td>-12.6</td><td>18.0</td><td>-0.1</td><td>26.9</td><td>4.0</td><td>3.0</td><td>8.0</td><td>-4.4</td></tr><tr><td>Production machinery</td><td>-5.4</td><td>5.6</td><td>21.1</td><td>11.0</td><td>22.4</td><td>4.8</td><td>6.1</td><td>1.1</td></tr><tr><td>Business oriented machinery</td><td>-9.8</td><td>18.8</td><td>21.3</td><td>5.0</td><td>12.9</td><td>23.8</td><td>15.9</td><td>17.2</td></tr><tr><td>Electrical machinery</td><td>-3.3</td><td>6.7</td><td>14.9</td><td>11.3</td><td>3.3</td><td>-5.1</td><td>7.3</td><td>-11.5</td></tr><tr><td>Transportation machinery</td><td>-6.1</td><td>3.8</td><td>40.9</td><td>20.5</td><td>7.6</td><td>11.2</td><td>12.2</td><td>4.7</td></tr><tr><td>Shipbuilding, Heavy machinery &amp; Other transportation machinery</td><td>4.2</td><td>-14.7</td><td>41.5</td><td>3.2</td><td>1.8</td><td>39.3</td><td>10.7</td><td>1.5</td></tr><tr><td>Motor vehicles</td><td>-7.4</td><td>6.6</td><td>40.8</td><td>22.1</td><td>8.1</td><td>9.1</td><td>12.4</td><td>5.0</td></tr><tr><td>Other manufacturing</td><td>-6.4</td><td>11.2</td><td>2.4</td><td>5.7</td><td>11.0</td><td>26.3</td

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

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
