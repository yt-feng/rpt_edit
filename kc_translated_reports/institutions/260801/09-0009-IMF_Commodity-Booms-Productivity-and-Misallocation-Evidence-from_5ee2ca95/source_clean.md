# Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL


# IMF Working Paper Research Department

Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data Prepared by Pablo Filippi, Ryan Kim, Nan Li, María Jesús Pérez, Younghun Shim\*

Authorized for distribution by Petia Topalova
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: We study how commodity booms affect productivity using administrative microdata from Chile combining firm exports by product and destination, employer-employee records, and firm-to-firm production networks. Exploiting differential Chinese demand across Chilean commodity products, we measure firms' exposure to the boom and trace its effects on productivity and resource allocation. We find three mechanisms. First, more exposed firms experience larger revenue increases but no differential productivity gains, channeling revenues into wages and materials. Second, among exposed firms, low-productivity firms expand employment while high-productivity firms do not, hiring workers from more productive employers. Third, domestic suppliers with greater indirect exposure show larger sales and productivity gains. We develop a model with heterogeneous export wedges and labor market frictions in which commodity booms can reduce sectoral productivity by exacerbating input misallocation, consistent with firm-level and aggregate evidence. Calibrated to Chile, this mechanism explains half of the mining TFP decline from 2005 to 2013.

RECOMMENDED CITATION: Filippi, P., R. Kim, N. Li, M. J. Pérez, and Y. Shim. 2026. Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data. IMF Working Paper WP/26/163. Washington, DC: International Monetary Fund.


# Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data

Prepared by Pablo Filippi, Ryan Kim, Nan Li, María Jesús Pérez, Younghun Shim

## 1 Introduction

The global commodity price fluctuations—including periods of sustained price change known as commodity super-cycles—have long been an important driver of economic activity in emerging economies. A substantial literature documents their effects on output volatility and long-run economic growth. Yet, how these booms affect productivity of commodity-exporting countries remains unclear, with several potential mechanisms pointing in different directions. Understanding these mechanisms matters for a large number of resource-dependent developing countries, from copper and lithium exporters in Latin America and Africa to oil producers in the Middle East. For these countries, whether commodity windfalls translate into lasting productivity gains, rather than transitory income, shapes long-run development. These questions are newly relevant as commodity markets appear to have entered a new super-cycle, driven by the global energy transition and rising demand for critical minerals.

This paper provides micro-level evidence on how commodity booms affect firm productivity and resource allocation. We focus on Chile, a commodity-dependent economy that experienced a striking pattern of productivity dynamics during the 2000s: the China-driven commodity boom generated massive export revenue increases, yet aggregate mining sector productivity declined sharply. Between 2005 and 2013, real mining total factor productivity (TFP) fell by approximately 8 percent even after controlling for geological factors, while non-mining sectors saw productivity gains (Figure 1 and A.1; De Solminihac et al., 2018). This aggregate pattern contradicts both the traditional “scale effect” prediction—where rising revenues could stimulate productivity by boosting investment or technological upgrading—and the classical Dutch disease mechanism, which predicts productivity declines in non-resource tradables rather than in the booming commodity sector itself (e.g., Corden and Neary 1982; Corden 1984).

What micro-level mechanisms can explain this aggregate pattern? $^{1}$ We argue that the answer lies in understanding how commodity booms interact with pre-existing distortions in resource allocation and affect firm-level efficiency—dynamics that granular firm- and worker-level data uniquely reveal. Chile offers an ideal setting for such an investigation due to the availability of detailed administrative microdata. We construct a comprehensive firm-level dataset by merging multiple administrative sources: transaction-level customs data on export and import prices (unit values) and quantities, firm-to-firm production networks capturing domestic supply chains, matched employer-employee records tracking worker mobility and wages, and administrative tax records on firm operations. This combined dataset, covering from 2003 to 2013, allows us to trace how global price shocks affect within-firm productivity, across-firm reallocation, workers, and propagation through supply chains at a highly detailed level of granularity, thereby uncovering the mechanisms underlying the aggregate productivity decline.

Figure 1: Global Copper Price and Chile's Mining TFP

[[KC_IMAGE_001]]

Notes. All series are expressed as ratios relative to the base year 2002. Global copper price is obtained from the London Metal Exchange, and TFP estimates are sourced from the Chilean National Commission of Productivity, which are obtained after controlling for geological factors such as ore grades, waste-to-ore ratio, pit slope, and the long gestation period of capital investments. See CNEP (2017) for details (CNEP 2017).

Our identification exploits differential price changes across commodity products, driven by China's WTO accession and rapid industrialization (Fernández et al., 2023). We assign these product-level price changes to firms using their pre-boom export shares. Because Chilean commodity exporters are highly specialized, each firm's shock is largely inherited from its dominant product, so the identifying variation comes from differences across firms in which product they specialize in, rather than from diversification within a firm's own export portfolio. To address a remaining concern about endogenous Chilean supply responses, we use a leave-one-out instrument—Chinese import prices from all countries except Chile, an approach common in the trade and labor literature (Autor et al., 2013)—which isolates the

China-driven demand component and lets us attribute differences in firm outcomes to the commodity price shock itself. $^{2}$

Our empirical analysis uncovers three key mechanisms through which commodity booms affect productivity. First, we document that while more exposed commodity exporters experience greater increases in revenues, material expenditures, and employment, they show no differential improvement in revenue-based TFP (TFPR) or sales per employee. This null effect persists across various production function specifications (including Cobb-Douglas, translog, and Leontief forms) that allow for flexible returns to scale. $^{3}$ Since commodity price increases likely raise firm-level output prices, an unchanged TFPR is consistent with declining physical productivity (TFPQ), potentially reflecting deteriorating ore grades or input quality as firms rapidly expand. $^{4}$ Moreover, these firms show no differential increase in domestic sales or capital accumulation, suggesting that export revenues flow primarily into variable inputs associated with exports rather than productivity-enhancing investments.

Second, we find evidence of labor misallocation across firms within the commodity sector: firms respond differently depending on initial productivity—not because low-TFPR firms face larger shocks, but because they expand more in response. Using matched employer-employee data, we show that among more exposed firms, those with high initial TFPR (above-median revenue productivity) do not differentially increase employment relative to less exposed high-TFPR firms. In contrast, low-TFPR firms that are more exposed to the commodity shock significantly expand their workforce relative to less exposed low-TFPR firms. This asymmetry is not a selection effect: the correlation between shock exposure and initial TFPR is essentially zero (-0.027). In addition, more exposed commodity exporters grow by hiring workers from other firms in the same sector, with a disproportionate share coming from more productive employers. This pattern of labor reallocation—from high- to low-productivity firms—provides direct micro-level evidence of increasing misallocation. When combined with our finding that more exposed exporters offer relatively higher wages, these results suggest that commodity booms enable less productive but export-favored firms to poach workers from more efficient producers, thereby reducing aggregate sectoral productivity.

Third, in contrast to the muted productivity response among commodity exporters, we document positive productivity spillovers to upstream domestic suppliers. Using firmto-firm transaction data, we construct measures of indirect exposure: firms that supply commodity exporters but do not themselves export commodities. We find that suppliers with greater indirect exposure (those more connected to commodity exporters) experience larger increases in sales, employment, materials expenditure, and importantly, capital investment and productivity—outcomes absent among directly exposed commodity exporters. This positive spillover effect aligns with the observed productivity gains in Chile’s non-mining sectors during the commodity boom (Figure A.1) and is consistent with demand-driven productivity improvements documented in other contexts (Ilzetzki, 2024).

To interpret the first two empirical patterns and clarify the aggregate implications, we develop a tractable theoretical framework. Our model features a small open economy with heterogeneous firms facing two distortions. First, firm-specific export wedges capture differential access to foreign markets (arising from subsidies, other differential policies, historical relationships, or others) that allow some firms to export more easily than others, regardless of their underlying productivity. Because such a wedge could be read as reduced-form heterogeneity rather than a real distortion, we discipline it in two ways: we provide three microfoundations, and we measure a concrete policy component directly from administrative data and show it moves firm behavior in the direction the mechanism requires (Section 6.4.2). Second, we model the labor market as oligopsonistic. Firms' wage-setting power generates firm-specific labor wedges, letting the model reproduce the wage increases and labor poaching we document in the data.

In this environment, a uniform increase in commodity demand has asymmetric effects across firms. Consistent with our empirical findings, the mechanism operates through differential sensitivity: firms with larger export wedges expand disproportionately, drawing labor and materials away from more productive but less export-favored competitors. This reallocation exacerbates misallocation: resources shift toward firms that generate high revenues due to privileged market access rather than superior technology. The model shows that aggregate sectoral productivity—properly measured as the output-weighted average of productivities—can decline even as output and employment rise. The framework also explains our empirical findings on labor reallocation and wage premia: in an oligopsonistic labor market, expanding low-productivity firms must offer higher wages to attract workers from more productive employers, generating the “poaching” patterns we observe in the data.

We calibrate the model to match key moments from Chilean administrative data, including export shares, sales dispersion, and export intensity variation across firms. Without targeting any of our firm-level regression coefficients, the calibrated model reproduces the muted productivity response and the disproportionate employment expansion among low-TFPR firms, both close to their empirical counterparts. These coefficients identify differential responses across firms that differ in exposure and initial productivity, net of the common boom absorbed by the intercept, and validate the reallocation mechanism at the firm level. Taking the same calibrated model to the aggregate level, we simulate a commodity boom comparable to Chile's experience. The resulting reallocation toward low-TFPR firms lowers sectoral productivity by 3.94 percent, roughly half of the $8\%$ TFP decline documented by CNEP (2017). The remaining gap likely reflects factors outside our parsimonious framework, such as capacity constraints in mining capital investment, within-firm productivity slowdown due to declining ore grades, or other sector-specific shocks and frictions. Our results demonstrate that the misallocation channel, operating through the interaction of export distortions and labor market power, can quantitatively explain a substantial portion of the aggregate productivity decline.

Literature Review. This paper contributes to several strands of literature. First, it adds to research on commodity price shocks and economic performance in small open economies (SOEs), which documents that many SOEs are highly sensitive to fluctuations in commodity prices. A central debate in this literature often concerns whether terms-of-trade shocks are key drivers of business cycle dynamics (Mendoza, 1995; Schmitt-Grohé and Uribe, 2018; Fernández et al., 2023). There are multiple channels through which commodity price shocks affect the aggregate economy, including wealth effects that benefit non-exporters more and low-tradability industries (Corden and Neary, 1982), a sovereign risk premium channel that affects borrowing costs (Shousha, 2016; Drechsel and Tenreyro, 2018), a wage channel that increases the cost of less skill-intensive industries and induces labor reallocation across sectors (Benguria et al., 2024a), and a banking sector liquidity channel that amplifies real responses (Toma and Cuba, 2024). Another recent literature quantifies the economic consequences of commodity super-cycles (Reinhart et al., 2016; Alberola and Benigno, 2017; Fernández et al., 2017; Kohn et al., 2021; González, 2021). Across this work, the focus is on aggregate and cross-country outcomes rather than on how a boom reallocates resources across firms within a sector. We use firm-level data to open that question, and find that pre-existing export distortions can channel inputs toward low-TFPR firms and lower the booming sector's productivity even as revenues surge.

Second, the paper also adds to the recent literature that studies the transmission of commodity price shocks using disaggregated data. For example, Benguria et al. (2024a)

analyzes the transmission of commodity price super-cycles in Brazil by focusing on regional variations and identifying wealth and cost channels through which these cycles affect local economies. Benguria et al. (2024b) extends this analysis to study spatial linkages, documenting substantial heterogeneity in how commodity booms affect workers across regions and skill levels, with inter-regional trade and migration playing crucial roles in the transmission. Similarly, Allcott and Keniston (2018) studies oil and gas booms in the United States, finding that manufacturing grows through upstream linkages rather than being crowded out—contradicting the classical Dutch disease prediction for non-resource tradables. Silva et al. (2024) investigates how commodity price shocks propagate through upstream and downstream linkages, affecting sectoral outputs and prices in SOEs. Amodio et al. (2025) use firm-to-firm transaction data to trace how a surge in Chinese beef demand propagates across sectors in Uruguay, finding sizable indirect gains in services linked to the export value chain. Taken together, these studies find that commodity booms propagate across regions and sectors, lifting output, wages, and producer prices in connected parts of the economy. We document a more troubling possibility within the booming sector itself: the same demand expansion that lifts firms downstream depresses productivity at its center, as inputs flow toward low-TFPR firms.

Third, we relate to the literature on misallocation and productivity. Following Hsieh and Klenow (2009)'s influential framework, numerous studies have documented substantial productivity losses from resource misallocation across firms (Oberfield, 2013; Restuccia and Rogerson, 2017; Adamopoulos et al., 2022; Heise and Porzio, 2022). A key question is how aggregate shocks reshape misallocation. Larrain and Stumpner (2017) and Bau and Matray (2023) show that positive shocks can reduce misallocation when they relax binding capital constraints on productive firms. We show how positive external shocks can instead exacerbate misallocation within the booming sector itself, where pre-existing export distortions channel inputs toward low-TFPR firms. $^{5}$ This perspective builds on Gopinath et al. (2017), who document that capital inflows in Southern Europe flowed to high-net-worth but low-productivity firms, reducing aggregate TFP. While their mechanism operates through selection, ours operates through differential sensitivity: low-TFPR firms do not face larger commodity shocks but respond more strongly to common shocks. Our perspective relates to Bai et al. (2024), which demonstrates that trade liberalization can worsen misallocation by disproportionately selecting subsidized, less efficient firms into exporting, contributing to emerging evidence that gains from trade can be muted in second-best environments (Choi, 2025; Berthou et al., 2020). While their mechanism largely operates on the extensive margin (which firms become exporters), ours operates on the intensive margin, showing how commodity demand shocks induce differential expansion among existing exporters.

Lastly, our paper adds to research on how firm-level demand shocks affect productivity. Ilzetzki (2024) shows that firms facing capacity constraints experience productivity gains following government purchase shocks. Atkin et al. (2017) finds that gaining export market access enhances firm-level productivity in Egyptian manufacturers. Aghion et al. (2024) documents that French firms respond to export demand shocks by increasing innovation, particularly among initially more productive firms. In contrast to these findings in manufacturing, we document that commodity exporters do not improve productivity following demand shocks, instead channeling revenue gains into inputs without efficiency improvements. However, we find that upstream suppliers to commodity exporters do experience productivity gains, consistent with this literature, suggesting that the muted response among commodity exporters reflects sector-specific distortions rather than a departure from established mechanisms. This distinction highlights important heterogeneity in how different sectors respond to demand expansions.

The remainder of the paper is structured as follows. Section 2 provides background on Chile's commodity dependence and the China-driven boom. Section 3 describes the data and key features. Section 4 outlines our empirical strategy. Section 5 presents empirical results on direct and indirect effects. Section 6 develops the theoretical framework and quantifies the misallocation channel, and Section 7 concludes.

## 2 The China-Driven Global Commodity Boom: Context for Chile

The role of commodities in Chile's economy. Chile's economy is heavily dependent on commodity exports, with mining products consistently accounting for over 50 percent of total exports during the 2000s. This dependence, combined with China's emergence as a global economic power following its WTO accession in 2001, created a natural experiment: Chile faced a massive external demand shock that was plausibly exogenous to domestic economic conditions.

Chile's mining sector exhibits substantial heterogeneity across firms and deep integration with domestic supply chains. The sector includes a mix of large state-owned and multinational mining companies alongside smaller private operators, varying widely in productivity, energy use, and capital and export intensity, even among firms operating under comparable geological conditions. $^{6}$ Firms differ in their product specialization—some focus on copper concentrate, others on refined copper or copper alloys—and in their geographic markets, with some firms exporting predominantly to China while others serve diverse destinations.

Beyond these direct exporters, the mining sector is deeply integrated with Chile's domestic economy through supply chain linkages. According to the 2010 Input-Output table, mining was the largest purchaser of intermediate inputs from domestic suppliers—including specialized equipment and machinery, transportation services, construction materials, and business services. This combination of firm heterogeneity among commodity exporters and extensive domestic production networks provides rich variation for understanding how commodity shocks propagate through the economy.

Figure 2: Copper Market Dynamics: Chinese Demand, Global Prices, and Chile's Production

[[KC_IMAGE_002]]


[[KC_IMAGE_003]]

Notes. The left panel plots the Chinese import value of copper along with the global price index of copper. Copper import values are derived from the BACI database, while the global copper price is obtained from the London Metal Exchange (LME). The right panel plots the quantity of copper production in Chile along with the export value of copper from Chile. The data are sourced from Cochilco, the Chilean National Copper Commission. All series are expressed as ratios relative to the base year (2003).

The commodity boom and aggregate patterns. Figure 2 illustrates the magnitude and nature of Chile's commodity boom experience in the early 2000s. Panel A shows that global copper prices nearly tripled between 2003 and 2011. This price surge coincided with a rapid increase in China's copper imports following its WTO accession in 2001, as the country undertook massive infrastructure development and urban construction programs (Fernández et al., 2023). As a major copper exporter, Chile was heavily exposed to this demand shock.

Panel B reveals a striking pattern: while the value of Chilean copper exports surged alongside prices, production volume remained nearly flat. Copper production grew by only 20 percent during this period, even as export revenues more than tripled. This modest output expansion required disproportionate increases in inputs—energy use rose 79 percent, employment increased 157 percent, and capital stock grew 178 percent—roughly an eightfold increase relative to what would be expected under constant productivity.

This input-output pattern points to deteriorating productivity at the aggregate level. Indeed, Chile's National Productivity Commission (CNEP, 2017) documented that mining sector total factor productivity (TFP) declined by approximately 8 percent between 2005 and 2013, averaging roughly 1 percent per year, even after accounting for two sector-specific factors: declining ore grades as easier deposits were exhausted, and the long gestation lags associated with mining capital investments. The fact that TFP fell substantially even after these adjustments suggests that other mechanisms must be at work.

These aggregate observations reveal an intriguing disconnect: a large and sustained positive price shock, driven by surging external demand, coincided with stagnant production and falling sectoral productivity. This divergence suggests that the China-led commodity boom may have acted as a large exogenous demand shock with adverse implications for mining TFP in Chile.

However, identifying the impact of a shock and its underlying mechanisms at the aggregate level poses significant challenges. Reverse causality and concurrent macroeconomic events (such as shifts in interest rates, credit expansion, or industrial restructuring) confound identification. In addition, aggregate data masks important within-firm dynamics and between-firm reallocations that affect aggregate productivity outcomes. To address these limitations, we turn to administrative microdata that enable the construction of firm-specific shocks and the detailed analysis of within- and across-firm dynamics. We describe the dataset in Section 3 and outline our identification strategy in Section 4.

