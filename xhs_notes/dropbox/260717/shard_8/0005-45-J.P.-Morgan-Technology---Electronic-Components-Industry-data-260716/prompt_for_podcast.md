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
# Technology – Electronic Components Industry data

Technology – Electronic Components
Akinori Kanemoto AC
+813-6736-8628
akinori.kanemoto@JPM.com
JPM Securities Japan Co., Ltd.

Technology – Consumer/Industrial/Precision
Junya Ayada
+813-6736-8631
junya.ayada@JPM.com
JPM Securities Japan Co., Ltd.

See the end pages of this presentation for analyst certification and important disclosures, including non-US analyst disclosures.

## End demand assumptions

<table><tr><td>FY(mn units)</td></tr><tr><td>End demand volume (shipment)</td></tr><tr><td>Global smartphone shipment</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Apple</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Samsung</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Others</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global PC shipment</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Notebook PC (Including Chrome)</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Desktop PC</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Server shipment</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>General Server</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>AI server</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>IHS-Global Auto Production</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Vehicle Sales</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>ICE</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>xEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>HEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>PHEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>BEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>FCV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr></table>

<table><tr><td>CY2020</td><td>CY2021</td><td>CY2022</td><td>CY2023</td><td>CY2024</td><td>CY2025</td><td>CY2026E</td><td>CY2027E</td></tr><tr><td>1,264.74</td><td>1,351.40</td><td>1,193.43</td><td>1,141.86</td><td>1,223.18</td><td>1,245.45</td><td>1,104.26</td><td>1,075.13</td></tr><tr><td>-</td><td>6.85%</td><td>-11.69%</td><td>-4.32%</td><td>7.12%</td><td>1.82%</td><td>-11.34%</td><td>-2.64%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>207.15</td><td>230.06</td><td>232.16</td><td>229.14</td><td>225.85</td><td>240.64</td><td>238.55</td><td>252.50</td></tr><tr><td>-</td><td>11.06%</td><td>0.91%</td><td>-1.30%</td><td>-1.44%</td><td>6.55%</td><td>-0.87%</td><td>5.85%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>255.52</td><td>274.50</td><td>257.95</td><td>225.46</td><td>222.91</td><td>239.13</td><td>230.93</td><td>228.50</td></tr><tr><td>-</td><td>7.43%</td><td>-6.03%</td><td>-12.59%</td><td>-1.13%</td><td>7.28%</td><td>-3.43%</td><td>-1.05%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>802.08</td><td>846.73</td><td>703.31</td><td>687.27</td><td>774.44</td><td>765.62</td><td>634.79</td><td>594.08</td></tr><tr><td>-</td><td>5.57%</td><td>-16.94%</td><td>-2.28%</td><td>12.68%</td><td>-1.14%</td><td>-17.09%</td><td>-6.41%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>308.17</td><td>341.73</td><td>284.20</td><td>242.28</td><td>247.65</td><td>268.63</td><td>245.71</td><td>249.53</td></tr><tr><td>-</td><td>10.89%</td><td>-16.83%</td><td>-14.75%</td><td>2.21%</td><td>8.47%</td><td>-8.53%</td><td>1.55%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>228.33</td><td>256.38</td><td>208.12</td><td>179.83</td><td>186.54</td><td>201.52</td><td>183.79</td><td>186.35</td></tr><tr><td>-</td><td>12.29%</td><td>-18.82%</td><td>-13.59%</td><td>3.73%</td><td>8.03%</td><td>-8.80%</td><td>1.39%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>79.84</td><td>85.34</td><td>76.08</td><td>62.45</td><td>61.11</td><td>67.11</td><td>61.93</td><td>63.18</td></tr><tr><td>-</td><td>6.89%</td><td>-10.85%</td><td>-17.91%</td><td>-2.15%</td><td>9.82%</td><td>-7.72%</td><td>2.03%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12.67</td><td>12.92</td><td>13.83</td><td>11.35</td><td>12.09</td><td>12.12</td><td>13.88</td><td>15.03</td></tr><tr><td>-</td><td>1.94%</td><td>7.04%</td><td>-17.90%</td><td>6.46%</td><td>0.25%</td><td>14.57%</td><td>8.27%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12.67</td><td>12.92</td><td>13.43</td><td>10.78</td><td>11.02</td><td>10.30</td><td>11.68</td><td>12.44</td></tr><tr><td>-</td><td>1.94%</td><td>3.94%</td><td>-19.75%</td><td>2.27%</td><td>-6.49%</td><td>13.39%</td><td>6.51%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>-</td><td>-</td><td>0.40</td><td>0.58</td><td>1.07</td><td>1.81</td><td>2.20</td><td>2.58</td></tr><tr><td>-</td><td>-</td><td>-</td><td>44.08%</td><td>84.66%</td><td>69.87%</td><td>21.28%</td><td>17.63%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>74.59</td><td>77.19</td><td>82.34</td><td>90.49</td><td>89.59</td><td>93.10</td><td>90.88</td><td>91.58</td></tr><tr><td>-</td><td>3.49%</td><td>6.66%</td><td>9.90%</td><td>-0.99%</td><td>3.92%</td><td>-2.38%</td><td>0.77%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>77.18</td><td>80.27</td><td>78.98</td><td>86.70</td><td>88.69</td><td>91.74</td><td>87.69</td><td>88.55</td></tr><tr><td>-</td><td>3.99%</td><td>-1.60%</td><td>9.76%</td><td>2.30%</td><td>3.44%</td><td>-4.42%</td><td>0.99%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>71.52</td><td>68.12</td><td>62.17</td><td>64.15</td><td>60.90</td><td>58.04</td><td>52.93</td><td>51.29</td></tr><tr><td>-</td><td>-4.77%</td><td>-8.73%</td><td>3.20%</td><td>-5.07%</td><td>-4.70%</td><td>-8.80%</td><td>-3.10%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>5.66</td><td>12.15</td><td>16.82</td><td>22.54</td><td>27.79</td><td>33.70</td><td>34.76</td><td>37.26</td></tr><tr><td>-</td><td>114.69%</td><td>38.42%</td><td>34.04%</td><td>23.27%</td><td>21.28%</td><td>3.13%</td><td>7.21%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2.72</td><td>5.71</td><td>6.22</td><td>8.16</td><td>9.84</td><td>11.07</td><td>12.39</td><td>13.92</td></tr><tr><td>-</td><td>110.01%</td><td>9.00%</td><td>31.17%</td><td>20.52%</td><td>12.57%</td><td>11.92%</td><td>12.33%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0.89</td><td>1.82</td><td>2.74</td><td>4.08</td><td>6.47</td><td>7.61</td><td>6.95</td><td>7.36</td></tr><tr><td>-</td><td>104.61%</td><td>51.14%</td><td>48.70%</td><td>58.63%</td><td>17.48%</td><td>-8.62%</td><td>5.91%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2.04</td><td>4.61</td><td>7.83</td><td>10.29</td><td>11.47</td><td>15.01</td><td>15.40</td><td>15.96</td></tr><tr><td>-</td><td>125.40%</td><td>69.98%</td><td>31.32%</td><td>11.48%</td><td>30.89%</td><td>2.58%</td><td>3.66%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0.01</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>-</td><td>86.31%</td><td>-0.36%</td><td>-40.88%</td><td>-36.62%</td><td>41.82%</td><td>35.00%</td><td>40.00%</td></tr></table>

