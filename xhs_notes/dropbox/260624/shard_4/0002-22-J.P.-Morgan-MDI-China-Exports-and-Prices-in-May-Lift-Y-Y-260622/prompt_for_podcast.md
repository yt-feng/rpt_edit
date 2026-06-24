你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
## MDI

China Exports and Prices in May Lift Y/Y

\- May MDI exports from China of 101kt were $49\%$ higher versus 68kt in May of 2025. 2026 YTD exports are $15.6\%$ higher y/y. 2026 YTD net exports of 258kt are 55kt higher y/y. Notably, shipments to Europe jumped $63\%$ from 51kt to 82kt ytd. Shipments to Turkey grew $68\%$ from 28kt to 47kt ytd.

\- Chinese average MDI export prices were 13% higher m/m and 25% higher y/y in May: prices averaged \$2,193/t compared with \$1,942/t in April and \$1,756/t in the prior-year period. The China import price was \$2,979/t in May, 115% higher m/m compared with \$1,906/t in April, and 21% higher y/y vs. \$1,385/t in May 2025. Please see Table 5 for more details.

\- 2025 net exports were 400kt or (496kt) lower y/y. 2025 exports were 805kt or (33%) lower y/y. See Table 3 for China exports by destination. 2025 exports to the US were sharply lower (83%) as were exports to Russia and the Netherlands. Full-year 2024 exports of 1,204kt were 15% or 160kt higher y/y. 2024 net exports were 896kt or 170kt higher y/y relative to 2023 net exports of 726kt. Full-year 2023 exports of 1,044kt were 6% or 55kt higher y/y. We estimate Huntsman's MDI volume to have been roughly lower by (10%) in 2022, lower by (14%) in 2023, higher by 7% in 2024, and 2% in 2025.

Chemicals: Specialty, Commodity, Agricultural, and Paper & Packaging

Jeffrey J. Zekauskas AC (1-212) 622-6644  
jeffrey.zekauskas@JPM.com

Katie Zhang (1-212) 622-3262 katie.zhang@jpmchase.com

Silke Kueck (1-212) 622-6503 silke.x.kueck@JPM.com

Lydia Huang  
(1-212) 622-0086  
lydia.huang@JPM.com  
JPM Securities LLC

Table 1: China MDI Trade Data (in kt)

<table><tr><td>Exports</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>44</td><td>43</td><td>40</td><td>43</td><td>66</td><td>83</td><td>91</td><td>101</td><td>63</td><td>64</td></tr><tr><td>February</td><td>32</td><td>53</td><td>47</td><td>45</td><td>91</td><td>59</td><td>116</td><td>76</td><td>80</td><td>61</td></tr><tr><td>March</td><td>46</td><td>40</td><td>76</td><td>89</td><td>106</td><td>100</td><td>102</td><td>113</td><td>75</td><td>90</td></tr><tr><td>April</td><td>40</td><td>63</td><td>65</td><td>33</td><td>82</td><td>83</td><td>99</td><td>127</td><td>57</td><td>81</td></tr><tr><td>May</td><td>57</td><td>44</td><td>43</td><td>28</td><td>113</td><td>114</td><td>109</td><td>94</td><td>68</td><td>101</td></tr><tr><td>June</td><td>68</td><td>80</td><td>43</td><td>30</td><td>76</td><td>117</td><td>89</td><td>134</td><td>70</td><td></td></tr><tr><td>July</td><td>51</td><td>46</td><td>63</td><td>53</td><td>79</td><td>83</td><td>78</td><td>78</td><td>64</td><td></td></tr><tr><td>August</td><td>55</td><td>53</td><td>59</td><td>64</td><td>85</td><td>58</td><td>97</td><td>87</td><td>61</td><td></td></tr><tr><td>September</td><td>46</td><td>64</td><td>49</td><td>54</td><td>90</td><td>89</td><td>75</td><td>95</td><td>80</td><td></td></tr><tr><td>October</td><td>30</td><td>46</td><td>55</td><td>51</td><td>74</td><td>57</td><td>55</td><td>97</td><td>70</td><td></td></tr><tr><td>November</td><td>47</td><td>45</td><td>51</td><td>55</td><td>78</td><td>93</td><td>79</td><td>102</td><td>58</td><td></td></tr><tr><td>December</td><td>46</td><td>39</td><td>40</td><td>69</td><td>75</td><td>53</td><td>54</td><td>101</td><td>60</td><td></td></tr><tr><td>Total</td><td>563</td><td>617</td><td>629</td><td>613</td><td>1,014</td><td>988</td><td>1,044</td><td>1,204</td><td>805</td><td>396</td></tr><tr><td>% change</td><td></td><td>9.7%</td><td>1.8%</td><td>(2.4%)</td><td>65.2%</td><td>(2.5%)</td><td>5.6%</td><td>15.3%</td><td>(33.1%)</td><td>15.6%</td></tr></table>

