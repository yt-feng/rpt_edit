Alphabet Inc.

# Unpacking TPU-As-A-Service

GOOGL is about to embark on a major new initiative to scale AI outside of its datacenter walls via a new economic model, initially with Anthropic, but potentially with others down the road. We think this effort could boost '28 cons. gross profit by 15% and OI by more.

The Key Take-Away: Google is about to kick off one of its largest new business models with the help of several partners, to increase AI capacity industry-wide. Most investors are aware of TPU-aaS given the commentary on the recent earnings call, but the magnitude of how big this effort could be is likely underappreciated by the Street. Semiconductor buysiders have a decent handle on this theme, but we think now is the time for the consumer internet buyside to take notice. TPU-aaS is where Google takes inventory and sells TPUs directly to customers as a merchant vendor. One only has to look at the \$811B (up +\$479B Q/Q) in purchase commitments buried in the 10-Q this week, the \$275B+ increase in backlog in the past 6 months, or AVGO's commitment of 20+ GWs, to start to see how massive this could be. We are raising our Google Cloud revenue and OI estimates significantly with this report, after a full rebuild of our model. We'd also point out that this effort may reverse some future capex growth (potentially downside to our \$500B '28 estimate), as this asset-light approach to AI infrastructure helps GOOGL's capital efficiency.

The TPU-aaS effort has implications for many companies across the AI ecosystem including:

\- Anthropic: gains additional control of its business model, vertically integrates, and is less exposed to restrictions around hyperscaler service agreements.

\- Broadcom: opens a substantial new revenue pool and diversifies its business to other partners (consistent with our semiconductor research team's companion report on this topic today).

\- Blackstone and others: allows the companies to scale up their investments into new AI infrastructure and financial vehicles.

\- Fluidstack: massively increases its footprint as a colo managed service provider (what the industry calls "smart hands", or managed kubernetes) outside of Google's walls. In our view, Fluidstack's recent fundraise may signal its intentions to become a TPU neocloud.

We view this new business model as a win-win across the ecosystem and should allow TPU to become more of an industry standard for AI developers and other AI labs.

GOOGL OVERWEIGHT Unchanged

U.S. Internet POSITIVE Unchanged

Price Target USD 425.00 Unchanged

Price (23-Jul-26) USD 317.69

Potential Upside/Downside +33.8% Source: Bloomberg, BARC

<table><tr><td>Market Cap (USD mn)</td><td>3889212</td></tr><tr><td>Shares Outstanding (mn)</td><td>12230.00</td></tr><tr><td>Free Float (%)</td><td>98.77</td></tr><tr><td>52 Wk Avg Daily Volume (mn)</td><td>33.9</td></tr><tr><td>Dividend Yield (%)</td><td>0.28</td></tr><tr><td>Return on Equity TTM (%)</td><td>49.55</td></tr><tr><td>Current BVPS (USD)</td><td>50.90</td></tr><tr><td colspan="2">Source: Bloomberg</td></tr></table>

![](images/128a062385cefaae23f730698ae21f994bf5fc911ce99287f3f44766806f3aa1.jpg)  
Source: IDC  
Link to BARC Live for interactive charting

## U.S. Internet

Ross Sandler

+1 415 263 4470

ross.sandler@BARC.com

Alex Hughes  
+1 212 526 3069  
alexander.hughes@BARC.com  
BCI, US

## Background On TPU-As-A-Service

Two major announcements have happened in the past quarter that could be material to GOOGL financials over the coming years. The first was on May 18 $^{th}$ where Blackstone and Google Cloud set up a JV run by a former Google exec to provide TPU-as-a-service to customers, with the first 0.5 GWs coming online in '27 and more capacity into the future $^{1}$ . This was followed up by another mega-deal announcement forming an AI XPV Platform between Broadcom and Blackstone/Apollo, enabling as much as 20 GWs of AI capacity through 2028, with the first >1 GW coming online starting in "mid-2026" $^{2}$ . The latter will involve AI labs bringing both TPUs and other custom ASICs (OpenAI's Jalepeno, etc.) online.

For purposes of this report we only really care about the portion that flows through Google's P+L. These two entities could bring online 15-20 GWs of TPU-as-a-service AI cloud capacity outside of what Google is doing inside GCP.

## First Off, What Is TPU-As-A-Service (TPU-aaS)?

Historically, the only way an AI lab or enterprise customer could access AI specific compute running on Google's TPUs was via Google Cloud Platform (GCP). Customers would enter into agreements with Google to rent AI capacity on various terms. However, this is starting to change in '26 with the new "off platform" structures noted above. In the very near future, AI labs who are the largest buyers of AI compute (Anthropic, OpenAI, Meta, etc.) will be able to buy compute through a new vehicle that allows for more direct control. Broadcom explained it best in their press release: "It also establishes a scalable framework for future deployments of XPU-based compute capacity and networking to enable frontier model training and inference at the lowest cost and lowest power, significantly lowering per-token delivery costs."3 The XPU cost through this new entity is likely to be comparable to buying the same capacity through the existing cloud providers, but offers more control to the AI labs.

## TPU-aaS Entity Structure

Noted above, this new AI XPV Platform was announced in early June by Broadcom, Blackstone, and Apollo. Because we are conducting the analysis from the perspective of impact to GOOGL's shareholders, we are calling it TPU-as-a-service (while Broadcom calls it XPU as it involves non-TPU compute as well, like OpenAI's upcoming Jalepeno chip).

The XPV structure looks a lot like other AI lab compute structures, with a few key layers of the stack. First, Blackstone/Apollo would set up a SPV (special purpose entity) which is financed with equity and debt (collateralized by the compute assets). This SPV would subsequently buy the TPUs from Google, which are co-designed with Broadcom and manufactured by TSMC. These compute assets would go into a datacenter provided by another entity and managed by Fluidstack. Anthropic would then lease the capacity from the SPV at predetermined rates. We have attempted to illustrate this structure below.

FIGURE 1. A Hypothetical 1 GW TPU-aaS Structure  
![](images/0101cc4c35c861e53c9db6465b38ca2228d2539e75747c390cdc1fa1d7230588.jpg)  
Source: BARC Estimates, Company Disclosures

## What Is Google's Incentive?

Investors may ask that if there is only a static number of TPUs being produced in any given year, and if Alphabet as a whole is compute constrained, then why wouldn't the company just keep all the TPUs for itself and continue the existing business model of GCP leasing capacity to others? The answer is likely somewhat complex: 1) there are natural limits around how much AI capex GOOGL can deploy on its own, namely capital and to a lesser degree DC power, 2) unlike traditional cloud computing, select large customers of GCP (like Anthropic, Meta, and others) increasingly demand more control and flexibility and are willing to pay Google for that, 3) the TPU-aaS structure is a capital-light way to standardize more of the AI industry and the developer community around your stack, which could have downstream benefits, and 4) selling TPUs insulates Alphabet from the downstream liabilities that may come up from time to time within AI around copyright, security, privacy, and many other issues that have yet to emerge.

## What Is Anthropic's Incentive? (Or Other AI Labs?)

Large AI labs have scaled on the back of cloud computing contracts, and while this has been a great "asset-light" way of building their businesses, limitations exist. GCP and AWS provide compute services to Anthropic and others, but that's basically it; the AI lab has zero rights beyond what is laid out in the agreement with the hyperscaler.

For Anthropic, the incentives around controlling its own infrastructure have many benefits to its business model. These include: 1) the company can customize compute more effectively at various layers, and owning compute (via SPV) allows much deeper root access to the TPUs that would not likely be granted within GCP, 2) the company can more easily vertically integrate, and 3) while unlikely to happen, controlling the compute insulates Anthropic's business model from any discrepancies in terms stated in hyperscaler cloud service agreements (i.e., violations of AUPs which can result in termination of said agreement).

## Google's Unit Economics

We estimate Google sells each TPU for around \$20k per unit to the SPV while likely earning around a 25% gross margin, or around \$5k gross profit per unit. Each GW in '26 can host around 700k units, or \~\$14B in revenue per GW to Google. Future clusters will have next-generation TPUs (8t, 8i, 9, etc.) whereby revenue per unit and revenue per GW likely moves upward like most compute systems going forward, illustrated below.

FIGURE 2. GOOGL Likely Earning \~25% GM On External TPU-aaS Sales

<table><tr><td>TPU Economics</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Unit Revenue</td><td>20,000</td><td>33,333</td><td>53,333</td></tr><tr><td>- Unit Cost</td><td>15,000</td><td>25,000</td><td>40,000</td></tr><tr><td>Gross Profit</td><td>5,000</td><td>8,333</td><td>13,333</td></tr><tr><td>% Gross Margin</td><td>25%</td><td>25%</td><td>25%</td></tr><tr><td colspan="4">Per GW:</td></tr><tr><td>TPU Revenue ($B)</td><td>14.3</td><td>18.3</td><td>22.0</td></tr><tr><td>TPUs per GW</td><td>714,286</td><td>549,286</td><td>411,964</td></tr></table>

Source: BARC Estimates, Company Disclosures

Broadcom has stated that this new AI XPV initiative amounts to 20 GWs over the next few years. The company has also stated that OpenAI and a few others are designing custom XPUs that would be included in this 20 GWs but separate from Google. We estimate TPU may be as much as 15 GW of the total, illustrated below.

FIGURE 3. Broadcom/Blackstone/Apollo AI XPV Platform GW Breakdown

<table><tr><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>Total</td></tr><tr><td>TPU GW</td><td>1.4</td><td>3.2</td><td>10.0</td><td>14.6</td></tr><tr><td>Other GW</td><td>--</td><td>--</td><td>--</td><td>5.4</td></tr><tr><td>Total GW</td><td></td><td></td><td></td><td>20</td></tr></table>

Source: BARC Estimates, Company Disclosures