<table><tr><td colspan="4">CY2025</td><td colspan="4">CY2026</td></tr><tr><td></td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1QE</td><td>2QE</td><td>3QE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>296.94</td><td>288.92</td><td>320.06</td><td>339.53</td><td>292.13</td><td>262.70</td><td>272.45</td><td>276.97</td></tr><tr><td>0.24%</td><td>-0.01%</td><td>3.26%</td><td>3.49%</td><td>-1.62%</td><td>-9.07%</td><td>-14.87%</td><td>-18.43%</td></tr><tr><td>-9.49%</td><td>-2.70%</td><td>10.78%</td><td>6.09%</td><td>-13.96%</td><td>-10.08%</td><td>3.71%</td><td>1.66%</td></tr><tr><td>55.01</td><td>44.79</td><td>56.50</td><td>84.33</td><td>60.41</td><td>49.69</td><td>56.79</td><td>71.66</td></tr><tr><td>12.95%</td><td>-1.77%</td><td>3.76%</td><td>9.39%</td><td>9.81%</td><td>10.93%</td><td>0.51%</td><td>-15.02%</td></tr><tr><td>-28.64%</td><td>-18.58%</td><td>26.15%</td><td>49.24%</td><td>-28.36%</td><td>-17.75%</td><td>14.29%</td><td>26.18%</td></tr><tr><td>60.55</td><td>57.50</td><td>60.64</td><td>60.45</td><td>59.00</td><td>57.37</td><td>59.10</td><td>55.46</td></tr><tr><td>0.95%</td><td>7.40%</td><td>5.54%</td><td>16.38%</td><td>-2.55%</td><td>-0.22%</td><td>-2.55%</td><td>-8.25%</td></tr><tr><td>16.57%</td><td>-5.03%</td><td>5.46%</td><td>-0.32%</td><td>-2.39%</td><td>-2.76%</td><td>3.00%</td><td>-6.15%</td></tr><tr><td>181.54</td><td>186.83</td><td>202.62</td><td>194.17</td><td>172.91</td><td>155.70</td><td>156.42</td><td>149.74</td></tr><tr><td>-3.48%</td><td>-1.56%</td><td>2.46%</td><td>-2.25%</td><td>-4.75%</td><td>-16.66%</td><td>-22.80%</td><td>-22.88%</td></tr><tr><td>-8.61%</td><td>2.92%</td><td>8.45%</td><td>-4.17%</td><td>-10.95%</td><td>-9.95%</td><td>0.46%</td><td>-4.27%</td></tr><tr><td>60.32</td><td>65.94</td><td>72.46</td><td>69.91</td><td>65.68</td><td>59.50</td><td>60.00</td><td>60.53</td></tr><tr><td>6.58%</td><td>8.05%</td><td>12.15%</td><td>6.88%</td><td>8.89%</td><td>-9.77%</td><td>-17.19%</td><td>-13.42%</td></tr><tr><td>-7.78%</td><td>9.33%</td><td>9.88%</td><td>-3.52%</td><td>-6.05%</td><td>-9.41%</td><td>0.85%</td><td>0.88%</td></tr><tr><td>44.96</td><td>49.60</td><td>54.64</td><td>52.32</td><td>49.16</td><td>44.39</td><td>44.92</td><td>45.32</td></tr><tr><td>7.14%</td><td>7.72%</td><td>11.19%</td><td>5.95%</td><td>9.33%</td><td>-10.50%</td><td>-17.78%</td><td>-13.39%</td></tr><tr><td>-8.97%</td><td>10.32%</td><td>10.16%</td><td>-4.23%</td><td>-6.06%</td><td>-9.69%</td><td>1.19%</td><td>0.88%</td></tr><tr><td>15.36</td><td>16.34</td><td>17.82</td><td>17.59</td><td>16.52</td><td>15.11</td><td>15.08</td><td>15.21</td></tr><tr><td>4.96%</td><td>9.07%</td><td>15.19%</td><td>9.75%</td><td>7.59%</td><td>-7.55%</td><td>-15.38%</td><td>-13.49%</td></tr><tr><td>-4.14%</td><td>6.40%</td><td>9.06%</td><td>-1.33%</td><td>-6.04%</td><td>-8.57%</td><td>-0.17%</td><td>0.87%</td></tr><tr><td>2.94</td><td>2.94</td><td>2.86</td><td>3.38</td><td>3.26</td><td>3.40</td><td>3.44</td><td>3.78</td></tr><tr><td>2.94%</td><td>-1.53%</td><td>-5.62%</td><td>5.05%</td><td>11.13%</td><td>15.63%</td><td>20.17%</td><td>11.88%</td></tr><tr><td>-8.68%</td><td>0.15%</td><td>-2.68%</td><td>18.03%</td><td>-3.39%</td><td>4.20%</td><td>1.14%</td><td>9.88%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Electronic components Sales index by application