Chile's Role in the Global Copper Market. One might worry that Chile, as a major copper producer, could influence global prices, which would complicate identification. However, Chile contributed less than 25 percent of global exports in 2003, insufficient to unilaterally influence global prices. $^{7}$ In contrast, China's share of global copper consumption exceeds 50 percent, highlighting its dominant role in driving the global commodity boom. In addition, copper is a globally traded commodity with prices determined in international markets, where Chile faces competition from numerous other producers. Moreover, China's copper imports from Chile represent only a fraction of China's total copper consumption; China also imports substantial quantities from other countries and produces domestically. These observations, together with statistics and tests at the firm-product level in Section 4, provide the foundation for our identification strategy.

## 3 Data

Our analysis uses microdata to trace how commodity price shocks affect firm-level productivity and resource allocation. We construct a comprehensive database by merging several administrative datasets from Chile's Internal Revenue Service (IRS) with international trade data. The result is a rich micro-level view of firm behavior, labor dynamics, and supply chain interactions in a commodity-dependent economy.

The administrative datasets cover all firms and employees in Chile's formal sector since 2004. Each firm and individual receives a unique tax ID, which allows us to link observations across data sources. Following Huneeus (2018), we define a firm as a tax ID. $^{8}$ Our final merged sample spans 2003 to 2013 and includes firms with positive sales and material costs and at least one employee.

## Firm-Level Administrative Tax Records

Our dataset draws on comprehensive firm-level administrative records from Chile's IRS. We use two primary tax forms that provide detailed financial and operational information. Form F22 reports annual information, including fixed assets, the main 6-digit industry classification (adapted from ISIC by the Chilean IRS), and headquarters location. Form F29 includes monthly data, which we aggregate to the annual level, covering domestic sales, exports, domestic and imported material goods expenditures, and investments. Because these forms cover all formal firms, we can observe the universe of formal-sector activity without the sampling biases inherent in survey data. $^{9}$

## Firm-to-Firm Transaction Data

A particularly valuable feature of our dataset is the detailed firm-to-firm transaction data (Form F3323), available from 2004 to 2010. This source maps Chile's domestic production network by recording buyer and seller tax IDs along with transaction years and values for each supplier-customer relationship. Firms with total intermediate goods expenditures exceeding approximately USD 390,000 must report a complete list of suppliers and buyers each year after meeting this threshold once. These reporting firms account for roughly 80 percent of Chile's total value added (Huneeus, 2018).

This network data allows us to identify which firms supply commodity exporters, measure the strength of these supply chain linkages, and quantify indirect spillovers from commodity exporters to their upstream partners.

## Employer-Employee Matched Data

We also use employer-employee matched data (Form DJ1887) to analyze labor market dynamics and worker reallocation. This dataset links every formal-sector employee to their employer via unique tax IDs and provides monthly information on total labor income, including wages, salaries, bonuses, tips, and other taxable compensation.

We aggregate the data to the annual level and use it to track how workers move across firms and how labor gets reallocated across firms with different productivity levels. Because we observe individual workers over time, we can identify job switchers, measure the productivity of their origin and destination firms, and test whether commodity exporters differentially attract workers from high- versus low-productivity competitors. This perspective is important for understanding labor misallocation.

## International Trade Data (Customs, BACI, WITS)

We combine the domestic administrative records with three international trade datasets crucial for identifying exogenous shocks and measuring firms' external exposure and export responses.

Customs data. Provided by the Chilean Customs public agency, this transaction-level data includes firm tax IDs, destination and origin countries for exports and imports, transaction values, and 6-digit HS product codes. This highly disaggregated information is essential for constructing each firm's initial export basket and measuring exposure to product-level global commodity price changes. Note that we are only permitted to match the specific exposure share utilized in Section 4 to the firm data and cannot utilize other variables from the Customs data. $^{10}$

BACI data. Published by CEPII, BACI is a cleaned version of UN Comtrade data with information on global trade flows at the product-country-month level (Gaulier and Zignago, 2010). It includes exporting and importing countries, year, 6-digit HS code, month, transaction value, and quantity. This global trade data lets us construct product-level price changes—both Chilean export prices to China (our baseline measure) and Chinese import prices from countries other than Chile (our instrumental variable), which isolates price variation unrelated to Chilean firm behavior.

WITS data. Tariff information is sourced from the World Integrated Trade Solution (WITS) database published by the World Bank. This dataset provides comprehensive tariff rates, including Most Favored Nation (MFN) applied rates for China in 2003 as well as China's preferential tariff rates applied to Chile in 2011 under the Chile-China Free Trade Agreement. We use all tariff figures as Ad Valorem Equivalent (AVE) percentages, which convert specific duties into a comparable value-based format and allow for consistent analysis of trade barriers over time and across policy regimes. We use this data to examine the Law of One Price relationship in Section 4.3.

## Sample Construction and Key Products

We merge all datasets using common firm tax IDs. Following the cleaning procedures in Huneeus (2018), we keep only firms with positive sales, positive material costs, at least one employee, and a non-missing industry classification. This merged dataset covers a substantial portion of Chile's formal economy and supports a detailed, multi-faceted analysis of how commodity price booms affect firms.

Our analysis specifically focuses on 83 commodity products that are actively sold from Chile to the global economy and are also demanded by China from third countries (excluding Chile). This selection ensures that our firm-specific shocks are directly relevant to the Chilean commodity sector's exposure to global demand shifts. The 83 products span copper products (refined copper, copper ore, copper concentrates, copper alloys, copper wire), other metals (molybdenum, iron ore), agricultural commodities (fresh fruit, wine, fishmeal, wood products), and industrial minerals (lithium, iodine, sodium nitrate).

## 4 Empirical Strategy and Identification

This section details our empirical strategy to identify the impact of global commodity demand on Chilean firms. Our identifying variation comes from differential changes in global commodity prices across granular products, which firms inherit through their initial export specialization. Micro-level data are particularly useful in this context: even for a globally significant commodity like Chilean copper, individual firms and products account for small shares of the global market, allowing us to isolate the China-driven demand shock from other confounding factors. We detail the construction and measurement of our key variables and explain how our identification approach addresses endogeneity.

## 4.1 Regression Specification

Our empirical strategy estimates the impact of commodity price shocks on firm-level outcomes using the following regression specification:

$$
y _ {f} ^ {g} = \beta_ {0} + \beta_ {1} \mathrm{shock} _ {f} + \mathbf {X} _ {f} ^ {\prime} \gamma + \epsilon_ {f}.\tag{1}
$$

The dependent variable, $y_{f}^{g}$ , represents the growth rate of firm $f$ 's outcome ( $Y_{f}$ ) over 2005–2013, defined as $y_{f}^{g} = \frac{2(Y_{f,2013} - Y_{f,2005})}{Y_{f,2013} + Y_{f,2005}}$ . Following the literature on firm dynamics (e.g., Davis et al., 1998), this growth rate is symmetric around zero and bounded between -2 and 2, mitigating outlier influence without requiring arbitrary winsorization. We examine growth rates for various outcomes, including exports, domestic sales, material expenses, number of employees, sales per employee, investment, and productivity, as well as measures related to worker mobility, such as the share of workers moving between firms with specific characteristics. Our key independent variable, $shock_{f}$ , measures the firm-specific commodity price shock between 2003 and 2011, constructed as detailed in Section 4.2. We measure outcomes over 2005–2013 to allow a two-year lag for firms to adjust their operations in response to price changes observed during 2003–2011.

This long-difference specification is designed to capture the cumulative, long-run effects of the commodity boom. $^{[11]}$ For our two-period panel (2003–2011 for the shock, 2005–2013 for outcomes), the long-difference approach is econometrically equivalent to including firm fixed effects, differencing out time-invariant firm characteristics that might correlate with both export exposure and outcome growth. The intercept $\beta_{0}$ absorbs aggregate trends common to all firms over this period, such as economy-wide macroeconomic shocks or technological changes. The coefficient of interest, $\beta_{1}$ , thus identifies the differential impact of firm-specific commodity price shocks on outcomes, conditional on firm-level controls in $X_{f}$ .

Our identification of $\beta_{1}$ relies on constructing an exogenous export shock variable based on two components: (i) firm-level export shares across products and destinations in the initial period, and (ii) subsequent changes in Chinese import demand for each product from third countries (i.e., excluding Chile). Identification holds if either the product-level price shifts are exogenous to individual Chilean firms (which our leave-one-out IV ensures by using Chinese imports from third countries) or firms' initial export shares are uncorrelated with unobserved growth determinants. We primarily rely on the former and provide a detailed discussion of the shock construction and instrument validity in Section 4.2.

Our control variables $X_{f}$ include 2-digit industry fixed effects, allowing us to compare firms within major sectors rather than relying solely on cross-sector variation. These fixed effects ensure that we compare, for example, a firm primarily producing copper products with other copper producers rather than with firms from unrelated industries. In addition, we control for the firm's initial commodity share to account for differences across firms in exposure intensity. Standard errors are clustered at the 4-digit industry level in all specifications. Results are also robust to controlling for initial firm size measured by sales or employment.

## 4.2 Global Commodity Product Price Changes


We focus on commodities—primary goods ranging from industrial metals to agricultural products—because their prices are predominantly determined by global supply and demand forces and traded on international exchanges, representing a largely exogenous shock to individual Chilean exporters. Furthermore, commodities are highly standardized, mitigating confounding factors related to product differentiation or firm-specific quality variations. This allows for consistent comparisons of firm responses to external price changes.

Direct Regressor: Chilean Export Prices to China. For our direct baseline regressor, we define $P_{p}$ as Chilean export prices to China. The price change is calculated as:

$$
\Delta \ln P _ {p} ^ {\mathrm{CL}} = \ln P _ {p, 2 0 1 1} ^ {\mathrm{CL}} - \ln P _ {p, 2 0 0 3} ^ {\mathrm{CL}}\tag{2}
$$

where $P_{p,t}^{\mathrm{CL}}$ is the price of product $p$ (defined at the 6-digit HS level) exported from Chile to China at time $t$ . This measure exploits China's rapid increase in commodity demand driven by accelerated industrialization and WTO accession in 2001. Importantly, the resulting global commodity boom did not affect all products equally; instead, our key identifying variation stems from the sharp, differential price changes across products rather than uniform increases (see Figure A.2).

Instrumental Variable: Chinese Import Prices from Other Countries. A potential concern with our baseline measure is that product-level price changes may partly reflect Chilean firms' supply decisions if they possess market power in specific product categories. To address this endogeneity concern, we construct an instrumental variable based on Chinese import prices from countries excluding Chile, following a strategy similar to that in Autor et al. (2013). Specifically, this instrument is defined as:

$$
\Delta \ln P _ {p} ^ {\mathrm{OT}} = \ln P _ {p, 2 0 1 1} ^ {\mathrm{OT}} - \ln P _ {p, 2 0 0 3} ^ {\mathrm{OT}}\tag{3}
$$

where $P_{p,t}^{OT}$ represents the Chinese import price of product p from countries other than Chile at time t. By using import prices from third countries, this instrument purges the influence of Chilean supply decisions and isolates the exogenous component of Chinese demand for commodity products.

## 4.3 Connection to the Law of One Price and IV Relevance

The Law of One Price (LOP) posits that identical goods should have the same price across locations, absent trade frictions. In our context, perfect LOP would imply $\Delta \ln P_{p}^{CL} = \Delta \ln P_{p}^{OT}$ —that is, Chilean export prices to China move one-for-one with Chinese import prices from other countries. If LOP held perfectly, our instrument would simply replicate the endogenous regressor, offering no independent variation for identification. Conversely, zero correlation would violate instrument relevance. Therefore, a significant but imperfect correlation, driven by deviations from perfect LOP, is essential for the validity and relevance of our instrument. These deviations typically arise from various trade frictions, including tariffs, non-tariff barriers, transportation costs, distribution markups, and residual product differentiation within detailed HS codes.

Table 1 presents our empirical investigation of the LOP relationship and tests instrument relevance. The dependent variable is the change in the log of Chilean export prices to China ( $\Delta \ln P_{Chile}$ ) and the independent variable is the change in the log of Chinese import prices from other countries ( $\Delta \ln P^{OT}$ ).

Column (1) shows a statistically significant coefficient of 0.45, substantially less than 1, confirming that LOP does not hold perfectly while maintaining instrument relevance. Columns 2–3 reveal that tariffs drive this deviation: pass-through is strong (0.70) for zero-tariff products but insignificant (0.13) for products with positive tariffs, indicating that tariffs effectively break the price linkage. Results are robust to controlling for initial tariffs (Columns 4–6).

Table 1: The Law of One Price Investigation


Notes. Dependent variable is the change in log Chilean export prices to China (2003–2011). Independent variable is the change in log Chinese import prices from other countries. Columns 2–3 split by 2011 tariff status; Columns 4–6 add initial (2002) tariff as control. Robust standard errors in parentheses. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01.

## 4.4 Firm-level Commodity Price Shock Construction

We assign the product-level price changes to firms using each firm's 2003 export shares. Because the median commodity exporter earns $93\%$ of its export value from a single 6-digit product, this firm-level shock is essentially the price shock of the firm's dominant product (Appendix A.2). The firm-level commodity price shock $(\mathrm{shock}_f^k)$ is:

$$
\mathrm{shock} _ {f} ^ {k} = \sum_ {p \in \mathcal {C}} \omega_ {p f} \Delta \ln P _ {p} ^ {k}.\tag{4}
$$

Here, $\Delta \ln P_{p}^{k}$ represents the price change for product p (either baseline k=CL or IV k=OT from Section 4.2), C denotes the set of commodity products, and $\omega_{pf}$ is firm f's initial export share of product p in 2003, calculated as firm f's exports of product p relative to its total exports across all products. We control for the initial share of non-commodity products in firm exports to account for diversification across product lines.

To ensure shock exogeneity, its construction is carefully decoupled from potentially endogenous firm trade decisions in two ways. First, $\omega_{pf}$ reflects the firm's product specialization across all export destinations, not solely exports to China. Second, the shock is assigned to all firms that exported at least one product China imported in 2003, regardless of whether the firm itself exported to China. This inclusive definition ensures that the firm's exposure reflects the global nature of commodity price movements, rather than its pre-existing, potentially endogenous, bilateral trade relationship with China.

Chilean commodity exporters are, individually, highly specialized: the typical firm earns almost all of its export revenue from a single 6-digit product (Figure A.3). The firm shock therefore decomposes into the price shock of the firm's dominant product, which varies across firms by which product they specialize in, and a smaller within-firm component from the firm's remaining products. The first part accounts for most of the variation—among copper producers, a firm specializing in refined cathodes faced a sharper price increase than one specializing in unwrought copper—so identification is driven largely, though not exclusively, by across-firm differences in specialization rather than within-firm portfolio diversity. A shock built from each firm's dominant product alone is almost perfectly correlated with the baseline and yields similar effects on firm outcomes (Appendix A.2). $^{13}$

## 4.5 Firm-Level Market Power and Shock Exogeneity

A fundamental premise of our identification strategy is that individual Chilean firms cannot significantly influence Chinese import prices from other countries ( $\Delta \ln P_p^{\mathrm{OT}}$ ), which form the price component of our instrument. This implies that their supply decisions for specific products cannot significantly impact these reference global prices, either because the product itself has a limited global market share, or the individual firm is small within that product's market (or both). This assumption is crucial for ensuring the exogeneity of the firm-level shock constructed using initial product shares, as it prevents reverse causality where Chilean firm actions might directly affect the instrument's price component.

Table 2 provides evidence that Chilean firms have limited market power in global commodity markets. At the firm level (Panel A), the median firm accounts for essentially zero percent of global exports in its product category, while even the largest firms average only 5%. At the country level (Panel B), Chile supplies just 8% of global exports on average, alleviating concerns that Chile could unilaterally influence world prices. Most critically for our identification strategy, Panel C shows that individual Chilean firms have negligible influence on Chinese import prices from third countries—the key component of our instrument. The median firm accounts for effectively zero percent of China’s imports, while even the largest firms average just 7%. $^{14}$ These patterns support the exogeneity of our identification strategy.

Table 2: Chilean Firm and Product Export Shares


Notes. Statistics summarize 83 commodity products in 2003. Panel A: Chilean firm shares in global exports. Panel B: Chile's aggregate shares in global exports and Chinese imports. Panel C: Chilean firm shares in China's total imports. Here, "median" and "max" refer to the median and largest Chilean firm by export value within each product. All shares calculated as firm (or country) exports divided by relevant global or Chinese import total.

A separate, time-series concern is that more exposed firms might have been on differential pre-trends before the boom. Two features limit this: the boom's onset in the early 2000s is sharp and externally driven by China's accession, and exposure is uncorrelated with firms' initial productivity (the correlation of the shock with initial TFPR is $-0.027$ ), so exposed firms are not a pre-selected group. $^{15}$

## 4.6 The Effects on Upstream Firms

The commodity exporters in Chile are largely supplied by other domestic firms. $^{16}$ Indeed, commodity exporters account for approximately 30\% of the total revenues of these upstream suppliers. Utilizing unique firm-to-firm transaction-level data, we construct a measure of these upstream firms' indirect exposure to the export shock experienced by their commodity-exporting customers. The key idea is that upstream firms that initially sold more to commodity-exporting firms experiencing a larger commodity price boom would subsequently face a greater increase in demand and revenue, assuming that commodity firms increase their demand for intermediate (material) inputs in response to the positive shock. Formally, we define the indirect shock for an upstream non-commodity sector firm i as:

$$
\text { indirect   shock } _ {i} = \sum_ {f \in \text { customers   of } i} \omega_ {i f} \cdot \text { shock } _ {f},\tag{5}
$$

where $\omega_{if}$ denotes the share of non-commodity sector firm i's sales to commodity firm f in firm i's total sales, and $shock_{f}$ is the direct commodity price shock faced by the commodity firm f. For $shock_{f}$ , our main regressor is the weighted average of Chinese commodity product import prices from Chile, and the instrumental variable is the weighted average of Chinese import commodity product prices from countries other than Chile.

## 5 Results