Noted above, Google also has a similar JV structure (outside of Broadcom's announced 20 GW) where it invested alongside Blackstone into a new TPU-aaS entity run by former Google infra exec Ben Treynor Sloss that amounts to another 500 MWs in 2027 and "plans to scale significantly" into the future.

Both of these result in a total of 3.7 GWs in '27 and 11.5 GWs in '28 of potential TPU-aaS external sales, illustrated below.

FIGURE 4. GOOGL Could Have $15+$ GWs Online By 2028

<table><tr><td>External TPU Sales Framework</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Blackstone-Google TPU Cloud JV</td><td></td><td></td><td></td></tr><tr><td># GW</td><td></td><td>0.5</td><td>1.5</td></tr><tr><td># TPUs</td><td></td><td>274,643</td><td>617,946</td></tr><tr><td>Broadcom-Apollo-Blackstone AI XPV Platform</td><td></td><td></td><td></td></tr><tr><td># GW</td><td>1.4</td><td>3.2</td><td>10.0</td></tr><tr><td># TPUs</td><td>1,000,000</td><td>1,757,714</td><td>4,119,643</td></tr><tr><td>Total External TPU GW</td><td>1.4</td><td>3.7</td><td>11.5</td></tr><tr><td># TPUs</td><td>1,000,000</td><td>2,032,357</td><td>4,737,589</td></tr><tr><td>GOOGL Revenue ($B)</td><td>20.0</td><td>67.7</td><td>252.7</td></tr><tr><td>TPU External ASP</td><td>20,000</td><td>33,333</td><td>53,333</td></tr><tr><td>GOOGL Gross Profit ($B)</td><td>5.0</td><td>16.9</td><td>63.2</td></tr></table>

For illustrative purposes  
Source: BARC Estimates, Company Disclosures

Based on the capacity scaling noted above, and using the ASP for the TPUs noted above, we think TPU-as-a-service revenue can reach as much as \$250B in 2028, at which point would represent 35%+ upside to current consensus Alphabet revenue and 15% to gross profit.

FIGURE 5. TPU-aaS Could Represent $15\%$ Potential Upside To Consensus Alphabet GP In '28

<table><tr><td></td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="5">Current Consensus Estimates:</td></tr><tr><td>Alphabet Total Revenue</td><td>402.8</td><td>493.0</td><td>597.9</td><td>711.1</td></tr><tr><td>% Y/Y Change</td><td>36%</td><td>22%</td><td>21%</td><td>19%</td></tr><tr><td>Alphabet Gross Profit</td><td>240.3</td><td>299.2</td><td>361.3</td><td>431.9</td></tr><tr><td>% Margin</td><td>60%</td><td>61%</td><td>60%</td><td>61%</td></tr><tr><td colspan="5">External TPU Contribution:</td></tr><tr><td>External TPU Revenue</td><td></td><td>20.0</td><td>67.7</td><td>252.7</td></tr><tr><td>% Upside to Total Revenue</td><td></td><td>4%</td><td>11%</td><td>36%</td></tr><tr><td>External TPU Gross Profit</td><td></td><td>5.0</td><td>16.9</td><td>63.2</td></tr><tr><td>% Upside to Total Gross Profit</td><td></td><td>2%</td><td>5%</td><td>15%</td></tr></table>

For illustrative purposes

Source: BARC Estimates, Company Disclosures, Bloomberg Consensus as of 7/23/26

This new structure has many benefits to Anthropic's business model (or any other AI lab/TPU customer), noted above, but it also begs the question around just how much more or less a 1 GW TPU-as-a-service cluster may cost in terms of overall capex and annual opex, relative to Anthropic's ability to just rent TPUs directly from GCP. Below we attempt to illustrate a side by side comparison.

FIGURE 6. Difference In AI Lab Unit Economics For GCP Rental Vs.Owned TPU-aaS

<table><tr><td>AI Lab Unit Econ - 1 GW</td><td>GCP</td><td>TPUaaS</td></tr><tr><td>TPUs per GW (m)</td><td>0.7</td><td>0.7</td></tr><tr><td>Training TPUs</td><td>0.4</td><td>0.4</td></tr><tr><td>Inference TPUs</td><td>0.4</td><td>0.4</td></tr><tr><td>Total Capex per GW ($m)</td><td>20,000</td><td>25,000</td></tr><tr><td>TPU Capex per GW ($m)</td><td>10,714</td><td>14,286</td></tr><tr><td>TPU ASP</td><td>15,000</td><td>20,000</td></tr><tr><td>Other Capex per GW ($m)</td><td>9,286</td><td>10,714</td></tr><tr><td>Other Capex per TPU</td><td>13,000</td><td>15,000</td></tr><tr><td>Annual Depreciation Cost per GW ($m)</td><td>4,000</td><td>5,000</td></tr><tr><td>Total Cost per TPU</td><td>28,000</td><td>35,000</td></tr><tr><td>Depreciation/TPU/Year</td><td>5,600</td><td>7,000</td></tr><tr><td>Useful Life (Years)</td><td>5</td><td>5</td></tr><tr><td>AI Lab Inference Revenue per GW ($m)</td><td>6,667</td><td>6,667</td></tr><tr><td>AI Lab Inference Margin</td><td>70%</td><td>63%</td></tr><tr><td>AI Lab Inference Cost per GW</td><td>2,000</td><td>2,500</td></tr></table>

2026E  
Source: BARC Estimates, Company Disclosures

## What's Already Been Announced

Noted above, Broadcom/Blackstone/Apollo's AI XPV initiative spans 20 GWs through 2028. It is not yet clear how big the Blackstone-Google JV TPU project (outside of the AI XPV initiative) is going to be longer term but has already announced 500 MWs in '27. We have identified the first tranches of datacenters coming online to support these efforts from TeraWulf and others, illustrated below.

We estimate Google has around \$88B of TPU revenue in the backlog as of 2Q26. This number should ramp up to over \$300B cumulative over time, but obviously some revenue starts dropping out of the backlog once TPUs have been sold through.

FIGURE 7. What's Already Been Announced From Compute DC Providers

<table><tr><td></td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td></tr><tr><td>AI Compute Capacity by Shell Provider (MW)</td><td>42</td><td>457</td><td>901</td><td>798</td><td>924</td><td>960</td><td>1,019</td></tr><tr><td>Terawulf</td><td>42</td><td>168</td><td>336</td><td>50</td><td>50</td><td>162</td><td>320</td></tr><tr><td>Cipher Digital</td><td></td><td>168</td><td>39</td><td></td><td></td><td>50</td><td>200</td></tr><tr><td>Next Frontier (Coatue)</td><td></td><td></td><td>300</td><td></td><td>130</td><td></td><td></td></tr><tr><td>Hut 8</td><td></td><td></td><td></td><td></td><td>245</td><td></td><td></td></tr><tr><td>Estimated Undisclosed Capacity</td><td>0</td><td>121</td><td>226</td><td>748</td><td>499</td><td>748</td><td>499</td></tr><tr><td>Cumulative Compute (MW)</td><td>42</td><td>499</td><td>1,400</td><td>2,198</td><td>3,122</td><td>4,081</td><td>5,100</td></tr><tr><td>Implied TPU Revenue ($B)</td><td>$0.6</td><td>$6.5</td><td>$12.9</td><td>$14.6</td><td>$16.9</td><td>$17.6</td><td>$18.7</td></tr><tr><td>Cumulative TPU Revenue ($B)</td><td>$0.6</td><td>$7.1</td><td>$20.0</td><td>$34.6</td><td>$51.5</td><td>$69.1</td><td>$87.7</td></tr><tr><td>% of 2Q26 Cloud Backlog</td><td>0.1%</td><td>1.4%</td><td>3.9%</td><td>6.7%</td><td>10.0%</td><td>13.4%</td><td>17.1%</td></tr><tr><td>Cumulative TPU COGS ($B)</td><td>$0.5</td><td>$5.4</td><td>$15.0</td><td>$26.0</td><td>$38.6</td><td>$51.8</td><td>$65.8</td></tr><tr><td>% of 2Q26 Purchase Commitments</td><td>0.1%</td><td>0.9%</td><td>2.5%</td><td>4.3%</td><td>6.4%</td><td>8.5%</td><td>10.8%</td></tr><tr><td>Inventory Balance</td><td>$10.0</td><td>$11.4</td><td>$14.4</td><td>$15.6</td><td>$16.8</td><td>$17.9</td><td>$19.6</td></tr></table>

Source: BARC Estimates, Company Disclosures

## Estimate Changes and Valuation

We have done a complete overhaul of our Google Cloud segment to factor in TPU-aaS revenues and profits. Google's CFO provided some high-level explanation of how TPU-aaS may flow through the company's financial statements last night, and combined with the new inventory line on the BS and the \$811B in purchase commitments, we can now piece together what this may look like.

We fully appreciate that our estimates are moving upwards rather dramatically on this revision, but as of now this is our best estimate of how the next three years may play out.

FIGURE 8. Estimate Changes

<table><tr><td rowspan="2"></td><td colspan="3">3Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old Est.</td><td>Delta</td><td>New</td><td>Old Est.</td><td>Delta</td><td>New</td><td>Old Est.</td><td>Delta</td><td>New</td><td>Old Est.</td><td>Delta</td></tr><tr><td colspan="13">Google Services</td></tr><tr><td>Search Revenue</td><td>64,486.4</td><td>64,486.4</td><td>0.0%</td><td>259,428.9</td><td>259,428.9</td><td>0.0%</td><td>285,371.8</td><td>285,371.8</td><td>0.0%</td><td>308,201.5</td><td>308,201.5</td><td>0.0%</td></tr><tr><td>YouTube Revenue</td><td>11,287.1</td><td>11,287.1</td><td>0.0%</td><td>44,860.2</td><td>44,860.2</td><td>0.0%</td><td>49,346.3</td><td>49,346.3</td><td>0.0%</td><td>54,280.9</td><td>54,280.9</td><td>0.0%</td></tr><tr><td>Other - Play/Subscription Revenue</td><td>14,800.5</td><td>14,800.5</td><td>0.0%</td><td>55,710.2</td><td>55,710.2</td><td>0.0%</td><td>64,066.7</td><td>64,066.7</td><td>0.0%</td><td>73,676.7</td><td>73,676.7</td><td>0.0%</td></tr><tr><td>Google Network Revenue</td><td>7,280.5</td><td>7,280.5</td><td>0.0%</td><td>29,304.2</td><td>29,304.2</td><td>0.0%</td><td>29,011.1</td><td>29,011.1</td><td>0.0%</td><td>28,721.0</td><td>28,721.0</td><td>0.0%</td></tr><tr><td>Total Advertising Revenue</td><td>83,053.9</td><td>83,053.9</td><td>0.0%</td><td>333,593.3</td><td>333,593.3</td><td>0.0%</td><td>363,729.1</td><td>363,729.1</td><td>0.0%</td><td>391,203.4</td><td>391,203.4</td><td>0.0%</td></tr><tr><td>Total Google Services Gross Revenue</td><td>97,854.4</td><td>97,854.4</td><td>0.0%</td><td>389,303.5</td><td>389,303.5</td><td>0.0%</td><td>427,795.9</td><td>427,795.9</td><td>0.0%</td><td>464,880.1</td><td>464,880.1</td><td>0.0%</td></tr><tr><td>Google Services Operating Income</td><td>39,644.5</td><td>39,644.5</td><td>0.0%</td><td>164,954.4</td><td>164,954.4</td><td>0.0%</td><td>183,401.2</td><td>183,401.2</td><td>0.0%</td><td>199,296.6</td><td>199,296.6</td><td>0.0%</td></tr><tr><td colspan="13">Google Cloud</td></tr><tr><td>Google Cloud Revenue</td><td>31,469.2</td><td>27,282.6</td><td>15.3%</td><td>117,844.7</td><td>101,224.2</td><td>16.4%</td><td>222,147.1</td><td>151,836.3</td><td>46.3%</td><td>485,610.5</td><td>212,570.8</td><td>128.4%</td></tr><tr><td>Google Cloud Operating Income</td><td>10,038.2</td><td>9,743.1</td><td>3.0%</td><td>35,978.9</td><td>34,367.6</td><td>4.7%</td><td>67,486.3</td><td>57,153.5</td><td>18.1%</td><td>144,848.5</td><td>84,941.8</td><td>70.5%</td></tr><tr><td colspan="13">Other Bets</td></tr><tr><td>Other Bets Revenue</td><td>450.0</td><td>450.0</td><td>0.0%</td><td>1,718.0</td><td>1,718.0</td><td>0.0%</td><td>1,925.0</td><td>1,925.0</td><td>0.0%</td><td>1,925.0</td><td>1,925.0</td><td>0.0%</td></tr><tr><td>Other Bets Operating Income</td><td>-1,550.0</td><td>-1,550.0</td><td>0.0%</td><td>-6,974.0</td><td>-6,974.0</td><td>0.0%</td><td>-6,075.0</td><td>-6,075.0</td><td>0.0%</td><td>-6,075.0</td><td>-6,075.0</td><td>0.0%</td></tr><tr><td colspan="13">Consolidated</td></tr><tr><td>Gross Revenue</td><td>129,883.6</td><td>125,697.0</td><td>3.3%</td><td>508,902.1</td><td>492,281.7</td><td>3.4%</td><td>651,949.7</td><td>581,638.9</td><td>12.1%</td><td>952,415.6</td><td>679,376.0</td><td>40.2%</td></tr><tr><td>TAC</td><td>16,195.2</td><td>16,195.2</td><td>0.0%</td><td>65,586.8</td><td>65,586.8</td><td>0.0%</td><td>69,897.1</td><td>69,897.1</td><td>0.0%</td><td>73,667.8</td><td>73,667.8</td><td>0.0%</td></tr><tr><td>Net Revenue</td><td>113,688.4</td><td>109,501.8</td><td>3.8%</td><td>443,315.3</td><td>426,694.9</td><td>3.9%</td><td>582,052.5</td><td>511,741.8</td><td>13.7%</td><td>878,747.9</td><td>605,708.2</td><td>45.1%</td></tr><tr><td>COGS</td><td>39,770.9</td><td>34,357.5</td><td>15.8%</td><td>144,688.0</td><td>129,665.8</td><td>11.6%</td><td>213,602.8</td><td>163,590.5</td><td>30.6%</td><td>393,541.6</td><td>203,693.9</td><td>93.2%</td></tr><tr><td>Total Operating Expense (ex. SBC)</td><td>73,899.5</td><td>68,475.1</td><td>7.9%</td><td>278,195.6</td><td>263,202.4</td><td>5.7%</td><td>368,771.6</td><td>319,459.8</td><td>15.4%</td><td>574,236.7</td><td>385,675.0</td><td>48.9%</td></tr><tr><td>GAAP EBIT</td><td>39,788.9</td><td>41,026.7</td><td>-3.0%</td><td>165,119.7</td><td>163,492.5</td><td>1.0%</td><td>213,281.0</td><td>192,281.9</td><td>10.9%</td><td>304,511.2</td><td>220,033.2</td><td>38.4%</td></tr><tr><td>Consolidated EBITDA (ex SBC)</td><td>56,226.8</td><td>57,505.8</td><td>-2.2%</td><td>228,487.7</td><td>226,906.4</td><td>0.7%</td><td>306,032.9</td><td>285,428.1</td><td>7.2%</td><td>441,290.7</td><td>357,117.8</td><td>23.6%</td></tr><tr><td>GAAP EPS</td><td>$2.82</td><td>$2.90</td><td>-2.9%</td><td>$20.20</td><td>$20.09</td><td>0.6%</td><td>$15.40</td><td>$13.94</td><td>10.5%</td><td>$21.88</td><td>$15.98</td><td>36.9%</td></tr><tr><td>Proforma EPS</td><td>$3.34</td><td>$3.42</td><td>-2.5%</td><td>$22.37</td><td>$22.14</td><td>1.0%</td><td>$17.83</td><td>$16.38</td><td>8.8%</td><td>$24.78</td><td>$18.88</td><td>31.3%</td></tr><tr><td>Total Capex</td><td>59,923.9</td><td>59,923.5</td><td>0.0%</td><td>200,490.5</td><td>200,493.3</td><td>0.0%</td><td>350,156.0</td><td>350,154.8</td><td>0.0%</td><td>500,324.2</td><td>500,324.4</td><td>0.0%</td></tr></table>

Source: BARC Estimates, Company Reports

We have maintained our \$425 price target by rolling back our valuation framework to straight 2027 on an average of 25x EPS and 15x EBITDA (vs. 2027/2028 hybrid previously). This updated framework takes a more near-term view of TPU-aaS impact to GOOGL shares, but we'd note that flipping to straight 2028 would result in a much higher potential valuation, illustrated below. Given all the moving pieces and the heightened capex outlook, we felt it was prudent to use 2027 for now.

FIGURE 9. GOOGL Valuation

<table><tr><td colspan="4">Google Inc. -- Valuation Worksheet(in millions except per share amounts)</td></tr><tr><td>Current Price</td><td>$317.69</td><td></td><td></td></tr><tr><td>Shares Outstanding</td><td>12,309.0</td><td></td><td></td></tr><tr><td>Current Market Cap</td><td>3,910,446.2</td><td></td><td></td></tr><tr><td>Plus Debt</td><td>98,165.0</td><td></td><td></td></tr><tr><td>Less Cash</td><td>242,474.0</td><td></td><td></td></tr><tr><td>Adj. Enterprise Value</td><td>3,766,137.2</td><td></td><td></td></tr><tr><td>Price to Earnings</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>GAAP EPS</td><td>$20.20</td><td>$15.40</td><td>$21.88</td></tr><tr><td>Current P/E multiple</td><td>15.7x</td><td>20.6x</td><td>14.5x</td></tr><tr><td>Adjusted EPS</td><td>$22.37</td><td>$17.83</td><td>$24.78</td></tr><tr><td>Current P/E multiple</td><td>14.2x</td><td>17.8x</td><td>12.8x</td></tr><tr><td>Target Multiple</td><td>25.0x</td><td>25.0x</td><td>25.0x</td></tr><tr><td>Implied Stock Price on fwd. EPS</td><td>$560</td><td>$450</td><td>$620</td></tr><tr><td>EV to EBITDA</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Adjusted EBITDA</td><td>$228,488</td><td>$306,033</td><td>$441,291</td></tr><tr><td>Current EV/EBITDA Multiple</td><td>16.5x</td><td>12.3x</td><td>8.5x</td></tr><tr><td>Target Multiple</td><td>15.0x</td><td>15.0x</td><td>15.0x</td></tr><tr><td>Enterprise Value</td><td>3,427,316</td><td>4,590,494</td><td>6,619,360</td></tr><tr><td>Plus FY End Cash</td><td>242,453</td><td>233,713</td><td>206,541</td></tr><tr><td>Less FY End Debt</td><td>98,165</td><td>98,165</td><td>98,165</td></tr><tr><td>Equity Value</td><td>3,571,604</td><td>4,726,042</td><td>6,727,736</td></tr><tr><td>FY End Projected Sharecount</td><td>12282.0</td><td>12253.7</td><td>12204.8</td></tr><tr><td>Implied Stock Price on fwd. EBITDA</td><td>$300</td><td>$400</td><td>$550</td></tr><tr><td>Average</td><td>$430</td><td>$425</td><td>$585</td></tr><tr><td>Target Price</td><td></td><td>$425</td><td></td></tr></table>

Source: BARC Estimates, Company Reports. Price as of 4pm EST on 07/23/26

## Income Statement

FIGURE 10. GOOGL Income Statement

<table><tr><td>Google - Quarterly Income Statement($ in Millions, except per share amounts)</td><td>FY2023A</td><td>FY2024A</td><td>FY2025A</td><td>Mar A1QA</td><td>Jun A2QA</td><td>Sep E3QE</td><td>Dec E4QE</td><td>FY2026E</td><td>FY2027E</td><td>FY2028E</td></tr><tr><td>Consolidated Net Revenue</td><td>256,508</td><td>295,118</td><td>342,910</td><td>94,668</td><td>103,617</td><td>113,688</td><td>131,342</td><td>443,315</td><td>582,053</td><td>878,748</td></tr><tr><td>Gross Revenue</td><td>307,394</td><td>350,018</td><td>402,836</td><td>109,896</td><td>119,796</td><td>129,884</td><td>149,327</td><td>508,902</td><td>651,950</td><td>952,416</td></tr><tr><td>Google Web Sites Revenue</td><td>206,543</td><td>234,231</td><td>264,899</td><td>70,282</td><td>74,326</td><td>75,773</td><td>83,908</td><td>304,289</td><td>334,718</td><td>362,482</td></tr><tr><td>Google Network Web Sites Revenue</td><td>31,312</td><td>30,359</td><td>29,792</td><td>6,971</td><td>7,303</td><td>7,280</td><td>7,750</td><td>29,304</td><td>29,011</td><td>28,721</td></tr><tr><td>TAC</td><td>50,886</td><td>54,900</td><td>59,926</td><td>15,228</td><td>16,179</td><td>16,195</td><td>17,985</td><td>65,587</td><td>69,897</td><td>73,668</td></tr><tr><td>Other, Cloud, Other Bets Revenue</td><td>69,539</td><td>85,428</td><td>108,145</td><td>32,643</td><td>38,167</td><td>46,830</td><td>57,669</td><td>175,309</td><td>288,221</td><td>561,212</td></tr><tr><td>Alphabet Net Revenue</td><td>256,508</td><td>295,118</td><td>342,910</td><td>94,668</td><td>103,617</td><td>113,688</td><td>131,342</td><td>443,315</td><td>582,053</td><td>878,748</td></tr><tr><td>New Segment Revenue (as of 4Q19)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Google Search &amp; Other</td><td>175,033</td><td>198,084</td><td>224,532</td><td>60,399</td><td>63,271</td><td>64,486</td><td>71,272</td><td>259,429</td><td>285,372</td><td>308,201</td></tr><tr><td>YouTube Ads</td><td>31,510</td><td>36,147</td><td>40,367</td><td>9,883</td><td>11,055</td><td>11,287</td><td>12,635</td><td>44,860</td><td>49,346</td><td>54,281</td></tr><tr><td>Subtotal: Google Properties</td><td>206,543</td><td>234,231</td><td>264,899</td><td>70,282</td><td>74,326</td><td>75,773</td><td>83,908</td><td>304,289</td><td>334,718</td><td>362,482</td></tr><tr><td>Google Network Members Properties</td><td>31,312</td><td>30,359</td><td>29,792</td><td>6,971</td><td>7,303</td><td>7,280</td><td>7,750</td><td>29,304</td><td>29,011</td><td>28,721</td></tr><tr><td>Google Advertising</td><td>237,855</td><td>264,590</td><td>294,691</td><td>77,253</td><td>81,629</td><td>83,054</td><td>91,657</td><td>333,593</td><td>363,729</td><td>391,203</td></tr><tr><td>Google Cloud</td><td>33,088</td><td>43,229</td><td>58,705</td><td>20,028</td><td>24,768</td><td>31,469</td><td>41,579</td><td>117,845</td><td>222,147</td><td>485,610</td></tr><tr><td>Google Other</td><td>34,688</td><td>40,340</td><td>48,030</td><td>12,384</td><td>12,911</td><td>14,801</td><td>15,615</td><td>55,710</td><td>64,067</td><td>73,677</td></tr><tr><td>Cost of Net Revenues</td><td>82,446</td><td>91,406</td><td>102,609</td><td>26,043</td><td>29,764</td><td>39,771</td><td>49,110</td><td>144,688</td><td>213,603</td><td>393,542</td></tr><tr><td>Gross Profit</td><td>174,062</td><td>203,712</td><td>240,301</td><td>68,625</td><td>73,853</td><td>73,918</td><td>82,232</td><td>298,627</td><td>368,450</td><td>485,206</td></tr><tr><td>Operating Expenses:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Product Development</td><td>45,427</td><td>49,326</td><td>61,087</td><td>17,032</td><td>18,219</td><td>20,450</td><td>22,590</td><td>78,290</td><td>100,700</td><td>129,628</td></tr><tr><td>Sales and Marketing</td><td>27,917</td><td>27,808</td><td>28,693</td><td>7,606</td><td>8,403</td><td>8,750</td><td>9,738</td><td>34,496</td><td>33,577</td><td>30,730</td></tr><tr><td>General and Administrative</td><td>16,425</td><td>14,188</td><td>18,025</td><td>4,291</td><td>4,961</td><td>4,929</td><td>5,040</td><td>19,221</td><td>20,892</td><td>20,337</td></tr><tr><td>Stock Based Compensation</td><td>22,460</td><td>22,785</td><td>24,953</td><td>6,751</td><td>7,957</td><td>7,997</td><td>8,670</td><td>31,375</td><td>37,121</td><td>44,170</td></tr><tr><td>Other</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating Expenses (ex. COGS, Stock Comp)</td><td>89,769</td><td>91,322</td><td>107,805</td><td>28,929</td><td>31,583</td><td>34,129</td><td>37,367</td><td>132,008</td><td>155,169</td><td>180,695</td></tr><tr><td>Total Operating Expenses</td><td>172,215</td><td>182,728</td><td>213,871</td><td>54,972</td><td>62,847</td><td>73,900</td><td>86,477</td><td>278,196</td><td>368,772</td><td>574,237</td></tr><tr><td>Income from Operations (GAAP)</td><td>84,293</td><td>112,390</td><td>129,039</td><td>39,696</td><td>40,770</td><td>39,789</td><td>44,865</td><td>165,120</td><td>213,281</td><td>304,511</td></tr><tr><td>Non -GAAP operating income (ex-SBC)</td><td>84,293</td><td>112,390</td><td>129,039</td><td>39,696</td><td>42,270</td><td>39,789</td><td>44,865</td><td>165,120</td><td>213,281</td><td>304,511</td></tr><tr><td>Depreciation &amp; Amortization</td><td>12,448</td><td>15,827</td><td>21,652</td><td>6,611</td><td>7,233</td><td>8,441</td><td>9,708</td><td>31,993</td><td>55,631</td><td>92,610</td></tr><tr><td>EBITDA (inc SBC)</td><td>96,741</td><td>128,217</td><td>150,691</td><td>46,307</td><td>48,003</td><td>48,230</td><td>54,573</td><td>197,113</td><td>268,912</td><td>397,121</td></tr><tr><td>Net Income Continuing Operations (GAAP)</td><td>73,795</td><td>100,118</td><td>132,170</td><td>62,578</td><td>112,193</td><td>34,645</td><td>38,892</td><td>248,308</td><td>188,738</td><td>267,057</td></tr><tr><td>Net Income (GAAP)</td><td>73,795</td><td>100,118</td><td>132,170</td><td>62,578</td><td>112,107</td><td>34,645</td><td>38,892</td><td>248,222</td><td>188,738</td><td>267,057</td></tr><tr><td>EPS (GAAP)</td><td>$5.81</td><td>$8.05</td><td>$10.81</td><td>$5.11</td><td>$9.11</td><td>$2.82</td><td>$3.17</td><td>$20.20</td><td>$15.40</td><td>$21.88</td></tr><tr><td>Diluted Shares Outstanding</td><td>12,721</td><td>12,447</td><td>12,230</td><td>12,238</td><td>12,309</td><td>12,297</td><td>12,284</td><td>12,282</td><td>12,254</td><td>12,205</td></tr><tr><td>Adjusted Net Income</td><td>95,965</td><td>118,346</td><td>152,132</td><td>67,979</td><td>119,973</td><td>41,043</td><td>45,828</td><td>273,408</td><td>218,435</td><td>302,393</td></tr><tr><td>Adjusted EPS</td><td>$7.55</td><td>$9.62</td><td>$12.84</td><td>$5.55</td><td>$9.75</td><td>$3.34</td><td>$3.73</td><td>$22.37</td><td>$17.83</td><td>$24.78</td></tr><tr><td>Adjusted EBITDA (ex SBC)</td><td>119,201</td><td>151,002</td><td>175,644</td><td>53,058</td><td>55,960</td><td>56,227</td><td>63,243</td><td>228,488</td><td>306,033</td><td>441,291</td></tr><tr><td>Adjusted Income from Operations</td><td>106,753</td><td>135,175</td><td>153,992</td><td>46,447</td><td>48,727</td><td>47,786</td><td>53,535</td><td>196,494</td><td>250,402</td><td>348,681</td></tr><tr><td>Free Cash Metrics</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Free Cash Flow</td><td>68,615</td><td>72,764</td><td>73,266</td><td>10,116</td><td>(5,855)</td><td>2,249</td><td>4,074</td><td>10,584</td><td>(59,249)</td><td>(78,467)</td></tr><tr><td>FCF per share</td><td>$5.39</td><td>$5.85</td><td>$5.99</td><td>$0.83</td><td>-$0.48</td><td>$0.18</td><td>$0.33</td><td>$0.86</td><td>-$4.84</td><td>-$6.43</td></tr><tr><td>Margin Analysis</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross Margin</td><td>56.6%</td><td>58.2%</td><td>59.7%</td><td>62.4%</td><td>61.6%</td><td>56.9%</td><td>55.1%</td><td>58.7%</td><td>56.5%</td><td>50.9%</td></tr><tr><td>Sales and Marketing as % of Net Revenue</td><td>10.9%</td><td>9.4%</td><td>8.4%</td><td>8.0%</td><td>8.1%</td><td>7.7%</td><td>7.4%</td><td>7.8%</td><td>5.8%</td><td>3.5%</td></tr><tr><td>Product Development as % of Net Revenue</td><td>17.7%</td><td>16.7%</td><td>17.8%</td><td>18.0%</td><td>17.6%</td><td>18.0%</td><td>17.2%</td><td>17.7%</td><td>17.3%</td><td>14.8%</td></tr><tr><td>General and Administrative as % of Net Revenue</td><td>6.4%</td><td>4.8%</td><td>5.3%</td><td>4.5%</td><td>4.8%</td><td>4.3%</td><td>3.8%</td><td>4.3%</td><td>3.6%</td><td>2.3%</td></tr><tr><td>Operating Margin (GAAP)</td><td>27.4%</td><td>32.1%</td><td>32.0%</td><td>36.1%</td><td>34.0%</td><td>30.6%</td><td>30.0%</td><td>32.4%</td><td>32.7%</td><td>32.0%</td></tr><tr><td>Operating Margin (% of Net Revenue)</td><td>32.9%</td><td>38.1%</td><td>37.6%</td><td>41.9%</td><td>39.3%</td><td>35.0%</td><td>34.2%</td><td>37.2%</td><td>36.6%</td><td>34.7%</td></tr><tr><td>Operating Margin (Non GAAP)</td><td>32.9%</td><td>38.1%</td><td>37.6%</td><td>41.9%</td><td>40.8%</td><td>35.0%</td><td>34.2%</td><td>37.2%</td><td>36.6%</td><td>34.7%</td></tr><tr><td>EBITDA Margin</td><td>37.7%</td><td>43.4%</td><td>43.9%</td><td>48.9%</td><td>46.3%</td><td>42.4%</td><td>41.6%</td><td>44.5%</td><td>46.2%</td><td>45.2%</td></tr><tr><td>Net Income (GAAP)</td><td>28.8%</td><td>33.9%</td><td>38.5%</td><td>66.1%</td><td>108.3%</td><td>30.5%</td><td>29.6%</td><td>56.0%</td><td>32.4%</td><td>30.4%</td></tr><tr><td>Adjusted Net Income</td><td>37.4%</td><td>40.1%</td><td>44.4%</td><td>71.8%</td><td>115.8%</td><td>36.1%</td><td>34.9%</td><td>61.7%</td><td>37.5%</td><td>34.4%</td></tr><tr><td>Adjusted EBITDA Margin</td><td>46.5%</td><td>51.2%</td><td>51.2%</td><td>56.0%</td><td>54.0%</td><td>49.5%</td><td>48.2%</td><td>51.5%</td><td>52.6%</td><td>50.2%</td></tr><tr><td>Effective Tax Rate</td><td>13.9%</td><td>16.4%</td><td>17.0%</td><td>19.2%</td><td>19.1%</td><td>16.0%</td><td>16.0%</td><td>18.2%</td><td>15.0%</td><td>15.0%</td></tr><tr><td>Pretax Income</td><td>33.4%</td><td>40.6%</td><td>46.3%</td><td>81.8%</td><td>133.9%</td><td>36.3%</td><td>35.3%</td><td>68.5%</td><td>38.1%</td><td>35.8%</td></tr></table>

Source: BARC Estimates, Company Reports

GOOGL: Quarterly and Annual EPS (USD)

<table><tr><td></td><td>2025</td><td colspan="3">2026</td><td colspan="3">2027</td><td colspan="2">Change y/y</td></tr><tr><td>FY Dec</td><td>Actual</td><td>Old</td><td>New</td><td>Cons</td><td>Old</td><td>New</td><td>Cons</td><td>2026</td><td>2027</td></tr><tr><td>Q1</td><td>3.17A</td><td>5.55A</td><td>5.55A</td><td>5.11A</td><td>3.70E</td><td>4.14E</td><td>3.66E</td><td>75%</td><td>-25%</td></tr><tr><td>Q2</td><td>2.82A</td><td>9.62A</td><td>9.75A</td><td>9.11A</td><td>4.08E</td><td>4.32E</td><td>3.85E</td><td>246%</td><td>-56%</td></tr><tr><td>Q3</td><td>3.57A</td><td>3.42E</td><td>3.34E</td><td>3.25E</td><td>4.13E</td><td>4.43E</td><td>3.97E</td><td>-6%</td><td>33%</td></tr><tr><td>Q4</td><td>3.28A</td><td>3.54E</td><td>3.73E</td><td>3.53E</td><td>4.47E</td><td>4.94E</td><td>4.41E</td><td>14%</td><td>32%</td></tr><tr><td>Year</td><td>12.84A</td><td>22.14E</td><td>22.37E</td><td>15.05E</td><td>16.38E</td><td>17.83E</td><td>15.63E</td><td>74%</td><td>-20%</td></tr><tr><td>P/E</td><td>24.7</td><td></td><td>14.2</td><td></td><td></td><td>17.8</td><td></td><td></td><td></td></tr></table>

Consensus numbers are from Bloomberg received on 23-Jul-2026; 12:50 GMT Source: BARC

Alphabet Inc. (GOOGL)

<table><tr><td>Valuation and leverage metrics</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>Average</td></tr><tr><td>P/E (adj) (x)</td><td>24.7</td><td>14.2</td><td>17.8</td><td>12.8</td><td>17.4</td></tr><tr><td>EV/sales (x)</td><td>11.5</td><td>8.9</td><td>6.8</td><td>4.5</td><td>7.9</td></tr><tr><td>EV/EBITDA (adj) (x)</td><td>22.4</td><td>17.3</td><td>12.9</td><td>9.0</td><td>15.4</td></tr><tr><td>FCF yield (%)</td><td>1.9</td><td>0.3</td><td>-1.5</td><td>-2.0</td><td>-0.3</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net debt/EBITDA (adj) (x)</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td></tr><tr><td>Selected operating metrics ($mn)</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td></td></tr><tr><td>Google sites net revenue</td><td>264,899</td><td>304,289</td><td>334,718</td><td>362,482</td><td></td></tr><tr><td>Network sites net revenue</td><td>29,792</td><td>29,304</td><td>29,011</td><td>28,721</td><td></td></tr><tr><td>Traffic acquisition cost</td><td>59,926</td><td>65,587</td><td>69,897</td><td>73,668</td><td></td></tr></table>

## U.S. Internet

<table><tr><td>Income statement ($mn)</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>CAGR</td></tr><tr><td>Revenue</td><td>342,910</td><td>443,315</td><td>582,053</td><td>878,748</td><td>36.8%</td></tr><tr><td>Gross profit</td><td>240,301</td><td>298,627</td><td>368,450</td><td>485,206</td><td>26.4%</td></tr><tr><td>EBITDA (adj)</td><td>175,644</td><td>228,488</td><td>306,033</td><td>441,291</td><td>35.9%</td></tr><tr><td>EBIT (adj)</td><td>129,039</td><td>165,120</td><td>213,281</td><td>304,511</td><td>33.1%</td></tr><tr><td>Pre-tax income (adj)</td><td>183,779</td><td>335,084</td><td>259,166</td><td>358,354</td><td>24.9%</td></tr><tr><td>Net income (adj)</td><td>152,132</td><td>273,408</td><td>218,435</td><td>302,393</td><td>25.7%</td></tr><tr><td>EPS (adj) ($)</td><td>12.84</td><td>22.37</td><td>17.83</td><td>24.78</td><td>24.5%</td></tr><tr><td>Diluted shares (mn)</td><td>12,230.0</td><td>12,282.0</td><td>12,253.7</td><td>12,204.8</td><td>-0.1%</td></tr><tr><td>DPS ($)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>N/A</td></tr></table>

<table><tr><td>Margin and return data</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>Average</td></tr><tr><td>EBITDA (adj) margin (%)</td><td>51.2</td><td>51.5</td><td>52.6</td><td>50.2</td><td>51.4</td></tr><tr><td>EBIT (adj) margin (%)</td><td>37.6</td><td>37.2</td><td>36.6</td><td>34.7</td><td>36.5</td></tr><tr><td>Pre-tax (adj) margin (%)</td><td>53.6</td><td>75.6</td><td>44.5</td><td>40.8</td><td>53.6</td></tr><tr><td>Net (adj) margin (%)</td><td>44.4</td><td>61.7</td><td>37.5</td><td>34.4</td><td>44.5</td></tr><tr><td>ROIC (%)</td><td>26.9</td><td>21.0</td><td>18.7</td><td>20.0</td><td>21.6</td></tr><tr><td>ROE (%)</td><td>35.7</td><td>43.4</td><td>21.7</td><td>22.3</td><td>30.8</td></tr></table>

<table><tr><td>Balance sheet and cash flow ($mn)</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>CAGR</td></tr><tr><td>Tangible fixed assets</td><td>246,597</td><td>423,213</td><td>718,255</td><td>1,126,485</td><td>65.9%</td></tr><tr><td>Intangible fixed assets</td><td>1,283</td><td>9,105</td><td>9,105</td><td>9,105</td><td>92.2%</td></tr><tr><td>Cash and equivalents</td><td>29,009</td><td>55,890</td><td>47,150</td><td>19,978</td><td>-11.7%</td></tr><tr><td>Total assets</td><td>595,281</td><td>1,027,502</td><td>1,337,758</td><td>1,759,588</td><td>43.5%</td></tr><tr><td>Short and long-term debt</td><td>46,547</td><td>98,165</td><td>98,165</td><td>98,165</td><td>28.2%</td></tr><tr><td>Other long-term liabilities</td><td>19,472</td><td>44,200</td><td>44,200</td><td>44,200</td><td>31.4%</td></tr><tr><td>Total liabilities</td><td>180,016</td><td>299,001</td><td>324,236</td><td>375,639</td><td>27.8%</td></tr><tr><td>Shareholders&#x27; equity</td><td>415,265</td><td>728,501</td><td>1,013,522</td><td>1,383,949</td><td>49.4%</td></tr><tr><td>Net debt/(funds)</td><td>17,538</td><td>42,275</td><td>51,015</td><td>78,187</td><td>64.6%</td></tr><tr><td>Change in working capital</td><td>618</td><td>586</td><td>1,069</td><td>9,673</td><td>150.1%</td></tr><tr><td>Cash flow from operations</td><td>164,713</td><td>211,074</td><td>290,908</td><td>421,857</td><td>36.8%</td></tr><tr><td>Capital expenditure</td><td>-91,447</td><td>-200,490</td><td>-350,156</td><td>-500,324</td><td>N/A</td></tr><tr><td>Free cash flow</td><td>73,266</td><td>10,584</td><td>-59,249</td><td>-78,467</td><td>N/A</td></tr></table>

Note: FY End Dec  
Source: Company data, Bloomberg, BARC  
Price (23-Jul-2026) USD 317.69  
Price Target USD 425.00  
Google continues to grow revenue and EPS at a \~20% CAGR on a normalized basis. The company continues to innovate its product, and its machine learning capabilities should help advertisers get higher ROI, causing them to continue to allocate their advertising budgets to Google.

## OVERWEIGHT

## Why OVERWEIGHT?

## Upside case USD 530.00

We expect Google to continue to take share from other channels in mobile advertising, and 50% of every incremental dollar going forward. Reduction of losses in "Other Bets" could be a source of upside to estimates.

<table><tr><td>Downside case</td><td>USD 210.00</td></tr></table>

Google is migrating toward lower-margin businesses and, having benefited from the substantial improvement in mobile monetization, the growth rate may decelerate going forward.

Upside/Downside scenarios

![](images/0644fc40d332258eed70a545075f3484c17646572f1f37d830895217213aadd2.jpg)

## Analyst(s) Certification(s):

I, Ross Sandler, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC"). All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

Where any companies are the subject of this research report, for current important disclosures regarding those companies please refer to https://publicresearch.barlays.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

The analysts responsible for preparing this research report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by investment banking activities, the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst.

Research analysts employed outside the US by affiliates of BARC Capital Inc. are not registered/qualified as research analysts with FINRA. Such non-US research analysts may not be associated persons of BARC Capital Inc., which is a FINRA member, and therefore may not be subject to FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst's account.

Analysts regularly conduct site visits to view the material operations of covered companies, but BARC policy prohibits them from accepting payment or reimbursement by any covered company of their travel expenses for such visits.

BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://

publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Primary Stocks (Ticker, Date, Price)

Alphabet Inc. (GOOGL, 23-Jul-2026, USD 317.69), Overweight/Positive, A/CD/CE/D/E/J/K/L/M/N

## Materially Mentioned Stocks (Ticker, Date, Price)

Broadcom Inc. (AVGO, 23-Jul-2026, USD 392.47), Overweight/Neutral, CD/CE/D/J/K/L/M/N

Unless otherwise indicated, prices are sourced from Bloomberg and reflect the closing price in the relevant trading market, which may not be the last available closing price at the time of publication.

## Disclosure Legend:

A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of the issuer in the previous 12 months.

B: An employee or non-executive director of BARC PLC is a director of this issuer.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by this issuer.

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by this issuer.

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Conduct) in respect of this issuer.