![](images/db4bdf31f5f296c60cc3d5e110cd4b89929f2e6eee281f13e049b705665e9b54.jpg)

For PC & Servers (including FCBGA, HDD related, 2Q18=100)  
![](images/267b1d68d2e4d95c5ec9cdef89cbdd8371e1547751bb3ddad0b7bb813548c765.jpg)

For Industrial Applications (2Q18=100)  
![](images/0b65d6adc619116a54c9e20297380b70be85be629ccdf695390d97b6d54769c1.jpg)

For Automotive (2Q18=100)  
![](images/30298bdd89b5ea0128aaaed1983a55351818bce3399ad7e9717296a220dfcf76.jpg)

## Quarterly automotive component revenues and \$ contents per car, comparison with theoretical contents growth

Automotive component revenues for 14 Japanese component makers  
![](images/81e41d0a9fcadea25eb5e7c038d48a527789bd489a0c62fd78b0018d1eb58824.jpg)

\$ contents per car for 14 Japanese component makers  
![](images/2b20bcb2478c7bdd2de312f3434557defce89920d8d9837b37d751e1a032bf3b.jpg)

Comparison between \$ contents per car for 14 Japanese component makers and theoretical \$ contents trend  
![](images/a4abb539d44133914e86c60fe0b0263b8ed902df09a36f6014c2fcf2b3404842.jpg)  
Source: Company data from Ibiden, Niterra, Mabuchi Motor, Murata Mfg., TDK, Taiyo Yuden, Nichicon, Nippon Chemi-con, Nippon Denpa Kogyo, Alps Alpine, Hirose Electric, JAE, Yokowo, Rohm, JPM