This section presents our empirical findings on how commodity price shocks affect commodity-exporting firms and cross-firm resource allocation. We begin by documenting the direct, reduced-form effects on commodity-exporting firms, demonstrating that while these firms experience significant scale expansion in exports and variable inputs, this growth is not accompanied by productivity gains or sustained capital investment (Table 3). We then investigate mechanisms underlying the observed productivity decline (Figure 1), showing how the commodity boom leads to a reallocation of labor towards less productive firms within the commodity sector itself, with low-revenue-productivity firms expanding their workforce, partly by attracting workers from more productive counterparts (Table 4). Finally, we document a contrasting pattern of productivity growth in non-commodity sectors, demonstrating that positive shocks propagate through domestic supply chain linkages to significantly improve the productivity of upstream firms (Table 5), consistent with the productivity gains observed in other sectors (Figure A.1).

## 5.1 Firm-level Outcomes

Table 3 presents our primary empirical findings on how commodity price shocks directly affect the operational adjustments and performance of commodity-exporting firms. The table reports results from both Instrumental Variable (IV, our preferred specification) and OLS across six key outcomes: exports, employment, materials expenditure, capital stock, productivity, and domestic sales. All measures are directly observable in the data except for firm-level productivity, which is constructed as a Solow residual:

Table 3: Commodity Price Shocks and Firm-Level Outcomes


Notes. This table reports the results from Equation (1). The dependent variables are the DHS growth rates of exports, employees, materials expenditure, capital stock, TFPR, sales per employee (Sales/emp.), and domestic sales (D. Sales), respectively. All regressions control for 2-digit industry fixed effects, and standard errors are clustered at the 4-digit industry level. Export is measured in Customs data as export value, and all other outcome variables are measured using firm-level administrative data. Regressions are weighted by export values for exports, by total sales for employees, domestic sales and materials expenditures. IV and OLS estimates use the same sample for each outcome. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01.

$$
\log \operatorname{tfpr} _ {f j t} = \log y _ {f j t} - \alpha_ {j} \log l _ {f j t} - \beta_ {j} \log m _ {f j t} - (1 - \alpha_ {j} - \beta_ {j}) \log k _ {f j t}
$$

where subscripts denote firm $(f)$ , sector $(j)$ , and time $(t)$ , and y, l, m, and k represent output, labor, material, and capital, respectively. $^{17}$ In our main specification, the sector-level output elasticities, $\alpha_{j}$ (for labor) and $\beta_{j}$ (for materials), are derived from the average ratio of wage bills to gross output and material expenditures to gross output, respectively, at the sector-year level, assuming constant returns to scale. Since we do not observe firm-level price data—a limitation common to most firm-level datasets—we follow standard practice in measuring productivity (such as Hsieh and Klenow, 2009) and deflate all output and input measures using sectoral price indices. This yields revenue-based total factor productivity (TFPR) rather than quantity-based productivity (TFPQ). This measurement is consistent with how we interpret the productivity in a theoretical framework in Section 6.

As a robustness check, we estimate firm-level productivity using the control function approach of Ackerberg et al. (2015). We employ two specifications. First, we estimate a gross output production function with capital, labor, and materials, using both Cobb-Douglas and translog functional forms. Second, following De Loecker and Scott (2025), we model gross output as a Leontief function of value added and materials, where value added is produced using capital and labor. $^{18}$ Appendix Table A.4 shows that our results hold across both gross output and value-added approaches, as well as across different functional forms. This consistency across specifications suggests that our findings are not driven by functional form assumptions or returns to scale restrictions.

Consistent with a positive external shock, commodity-exporting firms exhibit a substantial scale expansion: the IV estimates show a robust and significant increase in their exports, accompanied by a marked expansion in materials expenditures and employment. These findings suggest that firms affected by the commodity boom are indeed responsive to the increased demand, experiencing a boost in their international sales and scaling up their use of variable inputs. Across these specifications, IV estimates generally exceed OLS estimates, consistent with classical measurement error and the possibility that negative supply shocks—which raise commodity prices while reducing firm size—attenuate OLS coefficients toward zero.

However, this expansion in scale and variable inputs does not translate into significant long-term capital accumulation or improved operational efficiency. Our results for capital stock (column 4) show no evidence of firms investing in capital in response to the commodity boom; instead, the OLS estimate reveals a marginally significant decrease, while the IV estimate is statistically insignificant. This pattern suggests that the additional export revenues are primarily allocated towards short-run inputs directly associated with increased exports, rather than consistently fostering long-term capital accumulation.

More importantly, the IV estimates for firm-level productivity are statistically insignificant, indicating that despite increased revenues and expanded operations, these firms experience no measurable efficiency gains: both TFPR (column 5) and sales per employee (column 6) are statistically insignificant. While we cannot directly measure TFPQ, given that commodity price increases likely raise firm-level output prices (e.g., through strategic complementarity in pricing; see the derivation in Appendix B.2), unchanged TFPR may mechanically imply a decline in TFPQ. $^{19}$ A decline in TFPQ could reflect the deterioration of ore grade or other geological factors, or the degradation of input quality as firms rapidly expand their operations. But a purely geological account operates within firms and cannot generate the across-firm reallocation toward lower-TFPR firms documented above; consistently, our results hold when we exclude core copper mining (Table A.3), where grade concerns are most acute.

In addition, the effects on domestic sales (column 7) are negligible and statistically insignificant, suggesting that the benefits of the boom are concentrated on export-oriented activities with limited spillovers into the domestic market. This null effect on domestic sales is useful as it helps to ensure that our identified “shock” reflects a genuine foreign demand shock, rather than confounding factors associated with firms’ general production decisions, which would likely affect both domestic and foreign sales. $^{20}$

Overall, these findings suggest a pattern of extensive growth without intensive improvement: commodity-exporting firms expand scale but neither enhance within-firm productivity nor invest consistently in long-term capital. The F-statistics are consistently well above the conventional threshold of 10, confirming the strength of our instrument across all specifications. Regressions are weighted by initial values to match aggregate patterns, with results generally robust to alternative weighting schemes. $^{21}$

## 5.2 Labor Reallocation Toward Low-Productivity Firms

Having established that firms facing the commodity price boom do not increase within-firm productivity despite revenue gains, we now investigate a complementary mechanism: whether these firms expand in a way that misallocates resources and depresses aggregate productivity in the commodity sector. Following standard practice in the misallocation literature, we posit that the expansion of less productive firms, which may already be operating above their optimal scale due to existing distortions, can exacerbate aggregate resource misallocation. In principle, such firms could expand disproportionately for two distinct reasons: selection bias or differential sensitivity to the shock.

Table 4: Commodity Price Shocks and Labor Market Outcomes


Panel B: Worker Mobility


Panel C: Employee Growth by Firm Productivity Group


Notes. Specification as in Table 3. Panel A: dependent variables are log wage differences (2005–2013) for new workers (hired after 2004) and existing workers (hired in 2004), weighted by initial wage bill. Panel B: dependent variables are shares of movers (2005–2013) among total movers, weighted by initial sales. Same sector movers changed employers within the same sector; higher TFPR movers came from firms with higher TFPR in the same sector. Panel C: dependent variable is DHS growth rate of employees; firms split by initial within-sector median TFPR, weighted by initial sales. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01.

First, it might be possible that less productive firms are systematically exposed to larger positive commodity price shocks, thereby leading to misallocation through a selection effect. However, our methodology, detailed in Section 4, is specifically designed to address such selection concerns through the construction of the main regressor and the instrumental variable. Moreover, we directly test this possibility by examining the correlation between the commodity price shock defined in Equation (4) and firms' initial productivity. The correlation between the shock and initial TFPR is -0.027 (s.e. 0.028), confirming that shock exposure is uncorrelated with initial productivity. This rules out selection as the primary driver of differential firm responses.

Second, the alternative explanation is that firms with inherently lower TFPR exhibit greater sensitivity to commodity price shocks due to pre-existing distortions that allow them to persist at suboptimal productivity levels. If such distortions exist—for example, preferential access to export markets or subsidized financing—then less productive firms might expand disproportionately in response to positive shocks, potentially drawing resources (e.g., labor) away from more productive firms.

Table 4 provides strong evidence for this differential sensitivity mechanism by examining labor market adjustments among commodity-exporting firms. Panel A presents the impact on average wages. The IV estimates indicate a significant increase in wages for both new workers (0.255) and, more substantially, for existing workers (0.394), with OLS estimates showing similar patterns. This suggests that commodity-exporting firms, driven by increased revenues, are able to offer higher wages to attract and retain labor, particularly their established workforce.

Panel B investigates worker mobility. Specifically, it calculates the share of employees who move from the same sector or from higher-TFPR firms among all movers and uses these shares as dependent variables. The IV estimates show a significant positive effect on the share of movers to firms within the same sector (0.089) and, notably, a significant increase in the share of movers from higher TFPR firms to the affected commodity-exporting firms (0.157). This latter finding is crucial: it suggests that commodity-exporting firms, boosted by the boom, are actively attracting workers within the sector, even from more productive firms. This “labor poaching” across firms, especially from higher-productivity ones, is a direct channel through which resources (labor) could be reallocated towards potentially less productive commodity-exporting firms, thereby contributing to aggregate misallocation.

The direct evidence for the differential sensitivity of firms based on their initial productivity is presented in Panel C. This panel disaggregates the effect on employment growth by firms' initial TFPR. Strikingly, the IV estimate for firms in the lower productivity group (TFPR<p50) is a large and statistically significant coefficient of 0.620, indicating a substantial increase in employees for these firms. In contrast, the IV estimate for higher productivity firms (TFPR≥p50) is an insignificant -0.163, suggesting no positive expansion, and possibly a contraction, in their workforce. This strong differential response, where less productive firms disproportionately expand their employment, strongly supports our hypothesis that the commodity boom exacerbates resource misallocation by incentivizing the growth of firms that may already be operating at suboptimal efficiency due to underlying distortions.

One might worry that low-TFPR firms expand because TFPR proxies for export-market markups rather than for the export-related distortion. We formalize this markup channel as one microfoundation, but it implies a positive TFPR-size gradient, whereas in our data the correlation is zero to weakly negative; the cross-sectional moments thus favor the productivity-orthogonal wedge we adopt (Appendix C.1.3).

## 5.3 Increasing Non-Commodity Productivity: Upstream Propagation

While our previous analysis focused on the direct impact of commodity price shocks on exporting firms, this section investigates how these shocks propagate through domestic supply chain linkages to enhance productivity in non-commodity sectors, particularly among upstream firms. Chilean commodity exporters rely heavily on domestic suppliers; indeed, these exporters collectively account for approximately 30% of the total revenues of their upstream partners. Given these significant inter-firm connections, we anticipate that positive commodity price shocks will transmit through the supply chain, affecting the operational outcomes and productivity of these indirectly exposed upstream firms.

Table 5 presents the empirical results on how the commodity price shock, propagated through the domestic supply chain, affects the performance of upstream non-commodity firms. The findings demonstrate a clear positive impact on these indirectly exposed firms, encompassing both scale expansion and, crucially, productivity improvements.

Starting with firm-level scale, the results for total sales (column 1) indicate a significant expansion: a 1% increase in the customer-weighted commodity price shock experienced by downstream firms is associated with a 0.402% increase in the upstream firms' total sales under the IV specification. This result suggests that the increased demand from booming commodity exporters translates into tangible revenue growth for their domestic suppliers.

Table 5: Commodity Price Shocks and Upstream Firms' Outcomes


Notes. Specification as in Table 3. Regressions on sales and materials weighted by initial sales; employees weighted by wage bills. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01.

Unlike commodity exporters, upstream firms also increase capital investment: the IV estimate for capital stock (column 2) is positive and highly significant (0.112), suggesting that these firms translate demand increases into long-term capacity expansion.

More importantly, the analysis reveals a significant enhancement in the productivity of these upstream firms. The IV estimates show that a 1% increase in the propagated shock is associated with a 0.042% increase in TFPR (column 3) and a 0.092% increase in sales per employee (column 4). This finding stands in stark contrast to the direct effects observed within the commodity sector itself (Table 3), where we found no significant productivity improvements. This differential outcome suggests that the positive spillovers in upstream sectors might arise from various mechanisms, such as increased scale economies and learning-by-doing effects from supplying to rapidly expanding commodity firms.

Finally, examining input usage, the last two columns report the effects on materials expenditure and the number of employees. The IV estimates reveal positive and significant coefficients for both materials and employees. While the magnitude of the coefficient for materials expenditure is comparable to what was observed for directly affected commodity firms, the coefficient for employees is notably smaller. This indicates that upstream firms expand their variable inputs in response to the increased demand, but the labor response is relatively more contained compared to materials, a pattern consistent with upstream firms expanding through capital investment and productivity improvements rather than labor-intensive growth.

## 6 A Stylized Model: Commodity Boom and Misallocation

This section develops a stylized general equilibrium model to interpret the empirical patterns documented in Section 5, and to formalize the micro-level transmission channels through which global commodity price shocks affect firm productivity and resource allocation. The model links firm heterogeneity and pre-existing distortions to sectoral productivity changes following commodity demand shocks. While not a full-fledged quantitative framework, this parsimonious structure allows us to assess how much of the observed sectoral productivity decline it can explain.

Building on the seminal work of Hsieh and Klenow (2009) on resource misallocation, we introduce two key extensions designed to reflect the empirical mechanisms identified in our analysis of Chile's commodity boom.

First, we build a small open economy model based on Choi et al. (2024) and add firm-specific distortions in the form of export wedges, which capture differences in market access or policy-induced advantages such as subsidies, inspired by Bai et al. (2024). These wedges are critical for explaining why firms with lower TFPR can nonetheless achieve significant market shares and expand disproportionately in response to positive external demand shocks. As a result, resources shift toward firms that may not be the most productive from a social efficiency standpoint, exacerbating aggregate misallocation. We provide three microfoundations for this wedge—policy-induced advantages, heterogeneous intermediary access, and variable export markups—and, because it is otherwise a modeling assumption, we measure its concrete policy component directly and verify that it behaves as the model requires (Appendix C).

Second, we microfound the firm-specific labor wedge within an oligopsonistic labor market structure, following Berger et al. (2022). This extension serves two purposes. It provides a theoretical rationale for the empirically observed increases in firm-specific wages among firms benefiting from the commodity shock, and it formalizes the mechanism of "labor poaching," wherein expanding firms attract workers from other, often more productive, firms by offering higher wages.

To remain tractable, the model abstracts from capital accumulation, dynamics, and entry-exit. While this limits the ability to address investment responses and the extensive margin of exporting, the framework is designed to capture the key micro-level mechanisms we identify empirically: the absence of productivity improvements and labor reallocation toward less productive firms. We also abstract from explicitly modeling input-output linkages, despite their importance for upstream productivity gains, to have a sharper focus on the novel within-sector misallocation mechanisms. The supply chain channel (Acemoglu and Linn, 2004; Bloom et al., 2016; Huneeus, 2018) and demand-driven productivity upgrading (Ilzetzki, 2024; Atkin et al., 2017; Aghion et al., 2024) have been extensively studied in other contexts.

## 6.1 Setup

Households. A representative household maximizes utility with GHH preferences (Greenwood et al., 1988) by choosing consumption C and supplying labor L:

$$
\max _ {\{C, L \}} \log \left(C - \bar {\psi} \frac {L ^ {1 + \psi}}{1 + \psi}\right) \qquad \mathrm{s.t.} \qquad P C = W L + R K + P ^ {M} M + \Pi + T,
$$

where P is the final price index, which is normalized to one, and W is the wage. K and M denote capital and material endowments, respectively, R is the rental rate of capital, and $P^{M}$ is the price of material inputs. $\Pi = \sum_{j} \sum_{i \in F_{j}} \pi_{ij}$ is aggregate profits of all firms i across all sectors j, where $F_{j}$ denotes the set of firms in sector j. T represents lump-sum transfers from the government. $\bar{\psi}$ governs the level of disutility from labor supply, while $\psi$ governs the Frisch labor supply elasticity.

The household supplies differentiated labor to sectors and firms, where labor composite L aggregates labor through a nested CES (Berger et al., 2022):

$$
L = \left(\sum_ {j} L _ {j} ^ {\frac {\theta + 1}{\theta}}\right) ^ {\frac {\theta}{\theta + 1}}, \qquad L _ {j} = \left(\sum_ {i \in \mathcal {F} _ {j}} l _ {i j} ^ {\frac {\eta + 1}{\eta}}\right) ^ {\frac {\eta}{\eta + 1}},
$$

where $L_{j}$ is employment in sector j, and $l_{ij}$ is employment in firm i in sector j. $\eta > 0$ represents the elasticity of substitution across firms within a sector, while $\theta > 0$ denotes the elasticity across sectors. The aggregate and sectoral wage indices are $W = \left( \sum_{j} W_{j}^{\theta+1} \right)^{\frac{1}{\theta+1}}$ and $W_{j} = \left( \sum_{i \in \mathcal{F}_{j}} w_{ij}^{\eta+1} \right)^{\frac{1}{\eta+1}}$ , and the aggregate labor supply is $L = \left( \frac{1}{\bar{\psi}} \frac{W}{P} \right)^{\psi}$ .

Sectors. Firms' outputs are sold either in the domestic or foreign market. Outputs sold in the domestic market are aggregated into Home sectoral goods $Y_{j}^{H}$ at price $P_{j}^{H}$ as

$$
Y _ {j} ^ {H} = \left(\sum_ {i \in \mathcal {F} _ {j}} \left(y _ {i j} ^ {H}\right) ^ {\frac {\sigma - 1}{\sigma}}\right) ^ {\frac {\sigma}{\sigma - 1}}, \qquad P _ {j} ^ {H} = \left(\sum_ {i \in \mathcal {F} _ {j}} \left(p _ {i j} ^ {H}\right) ^ {1 - \sigma}\right) ^ {\frac {1}{1 - \sigma}},
$$

where $y_{ij}^{H}$ is the quantity of firm i's output sold in the domestic market, and $p_{ij}^{H}$ is the price in the domestic market. The Home sectoral goods and imports from the foreign country $Y_{j}^{M}$ are aggregated into sectoral goods as below:

$$
Y _ {j} = \left(\left(Y _ {j} ^ {H}\right) ^ {\frac {\rho - 1}{\rho}} + \left(Y _ {j} ^ {M}\right) ^ {\frac {\rho - 1}{\rho}}\right) ^ {\frac {\rho}{\rho - 1}}, \qquad P _ {j} = \left(\left(P _ {j} ^ {H}\right) ^ {1 - \rho} + \left(P _ {j} ^ {M}\right) ^ {1 - \rho}\right) ^ {\frac {1}{1 - \rho}},
$$

where $\rho$ is the elasticity of substitution between foreign and domestic goods, $P_{j}^{M}$ is the price of foreign good $Y_{j}^{M}$ , which is exogenous to the Home country.