D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from this issuer in the past 12 months.

E: BARC Bank PLC and/or an affiliate expects to receive or intends to seek compensation for investment banking services from this issuer within the next 3 months.

FA: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with US regulations.

FB: BARC Bank PLC and/or an affiliate beneficially owns a long position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FC: BARC Bank PLC and/or an affiliate beneficially owns a short position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FD: BARC Bank PLC and/or an affiliate beneficially owns $1\%$ or more of a class of equity securities of this issuer, as calculated in accordance with South Korean regulations.

FE: BARC Bank PLC and/or its group companies has financial interests in relation to this issuer and such interests aggregate to an amount equal to or more than 1% of this issuer's market capitalization, as calculated in accordance with HK regulations.

GD: One of the Research Analysts on the fundamental credit coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

GE: One of the Research Analysts on the fundamental equity coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

H: This issuer beneficially owns more than 5% of any class of common equity securities of BARC PLC.

I: BARC Bank PLC and/or an affiliate is party to an agreement with this issuer for the provision of financial services to BARC Bank PLC and/or an affiliate.

J: BARC Bank PLC and/or an affiliate is a liquidity provider and/or trades regularly in the securities of this issuer and/or in any related derivatives.

K: BARC Bank PLC and/or an affiliate has received non-investment banking related compensation (including compensation for brokerage services, if applicable) from this issuer within the past 12 months.