## Comparison of automotive semiconductors and electronic components

Automotive SEMI revenues for major analog/discrete/MCU makers  
![](images/c0f3e81c35bc61792f9c0209a8512b45009c6b7cbdd67761d9169ab76b2c9f0c.jpg)  
■ Renesas (Automotive) ■ ROHM (Automotive) ■ NXP (Automotive) ■ ON (Automotive) ■ STM (ADG) ■ IFX(ATV)

Note: For semiconductors, it is the total of IFX, STM, ON Semiconductor, NXP, Rohm, and Renesas Electronics; for Japanese electronic components, it is the total of Ibiden, Niterra, Mabuchi Motor, Murata Mfg., TDK, Taiyo Yuden, Nichicon, Nippon Chemicon, Nippon Denpa Kogyo, Alps Alpine, Hirose Electric, JAE, and Yokowo.

## \$ contents comparison for major analog/discrete/MCU makers and 14 Japanese component makers

![](images/2d50b128e56841943017484054221c88fd21c4f043afd4e3ebb691c7367e71d4.jpg)

YoY % change of \$ contents for major analog/discrete/MCU makers and 14 Japanese component makers  
![](images/8b7ac4004215f9420a625e85d90a4f712459f8672755348fd7460939e1ad212a.jpg)

## FA makers sales/orders vs. industrial component sales

FA makers sales and industrial component sales index (2Q18=100)  
![](images/1561556474263e9c3af0f7a232f7a0e293de05cc41d6870e2c3d2ea4120ab19e.jpg)  
FA makers orders and industrial component sales index (2Q18=100)

![](images/93ae330497ed44b636fff12e90152535bcf5a6730c50ca952b6a77c54a18c3b2.jpg)

## BB ratio and order index for Murata, Taiyo Yuden, Hirose, Rohm

![](images/59e6b33434a2b3c307595c299edc69d58aecbfe3972f1474ceeaebc956a8098b.jpg)