Finally, the sectoral goods are aggregated by a Cobb–Douglas aggregator as

$$
C = \exp \left(\sum_ {j} \alpha_ {j} \ln Y _ {j}\right), \qquad P = \exp \left(\sum_ {j} \alpha_ {j} \ln P _ {j}\right).
$$

Here, $\alpha_{j}$ are Cobb-Douglas expenditure shares across sectors, with $\sum_{j} \alpha_{j} = 1$ .

Firms. Each firm i faces monopolistic competition in both domestic and export markets, and oligopsonistic competition in the labor market. The production technology for firm i uses labor, capital, and materials in a Cobb-Douglas function as below:

$$
y _ {i j} = a _ {i j} l _ {i j} ^ {\gamma^ {L}} k _ {i j} ^ {\gamma^ {K}} m _ {i j} ^ {\gamma^ {M}}.
$$

Here, $y_{ij}$ denotes the firm's total output, sold to both domestic consumers ( $y_{ij}^{H}$ ) and foreign consumers ( $y_{ij}^{F}$ ), such that $y_{ij} = y_{ij}^{H} + y_{ij}^{F}$ . $a_{ij}$ is firm-level quantity total factor productivity (TFPQ). A key assumption following Bai et al. (2024) is the presence of a firm-specific export revenue wedge that captures advantages such as export subsidies, preferential access to export markets, lower effective export costs. This assumption is empirically relevant for Chile's commodity sector and is further discussed in Section 6.4.2.

The firm's profit maximization problem is

$$
\max _ {l _ {i j}, k _ {i j}, m _ {i j}, p _ {i j} ^ {H}, p _ {i j} ^ {F}} \Pi_ {i j} = p _ {i j} ^ {H} y _ {i j} ^ {H} + \left(1 - \tau_ {i j} ^ {F}\right) p _ {i j} ^ {F} y _ {i j} ^ {F} - w _ {i j} l _ {i j} - R k _ {i j} - P ^ {M} m _ {i j},
$$

where $\tau_{ij}^{F}$ is a firm-specific export revenue wedge, $w_{ij}$ is the wage of firm $i$ . When $\tau_{ij}^{F} < 0$ , it implies that the firm has an advantage in the export market, such as an export subsidy or a lower effective export cost. Domestic demand is given by solving the consumer's problem as $y_{ij}^{H} = \left(\frac{p_{ij}^{H}}{P_j^H}\right)^{-\sigma}Y_j^H$ . Likewise, export demand is given by $y_{ij}^{F} = (p_{ij}^{F})^{-\sigma}D_{ij}^{F}$ , where $D_{ij}^{F}$ is an exogenous export demand shifter, which is firm-specific and microfounded in Appendix B.1. It can also be mapped to the Bartik measure used in the empirical analyses, as shown in Appendix B.2.

In the labor market, firms engage in Cournot competition, choosing employment while internalizing their effect on wages. The CES aggregation of differentiated labor implies an upward-sloping labor supply curve for each firm:

$$
l _ {i j} = \left(\frac {w _ {i j}}{W _ {j}}\right) ^ {\eta} L _ {j}.\tag{6}
$$

This structure allows the model to capture the empirical pattern that expanding firms pay higher wages.

Product Market Distortions. The firm faces downward-sloping demand curves for its product in both domestic and export markets. It sets its prices to maximize profits from each market, considering its marginal cost. We assume that firms can price discriminate between the domestic and export markets. The optimal domestic price $p_{ij}^{H}$ is:

$$
p _ {i j} ^ {H} = \left(\frac {\sigma}{\sigma - 1}\right) M C _ {i j},\tag{7}
$$

where $\mu := \frac{\sigma}{\sigma-1}$ is the constant markup that firms charge. Likewise, the optimal export price $p_{ij}^{F}$ is

$$
p _ {i j} ^ {F} = \frac {1}{1 - \tau_ {i j} ^ {F}} \left(\frac {\sigma}{\sigma - 1}\right) M C _ {i j}.\tag{8}
$$

Comparing (7) and (8), we see that $p_{ij}^{F} = \frac{1}{1 - \tau_{ij}^{F}} p_{ij}^{H}$ . This indicates that the export wedge $\tau_{ij}^{F}$ directly influences the relative price between export and domestic markets. If $\tau_{ij}^{F} < 0$ , representing an export advantage, $p_{ij}^{F} < p_{ij}^{H}$ , leading to higher export demand and a larger export share. Conversely, if $0 < \tau_{ij}^{F} < 1$ , implying an export disadvantage, $p_{ij}^{F} > p_{ij}^{H}$ , resulting in lower export demand and a smaller export share.

Labor Market Distortions. Given the upward-sloping labor supply curve (Equation (6)), hiring an additional worker raises the wage the firm must pay to all workers. The firm internalizes this cost, leading to the first-order condition:

$$
\mathrm{mrpl} _ {i j} = \mu_ {i j} ^ {L} \cdot w _ {i j},\tag{9}
$$

where $mrpl_{ij} = \frac{\gamma^{L} p_{ij}^{H} y_{ij}}{\mu l_{ij}}$ is the marginal revenue product of labor, and $\mu_{ij}^{L} > 1$ is the labor markdown. The markdown is the labor market analog of a markup: just as firms charge prices above marginal cost, they pay wages below marginal revenue product.

The markdown depends on the firm-specific elasticity of labor supply:

$$
\mu_ {i j} ^ {L} := \frac {\epsilon_ {i j} ^ {L} + 1}{\epsilon_ {i j} ^ {L}}, \qquad \epsilon_ {i j} ^ {L} = \left(\frac {1}{\eta} + \left(\frac {1}{\theta} - \frac {1}{\eta}\right) s _ {i j} ^ {L}\right) ^ {- 1},
$$

where $s_{ij}^{L} = \frac{w_{ij}l_{ij}}{W_{j}L_{j}}$ is firm i's wage bill share in sector j. We assume $\eta > \theta$ , so workers move more easily across firms within a sector than across sectors. Larger firms dominate their sector's labor market, so their workers face the less elastic cross-sector margin, giving these firms greater monopsony power.

Capital and materials are priced competitively. The firm's marginal cost is:

$$
M C _ {i j} = \frac {1}{a _ {i j}} \left(\mu_ {i j} ^ {L} w _ {i j} / \gamma^ {L}\right) ^ {\gamma^ {L}} \left(R / \gamma^ {K}\right) ^ {\gamma^ {K}} \left(P ^ {M} / \gamma^ {M}\right) ^ {\gamma^ {M}}.\tag{10}
$$

## 6.2 Firm-Level TFPR

To connect the model to our empirical analysis, we define firm-level TFPR as total revenue divided by a Cobb-Douglas aggregate of inputs, consistent with standard measurement approaches:

$$
\mathrm{tfpr} _ {i j} \equiv \frac {p _ {i j} ^ {H} y _ {i j} ^ {H} + p _ {i j} ^ {F} y _ {i j} ^ {F}}{l _ {i j} ^ {\gamma_ {L}} k _ {i j} ^ {\gamma_ {K}} m _ {i j} ^ {\gamma_ {M}}}.\tag{11}
$$

Combining the firm's first-order conditions from Section 6.1 with the production technology yields measured TFPR (See Appendix Section B.3 for the complete derivation.)

$$
\mathrm{tfpr} _ {i j} = \underbrace {\frac {1}{1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}}} _ {\text {export wedge}} \cdot \underbrace {\left(\mu_ {i j} ^ {L}\right) ^ {\gamma^ {L}} \left(s _ {i j} ^ {L}\right) ^ {\frac {\gamma^ {L}}{1 + \eta}}} _ {\text {labor market power}} \cdot \underbrace {\mu \left(\frac {W _ {j}}{\gamma^ {L}}\right) ^ {\gamma^ {L}} \left(\frac {R}{\gamma^ {K}}\right) ^ {\gamma^ {K}} \left(\frac {P ^ {M}}{\gamma^ {M}}\right) ^ {\gamma^ {M}}} _ {\text {common across firms}}\tag{12}
$$

where $s_{ij}^{F} = \frac{p_{ij}^{F}y_{ij}^{F}}{p_{ij}^{H}y_{ij}^{H} + p_{ij}^{F}y_{ij}^{F}}$ is the firm's export share.

This expression reveals two sources of TFPR dispersion in our model, which operate in opposite directions. First, export subsidies lower TFPR. The export wedge term shows that firms with larger export advantages (more negative $\tau_{ij}^{F}$ ) exhibit lower measured TFPR, because subsidies allow firms to charge lower export price and induce them to produce above the level implied by their underlying productivity, which reduces revenue per unit of input. This distortion is amplified when export shares $s_{ij}^{F}$ are larger—and since export subsidies lower export prices (Equation (8)), heavily subsidized firms tend to have larger export shares, reinforcing the effect. Export subsidies are the primary source of misallocation in our calibrated model.

Second, labor market power raises measured TFPR, partially offsetting the export wedge distortion. Firms with greater monopsony power (higher $\mu_{ij}^{L}$ ) restrict employment, and larger firms (higher $s_{ij}^{L}$ ) must pay higher wages to attract workers, raising prices. Both effects increase TFPR, partially offsetting the export wedge distortion. The effect depends on the structure of distortions: $\gamma^{L}$ appears on both terms because labor market power only distorts the labor margin, scaled by labor's cost share, while $\frac{1}{1+\eta}$ on the wage-bill-share term captures how greater worker mobility across firms (higher $\eta$ ) attenuates this channel, as $\eta \to \infty$ , workers move freely across firms and this source of TFPR dispersion vanishes.

In a frictionless benchmark with $\tau_{ij}^{F}=0$ and competitive labor markets $(\eta,\theta\to\infty)$ , TFPR equalizes across firms. Away from this benchmark, a uniform positive export demand shock exacerbates misallocation: firms with lower initial TFPR (those with larger export subsidies) expand disproportionately, because their larger subsidies make them more export-oriented to begin with, so the same demand shock translates into a larger overall expansion. We include oligopsonistic labor markets primarily to match the empirical pattern of rising wages among expanding firms. A useful byproduct is that this provides a conservative estimate of misallocation effects, since rising labor market power among expanding firms partially offsets their falling TFPR. We demonstrate these results quantitatively in Section 6.4.

## 6.3 Sectoral Real TFP

Sectoral productivity aggregates firm-level outcomes, reflecting the allocation of resources across heterogeneous firms. Following standard practice, we define:

$$
A _ {j} \equiv \frac {\mathrm{TFPR} _ {j}}{\mathrm{PPI} _ {j}} = \left(\sum_ {i \in \mathcal {F} _ {j}} \left(a _ {i j} \frac {\mathrm{TFPR} _ {j}}{\mathrm{tfpr} _ {i j}}\right) ^ {\sigma - 1}\right) ^ {\frac {1}{\sigma - 1}},\tag{13}
$$

where $TFPR_{j}$ is sectoral revenue productivity and $PPI_{j}$ is the sectoral price index. $^{22}$ This expression shows that sectoral productivity $A_{j}$ depends not only on firms' physical productivity ( $a_{ij}$ ) but critically on the allocation of resources across firms: greater TFPR dispersion (larger gaps between $\mathrm{tfpr}_{ij}$ and $\mathrm{TFPR}_j$ reduces aggregate productivity. A commodity boom that reallocates inputs toward low-TFPR firms—those with export advantages—will lower $A_{j}$ even if no individual firm's physical productivity ( $a_{ij}$ ) declines.

Table 6: Calibration Results


## 6.4 Quantitative Assessment

We calibrate the model to match key features of the Chilean data and assess whether it can replicate the empirical patterns documented in Section 5. We then use the calibrated model to quantify how much of the observed productivity decline in the commodity sector can be attributed to the misallocation mechanism.

## 6.4.1 Calibration

We focus on j = 1 representing the commodity sector, with representative firms in all other sectors. Table 6 summarizes the calibration strategy.

Externally calibrated parameters (Panel A) are drawn from established estimates in the literature. We set the within-sector demand elasticity $\sigma = 3$ following Hsieh and Klenow (2009), labor substitution elasticities $\eta = 2.76$ (within-sector) and $\theta = 0.42$ (across-sector) from labor market power estimates in Yeh et al. (2022) and Berger et al. (2022), the Armington elasticity $\rho = 2$ from Boehm et al. (2023), and the Frisch elasticity $\psi = 0.5$ as in Chetty et al.

(2013).

Production function parameters (Panel B) come directly from input cost shares in Chilean administrative data. We compute wage bills, material expenditures, and sales for 2-digit industries containing commodity exporters, take the average of input shares across industries, and impose constant returns to scale $\left(\gamma^{K}=1-\gamma^{L}-\gamma^{M}\right)$ , yielding $\gamma^{L}=0.11$ , $\gamma^{M}=0.59$ , and $\gamma^{K}=0.30$ .

Internally calibrated parameters (Panel C) govern the distributions of firm productivity and export wedges. We assume $a_{i1}$ and $1 - \tau_{i1}^{F}$ are log-normally distributed with log-mean zero and log standard deviations $\sigma^{a}$ and $\sigma^{F}$ , respectively. We simulate 10,000 firms in the commodity sector and calibrate three parameters to match data moments: $\bar{D}^{F}$ , the common export demand shifter, targets the aggregate export share of 71% in 2005, $\sigma^{a}$ (productivity dispersion) matches the variance-to-mean ratio of sales, and $\sigma^{F}$ (export wedge dispersion) matches the variance of export shares across firms.

## 6.4.2 The Export Wedge in the Data

The export wedge is the one ingredient of our framework that is not directly observed in standard data, which raises a natural question—does it reflect a real policy distortion, or unmodeled heterogeneity?

We measure a concrete component of it. From administrative customs and statutory data, we construct a firm-level net export wedge for 2003 from four predetermined Chilean trade programs—export rebates (Reintegro Simplificado and Drawback) on the subsidy side, and fisheries individual transferable quotas and aquaculture concessions on the restriction side—aggregated to the firm by its 2003 export shares. Because it captures only explicit, legislated instruments, this measure is a conservative lower bound on the full wedge.

Comparing firms within the same sector, we find that those facing a more favorable net wedge expand exports significantly more when the commodity shock arrives, with the restriction (implicit-tax) margin carrying the predicted negative sign. Since every program was legislated for domestic reasons predating the boom, the wedge is largely predetermined with respect to the shock. This is direct evidence that the model's key distortion is real and policy-induced rather than reduced-form export-demand heterogeneity, and that it moves firm behavior in the direction the misallocation mechanism requires. The wedge we measure corresponds to the policy microfoundation of $\tau^F$ ; we also formalize two further sources (heterogeneous intermediary access and variable export markups) that generate the same firm-level behavior. See Appendix C for these microfoundations and the construction details.

Table 7: Targeted and Non-targeted Moments


Notes. This table reports targeted and non-targeted moments from the data and the model. Non-targeted moments in Panel B are regression coefficients from estimating our baseline specification (Equation (1)) on simulated data, where we regress DHS growth rates on the commodity price shock $\left(\Delta\log D_{ij}^{F}\right)$ . \*\*\* p<0.01, \*\* p<0.05, \* p<0.10.

## 6.4.3 Model Validation: Matching Untargeted Empirical Patterns

Having calibrated the model to match basic distributional features, we now assess whether it can reproduce our key empirical findings without directly targeting the regression coefficients from Section 5. This constitutes a stringent test of whether the two-friction framework (export wedges plus oligopsonistic labor markets) captures the essential misallocation mechanism.

To replicate our empirical exercise, we simulate the commodity price shock as follows. We randomly select half of the 10,000 simulated firms to receive a large shock, increasing their export demand $D_{i1}^{F}$ by 206%, corresponding to the 90–10 percentile difference in our firm-specific commodity price shock measure from the data. We then scale up export demand for all firms proportionally to match the observed 83% aggregate export value growth between 2005 and 2013. This two-step procedure captures both the cross-sectional variation in shock exposure and the aggregate boom. Finally, we compute each firm's simulated outcomes (exports, employment, wages, materials, TFPR) and run the identical DHS growth rate regression used in our empirical analysis.

Panel B of Table 7 reports the results. The model successfully reproduces the empirical patterns both qualitatively and quantitatively, despite none of these coefficients being directly

targeted in calibration:

Exports and Variable Inputs Expand Substantially The model predicts strong increases in exports, materials, and employment, consistent with firms scaling up production in response to the positive demand shock. The wage response confirms that expanding firms must raise wages to attract workers, though the model somewhat underpredicts the magnitude.

Productivity Shows No Improvement The simulated TFPR coefficient is small and similar to the statistically insignificant empirical estimate, confirming that export revenue gains do not translate into efficiency improvements within firms. Equation (12) implies that the firm level TFPR increases with $s_{ij}^{F}$ when $\tau_{ij}^{F} > 0$ , and decreases with $s_{ij}^{F}$ when $\tau_{ij}^{F} < 0$ . Because $\tau_{ij}^{F}$ is log-normally distributed with mean zero, these opposing effects tend to offset each other, making the regression coefficients close to zero. Labor market power also contributes: large firms may hire less labor than under perfect competition, which raises their measured TFPR. This generates a small positive coefficient on TFPR in the model.

Differential Employment Response by Initial TFPR The model reproduces the key asymmetric pattern documented in Table 4 Panel C: low-TFPR firms expand employment substantially while high-TFPR firms show muted growth. Simulated low-TFPR firms (those below the sectoral median) expand employment by 0.633, nearly identical to the empirical estimate of 0.620. High-TFPR firms in the model show modest expansion of 0.383, compared to the empirical estimate of -0.163 (though the latter has wide confidence intervals and is not statistically significant). While the model does not perfectly match the high-TFPR coefficient, it successfully captures the central empirical finding: the commodity boom disproportionately expands employment at less productive firms. This asymmetric response validates that our two-friction framework—combining export wedges with oligopsonistic labor markets—can account for the observed labor reallocation patterns.

Why does the model generate these patterns? Figure 3 illustrates the cross-sectional relationships in the calibrated economy. Panel A shows that export shares decline monotonically with the export wedge $\tau_{ij}^{F}$ : subsidized firms ( $\tau_{ij}^{F} < 0$ ) sell predominantly to foreign markets, with export shares approaching $100\%$ for the most heavily subsidized. Panel B reveals the corresponding TFPR gradient: these same export-oriented firms exhibit systematically lower measured productivity, as predicted by Equation (12). When a demand shock increases, firms with $\tau_{ij}^{F}<0$ expand disproportionately because their high export orientation makes them more exposed to foreign demand shifts. This expansion operates through the oligopsonistic labor market: booming firms raise wages to poach workers from competitors, including from higher-TFPR firms with less export exposure. While rising labor market power partially offsets the TFPR decline among expanding firms, the net effect is a reallocation of labor toward low-TFPR firms, which drives the aggregate productivity decline we quantify next.