L: This issuer is, or during the past 12 months has been, an investment banking client of BARC Bank PLC and/or an affiliate.

M: This issuer is, or during the past 12 months has been, a non-investment banking client (securities related services) of BARC Bank PLC and/or an affiliate.

N: This issuer is, or during the past 12 months has been, a non-investment banking client (non-securities related services) of BARC Bank PLC and/or an affiliate.

O: Not in use.

P: Not in use.

Q: BARC Bank PLC and/or an affiliate is a Corporate Broker to this issuer.

R: Not in use.

S: This issuer is a Corporate Broker to BARC PLC.

T: BARC Bank PLC and/or an affiliate is providing investor engagement services to this issuer.

## Risk Disclosure(s)

Master limited partnerships (MLPs) are pass-through entities structured as publicly listed partnerships. For tax purposes, distributions to MLP unit holders may be treated as a return of principal. Investors should consult their own tax advisors before investing in MLP units.

## Disclosure(s) regarding Information Sources

Bloomberg® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

## Guide to the BARC Fundamental Equity Research Rating System:

Our coverage analysts use a relative rating system in which they rate stocks as Overweight, Equal Weight or Underweight (see definitions below) relative to other companies covered by the analyst or a team of analysts that are deemed to be in the same industry (the "industry coverage universe").