<table><tr><td>Imports</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>20</td><td>33</td><td>30</td><td>18</td><td>28</td><td>17</td><td>27</td><td>38</td><td>25</td><td>39</td></tr><tr><td>February</td><td>22</td><td>20</td><td>23</td><td>36</td><td>26</td><td>20</td><td>19</td><td>27</td><td>20</td><td>30</td></tr><tr><td>March</td><td>27</td><td>26</td><td>28</td><td>25</td><td>28</td><td>29</td><td>26</td><td>23</td><td>30</td><td>42</td></tr><tr><td>April</td><td>15</td><td>32</td><td>27</td><td>33</td><td>21</td><td>24</td><td>25</td><td>22</td><td>34</td><td>16</td></tr><tr><td>May</td><td>14</td><td>34</td><td>23</td><td>36</td><td>28</td><td>23</td><td>23</td><td>23</td><td>31</td><td>11</td></tr><tr><td>June</td><td>15</td><td>26</td><td>26</td><td>26</td><td>23</td><td>15</td><td>18</td><td>18</td><td>23</td><td></td></tr><tr><td>July</td><td>18</td><td>21</td><td>26</td><td>44</td><td>28</td><td>23</td><td>32</td><td>25</td><td>42</td><td></td></tr><tr><td>August</td><td>19</td><td>37</td><td>22</td><td>33</td><td>21</td><td>28</td><td>28</td><td>19</td><td>30</td><td></td></tr><tr><td>September</td><td>22</td><td>30</td><td>18</td><td>35</td><td>27</td><td>41</td><td>38</td><td>33</td><td>49</td><td></td></tr><tr><td>October</td><td>16</td><td>20</td><td>18</td><td>28</td><td>24</td><td>17</td><td>21</td><td>20</td><td>31</td><td></td></tr><tr><td>November</td><td>21</td><td>18</td><td>37</td><td>26</td><td>29</td><td>22</td><td>36</td><td>28</td><td>34</td><td></td></tr><tr><td>December</td><td>26</td><td>37</td><td>40</td><td>27</td><td>14</td><td>27</td><td>25</td><td>32</td><td>56</td><td></td></tr><tr><td>Total</td><td>234</td><td>333</td><td>318</td><td>369</td><td>298</td><td>286</td><td>318</td><td>309</td><td>405</td><td>138</td></tr><tr><td>% change</td><td></td><td>42.2%</td><td>(4.5%)</td><td>16.1%</td><td>(19.3%)</td><td>(3.8%)</td><td>11.2%</td><td>(3.1%)</td><td>31.4%</td><td>(1.3%)</td></tr></table>

Source: China General Administration of Customs

Table 2: China MDI Annual Trade Data (in kt)

<table><tr><td></td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Net exports/imports</td><td>329</td><td>285</td><td>311</td><td>245</td><td>716</td><td>702</td><td>726</td><td>896</td><td>400</td><td>258</td></tr><tr><td>Net Change</td><td></td><td>(44)</td><td>26</td><td>(66)</td><td>471</td><td>(14)</td><td>23</td><td>170</td><td>(496)</td><td>55</td></tr></table>

Source: China General Administration of Customs

See page 4 for analyst certification and important disclosures.

Table 3: China MDI Exports by Destination (2024-2026YTD)