[[KC_IMAGE_004]]

A. $s_{ij}^{F}$


[[KC_IMAGE_005]]

B. $\log(\text{tfpr}_{ij})$
Notes. Panel A plots export share $s_{ij}^{F}$ and Panel B plots log firm-level TFPR, both against the export wedge $\tau_{ij}^{F}$ on the horizontal axis. Each point represents one of 10,000 simulated firms in the calibrated model. The strong negative relationship in Panel A shows that subsidized firms ( $\tau_{ij}^{F} < 0$ ) are export-oriented, while Panel B confirms these same firms have systematically lower measured productivity.

## 6.4.4 Aggregate Productivity Impact

Using the calibrated model, we compute the change in sectoral productivity following the simulated commodity boom using Equation (13). The results show that sectoral productivity in the commodity sector falls by 3.94%—roughly half the 8% decline in Chilean mining TFP observed between 2005 and 2013 (Figure 1).

This quantitative result demonstrates that the misallocation mechanism—the interaction of pre-existing export distortions with oligopsonistic labor markets—can account for a substantial share of the observed aggregate productivity decline. Our parsimonious model, which abstracts from capital dynamics, ore grade deterioration, and other sector-specific factors, nonetheless explains approximately 50% of the TFP drop solely through compositional shifts in resource allocation. The remaining gap likely reflects factors outside the model’s scope, including within-firm declines in TFPQ driven by the long gestation lags and capacity constraints in mining capital investment, ore deterioration or lower stripping ratio as documented by CNEP (2017), or potential negative spillovers to non-exporting firms we do not explicitly model.

The welfare implications are significant. While export revenues surge by $83\%$ and employment expands substantially, the economy deviates more from its efficient allocation. The commodity boom reallocates labor and materials toward firms with artificially enhanced export access rather than those with superior underlying productivity $(a_{ij})$ , reducing the sector's ability to convert inputs into output. Had the same demand shock occurred in an undistorted economy (with $\tau_{ij}^{F} = 0$ for all firms and competitive labor markets), aggregate productivity would have remained constant. Instead, the pre-existing distortions turn what would ordinarily be a positive terms-of-trade shock into a source of inefficiency, illustrating how gains from trade can be muted or even reversed in second-best environments.

## 7 Conclusion

This paper investigates how commodity booms affect firm-level productivity and resource allocation using comprehensive administrative data from Chile. We examine a striking pattern: while commodity exporters experienced massive revenue increases during the 2000s boom, aggregate mining sector productivity declined by approximately 8%, even as non-mining sectors saw productivity gains.

We document three key mechanisms that explain this pattern. First, commodity-exporting firms exhibit significant scale expansion without productivity gains or sustained investment. Despite surging exports and variable input usage, these firms show no improvement in TFPR. Since rising commodity prices likely increased firm-level output prices, the null TFPR result mechanically implies declining physical productivity (TFPQ). Second, within the commodity sector, labor reallocates toward less productive firms. Firms with below-median initial productivity expand employment in response to commodity price shocks, while high-productivity firms show no expansion. This occurs because expanding firms use their revenue windfall to offer substantially higher wages, enabling them to poach workers from more productive competitors. Third, positive shocks propagate through supply chains to enhance productivity among upstream domestic suppliers, contrasting sharply with the null effects observed among direct exporters.

We develop a stylized model with firm-specific export wedges and labor market frictions to formalize these mechanisms. Despite its parsimony, the model explains approximately 50% of the observed TFP decline through compositional shifts in resource allocation. The welfare implications are significant: while export revenues surge and employment expands, pre-existing distortions cause the commodity boom to exacerbate resource misallocation and reduce aggregate mining productivity. Our study underscores the importance of micro-level transmission channels in understanding the broader economic impact of commodity cycles.

## References

ACEMOGLU, DARON AND JOSHUA LINN (2004): “Market size in innovation: theory and evidence from the pharmaceutical industry,” The Quarterly journal of economics, 119 (3), 1049–1090.

ACKERBERG, DANIEL A, KEVIN CAVES, AND GARTH FRAZER (2015): “Identification properties of recent production function estimators,” Econometrica, 83 (6), 2411–2451.

ADAMOPOULOS, TASSO, LOREN BRANDT, JESSICA LEIGHT, AND DIEGO RESTUCCIA (2022): “Misallocation, Selection, and Productivity: A Quantitative Analysis with Panel Data from China,” Econometrica, 90 (3), 1261–1282.

ADAO, RODRIGO, MICHAL KOLESÁR, AND EDUARDO MORALES (2018): “Shift-Share Designs: Theory and Inference,” NBER working paper No.24944.

AGHION, PHILIPPE, ANTONIN BERGEAUD, MATTHIEU LEQUIEN, AND MARC J MELITZ (2024): “The Heterogeneous Impact of Market Size on Innovation: Evidence from French Firm-Level Exports,” Review of Economics and Statistics, 106 (3), 608–626.

ALBEROLA, ENRIQUE AND GIANLUCA BENIGNO (2017): “Revisiting the commodity curse: A financial perspective,” Journal of International Economics, 108, S87–S106.

ALLCOTT, HUNT AND DANIEL KENISTON (2018): “Dutch Disease or Agglomeration? The Local Economic Effects of Natural Resource Booms in Modern America,” The Review of Economic Studies, 85 (2), 695–731.

AMODIO, FRANCESCO, GIOVANNI CHIOVELLI, AND SERAFÍN FRACHE (2025): “Beefing up the Service Sector: Commodity Exports to China and Production Network Spillovers,” Tech. Rep. CEPR Discussion Paper DP20078, Centre for Economic Policy Research.

ATKESON, ANDREW AND ARIEL BURSTEIN (2008): “Pricing-to-Market, Trade Costs, and International Relative Prices,” American Economic Review, 98 (5), 1998–2031.

ATKIN, DAVID, AMIT K KHANDELWAL, AND ADAM OSMAN (2017): “Exporting and Firm Performance: Evidence from a Randomized Experiment,” The quarterly journal of economics, 132 (2), 551–615.

AUTOR, DAVID H, DAVID DORN, AND GORDON H HANSON (2013): “The China syndrome: Local labor market effects of import competition in the United States,” American economic review, 103 (6), 2121–2168.

BAI, LIANG AND SEBASTIAN STUMPNER (2019): “Estimating US consumer gains from Chinese imports,” American Economic Review: Insights, 1 (2), 209–224.

BAI, YAN, KEYU JIN, AND DAN LU (2024): “Misallocation Under Trade Liberalization,” American Economic Review, 114 (7), 1949–1985.

BAU, NATALIE AND ADRIEN MATRAY (2023): “Misallocation and Capital Market Integration: Evidence from India,” Econometrica, 91 (1), 67–106.

BENGURIA, FELIPE, FELIPE SAFFIE, AND SERGIO URZÚA (2024a): “The Transmission of Commodity Price Super-Cycles,” Review of Economic Studies, 91 (4), 1923–1955.

BENGURIA, FELIPE, FELIPE SAFFIE, AND SHIHANGYIN ZHANG (2024b): “Spatial Linkages and the Uneven Effects of a Commodity Boom,” Tech. rep., National Bureau of Economic Research.

BERGER, DAVID, KYLE HERKENHOFF, AND SIMON MONGEY (2022): “Labor market power,” American Economic Review, 112 (4), 1147–1193.

BERTHOU, ANTOINE, JOHN JONG-HYUN CHUNG, KALINA MANOVA, AND CHARLOTTE SANDOZ (2020): “Trade, Productivity and (Mis) allocation,” IMF Working Paper.

BLOOM, NICHOLAS, MIRKO DRACA, AND JOHN VAN REENEN (2016): “Trade induced technical change? The impact of Chinese imports on innovation, IT and productivity,” The review of economic studies, 83 (1), 87–117.

BOEHM, CHRISTOPH E, ANDREI A LEVCHENKO, AND NITYA PANDALAI-NAYAR (2023): "The Long and Short (Run) of Trade Elasticities," American Economic Review, 113 (4), 861–905.

BORUSYAK, KIRILL, PETER HULL, AND XAVIER JARAVEL (2022): “Quasi-experimental shift-share research designs,” The Review of economic studies, 89 (1), 181–213.

CHETTY, RAJ, ADAM GUREN, DAY MANOLI, AND ANDREA WEBER (2013): “Does Indivisible Labor Explain the Difference between Micro and Macro Elasticities? A Meta-Analysis of Extensive Margin Elasticities,” NBER Macroeconomic Annual, 27 (1), 1–56.

CHOI, JAEDO (2025): “Lobbying, trade, and misallocation,” Journal of International Economics, 155, 104086.

CHOI, JAEDO, ANDREI A LEVCHENKO, DIMITRIJE RUZIC, AND YOUNGHUN SHIM (2024): "Superstars or Supervillains? Large Firms in the South Korean Growth Miracle," Tech. rep., National Bureau of Economic Research.

CNEP (2017): “Productivity in the Chilean Copper Mining Industry,” Chilean Comision Nacional de Productividad.

CORDEN, WARNER MAX (1984): “Booming sector and Dutch disease economics: survey and consolidation,” oxford economic Papers, 36 (3), 359–380.

CORDEN, W. MAX AND J. PETER NEARY (1982): “Booming Sector and De-industrialisation in a Small Open Economy,” The Economic Journal, 92 (368), 825–848.

DAVIS, STEVEN J, JOHN C HALTIWANGER, AND SCOTT SCHUH (1998): “Job Creation and Destruction,” MIT Press Books, 1.

DE CHAISEMARTIN, CLÉMENT AND XAVIER D'HAULTFOEUILLE (2020): "Two-way fixed effects estimators with heterogeneous treatment effects," American economic review, 110(9), 2964–2996.

DE LOECKER, JAN AND PAUL T. SCOTT (2025): “Markup Estimation using Production and Demand Data: An Application to the US Brewing Industry,” Review of Economic Studies, accepted.

DE SOLMINIHAC, HERNAN, LUIS E GONZALES, AND RODRIGO CERDA (2018): “Copper

mining productivity: lessons from Chile,” Journal of Policy Modeling, 40 (1), 182–193.

DRECHSEL, THOMAS AND SILVANA TENREYRO (2018): “Commodity booms and busts in emerging economies,” Journal of International Economics, 112, 200–218.

DUBE, ARINDRAJIT, DANIELE GIRARDI, OSCAR JORDA, AND ALAN M TAYLOR (2023): “A local projections approach to difference-in-differences event studies,” Tech. rep., National Bureau of Economic Research Cambridge, Massachusetts.

FERNÁNDEZ, ANDRÉS, STEPHANIE SCHMITT-GROHÉ, AND MARTÍN URIBE (2017): “World shocks, world prices, and business cycles: An empirical investigation,” Journal of International Economics, 108, S2–S14.

—— (2023): “How important is the commodity supercycle?” .

GANDHI, AMIT, SALVADOR NAVARRO, AND DAVID A RIVERS (2020): “On the identification of gross output production functions,” Journal of Political Economy, 128 (8), 2973–3016.


GONZÁLEZ, GUSTAVO (2021): Commodity Price Shocks, Factor Utilization, and Productivity Dynamics, Working Paper.

GOPINATH, GITA, SEBNEM KALEMLI-ÖZCAN, LOUKAS KARABARBOUNIS, AND CAROLINA VILLEGAS-SANCHEZ (2017): “Capital Allocation and Productivity in South Europe,” The Quarterly Journal of Economics, 132 (4), 1915–1967.

GREENWOOD, J., Z. HERCOWITZ, AND G.W. HUFFMAN (1988): “Investment, capacity utilization and the real business cycle,” American Economic Review, 87, 342–362.

HEISE, SEBASTIAN AND TOMMASO PORZIO (2022): “Labor Misallocation Across Firms and Regions,” NBER Working Paper 30298, National Bureau of Economic Research.

HERESI, RODRIGO (2023): “Reallocation and Productivity in Resource-rich Economies,” Journal of International Economics, 145, 103843.

HSIEH, CHANG-TAI AND PETER J KLENOW (2009): “Misallocation and manufacturing TFP in China and India,” The Quarterly journal of economics, 124 (4), 1403–1448.

HUNEEUS, FEDERICO (2018): “Production Network Dynamics and the Propagation of Shocks,” Graduate thesis, Princeton University, Princeton, NJ, 52.

HUNEEUS, FEDERICO, KORY KROFT, AND KEVIN LIM (2021): “Earnings Inequality in Production Networks,” Tech. rep., NBER Working Paper No. 28424.

ILZETZKI, ETHAN (2024): “Learning by Necessity: Government Demand, Capacity Constraints, and Productivity Growth,” American Economic Review, 114 (8), 2436–71.

Kohn, David, Fernando Leibovici, and Håkon Tretvoll (2021): “Trade in commodities and business cycle volatility,” American Economic Journal: Macroeconomics, 13 (3), 173–208.

KROETZ, KAILIN, JAMES N. SANCHIRICO, JULIO PEÑA TORRES, AND DAVID

CORDERI NOVOA (2017): “Evaluation of the Chilean Jack Mackerel ITQ System,” Marine Resource Economics, 32 (2), 217–241.

LARRAIN, MAURICIO AND SEBASTIAN STUMPNER (2017): “Capital Account Liberalization and Aggregate Productivity: The Role of Firm Capital Allocation,” The Journal of Finance, 72 (4), 1825–1858.

MENDOZA, ENRIQUE G (1995): “The Terms of Trade, the Real Exchange Rate, and Economic Fluctuations,” International Economic Review, 101–137.

OBERFIELD, EZRA (2013): “Productivity and Misallocation During a Crisis: Evidence from the Chilean Crisis of 1982,” Review of Economic Dynamics, 16 (1), 100–119.

REINHART, CARMEN M, VINCENT REINHART, AND CHRISTOPH TREBESCH (2016): “Global cycles: Capital flows, commodities, and sovereign defaults, 1815–2015,” American Economic Review, 106 (5), 574–580.

RESTUCCIA, DIEGO AND RICHARD ROGERSON (2017): “The Causes and Costs of Misallocation,” Journal of Economic Perspectives, 31 (3), 151–174.

SCHMITT-GROHÉ, STEPHANIE AND MARTÍN URIBE (2018): “How important are terms-of-trade shocks?” International Economic Review, 59 (1), 85–111.

SHOUSHA, SAMER (2016): “Macroeconomic Effects of Commodity Booms and Busts: The Role of Financial Frictions,” American Economic Journal: Macroeconomics, 8 (4), 144–176.

SILVA, ALVARO, PETRE CARAIANI, JORGE MIRANDA-PINTO, AND JUAN OLAYA-AGUDELO (2024): “Commodity Prices and Production Networks in Small Open Economies,” Journal of Economic Dynamics and Control, 168, 104968.

TOMA, HIROSHI AND WALTER CUBA (2024): “The Financial Propagation Mechanism of Commodity Booms,” Working Paper.

WEINBERGER, ARIEL (2020): “Markups and misallocation with evidence from exchange rate shocks,” Journal of Development Economics, 146, 102494.

YEH, CHEN, CLAUDIA MACALUSO, AND BRAD HERSHBEIN (2022): “Monopsony in the US labor market,” American Economic Review, 112 (7), 2099–2138.

## Supplementary Material

## Appendix A Empirical Appendix

## A.1 TFP in Non-mining and Aggregate Sectors

Figure A.1: Chile's Non-Mining and Aggregate TFP

[[KC_IMAGE_006]]

Notes. TFP is estimated as residual of the equation $\log VA_{jt} = \alpha_j \log K_{jt} + (1 - \alpha_j) \log L_{jt} + \epsilon_{jt}$ , where $\alpha_j$ is calibrated at the sectoral level. $VA_{jt}$ represents the real value added, calculated using respective sectoral chained prices deflators. $K_{jt}$ denotes the capital stock at constant prices, adjusted for utilization rate, while $L_{jt}$ is the total number of working hours, corrected for the quality of human capital.

## A.2 The Firm-Level Commodity Shock

Our firm-level commodity shock, $shock_{f} = \sum_{p} \omega_{pf} \Delta P_{p}$ , combines product-level price changes $\Delta P_{p}$ with each firm's 2003 export shares $\omega_{pf}$ . This appendix documents what the shock is made of and how it behaves. Product price changes differ across goods, commodity exporters are nearly single-product, and as a result, each firm's shock is close to the price shock of its single dominant product.


[[KC_IMAGE_007]]

Figure A.2: Log Price Change for Selected Chilean Commodity Exports in China (2003–2011)

Notes. Log price changes between 2003 and 2011 for the top 14 Chilean commodity products by 2003 export value, sorted by price increase. We exclude products with large price drops (e.g., fish meat, HS 030490) for visualization. Each bar is the total log price change for a 6-digit HS product. Labels and HS codes: Wine (220421), Copper ores & conc. (260300), Copper unrefined anodes (740200), Copper refined cathodes (740311), Fish fillets frozen (030420), Grapes fresh (080610), Apples fresh (080810), Wood pulp coniferous (470321), Copper refined unwrought (740319), Coniferous wood sawn (440710), Salmon Pacific frozen (030319), Trout frozen (030321), Wood pulp unbleached coniferous (470311), Wood pulp non-coniferous (470329).

## A.2.1 Differential price changes across products

The identifying variation in our analysis is the change in commodity prices across granular products. Rather than an aggregate index, Figure A.2 shows heterogeneity in log price changes across 6-digit HS products, including within a broader commodity group. Refined copper cathodes (HS 740311) saw large increases while unwrought copper (HS 740319) gained considerably less, and outcomes range from a sharp surge in wine (HS 220421) to milder increases in apples (HS 080810) and wood pulp.

Figure A.3: Commodity Exporters Are Highly Specialized

[[KC_IMAGE_008]]

A. Top product share per firm


[[KC_IMAGE_009]]

B. Effective number of products per firm

Notes. One observation per Chilean exporting firm in 2003 (administrative Customs data). Panel A: the share of a firm's export value in its single largest 6-digit (HS6) product; the distribution piles up near one (median 0.93). Panel B: the effective number of HS6 products per firm, $1 / \mathrm{HHI}_f$ with $\mathrm{HHI}_f = \sum_p s_{fp}^2$ and $s_{fp}$ product $p$ 's share of firm $f$ 's exports; it equals one for a single-product firm and $N$ for $N$ equal products (median 1.15, mean 2.09; horizontal axis truncated at 15).