In addition to the stock rating, we provide industry views which rate the outlook for the industry coverage universe as Positive, Neutral or Negative (see definitions below). A rating system using terms such as buy, hold and sell is not the equivalent of our rating system. Investors should carefully read the entire research report including the definitions of all ratings and not infer its contents from ratings alone.

## Stock Rating

Overweight - The stock is expected to outperform the unweighted expected total return of the industry coverage universe over a 12-month investment horizon.

Equal Weight - The stock is expected to perform in line with the unweighted expected total return of the industry coverage universe over a 12-month investment horizon.

Underweight - The stock is expected to underperform the unweighted expected total return of the industry coverage universe over a 12-month investment horizon.

Rating Suspended - The rating and target price have been suspended temporarily due to market events that made coverage impracticable or to comply with applicable regulations and/or firm policies in certain circumstances including where the Investment Bank of BARC Bank PLC is acting in an advisory capacity in a merger or strategic transaction involving the company.

## Industry View

Positive - industry coverage universe fundamentals/valuations are improving.

Neutral - industry coverage universe fundamentals/valuations are steady, neither improving nor deteriorating.

Negative - industry coverage universe fundamentals/valuations are deteriorating.

Below is the list of companies that constitute the "industry coverage universe":

## U.S. Internet

Airbnb Inc. (ABNB)