<table><tr><td rowspan="2"></td><td colspan="3">Volumes in &#x27;000s of tons</td><td colspan="3">% of Total</td></tr><tr><td>2026</td><td>2025</td><td>2024</td><td>2026</td><td>2025</td><td>2024</td></tr><tr><td>EU-27</td><td>82</td><td>50</td><td>100</td><td>21%</td><td>15%</td><td>20%</td></tr><tr><td>Türkiye</td><td>47</td><td>28</td><td>33</td><td>12%</td><td>8%</td><td>7%</td></tr><tr><td>Russia</td><td>30</td><td>36</td><td>38</td><td>7%</td><td>11%</td><td>7%</td></tr><tr><td>India</td><td>26</td><td>26</td><td>21</td><td>7%</td><td>8%</td><td>4%</td></tr><tr><td>Republic of Korea</td><td>25</td><td>20</td><td>30</td><td>6%</td><td>6%</td><td>6%</td></tr><tr><td>Viet Nam</td><td>21</td><td>18</td><td>17</td><td>5%</td><td>5%</td><td>3%</td></tr><tr><td>Thailand</td><td>18</td><td>17</td><td>14</td><td>5%</td><td>5%</td><td>3%</td></tr><tr><td>Japan</td><td>16</td><td>11</td><td>12</td><td>4%</td><td>3%</td><td>2%</td></tr><tr><td>Brazil</td><td>15</td><td>15</td><td>17</td><td>4%</td><td>4%</td><td>3%</td></tr><tr><td>Other</td><td>116</td><td>121</td><td>227</td><td>29%</td><td>35%</td><td>45%</td></tr><tr><td>All</td><td>396</td><td>343</td><td>510</td><td></td><td></td><td></td></tr></table>

Source: China General Administration of Customs

Table 4: Chinese MDI Export/Import Price