## A.2.2 Commodity exporters are highly specialized

Most firms concentrate their exports in a single 6-digit product. The median firm holds a share of 0.93 in its largest product and has an effective number of products of 1.15, close to a single-product firm. Identifying variation in the firm shock therefore comes mostly from across-firm differences in which product a firm specializes in, rather than from within-firm portfolio diversity.

## A.2.3 The firm shock and its dominant product's shock

Because firms are specialized, the firm shock splits into the price shock of the dominant product plus a within-firm remainder:

$$
\mathrm{shock} _ {f} = \underbrace {\omega_ {d (f) f} \Delta P _ {d (f)}} _ {\text {dominant product (across - firm)}} + \underbrace {\sum_ {p \neq d (f)} \omega_ {p f} \Delta P _ {p}} _ {\text {within - firm portfolio}},\tag{14}
$$

where $d(f)$ is firm $f$ 's largest 2003 export product. The first term varies across firms by which product they specialize in, and the second reflects within-firm composition. The first term accounts for most of the variation. A shock built from the dominant product alone has a correlation of 0.96 with the baseline shock and accounts for about $94\%$ of its cross-firm

variance, as shown in Figure A.4.

Figure A.4: Baseline Shock vs. Dominant-Product Shock

[[KC_IMAGE_010]]

Notes. Each point is a firm in the commodity sample with both shocks defined $(N = 1,400)$ . Horizontal axis: baseline shock $(\sum_{p} \omega_{pf} \Delta P_{p}, 2003 \text{ export-share weighted})$ ; vertical axis: shock from the firm's single dominant 2003 HS6 product. Solid line: OLS fit; dashed: 45-degree line.

Table A.1 makes this concrete. Replacing the baseline shock with the dominant-product shock leaves the estimated effect on firm export growth largely unchanged, and in both the all-exporter and commodity samples the two shocks deliver similar positive and significant effects. Identification is thus driven largely, though not exclusively, by across-firm specialization.

Table A.1: Firm Export Growth: Baseline vs. Dominant-Product Shock


Notes. Firm export growth (DHS mid-point growth, 2003–2011) regressed on the commodity price shock, weighted by initial (2003) export value, with standard errors clustered at the dominant 4-digit industry; the sample is firms with both shocks defined. Within each sample the regressor alternates between the baseline shift-share shock and the dominant-product shock (the firm's single largest-share HS6). The two shocks deliver nearly identical, positive and significant effects, confirming that the result does not depend on within-firm portfolio variation (see Figure A.4). \*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.10.

The shift-share literature recommends standard errors that allow for correlated exposure among firms loading on the same shocks (Adao et al., 2018; Borusyak et al., 2022). In our setting, each firm is effectively assigned a single product, and a commodity exporter's 4-digit industry coincides with its export product. Clustering at the 4-digit industry level, therefore, groups firms by the product they specialize in, the level at which exposure is correlated.

Table A.2: Copper: Global Product Share and Firm Shares


Notes. This table highlights summary statistics for all copper products among 83 products we utilize. "Global product share" refers to the "Chilean share of global exports" for that product. "Median firm share" and "max firm share" refer to the "median Chilean firm's share of Chinese imports" and the "maximum Chilean firm's share of Chinese imports" for that product, respectively. These are calculated by interacting the export share of the Chilean firm with the median (or maximum, for max firm share) export value (to China) by Chile's total exports of that product to China, along with Chile's share of total Chinese imports from all countries for that product. This interaction effectively captures an individual Chilean firm's export share of China's total imports for a specific product. HS code is a 6-digit code based on 2002.

## A.3 Market Shares: Copper Exporters

Further reinforcing this limited market power at the firm level, Table A.2 presents data for key commodity products like copper. While copper is often perceived as Chile-driven and its importance grew in later periods, our analysis focuses specifically on the year 2003 and employs highly disaggregated product-level data. These factors combined reveal that even for these significant products, individual firm influence remains constrained.

For these copper products, while some exhibit high “global product share” (e.g., ‘Copper: refined, cathodes’ at 0.39; ‘Copper ores and concentrates’ at 0.37), their corresponding “median firm share” in China’s imports remains remarkably low (e.g., 0.01 for both). While the “max firm share” for these high global product share categories can be notable (e.g., 0.20 for ‘Copper: refined, cathodes’ and 0.11 for ‘Copper ores and concentrates’), these figures represent the absolute largest single firm’s presence and still suggest that even the most dominant firm in a given product in 2003 did not command an overwhelming share of the total market, especially when considering the global scope of these products. Conversely, for products where “median firm share" or "max firm share" shows a slightly higher value (e.g., 'Copper: copper mattes' at 0.21 for both), their "global product share" is very small (0.02). This consistent pattern of either a relatively low firm share (median or max) for globally significant products, or a high firm share only in globally minor products, is fundamental to arguing for the plausibility of our instrument's exogeneity. This low overall magnitude, particularly the limited extent to which even the largest individual firms dominate major product markets, suggests that the instrument's variation is unlikely to be systematically driven by individual firm outcomes or unobserved firm-specific factors that could confound our estimates, thereby supporting the argument that firms were not very large in a given product in 2003.

## A.4 Excluding Copper Sectors

Table A.3: Commodity Price Shocks and Firm-Level Outcomes, excluding Copper Sectors


Notes. This table reports the results from Equation (1). The dependent variables are the DHS growth rates of employees, materials expenditure, and domestic sales, respectively. All regressions control for 2-digit industry fixed effects, and standard errors are clustered at the 4-digit industry level. Regressions are weighted by total sales. F-statistics are reported for the first stage of the IV regressions.

## A.5 Alternative Measures of Productivity

As a robustness check, we estimate firm-level productivity using the control function approach of Ackerberg et al. (2015). This method addresses the endogeneity of input choices by using intermediate inputs (materials) as a proxy for unobserved productivity shocks. The approach employs a two-step GMM estimator. In the first stage, the unobserved productivity process is nonparametrically estimated using materials as a proxy, recovering expected productivity conditional on observables. In the second stage, moment conditions are formed based on timing assumptions about input choices: capital is determined one period in advance (and thus uncorrelated with productivity innovations), while labor and materials respond contemporaneously to productivity shocks. These moment conditions identify the production function coefficients via GMM.

We implement this approach using four different specifications, which vary along two dimensions: the output concept (gross output versus value added) and the functional form (Cobb-Douglas versus translog). First, in the gross output specifications (Columns 1-2), we estimate production functions with capital, labor, and materials as inputs, using both Cobb-Douglas and translog functional forms. Second, in the value-added specifications (Columns 3-4), following De Loecker and Scott (2025), we model gross output as a Leontief function of value added and materials, where value added is produced using capital and labor. This avoids the identification problem highlighted by Gandhi et al. (2020), whereby the scale of production and productivity cannot be separately identified in gross output specifications without additional assumptions. Consequently, this approach does not require imposing returns to scale assumptions ex ante.

Table A.4 presents the results. Across all four specifications, we find no significant effect of commodity price shocks on firm-level productivity, consistent with our baseline estimates in Table 3.

Table A.4: Commodity Price Shocks and Firm-Level Productivity


Notes. This table reports the results from Equation (1). The dependent variables are firm-level TFPR (Ackerberg et al., 2015; De Loecker and Scott, 2025). All regressions control for 2-digit industry fixed effects, and standard errors are clustered at the 4-digit industry level. F-statistics are reported for the first stage of the IV regressions.

## Appendix B Theoretical Appendix

## B.1 Foreign Household Problem (Global Consumer)

The foreign household (or global aggregate demand sector) aims to maximize its utility from consuming a composite good $C^{x}$ , the only good imported from the domestic economy.

The preferences for these differentiated varieties exported by individual firms i are CES, with an elasticity of substitution $\xi > 1^{23}$ :

$$
C ^ {x} = \left(\sum_ {i} \phi_ {i} ^ {\frac {1}{\xi}} (c _ {i} ^ {x}) ^ {\frac {\xi - 1}{\xi}}\right) ^ {\frac {\xi}{\xi - 1}}
$$

The associated price index for this aggregate of commodities is:

$$
P ^ {F} = \left(\sum_ {i} \phi_ {i} (p _ {i} ^ {x}) ^ {1 - \xi}\right) ^ {\frac {1}{1 - \xi}}
$$

From the cost minimization problem to achieve a given level of $C^{x}$ , the demand for an individual firm i's exported variety, $c_{i}^{x}$ , is derived as:

$$
c _ {i} ^ {x} = \frac {\phi_ {i} (p _ {i} ^ {x}) ^ {- \xi}}{(P ^ {F}) ^ {- \xi}} C ^ {x}.\tag{15}
$$

We define $D_{i}^{F} := \frac{\phi_{i} C^{x}}{(P^{F})^{-\xi}}$ as an exogenous export demand shifter.

## B.2 Multi-Product Extension and Bartik Microfoundation

The previous section considered $C^{x}$ as a single aggregate of all firm varieties. We now introduce a multi-product firm structure by defining $C^{x}$ as a nested aggregate where varieties are grouped by product j, which provides the microfoundation for the firm-specific Bartik instrument used in our empirical analysis.

## Two-Tier Demand Structure and Variety-Level Demand

Outer Nest: Aggregation Across Products. The final aggregate good $C^{x}$ is aggregated from distinct products $j \in J$ using a Cobb-Douglas structure with product-specific expenditure

shares $\alpha_{j}$ , where $\sum_{j\in \mathcal{J}}\alpha_{j} = 1$ :

$$
C ^ {x} = \prod_ {j \in \mathcal {J}} (C _ {j} ^ {x}) ^ {\alpha_ {j}}.
$$

If $E^{F}$ denotes the total expenditure and $P_{j}^{F}$ is the price index for product j, then from expenditure minimization, the demand for product aggregate j is:

$$
C _ {j} ^ {x} = \frac {\alpha_ {j} E ^ {F}}{P _ {j} ^ {F}}.\tag{16}
$$

Inner Nest: Aggregation Within Products. Each product-level composite good $C_{j}^{x}$ is a CES aggregate of firm i's varieties $y_{ij}^{x}$ within that product, with elasticity of substitution $\xi > 1$ :

$$
C _ {j} ^ {x} = \left(\sum_ {i} \left(\phi_ {i}\right) ^ {\frac {1}{\xi}} \left(y _ {i j} ^ {x}\right) ^ {\frac {\xi - 1}{\xi}}\right) ^ {\frac {\xi}{\xi - 1}}.
$$

From cost minimization, the demand for firm $i$ 's variety of product $j$ is:

$$
y _ {i j} ^ {x} = \phi_ {i} \left(\frac {p _ {i j} ^ {x}}{P _ {j} ^ {F}}\right) ^ {- \xi} C _ {j} ^ {x}.
$$

Substituting Equation (16) yields:

$$
y _ {i j} ^ {x} = \phi_ {i} (p _ {i j} ^ {x}) ^ {- \xi} \alpha_ {j} (P _ {j} ^ {F}) ^ {\xi - 1} E ^ {F}.\tag{17}
$$

## Derivation of the Bartik Instrument

Firm $i$ 's export revenue from product $j$ is $R_{ij}^{x} = p_{ij}^{x}y_{ij}^{x} = \phi_{i}(p_{ij}^{x})^{1 - \xi}\alpha_{j}(P_{j}^{F})^{\xi -1}E^{F}$ . Taking logs and differencing:

$$
\Delta \log R _ {i j} ^ {x} = \Delta \log \phi_ {i} + (1 - \xi) \Delta \log p _ {i j} ^ {x} + \Delta \log \alpha_ {j} + (\xi - 1) \Delta \log P _ {j} ^ {F} + \Delta \log E ^ {F}.
$$

Let $\omega_{ij,0} \equiv \frac{R_{ij,0}^x}{R_{i,0}^x}$ denote the initial revenue share of product $j$ in firm $i$ 's total export revenue. Since total revenue is $R_i^x = \sum_{j \in \mathcal{J}_i} R_{ij}^x$ , taking the total differential and dividing by initial revenue yields the log change in firm $i$ 's total export revenue:

$$
\Delta \log R _ {i} ^ {x} = \sum_ {j \in \mathcal {J} _ {i}} \omega_ {i j, 0} \Delta \log R _ {i j} ^ {x}.
$$

Substituting and using $\sum_{j\in \mathcal{J}_i}\omega_{ij,0} = 1$ :

$$
\Delta \log R _ {i} ^ {x} = (\xi - 1) \sum_ {j \in \mathcal {J} _ {i}} \omega_ {i j, 0} \Delta \log P _ {j} ^ {F} + \Xi_ {i},\tag{18}
$$

where

$$
\Xi_ {i} := \Delta \log \phi_ {i} + (1 - \xi) \sum_ {j \in \mathcal {J} _ {i}} \omega_ {i j, 0} \Delta \log p _ {i j} ^ {x} + \sum_ {j \in \mathcal {J} _ {i}} \omega_ {i j, 0} \Delta \log \alpha_ {j} + \Delta \log E ^ {F}
$$

captures firm-specific productivity changes and pricing decisions, as well as aggregate demand components. The aggregate components (common across all firms) are absorbed by the regression intercept, while the firm-specific components are orthogonal to the exogenous product-level price variation by construction.

The firm-specific Bartik shock is therefore defined as:

$$
\mathrm{BartikShock} _ {i} \equiv \Delta \log {\bf P} _ {i} ^ {F} := \sum_ {j \in \mathcal {J} _ {i}} \omega_ {i j, 0} \Delta \log P _ {j} ^ {F},\tag{19}
$$

where $\Delta \log P_j^F$ is measured using Chinese import prices from countries other than Chile (IV specification) or Chilean export prices to China (OLS specification). This instrument isolates each firm's exposure to exogenous commodity price movements through its predetermined product portfolio, with variation across firms arising from differential price changes across products weighted by heterogeneous initial product shares.

The theoretical coefficient on the Bartik shock in Equation (18) is $(\xi - 1)$ , where $\xi$ represents the elasticity of substitution among firm varieties within a product category. Our empirical IV estimate of 0.767 is consistent with $\xi \approx 1.77$ , indicating that firm varieties within the same commodity product are substitutable—an economically plausible pattern for commodity exports.

## B.3 Derivation of TFPR Expressions

This appendix provides the complete derivation of firm-level and sectoral TFPR expressions used in Section 6.2.

## B.3.1 Firm-Level Input Demands

Starting from the first-order condition for labor (Equation (9) in the main text):

$$
\frac {\gamma^ {L} p _ {i j} ^ {H} y _ {i j}}{\mu l _ {i j}} = \left(1 + \frac {1}{\epsilon_ {i j} ^ {L}}\right) w _ {i j},\tag{20}
$$

we rearrange to obtain the labor demand function:

$$
l _ {i j} = \frac {p _ {i j} ^ {H} y _ {i j}}{\mu \mu_ {i j} ^ {L} w _ {i j}} = \frac {p _ {i j} ^ {H} y _ {i j}}{\mu \mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{\eta + 1}} W _ {j}} = \frac {\gamma^ {L} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu \mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{\eta + 1}} W _ {j}},\tag{21}
$$

where the second equality uses the fact that the labor supply curve $l_{ij} = \left(\frac{w_{ij}}{W_j}\right)^\eta L_j$ implies $\left(\frac{w_{ij}}{W_j}\right)^{\eta + 1} = s_{ij}^L$ , with $s_{ij}^L = \frac{w_{ij}l_{ij}}{W_jL_j}$ denoting the firm's wage bill share. The third equality uses $r_{ij} = p_{ij}^F y_{ij}^F + p_{ij}^H y_{ij}^H$ as total revenue, $s_{ij}^F = \frac{p_{ij}^F y_{ij}^F}{r_{ij}}$ as export share, and the pricing equations to show that:

$$
p _ {i j} ^ {H} y _ {i j} ^ {H} = p _ {i j} ^ {H} (y _ {i j} - y _ {i j} ^ {F}) = p _ {i j} ^ {H} y _ {i j} - p _ {i j} ^ {F} y _ {i j} ^ {F} \frac {p _ {i j} ^ {H}}{p _ {i j} ^ {F}} = r _ {i j} \left(1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}\right),
$$

using $p_{ij}^{F} = \frac{1}{1 - \tau_{ij}^{F}} p_{ij}^{H}$ from Equation (8).

Similarly, first-order conditions for capital and materials yield:

$$
k _ {i j} = \frac {\gamma^ {K} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu R},\tag{22}
$$

$$
m _ {i j} = \frac {\gamma^ {M} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu P ^ {M}}.\tag{23}
$$

## B.3.2 Firm-Level TFPR

Substituting the input demand functions (21)-(23) into the TFPR definition (Equation (11)):

$$
\begin{array}{r l} & {\mathrm{tfpr} _ {i j} = \frac {r _ {i j}}{l _ {i j} ^ {\gamma^ {L}} k _ {i j} ^ {\gamma^ {K}} m _ {i j} ^ {\gamma^ {M}}}} \\ & {\quad = \frac {r _ {i j}}{\left(\frac {\gamma^ {L} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu \mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{\eta + 1}} W _ {j}}\right) ^ {\gamma^ {L}} \left(\frac {\gamma^ {K} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu R}\right) ^ {\gamma^ {K}} \left(\frac {\gamma^ {M} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu P ^ {M}}\right) ^ {\gamma^ {M}}}} \\ & {\quad = \frac {r _ {i j}}{r _ {i j} ^ {\gamma^ {L} + \gamma^ {K} + \gamma^ {M}}} \cdot \frac {\mu^ {\gamma^ {L} + \gamma^ {K} + \gamma^ {M}}}{(1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) ^ {\gamma^ {L} + \gamma^ {K} + \gamma^ {M}}} \cdot \frac {\left(\mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{\eta + 1}} W _ {j}\right) ^ {\gamma^ {L}} R ^ {\gamma^ {K}} (P ^ {M}) ^ {\gamma^ {M}}}{(\gamma^ {L}) ^ {\gamma^ {L}} (\gamma^ {K}) ^ {\gamma^ {K}} (\gamma^ {M}) ^ {\gamma^ {M}}}.} \end{array}
$$

Imposing constant returns to scale $(\gamma^{L} + \gamma^{K} + \gamma^{M} = 1)$ , this simplifies to Equation (12):

$$
\mathrm{tfpr} _ {i j} = \frac {\mu}{1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}} \left(\frac {\mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{1 + \eta}} W _ {j}}{\gamma^ {L}}\right) ^ {\gamma^ {L}} \left(\frac {R}{\gamma^ {K}}\right) ^ {\gamma^ {K}} \left(\frac {P ^ {M}}{\gamma^ {M}}\right) ^ {\gamma^ {M}}.
$$