Alphabet Inc. (GOOGL)

Amazon.com, Inc. (AMZN)

Booking Holdings Inc. (BKNG)

Chewy, Inc. (CHWY)

DoorDash, Inc. (DASH)

Duolingo, Inc. (DUOL)

eBay, Inc. (EBAY)

Ethos Technologies Inc. (LIFE)

Etsy Inc (ETSY)

Expedia Inc. (EXPE)

Liftoff Mobile, Inc. (LFTO)

Lyft, Inc. (LYFT)

Maplebear, Inc. (CART)

Match Group, Inc. (MTCH)

Meta Platforms, Inc. (META)

Pinterest, Inc. (PINS)

Roblox Corporation (RBLX)

Shopify (SHOP)

Snap, Inc (SNAP)

Tripadvisor Inc. (TRIP)

## U.S. Semiconductors & Semiconductor Capital Equipment

<table><tr><td>Advanced Micro Devices (AMD)</td><td>Allegro Microsystems (ALGM)</td><td>Analog Devices (ADI)</td></tr><tr><td>Applied Materials Inc. (AMAT)</td><td>Arm Holdings plc (ARM)</td><td>Astera Labs, Inc. (ALAB)</td></tr><tr><td>Broadcom Inc. (AVGO)</td><td>Camtek (CAMT)</td><td>Cerebras Systems Inc. (CBRS)</td></tr><tr><td>Cirrus Logic Inc. (CRUS)</td><td>Coherent Corp. (COHR)</td><td>Credo Technology Group (CRDO)</td></tr><tr><td>Intel Corp. (INTC)</td><td>KLA Corporation (KLAC)</td><td>Lam Research Corporation (LRCX)</td></tr><tr><td>Lumentum Holdings Inc. (LITE)</td><td>MACOM Technology Solutions Holdings, Inc. (MTSI)</td><td>Marvell Technology Group, Ltd. (MRVL)</td></tr><tr><td>Microchip Technology (MCHP)</td><td>Micron Technology, Inc. (MU)</td><td>Nova Limited (NVMI)</td></tr><tr><td>NVIDIA Corp. (NVDA)</td><td>NXP Semiconductors NV (NXPI)</td><td>ON Semiconductor (ON)</td></tr><tr><td>Penguin Solutions (PENG)</td><td>Qorvo Inc. (QRVO)</td><td>QUALCOMM, Inc. (QCOM)</td></tr><tr><td>Sandisk Corporation (SNDK)</td><td>Seagate Technology plc (STX)</td><td>Silicon Laboratories, Inc. (SLAB)</td></tr><tr><td>SiTime Corporation (SITM)</td><td>Skyworks Solutions, Inc. (SWKS)</td><td>Synaptics Incorporated (SYNA)</td></tr><tr><td>Texas Instruments, Inc. (TXN)</td><td>Veeco Instruments Inc (VECO)</td><td>Western Digital Corporation (WDC)</td></tr></table>

## Distribution of Ratings:

BARC Equity Research has 1791 companies under coverage.

51% have been assigned an Overweight rating which, for purposes of mandatory regulatory disclosures, is classified as a Buy rating; 46% of companies with this rating are investment banking clients of the Firm; 64% of the issuers with this rating have received financial services from the Firm.

34% have been assigned an Equal Weight rating which, for purposes of mandatory regulatory disclosures, is classified as a Hold rating; 39% of companies with this rating are investment banking clients of the Firm; 58% of the issuers with this rating have received financial services from the Firm.

14% have been assigned an Underweight rating which, for purposes of mandatory regulatory disclosures, is classified as a Sell rating; 32% of companies with this rating are investment banking clients of the Firm; 57% of the issuers with this rating have received financial services from the Firm.

## Guide to the BARC Price Target:

Each analyst has a single price target on the stocks that they cover. The price target represents that analyst's expectation of where the stock will trade in the next 12 months. Upside/downside scenarios, where provided, represent potential upside/potential downside to each analyst's price target over the same 12-month period.

## Types of investment recommendations produced by BARC Equity Research:

In addition to any ratings assigned under BARC' formal rating systems, this publication may contain investment recommendations in the form of trade ideas, thematic screens, scorecards or portfolio recommendations that have been produced by analysts within Equity Research. Any such investment recommendations shall remain open until they are subsequently amended, rebalanced or closed in a future research report.

BARC may also re-distribute equity research reports produced by third-party research providers that contain recommendations that differ from and/or conflict with those published by BARC' Equity Research Department.

## Disclosure of other investment recommendations produced by BARC Equity Research:

BARC Equity Research may have published other investment recommendations in respect of the same securities/instruments recommended in this research report during the preceding 12 months. To view all investment recommendations published by BARC Equity Research in the preceding 12 months please refer to https://live.barcap.com/go/research/Recommendations.

## Legal entities involved in producing BARC:

BARC Bank PLC (BARC, UK)

BARC Capital Inc. (BCI, US)

BARC Bank Ireland PLC, Frankfurt Branch (BBI, Frankfurt)

BARC Bank Ireland PLC, Paris Branch (BBI, Paris)

BARC Bank Ireland PLC, Milan Branch (BBI, Milan)

BARC Securities Japan Limited (BSJL, Japan)

BARC Bank PLC, Hong Kong Branch (BARC Bank, Hong Kong)

BARC Bank Mexico, S.A. (BBMX, Mexico)

BARC Capital Casa de Bolsa, S.A. de C.V. (BCCB, Mexico)

BARC Securities (India) Private Limited (BSIPL, India)

BARC Bank PLC, Singapore Branch (BARC Bank, Singapore)

BARC Bank PLC, DIFC Branch (BARC Bank, DIFC)

Alphabet Inc. (GOOGL / GOOGL)  
Stock Rating: OVERWEIGHT  
Industry View: POSITIVE  
Closing Price: USD 317.69 (23-Jul-2026)

Rating and Price Target Chart (as of 23-Jul-2026)  
![](images/fc140e7cd099090ab95f3ee3c7ec67c9ea8875ed07ca162fe142c76dca832029.jpg)  
Source: LSEG Data & Analytics, Bloomberg, BARC Link to BARC Live for interactive charting