![](images/9b1b225651d600e8e8bebbe44a25377fd028668902e9b1e09bd41ca31078a0c0.jpg)

![](images/c4dbe5ef4835b5c6fe04018b19d1c7dbafb2e43f79ca294ff8017fb8d440d5b7.jpg)  
Source: Company data, JPM.

Order Index (CY2019 2Q=100)  
![](images/dbb50e63f5aee2683f9d0f896b46aeb0e9fe05a862077465c69d40fa12ff5f1f.jpg)

## Inventory and DIO for Japanese components sector

![](images/942204e42e30adad894a986394ccf2f6bdad0c0a4ee56c1974f625c6df6af9b8.jpg)

Inventories and sales yoy % chg.  
![](images/1e0f6093492650961621b7cdc86adb231026c7565c976ff8593f29192ed2930c.jpg)

Inventories yoy % chg.  
![](images/231ddf9ec0458beeec5dc70b7841fa8ab5a53ed4470229be57c82232a5a06726.jpg)  
Note: Inventory and Sales include Murata Mfg., Taiyo Yuden, TDK, Kyocera, Rohm, Nichicon, Nippon Chemi-Con, MinebeaMitsumi, Ibiden, Hirose Electric, JAE, Alps Alpine, Niterra, Wacom, NISSHA. Source: Bloomberg Finance L.P., JEITA, JPM

## JEITA global component shipments

Electronic component shipment value by Japanese makers (JPY)

![](images/8abf2ed5e4e2221c9545a9a3dafab3944fe0cd3bf6a8ab37211f9d98c3905aad.jpg)  
Electronic component shipment value by Japanese makers (US\$)

![](images/46082220c45fd8d82695b2a3b0b9211348b97c294944f320833dedc01ddb8811.jpg)

## Electronic component market cap vs component monthly sales/orders

![](images/f2c3e7cc6554a2b9f4484a22cf26c1746dc2fc358f16b6dbd0070c8841b722d8.jpg)

## Electronic component sales index, yoy % chg.

![](images/b306b9c3a5f583bc0ac4888dbd6fe840bbedfb29993dc74ae6176628c1c64750.jpg)

## JEITA global component shipments by category (\$mn)

![](images/b83588ed2aca7dc5cda7a86a3452bac4b76c6b85c3d12f5349454b43f60f1795.jpg)

Connecting components  
![](images/90cc977015f9ee3c8cf681923e50e38b74fdee1c58b745300760201215bc49aa.jpg)

Transducers  
![](images/03598e774ae232a0c106568d37c8445f96f4cc650d4f938eb3ce41a9c5fa5c19.jpg)

Other components  
![](images/91bf7634be61d04c345f400cc91bc314588763f17a55276eeff015fa2d851918.jpg)  
Source: JEITA, JPM.

## JEITA global component shipments by key component (\$mn)

![](images/95c67be196e9c0bcd90bf9dd884278e05eec182a2deee809770f742b7157df5d.jpg)

![](images/92c017560e9ac9bff3e11638a3f515f6944f3d931bb471b1d6c09da21869660b.jpg)

Inductors  
![](images/7a1a11c51145c5e651d2877307a1e88c39d5824c5ba3523eca415646f1c28197.jpg)

Connectors  
![](images/82ba34fb03293be73a1a64957bd65b01f05cc2f2be86b69aa66b4bbd0da7d1a3.jpg)  
Source: JEITA, JPM.

## Domestic component and semiconductor production value (\$mn)

![](images/42a422be0ef76444be02744ba81d1da25504c29bbcb8ba9d9c092dc3cf3057c5.jpg)

![](images/5d15cf9a59666560dc8eeb5cc9d25d218df9ee6071679c244c2d4db5490841f2.jpg)

![](images/f487534ecbce2490c31af980dbf5a3c96484463dc95f3970289b53a5899f727f.

[中间内容因长度限制已省略]

r its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is

## Disclosures

under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.
"""