## B.3.3 Sectoral Aggregates

To derive sectoral TFPR, we first aggregate inputs across firms. Using the CES labor aggregator:

$$
\begin{array}{l} L _ {j} = \left(\sum_ {i \in \mathcal {F} _ {j}} l _ {i j} ^ {\frac {\eta + 1}{\eta}}\right) ^ {\frac {\eta}{\eta + 1}} \\ = \left(\sum_ {i \in \mathcal {F} _ {j}} \left(\frac {\gamma^ {L} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}) r _ {i j}}{\mu \mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{\eta + 1}} W _ {j}}\right) ^ {\frac {\eta + 1}{\eta}}\right) ^ {\frac {\eta}{\eta + 1}} \\ = \left(\sum_ {i \in \mathcal {F} _ {j}} \left(\gamma^ {L} \frac {\mathcal {S} _ {i j} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F})}{\mu \mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {\frac {1}{\eta + 1}} W _ {j}} \mathcal {R} _ {j}\right) ^ {\frac {\eta + 1}{\eta}}\right) ^ {\frac {\eta}{\eta + 1}}, \end{array}
$$

where $S_{ij} = \frac{r_{ij}}{R_j}$ denotes firm i's market share and $R_j = \sum_{i \in F_j} r_{ij}$ is total sectoral revenue.

For capital and materials (non-CES aggregation):

$$
\begin{array}{l} K _ {j} = \sum_ {i \in \mathcal {F} _ {j}} k _ {i j} = \sum_ {i \in \mathcal {F} _ {j}} \gamma^ {K} \frac {\mathcal {S} _ {i j} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F})}{\mu R} \mathcal {R} _ {j}, \\ M _ {j} = \sum_ {i \in \mathcal {F} _ {j}} m _ {i j} = \sum_ {i \in \mathcal {F} _ {j}} \gamma^ {M} \frac {\mathcal {S} _ {i j} (1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F})}{\mu P ^ {M}} \mathcal {R} _ {j}. \end{array}
$$

Sectoral TFPR is defined as:

$$
\mathrm{TFPR} _ {j} \equiv \frac {\mathcal {R} _ {j}}{L _ {j} ^ {\gamma^ {L}} K _ {j} ^ {\gamma^ {K}} M _ {j} ^ {\gamma^ {M}}}.
$$

Substituting the aggregates and simplifying yields:

$$
\mathrm{TFPR} _ {j} = \frac {\mu \left(\frac {W _ {j}}{\gamma^ {L}}\right) ^ {\gamma^ {L}} \left(\frac {R}{\gamma^ {K}}\right) ^ {\gamma^ {K}} \left(\frac {P ^ {M}}{\gamma^ {M}}\right) ^ {\gamma^ {M}}}{\left(\sum_ {i} \left(\frac {\mathcal {S} _ {i j} \left(1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}\right)}{\mu_ {i j} ^ {L} s _ {i j} ^ {L ^ {1 / (\eta + 1)}}}\right) ^ {\frac {\eta + 1}{\eta}}\right) ^ {\frac {\eta \gamma^ {L}}{\eta + 1}} \left(\sum_ {i} \mathcal {S} _ {i j} \left(1 - \tau_ {i j} ^ {F} s _ {i j} ^ {F}\right)\right) ^ {\gamma^ {K} + \gamma^ {M}}}.
$$

## B.3.4 Sectoral Productivity

Finally, sectoral productivity is defined as TFPR deflated by the sectoral price index:

$$
A _ {j} \equiv \frac {\mathrm{TFPR} _ {j}}{\mathrm{PPI} _ {j}},
$$

where the sectoral price index is:

$$
\mathrm{PPI} _ {j} = \left(\sum_ {i \in \mathcal {F} _ {j}} \tilde {p} _ {i j} ^ {1 - \sigma}\right) ^ {\frac {1}{1 - \sigma}},
$$

and $\tilde{p}_{ij} = p_{ij}^{H}\frac{y_{ij}^{H}}{y_{ij}} +p_{ij}^{F}\frac{y_{ij}^{F}}{y_{ij}}$ is the firm's average price across domestic and export sales.

Using the production function $y_{ij} = a_{ij} l_{ij}^{\gamma^{L}} k_{ij}^{\gamma^{K}} m_{ij}^{\gamma^{M}}$ and the definition of TFPR, we have:

$$
\tilde {p} _ {i j} = \frac {r _ {i j}}{y _ {i j}} = \frac {\mathrm{tfpr} _ {i j}}{a _ {i j}}.
$$

Substituting into the productivity definition:

$$
\begin{array}{l} A _ {j} = \mathrm{TFPR} _ {j} \left(\sum_ {i \in \mathcal {F} _ {j}} \left(\frac {\mathrm{tfpr} _ {i j}}{a _ {i j}}\right) ^ {1 - \sigma}\right) ^ {\frac {- 1}{1 - \sigma}} \\ = \mathrm{TFPR} _ {j} \left(\sum_ {i \in \mathcal {F} _ {j}} a _ {i j} ^ {\sigma - 1} \left(\mathrm{tfpr} _ {i j}\right) ^ {1 - \sigma}\right) ^ {\frac {- 1}{1 - \sigma}} \\ = \left(\sum_ {i \in \mathcal {F} _ {j}} \left(a _ {i j} \frac {\mathrm{TFPR} _ {j}}{\mathrm{tfpr} _ {i j}}\right) ^ {\sigma - 1}\right) ^ {\frac {1}{\sigma - 1}}, \end{array}
$$

which is Equation (13) in the main text. This expression shows that sectoral productivity depends on the distribution of firms' physical productivity ( $a_{ij}$ ) weighted by the inverse of their TFPR distortions. Greater dispersion in $tfpr_{ij}$ across firms—holding constant the distribution of $a_{ij}$ —reduces aggregate $A_{j}$ , representing the efficiency loss from misallocation.

## B.4 Firm-Level DRS and Measured TFP

This section formalizes why firm-level decreasing returns to scale (DRS) would appear as declining measured TFP under our constant returns to scale (CRS) measurement assumption.

## B.4.1 Setup

Suppose the true firm-level production function exhibits DRS:

$$
Y _ {i} = A _ {i} \cdot L _ {i} ^ {\alpha} \cdot K _ {i} ^ {\beta} \cdot M _ {i} ^ {\gamma}\tag{24}
$$

where $\alpha +\beta +\gamma <  1$

We measure TFP assuming CRS, using factor shares $s_{L}$ , $s_{K}$ , and $s_{M}$ that sum to one $(s_{L} + s_{K} + s_{M} = 1)$ :

$$
\widehat {\log T F P} _ {i} = \log Y _ {i} - s _ {L} \log L _ {i} - s _ {K} \log K _ {i} - s _ {M} \log M _ {i}\tag{25}
$$

## B.4.2 Scaling Up Inputs

Consider a firm that scales up all inputs by factor $\lambda > 1$ :

$$
L _ {i} ^ {\prime} = \lambda L _ {i}, \quad K _ {i} ^ {\prime} = \lambda K _ {i}, \quad M _ {i} ^ {\prime} = \lambda M _ {i}\tag{26}
$$

Under DRS, true output scales as:

$$
\begin{array}{c} Y _ {i} ^ {\prime} = A _ {i} \cdot (\lambda L _ {i}) ^ {\alpha} \cdot (\lambda K _ {i}) ^ {\beta} \cdot (\lambda M _ {i}) ^ {\gamma} \\ = \lambda^ {(\alpha + \beta + \gamma)} \cdot Y _ {i} \end{array}\tag{27}
$$

Since $\alpha + \beta + \gamma < 1$ , output grows less than proportionally: $Y_{i}^{\prime} < \lambda \cdot Y_{i}$ .

## B.4.3 Measured TFP After Expansion

The measured TFP for the scaled-up firm is:

$$
\log \widehat {T F P} _ {i} ^ {\prime} = \log Y _ {i} ^ {\prime} - s _ {L} \log L _ {i} ^ {\prime} - s _ {K} \log K _ {i} ^ {\prime} - s _ {M} \log M _ {i} ^ {\prime}\tag{28}
$$

Substituting the scaled inputs:

$$
\log \widehat {T F P} _ {i} ^ {\prime} = \log Y _ {i} ^ {\prime} - s _ {L} \log (\lambda L _ {i}) - s _ {K} \log (\lambda K _ {i}) - s _ {M} \log (\lambda M _ {i})\tag{29}
$$

Using logarithm properties and $s_{L} + s_{K} + s_{M} = 1$ :

$$
\log \widehat {T F P} _ {i} ^ {\prime} = \log Y _ {i} ^ {\prime} - \log \lambda - (s _ {L} \log L _ {i} + s _ {K} \log K _ {i} + s _ {M} \log M _ {i})\tag{30}
$$

Substituting $Y_{i}^{\prime} = \lambda^{(\alpha +\beta +\gamma)}\cdot Y_{i}$ :

$$
\begin{array}{c} \log \widehat {T F P} _ {i} ^ {\prime} = \log (\lambda^ {(\alpha + \beta + \gamma)} \cdot Y _ {i}) - \log \lambda - (s _ {L} \log L _ {i} + s _ {K} \log K _ {i} + s _ {M} \log M _ {i}) \\ = \log \widehat {T F P} _ {i} + [ (\alpha + \beta + \gamma) - 1 ] \log \lambda \end{array}\tag{31}
$$

Since $\alpha + \beta + \gamma < 1$ under DRS, we have $(\alpha + \beta + \gamma) - 1 < 0$ . Therefore, for expanding firms $(\lambda > 1)$ :

$$
\log \widehat {T F P} _ {i} ^ {\prime} <   \log \widehat {T F P} _ {i}\tag{32}
$$

This demonstrates that under firm-level DRS, expanding firms would exhibit declining measured TFP when we impose CRS in measurement.

## B.4.4 Empirical Implication

This derivation shows that if firm-level DRS exists, expanding firms would exhibit declining measured TFP under our baseline CRS measurement assumption. Specifically, a firm scaling up all inputs by factor $\lambda > 1$ would experience a decline in measured TFP proportional to $(\alpha + \beta + \gamma - 1) \log \lambda$ , where $\alpha + \beta + \gamma < 1$ under DRS. As discussed in the main text, our empirical findings are robust across multiple specifications that do not impose CRS ex ante, suggesting firm-level DRS is not the primary explanation for the patterns we observe.

## Appendix C The Export Wedge

The export wedge $\tau_{ij}^{F}$ enters our model in reduced form: it captures the gap between gross and net export revenue without committing to a single source. This appendix presents three analyses. First, it presents three microfoundations under which the same firm-level conditions and aggregate mechanism arise. Second, it measures a concrete, statutory component of the wedge directly from administrative data (C.2) using product-level subsidies and restrictions. Lastly, it shows that firms with a more favorable wedge expand exports disproportionately when the commodity shock arrives, the sign the misallocation mechanism predicts (C.3).

## C.1 Microfoundations of the Export Wedge

This section closes the model by giving three microfoundations for $\tau_{ij}^{F}$ , each specifying both the source of the wedge and the corresponding flow of resources back to households.

The first two microfoundations are motivated by features of Chile's commodity sector that generate firm-specific gaps between gross and net export revenue, with the wedge orthogonal to underlying productivity. The first microfoundation maps onto policy-induced advantages that effectively raise the per-unit return on exports for some firms relative to others, including stable tax treatment for foreign investors under Decree Law 600, long-term mining concessions held by incumbent firms, and differential access to export financing and promotion services. The second microfoundation captures heterogeneity in firms' access to foreign markets through intermediaries: some firms reach foreign buyers directly while others rely on intermediaries who absorb part of the export margin, generating cross-firm dispersion in net-of-intermediation export revenue. Both yield identical firm first-order conditions, and the calibration target—the variance of export shares across firms—identifies the dispersion of $\tau_{ij}^{F}$ .

The third microfoundation derives the export wedge from endogenous markup heterogeneity in the export market under oligopolistic competition (Atkeson and Burstein, 2008). It generates the same firm-level first-order conditions and a qualitatively similar aggregate misallocation mechanism as the first two, but $\tau_{ij}^{F}$ is endogenously increasing in firm productivity rather than orthogonal to it, with different cross-sectional implications that fit the Chilean data less well—in particular, it predicts a positive TFPR-size gradient, whereas the empirical correlation is zero to weakly negative (C.1.3). Our quantitative analysis in Section 6.4 retains the productivity-orthogonal formulation that better matches the cross-sectional moments in our setting.

## C.1.1 Policy-Induced Per-Unit Advantages

In this microfoundation, $\tau_{ij}^{F}$ represents an ad valorem policy wedge on export revenues, with negative values capturing the kinds of advantages already discussed in Section 6.1—DL600 tariff exemptions, preferential royalty rates under the mining concession system, or subsidized export financing through ProChile and CORFO. The four programs we measure in C.2—the Reintegro and Drawback rebates and the ITQ and aquaculture restrictions—are the explicit, quantifiable instances of this policy wedge; the advantages just listed (DL600 stability, concession rates, promotion financing) are additional but largely implicit instances that we do not measure, which is why the measured wedge is a lower bound. The firm’s profit-maximization problem coincides with that of Section 6.1, and pricing rules, input demands, and firm-level TFPR expressions are unchanged. What this microfoundation adds is a specification of how the aggregate residual revenue is mapped back to the household budget. The government balances its budget by rebating net policy revenue lump-sum to households, so that the transfer in the household budget constraint takes the form

$$
T = \sum_ {j} \sum_ {i \in \mathcal {F} _ {j}} \tau_ {i j} ^ {F} p _ {i j} ^ {F} y _ {i j} ^ {F}.\tag{33}
$$

Under GHH preferences, $T$ does not affect the household's labor supply decision, and the aggregate equilibrium coincides with the baseline.

## C.1.2 Heterogeneous Intermediary Access

In this microfoundation, $\tau_{ij}^{F}$ arises endogenously from firms' use of domestic export intermediaries, where firms differ in the share of their output for which direct foreign market access is institutionally available. $^{24}$ When firms lack such access, they sell to intermediaries who in turn export the products abroad. The microfoundation accommodates a natural interpretation of the baseline model in which the “domestic” market includes firms' sales to intermediaries alongside direct domestic consumption, with intermediated output recorded as domestic sales in firm tax records and direct exports recorded as export revenue in the same records. Cross-firm variation in intermediary reliance arises from a multi-product structure already implicit in our empirical strategy, with product-specific institutional access aggregated across each firm's portfolio rather than firm-wide differences in capability. $^{25}$

Setup. Each firm i in sector j produces a portfolio of products $P_{ij}$ , with foreign-bound output $y_{ijp}^{F}$ for each product $p \in P_{ij}$ . $^{26}$ Each product is classified by its access type. For accessible products ( $p \in P_{ij}^{A}$ ), the firm has the institutional standing to export directly at the foreign price $p_{ijp}^{F}$ . For intermediated products ( $p \in P_{ij}^{I}$ ), the firm lacks such access and channels exports through a domestic intermediary, who purchases the product domestically and resells it abroad. The partition $\{P_{ij}^{A}, P_{ij}^{I}\}$ is firm-product-specific and reflects accumulated institutional access. We treat this partition as exogenous and orthogonal to the firm's underlying productivity $a_{ij}$ . $^{27}$

We define the firm-level direct access fraction as the share of foreign-bound revenue from accessible products:

$$
\eta_ {i j} \equiv \frac {\sum_ {p \in \mathcal {P} _ {i j} ^ {A}} p _ {i j p} ^ {F} y _ {i j p} ^ {F}}{\sum_ {p \in \mathcal {P} _ {i j}} p _ {i j p} ^ {F} y _ {i j p} ^ {F}} \in [ 0, 1 ].\tag{34}
$$

Cross-firm variation in $\eta_{ij}$ arises from differences in product portfolios and from product-level differences in institutional access. The product-level structure is what makes this heterogeneity exogenous to firm productivity: whether firm $i$ has the institutional standing to reach foreign buyers for a specific product $p$ is a firm-product-specific historical fact rather than an attribute of the firm's productive efficiency. Firms with $\eta_{ij}$ close to one have direct access for most of their foreign-bound output; firms with $\eta_{ij}$ close to zero rely predominantly on intermediaries. The shift-share exposure measure used in our empirical strategy inherits its identifying variation from precisely this product-level heterogeneity, with a firm exposed to the commodity boom through products in $\mathcal{P}_{ij}^{A}$ realizing the price increase as direct export revenue, while a firm whose exposed products fall in $\mathcal{P}_{ij}^{I}$ sees the same price increase absorbed largely as intermediary markdown.

Intermediary Problem. For each intermediated product $p \in P_{ij}^{I}$ , the firm and a domestic intermediary engage in bilateral bargaining over the surplus from exporting that product. The intermediary, if successful in obtaining the product, can sell it abroad at the foreign price $p_{ijp}^{F}$ . The firm cannot directly export this product (by definition of $P_{ij}^{I}$ ), so the foreign-bound unit yields zero revenue absent intermediation, and the total surplus per unit available to the firm-intermediary pair is $p_{ijp}^{F}$ . $^{28}$ We assume Nash bargaining with firm bargaining weight $\beta \in (0,1)$ and intermediary weight $1 - \beta$ , both common across firm-intermediary pairs. The bargaining outcome assigns $\beta p_{ijp}^{F}$ to the firm and $(1 - \beta)p_{ijp}^{F}$ to the intermediary. The intermediary's retained share represents the markdown extracted from each unit of intermediated export, and we define the common markdown rate as $\delta \equiv 1 - \beta$ , so that the firm receives $(1 - \delta)p_{ijp}^{F}$ for each unit of intermediated foreign-bound output.

Aggregate Firm Revenue and the Export Wedge. At the firm level, foreign-bound output combines accessible and intermediated products. Let $R_{ij}^{F} \equiv \sum_{p \in P_{ij}} p_{ijp}^{F} y_{ijp}^{F}$ denote total foreign-bound output value evaluated at foreign prices. The firm retains the full foreign price on accessible products and the post-markdown share on intermediated products, so its total revenue from foreign-bound output is

$$
\begin{array}{r l} & {\sum_ {p \in \mathcal {P} _ {i j} ^ {A}} p _ {i j p} ^ {F} y _ {i j p} ^ {F} + \sum_ {p \in \mathcal {P} _ {i j} ^ {I}} (1 - \delta) p _ {i j p} ^ {F} y _ {i j p} ^ {F} = \eta_ {i j} R _ {i j} ^ {F} + (1 - \eta_ {i j}) (1 - \delta) R _ {i j} ^ {F}} \\ & {\qquad = [ 1 - (1 - \eta_ {i j}) \delta ] R _ {i j} ^ {F}.} \end{array}\tag{35}
$$