<table><tr><td>Publication Date</td><td>Closing Price*</td><td>Rating</td><td>Adjusted Price Target</td><td>Currency</td></tr><tr><td>22-Jul-2026</td><td>342.09</td><td></td><td>425.00 USD</td><td></td></tr><tr><td>30-Apr-2026</td><td>349.94</td><td></td><td>405.00 USD</td><td></td></tr><tr><td>04-Feb-2026</td><td>333.04</td><td></td><td>360.00 USD</td><td></td></tr><tr><td>29-Oct-2025</td><td>274.57</td><td></td><td>315.00 USD</td><td></td></tr><tr><td>02-Sep-2025</td><td>212.91</td><td></td><td>250.00 USD</td><td></td></tr><tr><td>23-Jul-2025</td><td>190.23</td><td></td><td>235.00 USD</td><td></td></tr><tr><td>29-Oct-2024</td><td>169.68</td><td></td><td>220.00 USD</td><td></td></tr><tr><td>25-Apr-2024</td><td>156.00</td><td></td><td>200.00 USD</td><td></td></tr><tr><td>30-Jan-2024</td><td>151.46</td><td></td><td>173.00 USD</td><td></td></tr><tr><td>24-Oct-2023</td><td>138.81</td><td></td><td>180.00 USD</td><td></td></tr><tr><td>25-Jul-2023</td><td>122.21</td><td></td><td>200.00 USD</td><td></td></tr></table>

On 23-Jul-2023, prior to any intra-day change that may  
have been published, the rating for this security was  
Overweight, and the adjusted price target was 160.00 USD.  
Source: Bloomberg, BARC  
\*This is the closing price referenced in the publication, which may not be the last available closing price at the time of publication.  
Historical stock prices and price targets may have been  
adjusted for stock splits and dividends.  
A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of Alphabet Inc. in the previous 12 months.  
CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by Alphabet Inc..  
CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by Alphabet Inc..  
D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from Alphabet Inc. in the past 12 months.

E: BARC Bank PLC and/or an affiliate expects to receive or intends to seek compensation for investment banking services from Alphabet Inc. within the next 3 months.

J: BARC Bank PLC and/or an affiliate is a liquidity provider and/or trades regularly in the securities by Alphabet Inc. and/or in any related derivatives.

K: BARC Bank PLC and/or an affiliate has received non-investment banking related compensation (including compensation for brokerage services, if applicable) from Alphabet Inc. within the past 12 months.

L: Alphabet Inc. is, or during the past 12 months has been, an investment banking client of BARC Bank PLC and/or an affiliate.

M: Alphabet Inc. is, or during the past 12 months has been, a non-investment banking client (securities related services) of BARC Bank PLC and/or an affiliate.

N: Alphabet Inc. is, or during the past 12 months has been, a non-investment banking client (non-securities related services) of BARC Bank PLC and/or an affiliate.

Valuation Methodology: Our \$425 price target is based on an average of 25x EPS and 15x EBITDA multiples on our FY27E estimates.

Risks which May Impede the Achievement of the BARC Valuation and Price Target: Increasing competition and regulatory issues could cause multiple compression and downward estimate revisions, while continued innovation, successful product launches and an uptick in GCP adoption could cause upside to our current estimates.

## Broadcom Inc. (AVGO / AVGO)

Stock Rating: OVERWEIGHT

Industry View: NEUTRAL

Closing Price: USD 392.47 (23-Jul-2026)

Rating and Price Target Chart (as of 23-Jul-2026)  
![](images/a0647723fc9c25e92025452f280aa55d6a7b1036cce72ac1ccdc3d3d5f1e1acb.jpg)  
Source: LSEG Data & Analytics, Bloomberg, BARC Link to BARC Live for interactive charting

<table><tr><td>Publication Date</td><td>Closing Price*</td><td>Rating</td><td>Adjusted Price Target</td><td>Currency</td></tr><tr><td>11-Dec-2025</td><td>406.37</td><td></td><td>500.00</td><td>USD</td></tr><tr><td>13-Oct-2025</td><td>356.70</td><td></td><td>450.00</td><td>USD</td></tr><tr><td>04-Sep-2025</td><td>306.10</td><td></td><td>400.00</td><td>USD</td></tr><tr><td>06-Jun-2025</td><td>256.85</td><td></td><td>265.00</td><td>USD</td></tr><tr><td>22-Apr-2025</td><td>166.21</td><td></td><td>215.00</td><td>USD</td></tr><tr><td>17-Jan-2025</td><td>229.41</td><td></td><td>260.00</td><td>USD</td></tr><tr><td>13-Dec-2024</td><td>180.66</td><td></td><td>205.00</td><td>USD</td></tr><tr><td>15-Jul-2024</td><td>1700.67</td><td></td><td>200.00</td><td>USD</td></tr><tr><td>12-Jun-2024</td><td>146.10</td><td></td><td>200.00</td><td>USD</td></tr><tr><td>17-Apr-2024</td><td>128.26</td><td></td><td>150.00</td><td>USD</td></tr><tr><td>19-Mar-2024</td><td>123.80</td><td>Overweight</td><td>140.50</td><td>USD</td></tr></table>

On 23-Jul-2023, prior to any intra-day change that may  
have been published, the rating and price target for this  
security were suspended.  
Source: Bloomberg, BARC  
\*This is the closing price referenced in the publication, which may not be the last available closing price at the time of publication.  
Historical stock prices and price targets may have been  
adjusted for stock splits and dividends.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by Broadcom Inc..

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by Broadcom Inc..

D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from Broadcom Inc. in the past 12 months.

J: BARC Bank PLC and/or an affiliate is a liquidity provider and/or trades regularly in the securities by Broadcom Inc. and/or in any related derivatives.

K: BARC Bank PLC and/or an affiliate has received non-investment banking related compensation (including compensation for brokerage services, if applicable) from Broadcom Inc. within the past 12 months.

L: Broadcom Inc. is, or during the past 12 months has been, an investment banking client of BARC Bank PLC and/or an affiliate.

M: Broadcom Inc. is, or during the past 12 months has been, a non-investment banking client (securities related services) of BARC Bank PLC and/or an affiliate.

N: Broadcom Inc. is, or during the past 12 months has been, a non-investment banking client (non-securities related services) of BARC Bank PLC and/or an affiliate.

Valuation Methodology: Our price target of \$500 is based on 22x our CY27E EPS of \$22.55.

Risks which May Impede the Achievement of the BARC Valuation and Price Target: Slowdown of AI spend. Slowdown of enterprise spend. Share loss in wireless.

## Disclaimer:

This publication has been produced by BARC Department in the Investment Bank of BARC Bank PLC and/or one or more of its affiliates (collectively and each individually, "BARC").

It has been prepared for institutional investors and not for retail investors. It has been distributed by one or more BARC affiliated legal entities listed below or by an independent and non-affiliated third-party entity (as may be communicated to you by such third-party entity in its communications with you). It is provided for information purposes only, and BARC makes no express or implied warranties, and expressly disclaims all warranties of merchantability or fitness for a particular purpose or use with respect to any data included in this publication. BARC may provide research to certain categories of recipients that do not use it for investment purposes, including public and private companies in covered industries, media organisations, regulators, and academic institutions that use such research for their own internal informational, news gathering, regulatory or academic purposes. To the extent that this publication states on the front page that it is intended for institutional investors and is not subject to all of the independence and disclosure standards applicable to debt research reports prepared for retail investors under U.S. FINRA Rule 2242, it is an “institutional debt research report” and distribution to retail investors is strictly prohibited. Media organisations are prohibited from re-publishing any opinion or recommendation concerning a debt issuer or debt security contained in any BARC institutional debt research report. Any recipients that do not want to continue receiving BARC institutional debt research reports should contact debtresearch@BARC.com. Unless clients have agreed to receive “institutional debt research reports” as required by US FINRA Rule 2242, they will not receive any such reports that may be co-authored by non-debt research analysts. Eligible clients may get access to such cross asset reports by contacting debtresearch@BARC.com. BARC will not treat unauthorized recipients of this report as its clients and accepts no liability for use by them of the contents which may not be suitable for their personal use. Prices shown are indicative and BARC is not offering to buy or sell or soliciting offers to buy or sell any financial instrument.

Without limiting any of the foregoing and to the extent permitted by law, in no event shall BARC, nor any affiliate, nor any of their respective officers, directors, partners, or employees have any liability for (a) any special, punitive, indirect, or consequential damages; or (b) any lost profits, lost revenue, loss of anticipated savings or loss of opportunity or other financial loss, even if notified of the possibility of such damages, arising from any use of this publication or its contents.

Other than disclosures relating to BARC, the information contained in this publication (including third-party data) has been obtained from sources that BARC believes to be reliable, but BARC does not represent or warrant that it is accurate or complete. Third-party data, including third-party forecasts and predictions, is provided for information purposes only, has not been adopted or endorsed by BARC, and does not represent the views or opinions of BARC. Presentations by Third-Party Speakers: Any views or opinions expressed by third-party speakers during a BARC-hosted event are solely those of the speaker and do not represent the views or opinions of BARC. BARC is not responsible for, and makes no warranties whatsoever as to, the information or opinions contained in any written, electronic, audio or video presentations by any third-party speakers, and such presentations have not been adopted or endorsed by BARC and do not represent the views or opinions of BARC. Content from third-party presentations is provided for information purposes only and has not been independently verified by BARC for its accuracy or completeness.