<table><tr><td></td><td>export $/ton</td><td>Sq % change</td><td>Y/y % change</td><td>import $/ton</td><td>Sq % change</td><td>Y/y % change</td></tr><tr><td>Jan-20</td><td>1,280</td><td>-1%</td><td>-17%</td><td>1,298</td><td>2%</td><td>-21%</td></tr><tr><td>Feb-20</td><td>1,269</td><td>-1%</td><td>-13%</td><td>1,224</td><td>-6%</td><td>-25%</td></tr><tr><td>Mar-20</td><td>1,234</td><td>-3%</td><td>-15%</td><td>1,308</td><td>7%</td><td>-16%</td></tr><tr><td>Apr-20</td><td>1,275</td><td>3%</td><td>-3%</td><td>1,163</td><td>-11%</td><td>-25%</td></tr><tr><td>May-20</td><td>1,311</td><td>3%</td><td>-9%</td><td>1,156</td><td>-1%</td><td>-29%</td></tr><tr><td>Jun-20</td><td>1,270</td><td>-3%</td><td>-11%</td><td>1,255</td><td>9%</td><td>5%</td></tr><tr><td>Jul-20</td><td>1,235</td><td>-3%</td><td>-5%</td><td>1,121</td><td>-11%</td><td>-11%</td></tr><tr><td>Aug-20</td><td>1,234</td><td>0%</td><td>-6%</td><td>1,095</td><td>-2%</td><td>-21%</td></tr><tr><td>Sep-20</td><td>1,274</td><td>3%</td><td>-2%</td><td>1,313</td><td>20%</td><td>-6%</td></tr><tr><td>Oct-20</td><td>1,316</td><td>3%</td><td>0%</td><td>1,335</td><td>2%</td><td>-1%</td></tr><tr><td>Nov-20</td><td>1,436</td><td>9%</td><td>18%</td><td>2,073</td><td>55%</td><td>66%</td></tr><tr><td>Dec-20</td><td>1,467</td><td>2%</td><td>13%</td><td>2,066</td><td>0%</td><td>62%</td></tr><tr><td>Jan-21</td><td>1,582</td><td>8%</td><td>24%</td><td>1,600</td><td>-23%</td><td>23%</td></tr><tr><td>Feb-21</td><td>1,494</td><td>-6%</td><td>18%</td><td>1,798</td><td>12%</td><td>47%</td></tr><tr><td>Mar-21</td><td>1,718</td><td>15%</td><td>39%</td><td>2,145</td><td>19%</td><td>64%</td></tr><tr><td>Apr-21</td><td>1,982</td><td>15%</td><td>55%</td><td>2,254</td><td>5%</td><td>94%</td></tr><tr><td>May-21</td><td>2,057</td><td>4%</td><td>57%</td><td>2,108</td><td>-6%</td><td>82%</td></tr><tr><td>Jun-21</td><td>2,034</td><td>-1%</td><td>60%</td><td>2,139</td><td>1%</td><td>70%</td></tr><tr><td>Jul-21</td><td>2,106</td><td>4%</td><td>71%</td><td>2,142</td><td>0%</td><td>91%</td></tr><tr><td>Aug-21</td><td>2,269</td><td>8%</td><td>84%</td><td>2,360</td><td>10%</td><td>115%</td></tr><tr><td>Sep-21</td><td>2,343</td><td>3%</td><td>84%</td><td>2,204</td><td>-7%</td><td>68%</td></tr><tr><td>Oct-21</td><td>2,315</td><td>-1%</td><td>76%</td><td>2,364</td><td>7%</td><td>77%</td></tr><tr><td>Nov-21</td><td>2,412</td><td>4%</td><td>68%</td><td>2,241</td><td>-5%</td><td>8%</td></tr><tr><td>Dec-21</td><td>2,349</td><td>-3%</td><td>60%</td><td>1,820</td><td>-19%</td><td>-12%</td></tr><tr><td>Jan-22</td><td>2,280</td><td>-3%</td><td>44%</td><td>2,016</td><td>11%</td><td>26%</td></tr><tr><td>Feb-22</td><td>2,218</td><td>-3%</td><td>48%</td><td>2,270</td><td>13%</td><td>26%</td></tr><tr><td>Mar-22</td><td>2,257</td><td>2%</td><td>31%</td><td>2,216</td><td>-2%</td><td>3%</td></tr><tr><td>Apr-22</td><td>2,298</td><td>2%</td><td>16%</td><td>2,223</td><td>0%</td><td>-1%</td></tr><tr><td>May-22</td><td>2,300</td><td>0%</td><td>12%</td><td>2,188</td><td>-2%</td><td>4%</td></tr><tr><td>Jun-22</td><td>2,093</td><td>-9%</td><td>3%</td><td>2,146</td><td>-2%</td><td>0%</td></tr><tr><td>Jul-22</td><td>2,259</td><td>8%</td><td>7%</td><td>2,122</td><td>-1%</td><td>-1%</td></tr><tr><td>Aug-22</td><td>2,271</td><td>1%</td><td>0%</td><td>1,972</td><td>-7%</td><td>-16%</td></tr><tr><td>Sep-22</td><td>2,109</td><td>-7%</td><td>-10%</td><td>1,734</td><td>-12%</td><td>-21%</td></tr><tr><td>Oct-22</td><td>2,053</td><td>-3%</td><td>-11%</td><td>1,671</td><td>-4%</td><td>-29%</td></tr><tr><td>Nov-22</td><td>1,914</td><td>-7%</td><td>-21%</td><td>1,492</td><td>-11%</td><td>-33%</td></tr><tr><td>Dec-22</td><td>1,862</td><td>-3%</td><td>-21%</td><td>1,340</td><td>-10%</td><td>-26%</td></tr><tr><td>Jan-23</td><td>1,758</td><td>-6%</td><td>-23%</td><td>1,436</td><td>7%</td><td>-29%</td></tr><tr><td>Feb-23</td><td>1,659</td><td>-6%</td><td>-25%</td><td>1,695</td><td>18%</td><td>-25%</td></tr><tr><td>Mar-23</td><td>1,700</td><td>3%</td><td>-25%</td><td>1,676</td><td>-1%</td><td>-24%</td></tr><tr><td>Apr-23</td><td>1,772</td><td>4%</td><td>-23%</td><td>1,616</td><td>-4%</td><td>-27%</td></tr><tr><td>May-23</td><td>1,661</td><td>-6%</td><td>-28%</td><td>1,506</td><td>-7%</td><td>-31%</td></tr><tr><td>Jun-23</td><td>1,645</td><td>-1%</td><td>-21%</td><td>1,498</td><td>-1%</td><td>-30%</td></tr><tr><td>Jul-23</td><td>1,722</td><td>5%</td><td>-24%</td><td>1,483</td><td>-1%</td><td>-30%</td></tr><tr><td>Aug-23</td><td>1,542</td><td>-10%</td><td>-32%</td><td>1,550</td><td>5%</td><td>-21%</td></tr><tr><td>Sep-23</td><td>1,462</td><td>-5%</td><td>-31%</td><td>1,461</td><td>-6%</td><td>-16%</td></tr><tr><td>Oct-23</td><td>1,420</td><td>-3%</td><td>-31%</td><td>1,659</td><td>14%</td><td>-1%</td></tr><tr><td>Nov-23</td><td>1,223</td><td>-14%</td><td>-36%</td><td>1,568</td><td>-6%</td><td>5%</td></tr><tr><td>Dec-23</td><td>1,567</td><td>28%</td><td>-16%</td><td>1,568</td><td>0%</td><td>17%</td></tr><tr><td>Jan-24</td><td>1,277</td><td>-18%</td><td>-27%</td><td>1,570</td><td>0%</td><td>9%</td></tr><tr><td>Feb-24</td><td>1,337</td><td>5%</td><td>-19%</td><td>1,578</td><td>1%</td><td>-7%</td></tr><tr><td>Mar-24</td><td>1,431</td><td>7%</td><td>-16%</td><td>1,657</td><td>5%</td><td>-1%</td></tr><tr><td>Apr-24</td><td>1,540</td><td>8%</td><td>-13%</td><td>1,580</td><td>-5%</td><td>-2%</td></tr><tr><td>May-24</td><td>1,678</td><td>9%</td><td>1%</td><td>1,591</td><td>1%</td><td>6%</td></tr><tr><td>Jun-24</td><td>1,646</td><td>-2%</td><td>0%</td><td>1,685</td><td>6%</td><td>13%</td></tr><tr><td>Jul-24</td><td>1,831</td><td>11%</td><td>6%</td><td>1,534</td><td>-9%</td><td>3%</td></tr><tr><td>Aug-24</td><td>2,020</td><td>10%</td><td>31%</td><td>1,508</td><td>-2%</td><td>-3%</td></tr><tr><td>Sep-24</td><td>2,024</td><td>0%</td><td>38%</td><td>1,521</td><td>1%</td><td>4%</td></tr><tr><td>Oct-24</td><td>1,878</td><td>-7%</td><td>32%</td><td>1,820</td><td>20%</td><td>10%</td></tr><tr><td>Nov-24</td><td>1,715</td><td>-9%</td><td>40%</td><td>1,629</td><td>-10%</td><td>4%</td></tr><tr><td>Dec-24</td><td>1,785</td><td>4%</td><td>14%</td><td>1,442</td><td>-12%</td><td>-8%</td></tr><tr><td>Jan-25</td><td>1,965</td><td>10%</td><td>54%</td><td>1,588</td><td>10%</td><td>1%</td></tr><tr><td>Feb-25</td><td>1,664</td><td>-15%</td><td>24%</td><td>1,736</td><td>9%</td><td>10%</td></tr><tr><td>Mar-25</td><td>1,733</td><td>4%</td><td>21%</td><td>1,563</td><td>-10%</td><td>-6%</td></tr><tr><td>Apr-25</td><td>1,791</td><td>3%</td><td>16%</td><td>1,578</td><td>1%</td><td>0%</td></tr><tr><td>May-25</td><td>1,756</td><td>-2%</td><td>5%</td><td>1,385</td><td>-12%</td><td>-13%</td></tr><tr><td>Jun-25</td><td>1,641</td><td>-7%</td><td>0%</td><td>1,616</td><td>17%</td><td>-4%</td></tr><tr><td>Jul-25</td><td>1,651</td><td>1%</td><td>-10%</td><td>1,512</td><td>-6%</td><td>-1%</td></tr><tr><td>Aug-25</td><td>1,596</td><td>-3%</td><td>-21%</td><td>1,543</td><td>2%</td><td>2%</td></tr><tr><td>Sep-25</td><td>1,569</td><td>-2%</td><td>-22%</td><td>1,541</td><td>0%</td><td>1%</td></tr><tr><td>Oct-25</td><td>1,567</td><td>0%</td><td>-17%</td><td>1,620</td><td>5%</td><td>-11%</td></tr><tr><td>Nov-25</td><td>1,542</td><td>-2%</td><td>-10%</td><td>1,530</td><td>-6%</td><td>-6%</td></tr><tr><td>Dec-25</td><td>1,448</td><td>-6%</td><td>-19%</td><td>1,520</td><td>-1%</td><td>5%</td></tr><tr><td>Jan-26</td><td>1,416</td><td>-2%</td><td>-28%</td><td>1,594</td><td>5%</td><td>0%</td></tr><tr><td>Feb-26</td><td>1,371</td><td>-3%</td><td>-18%</td><td>1,464</td><td>-8%</td><td>-16%</td></tr><tr><td>Mar-26</td><td>1,491</td><td>9%</td><td>-14%</td><td>1,657</td><td>13%</td><td>6%</td></tr><tr><td>Apr-26</td><td>1,942</td><td>30%</td><td>8%</td><td>1,906</td><td>15%</td><td>21%</td></tr><tr><td>May-26</td><td>2,193</td><td>13%</td><td>25%</td><td>2,979</td><td>56%</td><td>115%</td></tr></table>

Source: China General Administration of Customs.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage univers

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 22 Jun 2026 04:16 PM EDT

Disseminated 22 Jun 2026 04:16 PM EDT
"""