Mapping to the baseline, where the firm's revenue from foreign-bound output is $(1 - \tau_{ij}^{F})p_{ij}^{F}y_{ij}^{F}$ with $p_{ij}^{F}y_{ij}^{F} = R_{ij}^{F}$ at the firm aggregate, we obtain

$$
\tau_ {i j} ^ {F} = (1 - \eta_ {i j}) \delta \in [ 0, \delta ].\tag{36}
$$

Firms with high direct access $(\eta_{ij} \rightarrow 1)$ face $\tau_{ij}^{F} \rightarrow 0$ , while firms heavily reliant on intermediation $(\eta_{ij} \rightarrow 0)$ face $\tau_{ij}^{F} \rightarrow \delta$ . $^{29}$ The firm's profit-maximization problem coincides with that of Section 6.1 once $\tau_{ij}^{F}$ is defined by Equation (36), and pricing rules, input demands, and firm-level TFPR expressions are identical to the baseline.

Empirical Alignment and Closure. A central feature of this microfoundation is that intermediated foreign-bound output appears as domestic sales in the firm's tax records, since the intermediary acquires the product within Chile before reselling abroad. Cross-firm dispersion in $\eta_{ij}$ therefore generates dispersion in observed export shares—measured as the ratio of reported exports to total sales in firm tax records—consistent with the calibration target used in Section 6.4. Because $\eta_{ij}$ reflects institutional access factors orthogonal to underlying productivity, the framework accommodates cases in which less productive but well-positioned firms expand more strongly in response to a positive demand shock than highly productive firms whose institutional access is limited—reproducing the differential sensitivity of low-TFPR firms documented in Section 5. Intermediaries are domestic agents owned by the representative household, and their aggregate profits

$$
\Pi^ {I} = \sum_ {j} \sum_ {i \in \mathcal {F} _ {j}} (1 - \eta_ {i j}) \delta R _ {i j} ^ {F} = \sum_ {j} \sum_ {i \in \mathcal {F} _ {j}} \tau_ {i j} ^ {F} R _ {i j} ^ {F}\tag{37}
$$

are absorbed in the aggregate profit term $\Pi$ in the household's budget constraint. Under GHH preferences, the redistribution does not affect labor supply, and the aggregate equilibrium structure coincides with the baseline.

Why static heterogeneity rather than search and matching. A natural alternative microfoundation for differential intermediary access is a search-and-matching model in which firms and intermediaries match endogenously. We adopt the static heterogeneity formulation in $\eta_{ij}$ rather than such a model because standard search-and-matching frameworks generate efficiency sorting: more productive firms generate larger match surpluses and therefore secure better intermediary access in equilibrium, so $\eta_{ij}$ becomes positively correlated with underlying productivity $a_{ij}$ . Under this alternative, low-TFPR firms would no longer be the firms with favorable export access, and TFPR dispersion would reflect productivity dispersion rather than wedge dispersion. The misallocation mechanism that drives the aggregate productivity decline in Section 6.4—in which less productive but export-favored firms expand at the expense of more productive competitors—would disappear, and the framework would predict an aggregate productivity increase during the commodity boom rather than the empirical decline documented in Figure 1. The static formulation in $\eta_{ij}$ preserves the productivity-orthogonal heterogeneity that is essential for matching the empirical pattern, treating $\eta_{ij}$ as the equilibrium outcome of an underlying access process whose details are not material for the cross-sectional misallocation we identify.

## C.1.3 Variable Markup in the Export Market

In this microfoundation, $\tau_{ij}^{F}$ arises from endogenous markup heterogeneity in the export market under oligopolistic competition (Atkeson and Burstein, 2008).

Setup. Within each sector $j$ , firms face Cournot competition in the export market, internalizing their effect on the sector-level foreign price index. The within-sector elasticity $\sigma$ continues from the baseline, governing substitution across firms within a sector; we introduce a separate across-sector elasticity $\zeta$ governing substitution across sectors in foreign demand, with $\sigma > \zeta > 1$ . The firm-level export demand elasticity depends on the firm's within-sector world export share $s_{ij,W}^{F}$ :

$$
\epsilon_ {i j} ^ {F} = \sigma - (\sigma - \zeta) s _ {i j, W} ^ {F},\tag{38}
$$

yielding firm-specific export markups $\mu_{ij}^{F}=\epsilon_{ij}^{F}/(\epsilon_{ij}^{F}-1)$ that are strictly increasing in $s_{ij,W}^{F}$ . Domestic prices remain $p_{ij}^{H}=\mu MC_{ij}$ with $\mu=\sigma/(\sigma-1)$ as in the baseline, while the export pricing rule becomes $p_{ij}^{F}=\mu_{ij}^{F}MC_{ij}$ .

Mapping to the Baseline Wedge. The firm-level TFPR derivation in Appendix B.3 carries through with the modified pricing rules. The only object that changes relative to the baseline expression in Equation (12) is the front markup term: where the baseline carries $\mu/(1 - \tau_{ij}^{F} s_{ij}^{F})$ , this microfoundation carries the harmonic average of domestic and export markups weighted by revenue shares,

$$
\bar {\mu} _ {i j} \equiv \left[ \frac {1 - s _ {i j} ^ {F}}{\mu} + \frac {s _ {i j} ^ {F}}{\mu_ {i j} ^ {F}} \right] ^ {- 1},\tag{39}
$$

which obtains by writing total revenue as $r_{ij} = \mu MC_{ij}y_{ij}^{H} + \mu_{ij}^{F}MC_{ij}y_{ij}^{F}$ and substituting $y_{ij}^{H} = (1 - s_{ij}^{F})r_{ij}/(\mu MC_{ij})$ and $y_{ij}^{F} = s_{ij}^{F}r_{ij}/(\mu_{ij}^{F}MC_{ij})$ . The resulting firm-level TFPR is

$$
\mathrm{tfpr} _ {i j} = \bar {\mu} _ {i j} \left(\frac {\mu_ {i j} ^ {L} (s _ {i j} ^ {L}) ^ {1 / (1 + \eta)} W _ {j}}{\gamma^ {L}}\right) ^ {\gamma^ {L}} \left(\frac {R}{\gamma^ {K}}\right) ^ {\gamma^ {K}} \left(\frac {P ^ {M}}{\gamma^ {M}}\right) ^ {\gamma^ {M}},\tag{40}
$$

where the labor markdown $\mu_{ij}^{L}$ and the factor cost terms in capital and materials are unchanged from the baseline. The two formulations map onto each other under the substitution $\mu/(1-\tau_{ij}^{F}s_{ij}^{F})=\bar{\mu}_{ij}$ , which simplifies to

$$
\tau_ {i j} ^ {F} s _ {i j} ^ {F} = \left(1 - \frac {\mu}{\mu_ {i j} ^ {F}}\right) s _ {i j} ^ {F}.\tag{41}
$$

A firm with above-average export markup $(\mu_{ij}^{F} > \mu)$ maps onto a positive effective wedge $(\tau_{ij}^{F} > 0)$ , while a firm at the competitive limit $(\mu_{ij}^{F} \to \mu)$ maps onto $\tau_{ij}^{F} = 0$ . The export wedge term $\tau_{ij}^{F}s_{ij}^{F}$ in the baseline TFPR decomposition (Equation (12)) is replaced by $(1 - \mu/\mu_{ij}^{F})s_{ij}^{F}$ , with cross-firm dispersion in TFPR driven by dispersion in export markups weighted by export shares.

Sectoral productivity follows the Hsieh-Klenow aggregator in Equation (13) with $tfpr_{ij}$ now given by Equation (40). The microfoundation therefore generates a misallocation mechanism analogous to the policy and intermediary microfoundations of Sections C.1.1 and C.1.2, but with a different distortion source. Comparing each firm's export quantity to the frictionless benchmark $y_{ij}^{F,eff}$ obtained at the common markup $\mu$ , CES export demand implies

$$
\frac {y _ {i j} ^ {F}}{y _ {i j} ^ {F , \mathrm{eff}}} = \left(\frac {\mu_ {i j} ^ {F}}{\mu}\right) ^ {- \sigma},\tag{42}
$$

so that high-productivity firms with $\mu_{ij}^{F} > \mu$ under-produce relative to their productivity ( $y_{ij}^{F}/y_{ij}^{F,eff} < 1$ ), ceding scale to low-productivity firms with $\mu_{ij}^{F} \approx \mu$ that produce closer to the frictionless benchmark. A common positive export demand shock amplifies this dispersion through the heterogeneous demand elasticities in Equation (38): high-productivity firms face less elastic demand and widen markups further, while low-productivity firms face more elastic demand and absorb expansion through quantity, drawing resources toward the less productive segment of the sector and reducing $A_{j}$ .

Closure. The implied export wedge $\tau_{ij}^{F}=1-\mu/\mu_{ij}^{F}$ in this microfoundation generates extra revenue accruing to the firm relative to the competitive benchmark. These additional revenues enter aggregate firm profits

$$
\Pi^ {M} = \sum_ {j} \sum_ {i \in \mathcal {F} _ {j}} \tau_ {i j} ^ {F} R _ {i j} ^ {F} = \sum_ {j} \sum_ {i \in \mathcal {F} _ {j}} \left(1 - \frac {\mu}{\mu_ {i j} ^ {F}}\right) R _ {i j} ^ {F},\tag{43}
$$

which are absorbed in the household budget constraint as part of the aggregate profit term $\Pi$ . Under GHH preferences, $\Pi^{M}$ does not affect the household's labor supply decision, and the aggregate equilibrium structure coincides with the baseline.

Empirical Fit and Calibration. The cross-sectional relationship between TFPR and firm size differs sharply between this microfoundation and the productivity-orthogonal microfoundations of Sections C.1.1 and C.1.2. Using $s_{ij}^{L}$ as a size proxy and applying $-\log(1-\tau_{ij}^{F}s_{ij}^{F})\approx\tau_{ij}^{F}s_{ij}^{F}$ for small wedge dispersion, the cross-sectional gradient of log TFPR with respect to size takes the form

$$
\frac {\partial \log \mathrm{tfpr} _ {i j}}{\partial \log s _ {i j} ^ {L}} = \underbrace {\frac {\partial X _ {i j}}{\partial \log s _ {i j} ^ {L}}} _ {\text {distortion channel}} + \underbrace {\gamma^ {L} \frac {\partial \log \mu_ {i j} ^ {L}}{\partial \log s _ {i j} ^ {L}} + \frac {\gamma^ {L}}{1 + \eta}} _ {\text {labor markdown channel}},\tag{44}
$$

where $X_{ij} = \tau_{ij}^{F} s_{ij}^{F}$ in the policy and intermediary microfoundations and $X_{ij} = (1 - \mu / \mu_{ij}^{F}) s_{ij}^{F}$ here. The labor markdown channel is identical across microfoundations and strictly positive. The distortion channel, however, differs sharply across the two cases. In the productivity-orthogonal microfoundations, $\tau_{ij}^{F}$ is orthogonal to underlying productivity, and the distortion channel admits zero, weakly negative, or weakly positive contributions depending on the joint distribution of wedges and export shares, leaving the gradient ambiguous. In the markup case, $\mu_{ij}^{F}$ is endogenously increasing in firm size through $s_{ij,W}^{F}$ , so $1 - \mu / \mu_{ij}^{F}$ is increasing in size while $s_{ij}^{F}$ remains non-negative; the distortion channel is therefore positive across firms, and combined with the positive labor markdown channel, the gradient is positive regardless of whether size is measured by sales or employment.

The empirical TFPR-size correlation in the Chilean commodity sector is zero or weakly negative, indicating that the cross-sectional moments in our setting are not well captured by this microfoundation. Quantifying it would require recalibrating $\zeta$ and the $\mu_{ij}^{F}$ distribution to match a different set of empirical moments; we do not pursue this quantification, given the weaker fit and to retain the baseline calibration in Section 6.4.

## C.2 Measurement

The wedge is the net statutory subsidy or tax a firm faces on its exports, as a percent of FOB value: a subsidy side (programs that pay exporters) minus a restriction side (programs that cap output and extract rent). We combine our institutional index of program rules with two administrative customs files: export shipments (Aduanas Salidas, 2003, with the taxpayer

ID, HS6 product, FOB value, and the operation-type code that distinguishes genuine exports from re-exports and temporary movements) and import declarations (Aduanas Entradas, 2003, with CIF value and duties actually paid). Chile ran many export-related programs; we focus on the four that are both large and cleanly expressible as a percent of FOB, two on each side. We capture explicit instruments only, so the measure is a conservative lower bound on the dispersion the model allows.

Subsidy side. Reintegro Simplificado (Law 18,480, 1985) is a cash payment of 3% of FOB to exporters of non-traditional goods. Drawback (Law 18,708, 1988) refunds the import duties paid on inputs incorporated into the export, with an ad valorem equivalent equal to the product's input tariff $t_{h}$ (defined below). The two are statutory alternatives—a firm claims one or the other on a shipment—so the subsidy rate is the larger of the two.

Restriction side. Fisheries individual transferable quotas (ITQ, Law 19,713, 2001) cap the catch and make the quota a tradable right, working like a tax on the marginal catch worth roughly 15% of landed value (Kroetz et al., 2017). Aquaculture concessions (Decree 125 of 2003) administratively limit the number and size of maritime sites, which we treat as a 2% restriction.

Product-level wedge. For each HS6 product h,

$$
\begin{array}{r} \mathrm{subsidy} _ {h} = \max \big (0. 0 3 \cdot \mathbf {1} [ \mathrm{Reintegro} _ {h} ], t _ {h} \cdot \mathbf {1} [ \mathrm{Drawback} _ {h} ] \big) \cdot s _ {h} ^ {\mathrm{norm}}, \\ \mathrm{restriction} _ {h} = \left(0. 1 5 \cdot \mathbf {1} [ \mathrm{ITQ} _ {h} ] + 0. 0 2 \cdot \mathbf {1} [ \mathrm{Aqua} _ {h} ]\right) \cdot s _ {h} ^ {\mathrm{norm}}, \end{array}
$$

with net product wedge $\tau_{h}=subsidy_{h}-restriction_{h}$ . The input tariff $t_{h}$ is built from customs data alone in three steps: a national HS6 tariff $t_{j}^{nat}=\sum_{2003}duties_{j}/\sum_{2003}CIF_{j}$ , the effective duty on inputs of HS6 j (capped at the statutory 11%); a firm input tariff $t_{f}^{input}=\sum_{j}w_{fj}^{imp}t_{j}^{nat}$ , where $w_{fj}^{imp}$ is firm f's CIF share in input j; and a product tariff $t_{h}=\sum_{f}w_{fh}^{exp}t_{f}^{input}$ , the FOB-weighted average of $t_{f}^{input}$ across firms exporting h. The multiplier $s_{h}^{norm}$ is the 2003 FOB share of h shipped under the normal-export operation code; it down-weights products whose recorded flow is mostly re-export or temporary movement (its median is one, so only the re-export-heavy tail is affected).

Firm-level wedge. We aggregate to firms by a 2003 export-share shift-share, $\tau_f^F = \sum_h w_{fh} \tau_h$ , where $w_{fh}$ is firm $f$ 's 2003 FOB share in commodity-shock product $h$ . Each product term is a statutory parameter set independently of the firm's decisions, and the 2003 portfolio weights are predetermined relative to the 2003–2011 shock, so $\tau_f^F$ is predetermined; it also lives in the same shift-share space as the firm shock. In the commodity-exporter sample, $\tau^{F}$ splits cleanly into net-subsidy firms (Reintegro/Drawback-eligible, $\tau^{F} > 0$ ), zero-wedge firms (mining, primary copper, raw agriculture, $\tau^{F} \approx 0$ ), and net-restriction firms (fisheries and aquaculture, $\tau^{F} < 0$ ).

Scope and caveats. The measure is statutory-imputed (rate × eligibility), not realized refunds or duties, and it captures explicit instruments only. Implicit support—state financing for the national copper producer, DL 600 tax stability for foreign miners, sectoral promotion through ProChile and CORFO—is not measured, reinforcing the lower-bound interpretation. We exclude the copper-export levy (Cobre Reservado, Law 13,196) because by statute it falls on a single firm whose net position is confounded by unmeasured state support.

## C.3 The Wedge Predicts Differential Expansion

If $\tau_{f}^{F}$ captures a genuine export advantage, firms with a higher net wedge should expand exports more when the shock hits—the misallocation prediction. On the cross-section of commodity exporters we estimate

$$
g _ {f} = \beta \operatorname{shock} _ {f} + \delta \tau_ {f} ^ {F} + \gamma (\operatorname{shock} _ {f} \times \tau_ {f} ^ {F}) + \alpha_ {h (f)} + \varepsilon_ {f},
$$

where $g_{f}$ is 2003–2011 export growth (Davis–Haltiwanger–Schuh mid-point growth) and $\alpha_{h(f)}$ are fixed effects for the firm's dominant 2-digit sector, with standard errors clustered at that level; the wedge is centered. The prediction is $\gamma > 0$ . Table A.5 confirms it: comparing firms within the same broad sector, those with a more favorable net wedge expand exports significantly more when the shock arrives. The effect is robust to dropping the normal-channel multiplier $s^{norm}$ and to winsorizing the outcome at the 1st and 99th percentiles. Decomposing the wedge, the net effect is driven by the restriction (implicit-tax) side; the subsidy side has little cross-firm variation in this sample and is imprecisely estimated. Identification compares firms within the same broad (2-digit) sector, which is the level at which the wedge varies across firms: the wedge differs mainly across narrow product lines within a sector, so this is the appropriate comparison.

Table A.5: Export Wedge × Commodity Shock and Firm Export Growth


Notes. Dependent variable: firm export growth (DHS mid-point growth, 2003–2011). Cross-section of commodity exporters. The firm net export wedge (subsidy minus restriction) is built from four predetermined statutory programs and aggregated to the firm by 2003 export shares (Appendix C.2); it is centered. Each column regresses export growth on the commodity shock, the net wedge, and their interaction, with dominant-HS2 fixed effects and standard errors clustered by dominant HS2. Column (2) drops the normal-channel multiplier $s_{norm}$ ; column (3) winsorizes the outcome at the 1st and 99th percentiles. A positive interaction is the misallocation prediction: firms with a more favorable wedge expand more when the shock arrives. $* * * p < 0.01$ , $**p < 0.05$ , $*p < 0.10$ .


[[KC_IMAGE_011]]


## PUBLICATIONS