The views in this publication are solely and exclusively those of the authoring analyst(s) and are subject to change, and BARC has no obligation to update its opinions or the information in this publication. Unless otherwise disclosed herein, the analysts who authored this report have not received any compensation from the subject companies in the past 12 months. If this publication contains recommendations, they are general recommendations that were prepared independently of any other interests, including those of BARC and/or its affiliates, and/or the subject companies. This publication does not contain personal investment recommendations or investment advice or take into account the individual financial circumstances or investment objectives of the clients who receive it. BARC is not a fiduciary to any recipient of this publication. The securities and other investments discussed herein may not be suitable for all investors and may not be available for purchase in all jurisdictions. The United States imposed sanctions on certain Chinese companies (https://ofac.treasury.gov/sanctions-programs-and-country-information/chinese-military-companies-sanctions), which may restrict U.S. persons from purchasing securities issued by those companies. Investors must independently evaluate the merits and risks of the investments discussed herein, including any sanctions restrictions that may apply, consult any independent advisors they believe necessary, and exercise independent judgment with regard to any investment decision. The value of and income from any investment may fluctuate from day to day as a result of changes in relevant economic markets (including changes in market liquidity). The information herein is not intended to predict actual results, which may differ substantially from those reflected. Past performance is not necessarily indicative of future results. The information provided does not constitute a financial benchmark and should not be used as a submission or contribution of input data for the purposes of determining a financial benchmark.

This publication is not investment company sales literature as defined by Section 270.24(b) of the US Investment Company Act of 1940, nor is it intended to constitute an offer, promotion or recommendation of, and should not be viewed as marketing (including, without limitation, for the purposes of the UK Alternative Investment Fund Managers Regulations 2013 (SI 2013/1773) or AIFMD (Directive 2011/61)) or pre-marketing (including, without limitation, for the purposes of Directive (EU) 2019/1160) of the securities, products or issuers that are the subject of this report.

Third Party Distribution: Any views expressed in this communication are solely those of BARC and have not been adopted or endorsed by any third party distributor.

United Kingdom: This document is being distributed (1) only by or with the approval of an authorised person (BARC Bank PLC) or (2) to, and is directed at (a) persons in the United Kingdom having professional experience in matters relating to investments and who fall within the definition of "investment professionals" in Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (the "Order"); or (b) high net worth companies, unincorporated associations and partnerships and trustees of high value trusts as described in Article 49(2) of the Order; or (c) other persons to whom it may otherwise lawfully be communicated (all such persons being "Relevant Persons"). Any investment or investment activity to which this communication relates is only available to and will only be engaged in with Relevant Persons. Any other persons who receive this communication should not rely on or act upon it. BARC Bank PLC is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority and is a member of the London Stock Exchange.

European Economic Area (“EEA”): This material is being distributed to any “Authorised User” located in a Restricted EEA Country by BARC Bank Ireland PLC. The Restricted EEA Countries are Austria, Bulgaria, Estonia, Finland, Hungary, Iceland, Liechtenstein, Lithuania, Luxembourg, Malta, Portugal, Romania, Slovakia and Slovenia. For any other “Authorised User” located in a country of the European Economic Area, this material is being distributed by BARC Bank PLC. BARC Bank Ireland PLC is a bank authorised by the Central Bank of Ireland whose registered office is at 1 Molesworth Street, Dublin 2, Ireland. BARC Bank PLC is not registered in France with the Autorité des marchés financiers or the Autorité de contrôle prudentiel. Authorised User means each individual associated with the Client who is notified by the Client to BARC and authorised to use the Research Services. The Restricted EEA Countries will be amended if required.

Finland: Notwithstanding Finland's status as a Restricted EEA Country, Research Services may also be provided by BARC Bank PLC where permitted by the terms of its cross-border license.

Americas: The Investment Bank of BARC Bank PLC undertakes U.S. securities business in the name of its wholly owned subsidiary BARC Capital Inc., a FINRA and SIPC member. BARC Capital Inc., a U.S. registered broker/dealer, is distributing this material in the United States and, in connection therewith accepts responsibility for its contents. Any U.S. person wishing to effect a transaction in any security discussed herein should do so only by contacting a representative of BARC Capital Inc. in the U.S. at 745 Seventh Avenue, New York, New York 10019.

Non-U.S. persons should contact and execute transactions through a BARC Bank PLC branch or affiliate in their home jurisdiction unless local regulations permit otherwise.

This material is distributed in Canada by BARC Capital Canada Inc., a registered investment dealer, a Dealer Member of Canadian Investment Regulatory Organization (www.ciro.ca), and a Member of the Canadian Investor Protection Fund (CIPF).

This material is distributed in Mexico by BARC Bank Mexico, S.A. and/or BARC Capital Casa de Bolsa, S.A. de C.V. This material is distributed in the Cayman Islands and in the Bahamas by BARC Capital Inc., which it is not licensed or registered to conduct and does not conduct business in, from or within those jurisdictions and has not filed this material with any regulatory body in those jurisdictions.

Japan: This material is being distributed to institutional investors in Japan by BARC Securities Japan Limited. BARC Securities Japan Limited is a joint-stock company incorporated in Japan with registered office of 6-10-1 Roppongi, Minato-ku, Tokyo 106-6131, Japan. It is a subsidiary of BARC Bank PLC and a registered financial instruments firm regulated by the Financial Services Agency of Japan. Registered Number: Kanto Zaimukyokucho (kinsho) No. 143.

Asia Pacific (excluding Japan): BARC Bank PLC, Hong Kong Branch is distributing this material in Hong Kong as an authorised institution regulated by the Hong Kong Monetary Authority. Registered Office: 41/F, Cheung Kong Center, 2 Queen's Road Central, Hong Kong.

All Indian securities-related research and other equity research produced by BARC' Investment Bank are distributed in India by BARC Securities (India) Private Limited (BSIPL). BSIPL is a company incorporated under the Companies Act, 1956 having CIN U67120MH2006PTC161063. BSIPL is registered and regulated by the Securities and Exchange Board of India (SEBI) as a Research Analyst: INH000001519; Portfolio Manager INP000002585; Stock Broker INZ000269539 (member of NSE and BSE); Depository Participant with the National Securities & Depositories Limited (NSDL): DP ID: IN-DP-NSDL-478-2020; Investment Adviser: INA000000391. BSIPL is also registered as a Mutual Fund Advisor having AMFI ARN No. 53308. The registered office of BSIPL is at Nirlon Knowledge Park, 9th floor, Block B-6, Off. Western Express Highway, Goregaon (East), Mumbai – 400063, India. Telephone No: +91 22 61754000 Fax number: +91 22 61754099. Any other reports produced by BARC' Investment Bank are distributed in India by BARC Bank PLC, India Branch, an associate of BSIPL in India that is registered with Reserve Bank of India (RBI) as a Banking Company under the provisions of The Banking Regulation Act, 1949 (Regn No BOM43) and registered with SEBI as Merchant Banker (Regn No INM000002129) and also as Banker to the Issue (Regn No INBI00000950). BARC Investments and Loans (India) Limited, registered with RBI as Non Banking Financial Company (Regn No RBI CoR-07-00258), and BARC Wealth Trustees (India) Private Limited, registered with Registrar of Companies (CIN U93000MH2008PTC188438), are associates of BSIPL in India that are not authorised to distribute any reports produced by BARC' Investment Bank.

This material is distributed in Singapore by the Singapore Branch of BARC Bank PLC, a bank licensed in Singapore by the Monetary Authority of Singapore. For matters in connection with this material, recipients in Singapore may contact the Singapore branch of BARC Bank PLC, whose registered address is 10 Marina Boulevard, #23-01 Marina Bay Financial Centre Tower 2, Singapore 018983.

This material, where distributed to persons in Australia, is produced or provided by BARC Bank PLC.

This communication is directed at persons who are a “Wholesale Client” as defined by the Australian Corporations Act 2001.

Please note that the Australian Securities and Investments Commission (ASIC) has provided certain exemptions to BARC Bank PLC (BBPLC) under paragraph 911A(2)(I) of the Corporations Act 2001 from the requirement to hold an Australian financial services licence (AFSL) in respect of financial services provided to Australian Wholesale Clients, on the basis that BBPLC is authorised by the Prudential Regulation Authority of the United Kingdom (PRA) and regulated by the Financial Conduct Authority (FCA) of the United Kingdom and the PRA under United Kingdom laws. The United Kingdom has laws which differ from Australian laws. To the extent that this communication involves the provision of financial services by BBPLC to Australian Wholesale Clients, BBPLC relies on the relevant exemption from the requirement to hold an AFSL. Accordingly, BBPLC does not hold an AFSL.

This communication may be distributed to you by either: (i) BARC Bank PLC directly, (ii) Barrenjoey Markets Pty Limited (ACN 636 976 059, "Barrenjoey"), the holder of Australian Financial Services Licence (AFSL) 521800, a non-affiliated third party distributor, where clearly identified to you by Barrenjoey. Barrenjoey is not an agent of BARC Bank PLC or (iii) such other non-affiliated third-party distributor(s) as may be clearly identified to you. Such non-affiliated third-party distributor(s) are not agents of BARC Bank PLC.

This material, where distributed in New Zealand, is produced or provided by BARC Bank PLC. BARC Bank PLC is not registered, filed with or approved by any New Zealand regulatory authority. This material is not provided under or in accordance with the Financial Markets Conduct Act of 2013 (“FMCA”), and is not a disclosure document or “financial advice” under the FMCA. This material is distributed to you by either: (i) BARC Bank PLC directly or (ii) Barrenjoey Markets Pty Limited (“Barrenjoey”), a non-affiliated third party distributor, where clearly identified to you by Barrenjoey. Barrenjoey is not an agent of BARC Bank PLC. This material may only be distributed to “wholesale investors” that meet the “investment business”, “investment activity”, “large”, or “government agency” criteria specified in Schedule 1 of the FMCA.

Middle East: Nothing herein should be considered investment advice as defined in the Israeli Regulation of Investment Advisory, Investment Marketing and Portfolio Management Law, 1995 (“Advisory Law”). This document is being made to eligible clients (as defined under the Advisory Law) only. BARC Israeli branch previously held an investment marketing license with the Israel Securities Authority but it cancelled such license on 30/11/2014 as it solely provides its services to eligible clients pursuant to available exemptions under the Advisory Law, therefore a license with the Israel Securities Authority is not required. Accordingly, BARC does not maintain an insurance coverage pursuant to the Advisory Law.

This material is distributed in the United Arab Emirates (including the Dubai International Financial Centre) and Qatar by BARC Bank PLC. BARC Bank PLC in the Dubai International Financial Centre (Registered No. 0060) is regulated by the Dubai Financial Services Authority (DFSA). Principal place of business in the Dubai International Financial Centre: The Gate Village, Building 4, Level 4, PO Box 506504, Dubai, United Arab Emirates. BARC Bank PLC-DIFC Branch, may only undertake the financial services activities that fall within the scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.

<table><tr><td colspan="2">U.S. Internet</td></tr><tr><td>Owen Clendenin</td><td>Alexander Kessinger</td></tr><tr><td>+1 212 526 7518</td><td>+1 212 526 1324</td></tr><tr><td>owen.clendenin@BARC.com</td><td>alexander.kessinger@BARC.co</td></tr><tr><td>BCI, US</td><td>m</td></tr><tr><td></td><td>BCI, US</td></tr></table>