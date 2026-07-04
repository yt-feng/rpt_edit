# Road Investment and Violence in DRC Perishable Peace Dividends
## Abstract

This paper explores the effect of road rehabilitation on violent conflict using a novel, rich dataset of road rehabilitation projects in the Democratic Republic of Congo. The country received massive external investments in transport infrastructure rehabilitation under conditions of endemic conflict, often with the explicit objective of supporting peacebuilding objectives. The paper finds that investments in road rehabilitation deter violence, which decreases significantly by around 5 to 10 percentage points after the completion of road rehabilitation. However, another significant finding, based on large-scale machine learning analysis of remote sensing data of road quality over time, is that the peace dividend of infrastructure investments is perishable: violence increases again as roads progressively deteriorate. Improved durability and systematic maintenance of roads are thus necessary to extend the “peace dividend” of road investments.

# Road Investment and Violence in DRC: Perishable Peace Dividends\*

Mathilde Lebrand $^{1}$ , Hannes Mueller $^{2}$ , Peer Schouten $^{3}$ , and Jevgenijs Steinbuks $^{1}$

$^{1}$ The World Bank $^{2}$ The Barcelona School of Economics $^{3}$ Danish Institute for International Studies

Keywords: DRC, mining, remote sensing, road infrastructure, violence
JEL Classification: O18, O19, O55, Q34

## 1 Introduction

In recent decades, billions of dollars have been spent on road projects in conflict-affected areas. Such investments are often motivated by a combination of donor objectives, which may include access to resources, economic development, stabilization, and state-building. While there is a growing body of literature around the impact of investments in transport infrastructure on economic development in fragile states (Ali et al. 2015; Berg et al. 2017; Damania et al. 2018), there is little evidence that transport infrastructure also improves stability in conflict-affected countries (Bachmann and Schouten 2018; Schouten et al. 2022).

This paper addresses this gap by analyzing the impact of road rehabilitation projects on violence in the Democratic Republic of Congo (DRC). The DRC is an ideal setting to explore the relationships between roads and violence. Since 1997, it has been home to one of the most protracted humanitarian crises and complex conflicts in the world and has a road network that ‘is about 152,400 kilometers long but, for a large part, it only exists on maps’ (World Bank 2017). Concomitantly, the DRC has been subjected to sustained reconstruction and stabilization efforts by the international community, involving large investments in its road network. We, therefore, ask the following question: what effect, if any, did these investments in the road network have on violence in the DRC? We explore the impact of road investments on violence through a longitudinal study, monitoring conflict incidence before, during, and after road rehabilitation, comparing levels of violence to areas where no roads were rehabilitated. We are also interested in how long the putative effects of roadworks on violence lasted: while the theories of change of road projects assume ‘forever impacts’, previous research suggests that rehabilitated roads rapidly deteriorate again, given a lack of maintenance (Bachmann and Schouten 2018; Schouten et al. 2022). Does the effect of road rehabilitation on violence wane as the road quality gradually decreases again?

We first assembled a new database of the main transport infrastructure projects that occurred in the DRC since the end of the Second Congo War in 2003. A comprehensive list of such projects did not exist. We collected project data (start and completion years, cost, location, and type of infrastructure) from multiple sources, including international donors and government agencies, to create a panel of geolocalized investments. Our final panel of large inter-city road investments includes 192 projects (see Appendix B).

To answer our first question, we estimated the causal impacts of road construction on conflicts. Establishing causal links is challenging because of the interaction of road projects and the activity of armed actors with other, often unobserved factors, such as conflict dynamics and economic activity. For instance, mining (a key economic activity in eastern DRC), outbreaks of violence, and road construction are all placed endogenously, often reacting to each other (cf. Luo et al. (2021)). We address this issue of causality between roads and conflicts in three ways. First, we show that road projects do not select into peaceful regions. This means that it is unlikely that armed violence generally forces road rehabilitation out of a conflict-affected region. Second, we use an identification strategy exploiting the fact that a road project crosses a 55km by 55km cell. Such localized treatment is unlikely to be related to local violence trends as the project completion is recorded at a higher level.

Third, we demonstrate this using a matched difference-in-difference method introduced by Mueller and Rauh (2023) but at the local cell level. This method matches treated cells with other untreated cells on the predicted conflict risk before treatment. Treated and untreated units are then analyzed together using a new two-way fixed effects method introduced by Callaway and Sant'Anna (2021). If road completion is selected for de-escalating conflict dynamics, then this would be detected by the local conflict forecast and lead to significantly lower treatment effects. By contrast, and in line with the declared international stabilization strategy for DR Congo of the 2010s (see DFID 2011), we find that controlling for conflict risk during the construction period, if anything, increases the estimated treatment effect of road project completion.

To answer our second question, we use novel techniques to extract information on changes in road quality based on satellite images. This allows us to observe how long road rehabilitation has had effects on road quality, and whether decreasing road quality correlates with an uptake of violence. Our findings can be summarized as follows. First, we see a statistically significant reduction in the incidence of violence after road rehabilitation projects are completed. Depending on the estimation method, we find that the completion of a project reduces violence by around 5-10 percentage points. The association between roads and reduction in violence tends to be the strongest for violence against civilians. Within our sample, the improved quality of transport infrastructure thus has a beneficial effect on conflict dynamics and stabilization (a 'peace dividend'). Second, we observe statistically that the effect of road rehabilitation on the number of violent incidents diminishes significantly after some time. The dynamic treatment effects we estimate around the completion date show that violence is first reduced directly after completion of a road project, but rebounds to pre-rehabilitation levels within three years. These findings are consistent with the suggestion that rehabilitated roads deteriorate again after projects are completed. To further substantiate this, we combine machine learning with thousands of remote sensing data observations to estimate overall road degradation patterns. Doing so, we arrive at a road discount factor of 0.735 per year, meaning that within three years, the road quality of rehabilitated roads on average decreases by 60 percent. $^{1}$

Our findings speak back to the literature on the links between transport infrastructure and conflict. Theories on these links vary wildly. On the one hand, road density is often used as a proxy for government control and associated with peace. Bad geography, from this perspective, is seen as an opportunity for rebels and an impediment to international peacekeepers and government security forces (Ruggeri et al. 2016; Müller-Crepon et al. 2021). Faulty transport networks also dampen economic activity that may constitute stumbling blocks to peace and prosperity. On the other hand, transport infrastructure and the ease of access it entails may also increase violence by facilitating the logistics of armed actors, whether rebels or military, and roads may act as magnets for violence (Zhukov 2012; Getmanski et al. 2019; Moreno et al. 2019; Rogall 2021; Voigtländer and Voth 2022; González et al. 2023; Raleigh and Hegre 2009). If there are strong hypotheses for both a negative and positive association between roads and political violence (Juan and Pierskalla 2014), it becomes all the more crucial to explore these links empirically, focusing on the impact of road interventions on conflicts. Taking advantage of new data on road rehabilitation over time to identify causal impacts, to the best of our knowledge, our paper is among the first to identify the positive, but temporary, impact of roadworks on conflict.

The rest of the paper is organized as follows. Section 2 provides a brief overview of the country's background and possible mechanisms at stake. Section 3 presents the data. Section 4 discusses our empirical framework and presents the main results. Section 5 brings additional results. Section 6 concludes.

## 2 Background

## 2.1 Country Background

Roads have a turbulent and violent history in Congo. They arguably only made their first appearance in the early 20th century, when the Belgian colonial administration began forcing local communities through appointed chiefs to expand and maintain the colonial road network to more efficiently project colonial power, replace endemic and deadly porterage that colonial logistics overbearingly relied on, and feed agricultural produce to the burgeoning population centers emerging around mines (Northrup 1988). Around the late 1940s, the Belgian Congo boasted over 130,000 km of road, most of it unpaved earth roads constructed through forced labor (see Figures 1 and 2).


[[KC_IMAGE_001]]

Figure 1: Road network in Belgian Congo, 1919

Tropical conditions meant that these roads needed near-permanent maintenance, which was largely ‘subsidized’ by the colonial administration through forced labor exactions. When the country became independent in 1960, the Congolese, of course, immediately gave up on forced roadworks, epitomizing as it did colonial oppression. As a result, within a matter of months after independence, 60 percent of the road network was unusable; by 1965, only 5,000 of the initial 130,000 km of road network was in good state (Eycken and Vorst 1967, p.421). Mobutu — the dictator ruling from 1965 to 1997 - was considered an ally of the West and consistently received major donor funding to maintain and rebuild main arteries. International donors held that maintenance of the vast road network that Zaire—as the country was called under Mobutu—inherited from the Belgians was not economically feasible, with the cost of rehabilitation exceeding the tax revenues the roads would yield, so donor funds focused on keeping open ‘priority roads’ that facilitated raw material exports and bulk imports (World Bank 1975, p.3). This mainly targeted the rail- and road network connecting copper mines in southeastern Zaire’s Katanga region to the Congo River and neighboring countries. Even so, much of these funds were misappropriated by Mobutu and his cronies (Willame 1986). The plummeting of copper prices in 1974, waves of failed nationalization, and structural adjustment destroyed already corrupt and faltering road maintenance parastatals in the 1980s, accelerating infrastructural dilapidation (Pourtier 1993).


[[KC_IMAGE_002]]

Figure 2: Road network in Belgian Congo, 1960

Maintenance of feeder roads in rural areas was by and large neglected, and rural populations were forced to rely on subsistence farming; underpaid government agents and local authorities lined whatever rural roads remained with roadblocks to extract wealth from farmers, largely as a legacy of colonial rule (Newbury 1984). When Western donors began investing in rural road rehabilitation in the 1980s as part of efforts to connect poor farmers to markets, anthropologists observed that improved transport connections only exacerbated wealth extraction by local authorities (Fairhead 1992).

Mobutu was allegedly wary of constructing direct roads between the capital Kinshasa and the East for fear of allowing insurrection to reach the capital. What he feared nonetheless happened, when in 1997 a Rwanda- and Uganda-backed rebel force swept across the country, taking town after town and eventually overtaking the capital Kinshasa. Ever since, eastern Congo has remained mired in conflict, the region's roads transformed into sinews of war. The number of armed groups has, over time, exploded, with larger groups fragmenting and new militia popping up. By the latest count, there are well over 120 armed groups active in Eastern Congo (Kivu Security Tracker 2021), many of which maintain connections to networks of patronage inside the Congolese army—which has itself been called the country's largest armed group, for the similarities in its mode of operating on the ground. Over decades of conflict, government forces and militia alike have sustained and enriched themselves as much through extracting rents from artisanal mines and farmers as from road users through roadblocks (Schouten 2022). While dynamics are extremely fluid and can, at times, be volatile, overall, government agents and larger armed groups such as M23 have competed for control over main roads, while government soldiers and smaller militia have tended to dominate rural connections in the countryside. Indeed, in 2017, 70% of the roadblocks with a government/army presence in North Kivu sat on national or provincial roads, while 79% of rebel roadblocks sat along tertiary/feeder roads (Schouten 2022, pp. 117-118). However, such patterns are highly unstable over time, with rebels periodically overtaking control over main roads. Roads are, therefore, magnets of continuous and often violent contestation among different types of authorities and road users over how goods, people, and capital circulate and who gets to benefit. According to the Congo Research Group (CRG 2019, p. 6), almost half of all violent events between 2017 and 2019 took place at or near roads, as opposed to mines or villages (cf. (O'Mealia 2022)).

In this context, stabilization operations by the international donor community have sought to intervene by coupling peacekeeping, humanitarian, and development efforts with ambitious road rehabilitation efforts. Rehabilitating roads would bring down the cost of logistics for aid and peacekeeping, kickstart economic development, and facilitate the extension of state authority (Bachmann and Schouten 2018, p. 14). To wit, the UN-led stabilization strategy for Congo spearheaded that roads are key because

‘rural areas are completely isolated and armed groups in the east have been able to move unhindered, populations have been cut-off and commerce has all but disappeared... Rebuilding roads and creating jobs in the process, expanding the transport grid and clearing corridors of checkpoints will not only destroy key profit centres of the remaining armed groups, these actions will also accelerate the economic reunification of the east, return markets to their past vibrancy and permit people to move freely.’ (DFID 2011, p. 14)

## 2.2 Theory Background

The premises upon which such strategies rest have been subject to a lively academic debate, which posits contradictory linkages between roads and violence.

Conflict studies typically assume that low road density, rough terrain and inaccessibility are enabling conditions for the onset and duration of civil war, arguing that rebels thrive in ‘ungoverned zones’ because of an absence of adequate transport infrastructure to enable government forces to maintain order (Tollefsen and Buhaug 2015; Hendrix 2011; Müller-Crepon et al. 2021). Such studies are based on the assumption that transport networks represent a form of ‘infrastructural power’, indispensable for states to actually control the population within their territories (Mann 1984; Scott 2009; Schouten and Bachmann 2022). By extension, the absence of well-functioning transport infrastructure is often taken as a key aspect of state fragility (Herbst 2014; Jimenez-Ayora and Ulubaşoğlu 2015; Schouten 2013). The policy implication is clear and has been widely internalized by stabilization operations: overcome the ‘friction of terrain’ by investing in road rehabilitation to allow government forces logistical access (Schouten and Bachmann 2017). Or, as Lt. Gen. Karl Eikenberry, then American military commander in Afghanistan, famously posited ‘Wherever the road ends, that’s where the Taliban starts’.

It is, however, just as easy to argue that efficient transport infrastructure facilitates more violence (Zhukov 2012). Rough terrain, from this angle, may protect populations from violence (Nunn and Puga 2012), whether affiliated to the state or not. Building on this idea, Mueller et al. (2022) argue that there is a dark side to proximity, in which higher transport costs between attackers and defenders reduce violence. In line with this, several case studies use the ease of transportation as an instrument for the intensity of adverse violence treatment. The most striking example here is Rogall (2021), who shows that bad road quality protected villages during the Rwandan genocide. There is some evidence that donor roads meant to increase the reach of the state in South Sudan inadvertently helped government forces perpetrate violence against civilians (Schouten and Bachmann 2017). Similarly, Ali et al. (2015) found that distance from roads may offer villagers in the Congolese countryside some protection from conflict. They suggest that ‘when conflict is high … better roads enhance the payoffs from rebellion’ (Ali et al. 2015, p.21). In other words, there are good arguments for both a positive and negative relation between road investments and violence in conflict settings.

Studying this dynamic is complicated by the fact that road investments and violence tend to cluster in mineral-rich Congolese provinces, making it difficult to isolate road-conflict dynamics from violent incidents that may be related to resource rents in the same geographical space. While the links between mining and conflict are as much researched as they are contested, few analyses have tried to pick apart the connections between mines, roads and conflict. Correlating data on mining, checkpoints, and violent incidents, O'Mealia (2022) finds that in mineral-rich provinces, competitive violence between Congolese armed actors concentrates spatially around key nodes of the transport network through which mineral supply chains run, rather than at production sites, which are marked by less violent incidents (cf. (Idler 2020)). As De la Sierra (2020) and Schouten (2022) suggest, this may be an effect of the ‘obstructability’ (Ross 2003) of different minerals: dispersed artisanal mining activities and easy-to-hide minerals like gold and diamonds may be difficult to tax at the mine itself, increasing competition for rents along evacuation routes and hubs, while bulky, low-value minerals like coltan, copper, and cobalt are easy to obstruct and tax at mining sites, leading to competition for rackets at the production sites themselves. By contrast, Krauser (2020) suggests that a relative absence of violence around Congolese mining sites compared to roads has to do with the incentives for armed actors interested in extracting rents from mines: to attract the mobile workforce of artisanal miners—who can ‘vote with their feet’ and leave a dangerous mine—armed actors are nudged to project violence elsewhere.

Violence itself can take multiple forms (looting/riots versus battle events) and originate from various actors (civilians versus organized actors). The impacts of road projects can differ across different forms of violence. Scholars have used different measures of violence as dependent variables either in sensitivity tests or in order to shed light on potential channels of causation (Besley and Persson 2011; Bazzi and Blattman 2014; Harari and Ferrara 2018; McGuirk and Burke 2020). In particular, the conflict literature makes the distinction between violent events related to the control of territory (factor conflict) and those related to grabbing resources (output conflict). These two can react differently to road rehabilitation, the same way they have been shown to react differently to local income shocks (e.g., crop price shocks in McGuirk and Burke (2020)). By increasing farm wages, for example, rising grain prices can reduce the supply of labor to armed groups, thereby causing a decline in conflict battles in rural areas. At the same time, high prices or the availability of harvests could provoke conflict over the appropriation of the commodity itself in the form of looting. Controlling for both cell fixed effects and country-year fixed effects, McGuirk and Burke (2020) find that a 1 standard deviation rise in producer prices lowers the probability of conflict by around 15% in food-producing areas, but increases the probably of conflict in no crop producing areas.

This discussion highlights the complex and essentially contested connections between roads, violence, and resource rents, and the necessity to control for the possible effect that minerals may have on the link between roads and violence.

## 3 Data

## 3.1 Political Violence

Our outcome variable is political violence in the Democratic Republic of Congo (DRC). Figure 3 gives a first impression of the cross-sectional distribution of political violence as measured by the two most popular datasets, the ACLED and the UCDP. $^{2}$ It is clearly visible that many regions are extremely violent, and few regions are completely peaceful. This motivates an approach in which we make all of the DRC our test sample instead of only the most conflict-affected regions in the East of the country: Ituri, Nord-Kivu, and Sud-Kivu.

Figure 3: Political Violence in the DRC

[[KC_IMAGE_003]]

Notes: Figure shows the location of ACLED and UCDP events in the DRC.

## 3.2 A New Database of Road Investments


First, we created a database of road transport projects relying on multiple sources of information: universities (William & Mary, Boston University, and Johns Hopkins University), government bodies (Plateforme de Gestion de l'Aide et des Investissements, Cellule Infrasstructure), and international donors' websites (World Bank, African Development Bank). Each source provides different sets of information, and a few of them include the exact location of the road projects. Most of the work consisted of bringing together sparse information about road transport projects in the DRC in one unified database and cross-checking the data using multiple sources of information. In addition to the information extracted from the previous sources, updates were added mostly by extensive online search. Lastly, we worked on avoiding duplicates. The database we obtained is the most complete one that exists, but unfortunately, some projects had information gaps, and it has been difficult to associate each project with its exact location.

Second, we constructed road segments based on the previous project list. Most of the previous sources of information do not provide the exact location of the project. Different methods were used to identify the location. For some projects, particularly from international donors such as the World Bank or the African Development Bank, documents detailing the initial commitment, rationales for the project, and disbursements over time can be found online. For others, the project's title often includes the start and end city names or such information can be found online. Figure 4 shows the mapping of the projects we managed to localize.

Third, we put together a spatial panel of road projects by merging the map of projects with the PRIO grid cell - a grid structure that aids the compilation, management, and analysis of spatial data within a time-consistent framework. $^{3}$ We end up with a panel of grid cells with information on whether a road project is happening or not and whether it has been completed or is ongoing.


[[KC_IMAGE_004]]

Figure 4: Map of Geolocalized Projects

The final panel of road investments includes 192 projects; among them, 113 have start and end years, a commitment amount, and are not classified as dropped or suspended. The following statistics apply to these 113 projects. The average starting year is 2010, which is also the year with the largest number of infrastructure projects that started. The average duration of projects is 3 years, with a large number of projects lasting less than a year. More details about the database's construction can be found in Appendix B.

One of the main concerns regarding the analysis of roads and violence is the self-selection of road projects into peaceful regions or peaceful periods in violent regions. Three arguments speak against this concern. First, at the provincial level, we see little evidence of this selection. If anything, Figure 5 shows that the commencement of road projects is selected into the more violent rather than peaceful places. The Figure shows the log of armed conflict event totals per million inhabitants together with the log of completed road project length at the province level. The relationship is clearly positive, i.e. more and longer road projects were completed in the most violent provinces. The same pattern holds without population weighting of violence intensity. This is in line with the anecdotal evidence and the motivation of the projects to contribute to stabilization. Thus, unless the timing of completion is strongly affected by violence, this alleviates endogeneity concerns somewhat— although this question merits exploration on a more granular level, as Congolese provinces are the size of small European countries.

Second, investment in international donors' financed projects, which constitute the overwhelming amount of road investment in the DRC, is typically spread out over several years following the original approval of the project (Kraay 2012). This means that fluctuations in project spending in a given year are largely determined by fluctuations in project approval decisions made in previous years and are unlikely to be correlated with unanticipated conflict outbreaks in the current year.

Figure 5: Roads and Violence at the Province Level

[[KC_IMAGE_005]]

Notes: Figure shows the log of armed conflict event totals per million inhabitants together with the log of completed road projects at the province level.

Finally, we provide evidence that the completion of projects is not directly affected by the level or the intensity of conflicts. Section B.5 in Appendix B reports extracts of Implementation Completion Reports (ICR), a World Bank document that lists the reasons for delays once World Bank projects are completed. For each of the listed projects, delays were mostly due to the slow implementation of initial administrative tasks connected to weak institutional capacity, the slow resettlement process, the slow adoption of laws to facilitate the project, and the limited capacity of the responsible investment party. A main road rehabilitation project was delayed between 2017 and 2018 due to repeated cases of gender-based violence, ranging from sexual harassment to sexual exploitation and abuse, and rape linked to the implementation of the project and the influx of workers on the project site. $^{4}$ We check whether an increase in gender-based violence, classified as violence against civilians in ACLED data, during the project implementation only could drive our results by restricting our analysis to other types of violence (one-sided violence in UCDP or battles in ACLED). In addition, increased gender-based violence due to the influx of workers might be considered as orthogonal to the reasons for local conflicts in DRC. While it is possible for other countries and other non-World Bank projects, none of the World Bank ICR documents lists the eruption of local violence as a reason for stopping or delaying the project. While World Bank projects are only a subset of all projects, their completion would be more likely to be disrupted in case of increased violence compared to projects led by the government. Therefore, it is unlikely that the completion date of such long and often delayed projects is explained by a sharp decrease in violence.

## 3.3 Using Satellite Images to Infer Road Quality

The road project data detailed in the previous section gives us a start and end year for the project. We will maintain the assumption that between these dates, the project is ongoing, delivering improved road quality only towards the end, where implementation tends to concentrate. What cannot be said, however, is how long the increased road quality is maintained after the end of the project—what one could call the perishability of the peace dividend of road rehabilitation. This matters to identify the impacts of road rehabilitation on conflicts. We expect the average quality on rehabilitated roads to increase until the completion of the project and then gradually fall again, given the harsh tropical conditions reducing the lifespan of newly rehabilitated unpaved earth roads (see discussion in section 2.1).

We use machine learning models for assessing the quality of roads using satellite imagery (Cadamuro et al. 2018; Thegeya et al. 2022; Conner et al. 2023). We first classify the images as described in Muhebwa et al. (2023) to then find a parameter that describes the decay of road quality over time in a particular region of the DRC. Each image is given predicted quality labels from a 2-class and 5-class classifier. We encountered two main problems. First, extensive road quality data is not available to train the machine learning models. We had to use road quality data from other African contexts (Kenya and Liberia) to train the model and then use satellite imagery for the DRC (Muhebwa et al. 2023).

Second, getting remote sensing data for the entire sample period and road network in DRC is not possible due to the limited image availability. We, therefore, focus on estimating a road discount factor from three large road projects taken from our database that were completed after 2010. These projects were large road rehabilitation projects in conflict-ridden regions in eastern DRC. Muhebwa et al. (2023) provides a road quality classification for 7,121 images of project roads. $^{5}$ Each image is a 256 by 256-pixel satellite image at 60 cm/px resolution. We, therefore, obtain a road quality class index for short road segments of 150m by 150m based on a classifier. The classifier was trained on groupings based on the International Roughness Index (Sayers et al. 1986), and we use these evaluations to classify a road as either good (IRI of 0 - 7) or bad (IRI > 7).

Figure 6: Example of satellite imagery aggregation
Project 04 Segments

[[KC_IMAGE_006]]


Project 04 Segments (Zoomed)

[[KC_IMAGE_007]]

Notes: The road for one of the three projects is divided into segments of 10 km. Segments 180, 181, and 182 are highlighted in red.

We then use the date, longitude, and latitude of each image to order the images in time and space and attribute them to specific road projects. This way, we are able to track what happens to road segments over time. For our analysis, we aggregate images to 10 km segments to reduce measurement noise (figures 6 and 7). Additionally, we bin by year, as seen in figure A3, which further reduces noise. This means that our model does not account for seasonal variation in decay. $^{6}$ Figure 6 illustrates this analysis. The left figure shows one of three projects we scanned repeatedly with the satellite data. The 10 km segments we use for our decay analysis are shown as white dots on the map. Segments 180, 181, and 182 of the project are highlighted in red. On the right, we zoom in on these three segments.

The overall method is to fit an exponential decay for each segment's quality per year starting from the point of road improvement and take a weighted average. We then obtain a final decay parameter for a binary model where a quality of 1 indicates a ‘good’ road and 0 a ‘bad’ road.

Figure 7: Satellite road quality inputs for the decay estimation
2012

[[KC_IMAGE_008]]


2016

[[KC_IMAGE_009]]


2021
Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is marked with a light blue point. Each colored pixel represents one of the tiles fed into the deep-learning classifier, and the color represents the predicted probability, where a darker green tile means a better road and a darker red tile means a worse road.

We first determined the peak quality of each segment for any time between the start and end of the construction project. We removed any significant improvements in road quality, where we saw an increase of more than 0.05, to remove noise induced by repeated work on a road segment. We then order all remaining data from all segments across all projects to calculate the road discount factor. To estimate decay, we use an equation in exponential form. $^{7}$ The equation we estimate is given by:

$$
y = a _ {0} \cdot \exp (b _ {0} \cdot t) = a _ {0} \cdot \delta^ {t}
$$

where t indicates the years since the segment quality peak. We fit $b_{0}$ and use this value to compute a $\delta$ to describe the decay of all roads. When computing the slope of a single segment, we weigh the slope by the number of images in that year. This ensures the model puts more weight in places where there are more measurements. The slopes of each segment ( $b_{0}$ ) are combined into one discount factor using a weighted average, where the weight is the number of images in a particular segment.

To illustrate our data y, Figure 7 zooms into segments 180, 181, and 182 and shows the IRI classifier output for each image for three years. The edge of each segment is marked with a light blue point. Each colored pixel represents one of the tiles fed into the deep-learning classifier, and the color represents the predicted probability, where a darker green tile means a better road and a darker red tile means a worse road. Road quality declines overall. This is visible through the increasing red shades on the right. The exception is segment 180, which is the first segment. This segment first declines in quality from 2012 to 2016 and then increases in quality again in 2021. $^{8}$ The resulting data is shown in Appendix Figure A4. From this data, we estimate the road discount factor using the equation above as $(0.735 \pm 0.05)$ . This implies that, after three years, 40 percent of a rehabilitated road would still be of the same quality as just after rehabilitation, and 60 percent would be unusable.

## 3.4 Mining and Natural Resources

As discussed in section 2.2, mining can be an important mediating factor affecting both roads and conflict events. We collected information on the location of both large and artisanal mines in eastern DRC. We used data from the World Bank and S&P Global to compile a list of mining sites, including information on their name, type of commodity extracted, status, and location. We complemented this list with additional research on the company, the type of involvement (Private vs. Public vs. Joint Venture), and the country of ownership. We used IPIS Open Artisanal and Small-Scale Mining in eastern DRC data to map the artisanal mining sites. $^{9}$

Mapping the location of mines and donor-funded road rehabilitation projects shows that mining sites cluster near road investment projects (Figure 8). The first reason is colonial path dependency: many of today's mines exploit deposits first brought up to stream by the Belgian colonial administration, which developed the road network in large part to facilitate mining. However, not all currently exploited deposits existed during colonial times, and many colonial-era mining roads have been overtaken by the jungle in the decades since. The second reason is that miners find a way to reach mines and transport ores if profits exceed the costs of production and transport. In many cases, artisanal miners cut new, improvised footpaths to mining sites; in the case of rich mineral deposits, more capital-intensive roadwork may follow the mining activity, entailing road improvement exclusively with the transport of mining material in mind. There is important variation here between different minerals: bulky minerals with a low value per weight unit, like coltan or cobalt, have a lower profitability range in the absence of good roads than gold and diamonds, which are high value at small quantities and can thus be profitably mined and transported along footpaths from more remote locations (De la Sierra 2020). In either case, once established, such mining paths tend to attract other forms of traffic and become ‘roads’ (see Kleinschroth et al. (2019) for similar dynamics of logging roads). While small-scale mining of high-value minerals is thus less road-dependent than bulky minerals, industrial mining is fully road-dependent, illustrated by the heavy road investments by Kibali Gold in the northeast DRC and Chinese involvement in road building to reduce transport costs of minerals out of Katanga and via the Indian Ocean to China (Mathebula and Sekgololo 2023). Given the pattern of violence shown in small artisanal mines in the North East and large mines in the southeast in Figure 3, it should also be clear that there is no simple cross-sectional relationship between all mines and violence in our data: as discussed in the theory section, most violent events seem to cluster where artisanal mines are found, and not around the industrial mines in Katanga (also see Stoop et al. (2019)).

Figure 8: Mining Locations and Roads

[[KC_IMAGE_010]]

Notes: Mining locations for small artisanal mines and large projects together with road investments by international actors.

## 4 Roads and Armed Conflict

## 4.1 Hypothesis and Descriptive Evidence

While we focus our analysis on PRIO-grid cells, we first examine the broad correlation between violence and road projects at the provincial level. The mainstream assumption is that road quality is a proxy for government reach and, therefore, correlates with a reduction of violence and increased ‘peaceful’ economic activities (see discussion in sections 2.1 and 2.2). That is, improved connectivity in areas of operation of government versus rebel groups leads to a reduction in violence (Müller-Crepon et al. 2021). But there is also the obverse hypothesis, namely, that all-weather roads are spaces where armies and rebels concentrate extraction (and competition for extraction), increasing the likelihood of violent incidents, meaning that remote/rugged areas and areas with bad roads experience fewer incidents (Nunn and Puga 2012; González et al. 2023). Given the complicated and convoluted landscape of armed actors in Eastern Congo (Stearns 2022), road rehabilitation interventions may only temporarily reshuffle patterns of violent incidents, as Schouten et al. (2022) have hypothesized (cf. Bachmann et al. 2022a).

Note that some of the earlier results leading to opposite hypotheses could come from different thresholds of road access at which impacts on violence were estimated. In principle, no region is ever fully isolated: even if roads are completely impracticable, people still manage to go around on foot—and much of Congolese army and rebel movements rely on such 'unconventional' logistics (Schouten 2022). If a region is therefore never completely insulated, there could be a reduction of violence as lower-quality roads see improvement. From an econometric standpoint, this is a question of whether we observe correlations of roads and violence within or between regions or provinces. As regards the regional (or between) variation, the positive relationship between roads and violence at the province level is shown in Figure 5. This positive correlation is not entirely surprising, given the relationship between mines, roads, and violence discussed in section 3.4. If roads facilitate mining activity and mines attract violence, then this can establish a positive association in the cross-section.

Given a significant cross-sectional bias, it is, therefore, important to look at the time variation. When we look at the available time variation at the country and provincial levels, the picture changes dramatically. One of the first pieces of evidence is provided in Figure 9, which shows a negative association between completed road projects and violence. Years in which many road projects are completed in the DRC and provinces tend to be more peaceful than years with fewer completed projects.

Figure 9: Roads and Armed Conflict in DRC

[[KC_IMAGE_011]]

Notes: The Figure shows the number of violent events sourced from UCDP and the sum of completed road projects per year for the DRC.

This could obviously be a coincidence—or contingent on external factors such as peace agreements—but if we look at specific provinces, the link becomes even stronger. Figure 10 shows the same data as Figure 9 but just for North Kivu, arguably the most conflict-affected provinces in eastern Congo, and we see an even stronger negative association between conflict events and road projects. Completed road projects seem to reduce violence. The same picture emerges if we focus on South Kivu. As previously discussed, this is not due to a strong selection away from violence in terms of provinces (Figure 5).

Figure 10: Roads and Armed Conflict in North Kivu

[[KC_IMAGE_012]]

Notes: The Figure shows the number of violent events sourced from UCDP and the number of PRIO cells with a newly or recently (last year) completed road project for Nord-Kivu.

If the completion of road rehabilitation seems to correlate with an ensuing reduction of violent events, it is obviously of interest how long rehabilitated roads retain their peace effect. To visualize the effect of the discount factor we derived through remote sensing, we show the road project stock that we estimate for North Kivu in Figure 11. The starting point here is the same as in Figure 10 –i.e. the peaks in the Figure represent the quality of roads just after the completion date of road rehabilitation projects—but now we treat the completed road projects as an ‘investment’ that adds to a ‘capital stock’ that decays with the road discount factor derived above, with the gentle slopes downward from top quality peaks representing the gradual degradation of the rehabilitated roads. The red line in the Figure shows the number of violent incidents, and these indeed rise each time the quality of roads nears its lowest point. The overarching pattern seems one of a cyclical dialectic between road rehabilitation and armed violence.

Figure 11: Road Stock and Armed Conflict in North Kivu

[[KC_IMAGE_013]]

Notes: The Figure shows the number of violent events sourced from UCDP and the road project Stock for North Kivu. A newly completed project takes a value of one. This value goes down as the road deteriorates.

## 4.2 Regression Analysis

We address the issue of endogeneity of the completion of road projects with the overall violent environment at the province level through two strategies. First, we run the analysis and data collection at the smaller PRIO grid cell level (0.5×0.5 decimal degrees). It is unlikely that at that level, the completion of the road project is driven by violence in the cell. This level of analysis also allows us to control for province/year fixed effects. Second, we match grid cells on their violence risk outlook following the methodology proposed by Mueller and Rauh (2023). This allows us to compare cells with the same violence risk profile before and after the completion of a road project.

OLS with cell-fixed effects We test the link between conflicts and road investment by running the following regression controlling for both cell-fixed effects and year-fixed effects

$$
y _ {i t} = \theta_ {i} + \theta_ {t} + \beta_ {1} r o a d s _ {i t} + \varepsilon_ {i t}
$$

where $y_{it}$ represents fatalities and events and is expressed in natural logs. We start by using the aggregate number of events and fatalities and we then run the same regression for different categories of events. We use three types of road investment variables in the regression: (1) a dummy indicating if at least one project is ongoing in the cell, (2) a dummy indicating if at least one project has been completed in the cell that year, and (3) a variable that quantifies the stock of road projects happening in that cell. The last variable sums the number of road projects that have happened in the cell including the decay of roads over time. A project that was completed that year takes a value of one, while previously completed projects have a lower weight depending on their decay which is the function of the difference in years since the project was completed.

Table 1: Roads and Armed Conflict


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

We first report the results for the total number of events and fatalities (Table 1). Road projects and violence in the within variation using cell fixed effects are negatively associated. The table shows results for different measures of road project activity and completion. We analyze UCDP events in columns (1) to (3) and UCDP fatalities separately in columns (4) to (6). Columns (1) and (4) show results for ongoing road projects. We see a negative point estimate, which is statistically insignificant. Columns (2) and (5) show results for the year of completion. We find very similar point estimates, but the coefficient is only significant for UCDP events. According to these estimates, the completion of road projects reduces violence by 5 percentage points. Columns (3) and (6) contain our main specification, which tracks the road project stock using the discount factor from the remote sensing exercise. While this indicator does not consider the period before completion, it provides a more accurate estimate of the impact of road rehabilitation projects. First it sums up all projects at the cell level. Second it depreciates the presence of a road over time. We now have statistically significant coefficients for both events and fatalities.

The impact of an ongoing project is weaker and non significant in that specification. The lack of results can be explained by the fact that ongoing projects may have not reduced transport time/cost yet. Ongoing projects can also affect incentives for violence in different ways. They can increase economic opportunities, attract labor and raise the recruitment costs of armed actors, which then leads to reductions in violence. This result may add reservations to the idea behind labor-intensive road rehabilitation projects, which are funded as ‘quick impact’ projects, that an influx of cash for work into conflict areas may affect violence (Bachmann and Schouten 2018). However, such question would require a more precise data collection effort to precisely identify when works are performed and workers getting paid.

In the appendix, we provide robustness checks. Generally, we find that the road stock results hold up better - the semi-structural model of road stock decay leads to statistically significant and robust findings regarding violence reduction. Importantly, the road stock results are robust, considering the inclusion of province/year fixed effects. This means that effects are identified within a province, i.e. they are not driven by changes at the province level like other policies that were implemented in these larger political units. We will further discuss robustness to different violence types and data sources.

Prediction Matched Difference-in-Difference As discussed earlier, a key problem for identification is the endogeneity of road placement. Even if, as we argue in section 3.2, the start and completion of projects are not directly a function of how violent a region is, the completion of projects could be affected by violence in the sense that project implementation is affected by unobserved factors (such as e.g., local capacity) correlated with violence. This is a hard identification problem to address with observational data.

Mueller and Rauh (2023) develop a method that we call Prediction Matched Difference-in-Difference (PreMDiD) to address this issue. The idea is simple: matching observations on the pre-treatment risk evaluation from conflictforecast.org allows us to control for the violence outlook in the year before the treatment. $^{10}$ We take the December forecast of the year before road completion to construct a control group and then hold three years before and after road completion in treated cells next to three years before and after a placebo treatment in control groups with the same risk forecast. The resulting data of real and placebo treatment windows is then analyzed through the cutting-edge difference-in-difference estimation method by Callaway and Sant'Anna (2021). A key advantage of this method is that it allows for a study of violence dynamics in treatment cells compared to untreated cells. This allows us to study pre-trends and violence dynamics after road completion.

This takes care of a main challenge to identification because it allows us to control for conflict risk when analyzing the effect of road on conflict events. What we are asking is: Holding risk at the cell-level constant, did road projects reduce the realized violence? Figures 12 and 13 show results for the log of UCDP events and fatalities. Period 0 indicates the year in which the treated cells receive a completed road project. The year -1 is the year before roads are completed. Year -3 is the omitted category. Point estimates show the difference between the treatment and control groups. If roads reduce violence, we expect these to fall with completion in year 0. There is a notable reduction of violence intensity (measured by log events and fatalities) with the completion of a road - even if we control for the risk before completion. The ATTs we estimate are 4 percentage points for events and 10 percentage points for fatalities, and both are statistically significant. We conclude from this and the earlier results that violence is reduced by about 5 to 10 percentage points with the completion of a project.

The dynamics of the effect are extremely interesting. Violence drops fast after completion and finds its minimum in the year after completion. It then rebounds, and the point estimate is close to 0 three years after completion. This suggests that road rehabilitation does not have a lasting effect on violence in our sample but only reduce violence for a few years. This effect is very closely aligned with the decay factor we estimated from the remote sensing which reinforces the idea that road degradation might indeed significantly enable violence.

Figure 12: Roads and Events: PreMDiD

[[KC_IMAGE_014]]

Notes: Figure shows the effect of road completion at year 0 compared to a control group that is matched by violence prediction in year -1.

Figure 13: Roads and Fatalities: PreMDiD

[[KC_IMAGE_015]]

Notes: Figure shows the effect of road completion at year 0 compared to a control group that is matched by violence prediction in year -1.

In addition, there is some indication of a positive pre-trend in violence before the completion of roads. Remember that we matched observations by the UCDP violence risk in period -1. What we, therefore, find here is that treated cells might have suffered a slight escalation of violence before road completion. What could explain this? Armed forces brought in by the government or UN to secure a project perimeter may meet armed resistance or engage in violent wealth extraction to finance their deployment. It may also be that the roadworks attracted attempts of resistance by local armed actors or that the rents that the project brought led to fights. Impending roadworks may also turn stationary bandits roving, i.e. disturb entrenched and predictable armed group revenue generation strategies such as roadblocks, leading to violent transitioning to alternative forms of wealth extraction (see (Schouten et al. 2022)). According to ibid and expert interviews, it is also true that road project announcements often lead to land grabbing in the area. This might cause violence to increase before the actual start of the project. However, the timing here is important - road projects usually go on for several years, and the sudden increase of violence before completion is not consistent with land grabbing at the start of the project. An alternative interpretation is that violence is causally linked to the government showing its strength with the increased connectivity.

## 5 Robustness Checks and Potential Channels

## 5.1 Different Types of Violence

In the previous regressions, we only focused on the total number of events and fatalities. However, such aggregates cover very different types of violent events, and some of them, like protests, are not the focus of this paper. We, therefore, run the OLS regressions again using different subsets of violent events. Different measures of violence as dependent variables either in sensitivity tests or in order to shed light on potential channels of causation have been used (Besley and Persson 2011; Bazzi and Blattman 2014; Harari and Ferrara 2018; McGuirk and Burke 2020). Using UCDP data, we focus on (1) one-sided and (2) non-state violence. One-sided violence is defined as "the deliberate use of armed force by the government of a state or by a formally organized group against civilians which results in at least 25 deaths in a year". A non-state conflict is defined as "the use of armed force between two organized armed groups, neither of which is the government of a state, which results in at least 25 battle-related deaths in a year". Using ACLED data, we focus on violence against civilians and battles. Violence against civilians includes sexual violence, attack, and abduction/forced disappearance. Battles include events when the government regains territory, when a non-state actor overtakes territory, and when armed clashes occur.

First, we get strong and robust findings on the relationship between road projects and violence targeting civilians using one-sided violence in UCDP and violence against civilians in ACLED. While the two sources are quite different in the way they define violence against civilians, the estimates are similar and show that the reduction of violence associated with road projects applies to violence against civilians (Tables 2 and 3).

Table 2: Roads and One-Sided Violence (UCDP)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

Table 3: Roads and Violence against Civilians (ACLED)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

Second, we also get a strong negative relationship between road projects and battles using ACLED data. Battles relate to events linked to fights for territory and armed clash. The coefficients remain negative and significant for the number of events but are not significant any more for the number of fatalities. Last, the results for non-state violence and state-based violence using UCDP are insignificant (Table A3).

Table 4: Roads and Battles (ACLED)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

Overall, the association between roads and violence reduction is strongest for violence that targets civilians and there is some evidence on reductions of battles in the ACLED data. Road projects are not associated with a reduction in state and non-state violence.

In additional results in Appendix table A4 we show that ruggedness, measured by strong slopes in a cell, do not seem to interact strongly with roads. However, for one-sided violence we find that the effect of road project is dramatically increased in rugged terrain.

As we do not have forecasts for ACLED fatalities or sub-categories of the UCDP data, we do not apply the PreMDiD method to other violence types as the control group cannot be properly matched.

## 5.2 The Role of Mining Revenues

Access to mining revenues is a driver of violence, and improved roads facilitate access to mining resources. We first control for the presence of mines as a robustness check for our main estimates of the impact of roads and then interact the presence of mines with road projects to understand how the impacts of road projects vary depending on the presence of mines.

First, we add changes in mining revenues in the first specification (Table 1). We multiply the number of mines in a cell times by the commodity price of these mines to get to a proxy of revenue and add it as controls. We show the results for artisanal gold mines and the two most common types of large mines: copper and cobalt. The main estimates for the impacts of road completion and the stock of roads remain similar (Table A5). The results of the PreMDiD are also robust to additional mining controls.

Second, we interact mining revenues with the road stock variable in the first specification to understand the interactions of roads and mines on violence. We show results when including all events and fatalities (Table A6), and when using categories of violence as in the previous section. Results using UCDP data for one-sided and non-state violence are presented in Table A7. Results using ACLED data for violence against civilians and battles are presented in Table A8.

Overall, we find a different impact of the presence of mines depending on the types of mines. In most specifications, higher revenues from gold produced by small artisanal mines is positively associated with more violence. This may be because gold is the only mineral that eludes certification and supply chain initiatives and/or because artisanal gold mines have a consistently higher presence of armed groups than other minerals (Leysen et al. 2023). Copper and cobalt, by contrast, are mined outside the most conflict-affected provinces under consideration here (North and South Kivu) and instead are subject to much more government control because of their importance for government revenues. Higher revenue from cobalt mines is associated with more total violent events, and in particular more violence against civilians and more battles using ACLED data (Table A8). Higher revenue from copper mines is associated with less violence, in particular for violence against civilians and battles.

Mining revenue is generally not interacting with roads. A crucial exception is the ACLED data which features two types of interactions. First, roads increase violence in moments/locations of high gold revenues. This is consistent with an increase of rapacity effects with roads in which high revenue areas become more accessible with roads and, hence, become more contested. On the other hand, roads have the opposite effect with cobalt revenue in the ACLED data (Table A8). An interpretation would be that roads here signal central engagement which reduces violence. However, nothing definitive should be taken away from this, as these results are not robust across violence datasets.

The completion of road projects when mining revenues increase has a very different impact if the revenues come from small artisanal gold mines or from large cobalt mines (Table A8). The completion of roads is associated with a decrease in violence when mining gold revenues are very low, but an increase in violence as the revenues increase. The opposite happens for cobalt mining revenues and road projects.

## 5.3 Discussing the Possible Channels

There are at least three possible non-exclusive channels through which better roads can reduce violence. First, better roads allow government forces to maintain order. Second, better roads increase economic opportunities and may convince some current or future members of armed groups to stop fighting. Third, better roads can increase the incentives of armed forces to settle in a specific territory, to unilaterally control it, and to generate income from the population (i.e., “the stationary-banditry” theory). From discussions with World Bank practitioners, roads seem to play an important role in allowing government forces to bring back order and reduce violence.

We test the hypothesis that road projects increase economic opportunities using the same specification as in Table 1 replacing violence with nighttime lights. We use the average calibrated nightlights from the DMSP-OLS nighttime lights Time Series Version 4 for the period


The last channel of interest is the adaptation of armed groups from being “roving bandits”, exerting violence to extract maximum benefit in the short term, to “stationary bandits” that set up regular taxation systems and leave a portion of resources for the population to use for accumulation, investment, and subsequent increases in production. Improved roads could reduce violence against civilians and generate taxable traffic that can generate longer-term revenue, through roadblocks for example, rather than through more violent, ‘roving bandit’ tactics. More work and access to more granular data will be needed to fully disentangle these effects.

Overall, our results suggest that roads do not affect violence only through one channel but might increase violence through increasing opportunities for attacks and raids while at the same time increasing stability by increasing state capacity or opportunity costs for violence. Such a complex role of trade linkages is consistent with recent theoretical work (Couttenier et al. (2023)).

## 6 Conclusion

Understanding the impacts of roads on violence is important to better support the efforts of stabilization and reconstruction in conflict-ridden countries. The present paper quantifies the impact of road construction and rehabilitation on violence in the DRC by using temporal variation in road project rehabilitation using a new database of large inter-city road projects and road quality using the latest machine learning models using satellite imagery.

Our main finding is that there is indeed a statistically significant reduction in the incidence of violent events recorded by the UCDP after road rehabilitation projects are completed. The improved quality of transport infrastructure thus has a beneficial effect on conflict dynamics. However, this effect is relatively short-lived as the positive impact of roads on the number of violent incidents reduces significantly after some time, as road quality decreases due to a lack of maintenance. Both findings are mutually reinforcing and suggest that, for the empirical case at hand, the quality of the road network indeed has a dampening effect on violence, with violence decreasing just after road rehabilitation and increasing again as roads gradually deteriorate over time.

Assuming these findings turn out to be externally valid (i.e., they hold for road rehabilitation projects in other conflict-affected contexts), the policy implication is that investments in road rehabilitation have a ‘peace dividend’ but that such a peace dividend is perishable, decreasing as road roughness increases with time. This aligns with qualitative studies that have suggested that road projects in tropical, conflict-affected settings only have temporary effects on road quality (Bachmann et al. 2022b) and, therefore, never durably impact conflict dynamics (Schouten 2022). If such investments are to deliver sustained peace, investment should be made in durable roads, prioritizing more resilient road types or investing in road maintenance (and preferably both).

While the impact of roads on violence has intuitive appeal, we suggest several mechanisms through which they interact. Is it that roads facilitate the deployment of government forces and, thereby, the re-establishment of state authority in areas previously under rebel control? Do improved roads facilitate mistrustful communities to interact peacefully through commercial exchange? Does increased trade incentivize stationary banditry by conflict actors, thus leading to a reduction in violent extractions? Or is there an entirely different reason that violence decreases when roads are more passable? We provide preliminary responses to such questions. The positive impacts of road projects are significant for one-sided violence using UCDP data, and for violence against civilians and battles using ACLED data. These findings suggest that not all forms of violence are evenly affected by road projects. Second, higher mining revenues affect differently the impact of roads on violence across the types of minerals. The completion of road projects when revenues from artisanal gold mining increase tends to increase the likelihood of violence while the opposite is true for large cobalt mining activities.

## References

Ali, Rubaba, Alvaro Federico Barra, Claudia N Berg, Richard Damania, John D Nash, and Jason Russ, “Infrastructure in Conflict-Prone and Fragile Environments: Evidence from the Democratic Republic of Congo,” World Bank Policy Research Working Paper 7273, The World Bank, Washington, DC 2015.

Bachmann, Jan and Peer Schouten, “Concrete Approaches to Peace: Infrastructure as Peacebuilding,” International Affairs, 2018, 94 (2), 381–398.

\_, Naomi Ruth Pendle, and Leben Moro, “The longue durée of short-lived infrastructure – Roads and state authority in South Sudan,” Geoforum, 2022, 133, 176–184.

\_, \_ , and \_, “The Longue Durée of Short-Lived Infrastructure–Roads and State Authority in South Sudan,” Geoforum, 2022, 133, 176–184.

Bazzi, Samuel and Christopher Blattman, “Economic Shocks and Conflict: Evidence from Commodity Prices,” American Economic Journal: Macroeconomics, October 2014, 6 (4), 1–38.

Berg, Claudia N, Uwe Deichmann, Yishen Liu, and Harris Selod, “Transport Policies and Development,” The Journal of Development Studies, 2017, 53 (4), 465–480.

Besley, Timothy and Torsten Persson, “The Logic of Political Violence,” The Quarterly Journal of Economics, 2011, 126 (3), 1411–1445.


Callaway, B. and P.H.C. Sant'Anna, "Difference-in-Differences with Multiple Time Periods," Journal of Econometrics, 2021, 225 (2).

Conner, Miguel B., Ramon Talvi Robledo, and Dominik J. Wielath, “Leveraging Satellite Imagery to Assess Road Quality in the Democratic Republic of the Congo,” Master’s thesis, Barcelona School of Economics, Barcelona 2023.

Couttenier, Mathieu, Julian Marcoux, Thierry Mayer, and Mathias Thoenig, "The Gravity of Violence," Unpublished Manuscript, September 25 2023.

CRG, “Congo, Forgotten: The Numbers Behind Africa’s Longest Humanitarian Crisis,” Technical Paper, Congo Research Group, New York 2019.

Damania, Richard, Jason Russ, David Wheeler, and Alvaro Federico Barra, “The Road to Growth: Measuring the Tradeoffs between Economic Growth and Ecological Destruction,” World Development, 2018, 101, 351–376.

DFID, “Memorandum of Understanding Between The Department for International Development (DFID), United Kingdom of Great Britain and Northern Ireland and UNOPS - Roads in the East of the Democratic Republic of Congo(DRC) Phase 2, ARIES number 203164,” Official Document, DFID, London 2011.

Eck, Kristine, “In Data We Trust? A Comparison of UCDP GED and ACLED Conflict Events Datasets,” Cooperation and Conflict, 2012, 47 (1), 124–141.


Eycken, H Vander and F Vander Vorst, “Le Blocage de la Croissance en République Démocratique du Congo,” Revue Tiers Monde, 1967, pp. 411–434.

Fairhead, James, “Paths of Authority: Roads, the State and the Market in Eastern Zaire,” The European Journal of Development Research, 1992, 4 (2), 17–35.

Getmanski, Anne, Guy Grossman, and Austin L. Wright, “Border walls and smuggling spillovers,” Quarterly Journal of Political Science, 2019, 14 (3), 329–347.

González, Felipe, Josepa Miquel-Florensa, Mounu Prem, and Stéphane Straub, "The Dark Side of Infrastructure: Roads, Repression, and Land in Authoritarian Paraguay," SSRN Working Paper, 2023.

Harari, Mariaflavia and Eliana La Ferrara, “Conflict, Climate, and Cells: A Disaggregated Analysis,” The Review of Economics and Statistics, October 2018, 100 (4), 594–608.

Hendrix, Cullen S., “Head for the Hills? Rough Terrain, State Capacity, and Civil War Onset,” Civil Wars, 2011, 13 (4), 345–370.

Herbst, Jeffrey, States and Power in Africa: Comparative Lessons in Authority and Control, Vol. 149, Princeton University Press, 2014.

Idler, A., “The Logic of Illicit Flows in Armed Conflict,” World Politics, 2020, 72 (3), 335–376.

Jimenez-Ayora, Pablo and Mehmet A. Ulubaşoğlu, “What underlies weak states? The role of terrain ruggedness,” European Journal of Political Economy, 2015, 39, 167–183.

Juan, Alexander De and Jan H. Pierskalla, “Manpower to coerce and co-opt—State capacity and political violence in southern Sudan 2006–2010,” Conflict Management and Peace Science, 2014, 32 (2), 175–199.

Kivu Security Tracker, “The Landscape of Armed Groups in Eastern Congo,” Kivu Security Tracker 2021. Available online: URL to be added.

Kleinschroth, Fritz, Nadine Laporte, William F Laurance, Scott J Goetz, and Jaboury Ghazoul, “Road Expansion and Persistence in Forests of the Congo Basin,” Nature Sustainability, 2019, 2 (7), 628–634.

Kraay, Aart, “How Large is the Government Spending Multiplier? Evidence from World Bank Lending,” The Quarterly Journal of Economics, 2012, 127 (2), 829–887.

Krauser, Mario, “In the Eye of the Storm: Rebel Taxation of Artisanal Mines and Strategies of Violence,” Journal of Conflict Resolution, 2020, 64 (10), 1968–1993.

la Sierra, Raul Sanchez De, “On the Origins of the State: Stationary Bandits and Taxation in Eastern Congo,” Journal of Political Economy, January 2020, 128 (1), 32–74.

Leysen, Jan, Ken Matthysen, Ntakobajira Zacharie Bulakali, and Thomas Muller, “Analysis of the interactive map of artisanal mining areas in eastern Democratic Republic of Congo (2023 update),” Research Report, International Peace Information Service (IPIS), Antwerp 2023.

Luo, Jie, Guoxiang Wang, Guoli Li, and Giovanni Pesce, “Transport infrastructure connectivity and conflict resolution: a machine learning analysis,” Neural Computing and Applications, 2021, 34 (9), 6585–6601.

Mann, Michael, “The Autonomous Power of the State: its Origins, Mechanisms and Results,” European Journal of Sociology, 1984, 25 (2), 185–213.

Mathebula, Ndzalama C and Mancha J Sekgololo, “Africa-China Relations: A Case of Foreign Direct Investment and the Democratic Republic of Congo’s Mining Sector,” The African Review, 2023, 1 (aop), 1–15.

McGuirk, Eoin and Marshall Burke, “The Economic Origins of Conflict in Africa,” Journal of Political Economy, 2020, 128 (10), 3940–3997.

Moreno, Laura, Jorge Gallego, and Vargas Juan, “More roads, more conflict? The effect of rural roads on armed conflict and illegal economies in Colombia,” Universidad de Rosario Working Paper, 2019, 248, 1–49.

Mueller, Hannes and Christopher Rauh, “The Hard Problem of Prediction for Conflict Prevention,” Journal of the European Economic Association, 2022, 20 (6), 2440–2467.

\_ and \_, “Building Bridges to Peace: A Quantitative Evaluation of Power-Sharing Agreements,” Economic Policy, 2023. Accepted.

–, Dominic Rohner, and David Schönholzer, “Ethnic Violence Across Space,” The Economic Journal, 2022, 132 (642), 709–740.

Muhebwa, Aggrey, Gabriel Cadamuro, and Jay Taneja, “Pixel Perfect: Using Vision Transformers to Improve Road Quality Predictions from Medium Resolution and Heterogeneous Satellite Imagery,” ACM J. Comput. Sustain. Soc., Sep 2023, 1 (1), Article 3.

Müller-Crepon, Carl, Philipp Hunziker, and Lars-Erik Cederman, “Roads to Rule, Roads to Rebel: Relational State Capacity and Conflict in Africa,” Journal of Conflict Resolution, 2021, 65 (2-3), 563–590.

Newbury, M. Catherine, “Ebutumwa Bw’Emiogo: The Tyranny of Cassava A Women’s Tax Revolt in Eastern Zaïre,” Canadian Journal of African Studies / Revue Canadienne des Études Africaines, 1984, 18 (1), 35–54.

Northrup, David, “The Ending of Slavery in the Eastern Belgian Congo,” The End of Slavery in Africa, 1988, pp. 462–82.

Nunn, Nathan and Diego Puga, “Ruggedness: the Blessing of Bad Geography in Africa,” The Review of Economics and Statistics, 2012, 94, 20–36.

O'Mealia, T., “Violence, Protection, and the Political Economy of Security Provision in Ongoing Conflicts.” PhD dissertation, University of Michigan, Ann Arbor, MI 2022.

Pourtier, Roland, “Désorganisation des transports et spirales du sous-développement au Zaïre,” in Chantal Blanc-Pamard, ed., Dynamique des systèmes agraires: politiques agricoles et initiatives locales: adversaires ou partenaires, ORSTOM, 1993, pp. 49–69.

Raleigh, Clionadh and Håvard Hegre, “Population size, concentration, and civil war: A geographically disaggregated analysis,” Political Geography, 2009, 28 (4), 224–238.

\_, Roudabeh Kishi, and Andrew Linke, “Political Instability Patterns are Obscured by Conflict Dataset Scope Conditions, Sources, and Coding Choices,” Humanities and Social Sciences Communications, 2023, 10 (1), 1–17.

Rogall, Thorsten, “Mobilizing the Masses for Genocide,” American Economic Review, 2021, 111 (1), 41–72.

Ross, Michael L., “Oil, Drugs, and Diamonds: The Varying Roles of Natural Resources in Civil War,” in Karen Ballentine and Jake Sherman, eds., The Political Economy of Armed Conflict: Beyond Greed and Grievance, Boulder: Lynne Rienner, 2003, p. Specific page range if available.

Ruggeri, Andrea, Han Dorussen, and Theodora-Ismene Gizelis, “On the Frontline Every Day? Subnational Deployment of United Nations Peacekeepers,” British Journal of Political Science, 2016, 48 (4), 1005–1025.

Sayers, Michael W., Thomas D. Gillespie, and William D. O. Patterson, “Guidelines for Conducting and Calibrating Road Roughness Measurements,” Technical Paper 46, World Bank, Washington D.C. 1986.

Schouten, Peer, “The Materiality of State Failure: Social Contract Theory, Infrastructure and Governmental Power in Congo,” Millennium, 2013, 41 (3), 553–574.

\_, Roadblock Politics: the Origins of Violence in Central Africa, Cambridge University Press, 2022.

\_ and Jan Bachmann, “Roads to Peace? The Role of Infrastructure in Fragile and Conflict-Affected States,” 2017.

\_ and \_, “Infrastructural frontiers: Terrains of resistance at the material edge of the state,” Geoforum, 2022.

\_, Judith Verweijen, Janvier Murairi, and Saidi Kubuya Batundi, “Paths of authority, roads of resistance: Ambiguous rural infrastructure and slippery stabilization in eastern DR Congo,” Geoforum, 2022, 133, 176–184.

Scott, James C., The Art of Not Being Governed: An Anarchist History of Upland South-east Asia, Yale University Press, 2009.

Stearns, Jason, “Involution and symbiosis: the self-perpetuating conflict in the Democratic Republic of Congo,” International Affairs, 2022, 98 (3), 873–891.

Stoop, Nik, Marijke Verpoorten, and Peter Van Der Windt, “Artisanal or Industrial Conflict Minerals? Evidence from Eastern Congo,” World Development, 2019, 122, 660–674.

Thegeya, Aaron, Thomas Mitterling, Arturo Martinez Jr, Joseph Albert Bulan, Ron Lester Durante, and Jayzon Mag-atas, “Application of machine learning algorithms on satellite imagery for road quality monitoring: An alternative approach to road quality surveys,” ADB Economics Working Papers Series, Dec 2022.

Tollefsen, Andreas Forø and Halvard Buhaug, “Insurgency and Inaccessibility,” International Studies Review, 2015, 17 (1), 6–25.

Voigtländer, Nico and Hans-Joachim Voth, “Highway to Hitler,” American Economic Journal: Applied Economics, 2022.

Willame, Jean-Claude, “Zaïre,” L’épopée d’Inga. Chronique d’une Prédation Industrielle, Paris, L’Harmattan, 1986.

World Bank, “Zaire - Third Highway Project,” Technical Paper, World Bank, Washington D.C. 1975.

\_, “Second High Priority Roads Reopening and Maintenance Project (P161877) Project Information Document/Integrated Safeguards Data Sheet (PID/ISDS),” Technical Paper, World Bank Report No: PIDISDSC20608, Washington D.C. 2017.

Zhukov, Yuri M., “Roads and the Diffusion of Insurgent Violence,” Political Geography, 2012, 31 (3), 144–156.

## Appendix A

## A.1 Additional tables

Some first robustness checks are in Table A1. The association for road stocks is remarkably robust. It even holds if we control for province/year fixed effects in columns (2) and (4) in Table A1. Effects are generally stronger within the most recent decade 2010 to 2021.

Table A1: Roads and Armed Conflict (Robustness)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and province/year fixed effects are included in columns (1) to (4). Cell and year-fixed effects are included in columns (5) to (8). The sample is restricted to after 2010 in columns (5) to (8). Events and fatalities are in logs (+1).

As an additional robustness check, we run our analysis with ACLED data (Table A2). Here, the results are generally weaker but have the same point estimate size. Given the significantly different nature of the ACLED data, this is reassuring.

Table A2: Roads and Armed Conflict (Robustness)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year fixed effects are always included. Events and fatalities are in logs (+1).

## A.2 Different types of violence

Table A3: Roads and Armed Conflict Non-state (UCDP)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

## A.3 Ruggedness

We use the average slope variable from Nunn and Puga (2012) to separate PRIO grid cell in cells with high slope and those with little slope. We picked a cut-off of 1.8 for the slope indicator which captures the top 25% most rugged cells. Results are robust to other cut-offs. Our hypothesis was that the effect of road projects in rugged terrain should be larger as roads would make rugged terrain especially more accessible.

We find mixed results. Columns (1) to (4) show results on the overall UCDP and ACLED data. We generally get a negative but significant coefficient. There is some evidence in columns (5) and (6) that the effect of roads for one-sided violence is amplified in the most rugged terrains.

Table A4: Roads and Ruggedness


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1). Columns (1), (2), (5) and (6) use UCDP data. Remaining columns show ACLED data. Rugged terrain are cells are in the top 25% regarding slope.

## A.4 Roads and mines

To better understand the interactions between roads and mining revenue, we construct interaction effects between our road stock measure and the mining revenue proxies. The results for large mines reported in Table A6 are striking: we now get a clear negative sign for road stock itself, and cobalt revenue is positively associated with violence but only without roads. In other words, present or recent road projects mute the effect of Cobalt revenue in the DRC.

Table A5: Roads, Mining Revenue and Armed Conflict


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

Table A6: Interaction of Roads and Mining


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

This finding fits well with the general observation that violent effects will depend critically on the incentives and ability of the potential conflict parties to negotiate and how this changes with mining revenue and road access. Roads here could be a sign of strong economic interest by the central government. Many of the large Cobalt mines are run by Chinese companies, and there is a strong outside interest in keeping them under control. This might lend some commitment power and capacity to the central government, leading to more negotiated solutions to conflicts with rising revenues.

Table A7: Roads, Mining, and one-sided/state violence (UCDP)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

Table A8: Roads, Mining, violence against civilians/battles (ACLED)


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1).

## A.5 The economic channel

Table A9: Roads and Nightlight Emission


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Night lights are normed to be between 0 and 100. In columns (1) to (3) night lights are between 2000 to 2014 and in columns (4) to (6) night lights are between 2012 and 2021.

Table A10: Main Results Robustness to Periods


Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors are clustered at the cell level. Cell and year-fixed effects are always included. Events and fatalities are in logs (+1). Columns (1) to (3) restrict the sample to 2000 to 2015. Columns (4) to (6) restrict the period to 2010 to 2021.

## A.6 Using satellite images for road quality


[[KC_IMAGE_016]]

Figure A1: A sample of five images from each class, as determined by the 5-class classifier.

Predicted Labels by Month with Variability (2-Class)

[[KC_IMAGE_017]]

Figure A2: The mean quality score by month and standard deviation for the road quality classifier.


[[KC_IMAGE_018]]

Figure A3: The predicted labels for the binary classifier are averaged along all segments per year. Here, we show a sample of the points for segments 180, 181, and 182. Note that the data from 2012, 2016, and 2021 correspond to the data shown in Fig. (7).

Quality Discount Factor Estimate (2-Class)

[[KC_IMAGE_019]]

Figure A4: The Figure shows the road quality peak as period 0 and then subsequent measurements in years 1 to 10 after that peak. Each point represents a binned quality prediction for a single year for one road segment. Each segment has a different color. The different dashed curves serve to represent the same decay rate but from different starting points.

## Appendix B: A new panel of road investments

Significant investments in the Democratic Republic of Congo (DRC) have been made since 2000, particularly focused on large infrastructure projects around 2010. Yet, there seems to be a lack of quantitative evidence on their benefits, partly due to the lack of available granular data on these infrastructure projects. An important contribution of this paper is the construction of the first panel of road investments in the DRC since 2002. We collect data from multiple sources to create the first database that gathers the exact location, timing, and amount spent on transport projects since 2000. First, we create a database of road transport projects in DRC. Second, we geolocalize as many investment projects as possible. Third, we create a panel of data that can be used with the rest of the data.

## B.1 Create a database of road transport projects

We rely on multiple sources of information: universities (William & Mary, Boston University & Johns Hopkins), government bodies (Plateforme de Gestion de l'Aide et des Investissements, Cellule Infrastructure), and donors' websites (World Bank, ADB).

## 1. AidData – DRC AIMS Geocoded Research Release, Version 1.3.1 $^{1}$


2. AidData – AidData’s Geocoded Global Chinese Official Finance, Version 1.1.1 $^{2}$

This dataset geolocates Chinese government-financed projects that were implemented between 2000 and 2014 globally. It captures 3,485 projects worth \$273.6 billion in total official financing. The dataset includes both Chinese aid and non-concessional official financing. All sectors are covered. The second major contribution from AidData is their geocoded China dataset from 2018. The dataset complements the first AidData database and includes project-level locations for each project. This is one of the most thorough collections of spatial data on China's activities in DRC. China is one of the world's largest official creditors, yet its activities are often opaque and not publicized. All data in this dataset were collected using AidData's Tracking Underreported Financial Flows (TUFF) methodology, version 1.34. The methodology has been used for AidData's 2021 paper named How China Lends, which seeks to systematically analyze how Chinese lenders have been engaging with the developing world. The database includes 39 projects total for DRC, but only 3 projects are related to “Transport and Storage”.

## 3. Plateforme de Gestion de l'Aide et des Investissements (PGAI) $^{4}$

This is a centralized platform of all aid activities in DRC which was launched by the Congolese government in 2008. Up until 2014, AidData - AIMS and PGAI are understood to have shared the same source, which is the data from the Congolese Ministry of Planning and a technical provider named Development Gateway. The geocoded data were collected through direct engagement by Development Gateway and AidData, with collaboration from the Ministry of Planning to seek higher transparency and improve the GIS aid mapping efforts for DRC. Since the web access for PGAI has been spotty and often not functional at all, our team has reached out to the contacts at PGAI for their back-end database of all aid projects in DRC.

We were provided with historical and most current project-level information pertaining to four sectors: water, transport, communications, and energy. There are \$547 million in total commitments for the 94 non-geocoded projects in DRC from 2014 to the present.

## 4. Cellule Infrastructure $^{4}$

The Cellule Infrastructure is a technical body of the Ministry of Infrastructure, Public Works and Reconstruction (MITPR) in DRC, with administrative and financial autonomy. The general mandate of the CI is sectoral coordination and institutional support to the MITPR, mainly in its project management role. It provides an advisory service to MITPR in the design, implementation, and monitoring of investments in the infrastructure sector. While the Cellule Infrastructure data (2021) contained many new road segments that were not present in our existing data, it lacked important information such as start/end years, donors, nature of work, and committed investment amount. This made it challenging to determine whether the data were repetitive with other sources accurately.

## 5. World Bank

The World Bank's own Projects and Operations website has a download function that provides the back-end project information for all World Bank projects pertaining to specific search criteria. It is one of the most up-to-date information on the World Bank's 125 projects in DRC since 2000. This dataset includes most of the GEMS projects, as well as the 47 AidData World Bank projects, which were published in their World Bank Geocoded Release v.1.4.2 dataset. The website's database is, therefore, the most expansive in its time coverage (includes all historical data up to the latest) and contains the most updated collection of the World Bank's activities in DRC.

## 6. World Bank Geo-Enabling initiative for Monitoring and Supervision (GEMS) $^{5}$

The GEMS dataset originally came with a list of 15 unique World Bank projects and their locations on a coordinate level. Each project is associated with a precise list of locations where it happened. Road investments are reported as a long series of points along the road segment. For example, a single project, such as P128887, comes with 3772 rows of precise coordinates. This is in stark contrast with the level of precision offered by AidData, which only provides locations at the administrative level. However, most projects were not road investments or were repetitive. We use these data to double-check other sources of information.

## 7. African Development Bank (ADB)

The data portal from ADB contains downloadable project information on all historical and current aid activities in the DRC. One thing to note is the currency used, which is the UA/IMF Special Drawing Rights (SDR).

## 8. BU China Loans


Most of the work consisted of bringing together sparse information about road transport projects in DRC in one unified database and cross-checking the data using multiple sources of information. In addition to the information extracted from the previous sources, updates were added mostly by extensive online search. When the sector categorization was not complete, multiple rounds of search were conducted to include not only projects with the word road in its title but also broader projects with a main transport component, such as the "DRC Agriculture Rehabilitation and Recovery: Additional Financing (P159037)". Lastly, we worked on avoiding duplicates.

## B.2 Create road segments based on the Excel list and merge with the main dataset

Most of the previous sources of information do not provide the exact location of the project. The following steps were undertaken to create road segments in the shapefile based on the updated and added road projects from the previous list.

1. Identifying city/village names: The first step involved identifying at least two city/village names that would serve as the start and end points for each road segment. Some project titles already included this information, such as "Kavumu-Kalahe-Goma." However, many projects lacked location information in their titles, which is why some of the projects could not be georeferenced in the shapefile.

2. Researching project location information: For projects without location information, extensive research was conducted on project information papers, contracts, and other relevant documents. The aim was to gather the necessary city or village names required to create the road segment.

3. Inserting latitude and longitude columns: To create a geospatial dataset compatible with tools like QGIS, latitude and longitude columns were inserted for each city or village identified in the previous steps.

4. Connecting the start/end points in QGIS.

5. Merging the newly created road segment layers into one layer: Merge all the newly created project-based layers into one vector file.

## B.3 Create a panel of roads

We finally use the geolocated road segments to create a panel data set in three steps:

1. Join Road Investment shapefile with the PRIO grid cell.

2. Calculate the length of road segment per each cell grid

3. Create a time-series format with dummy variables.

We include projects whose status is completed or ongoing and remove projects whose status is dropped or suspended. One limitation is that some projects could not be included in the panel dataset as they were missing either one or both start/end year values.

## B.4 Statistics and maps

The final list of road investments includes 192 projects; among them, 113 have start and end years, have a commitment amount, and are not classified as dropped or suspended. The following statistics apply to these 113 projects. Figures A5, A6, and A7 report the distribution of the number of projects by the starting year, the end year, and their duration. The average starting year is 2010, the year with the largest number of infrastructure projects that started. The average duration of projects is 3 years, with a large number of projects lasting less than a year.

Figures 4 and A8 map the location of all road investments that have been geolocalized and the investments by the donor (China, World Bank, UNOCHA, Belgium, etc.). The latest shows that most Chinese investments are located in the South, while World Bank investments are focused on the East and Northern parts of the country.


[[KC_IMAGE_020]]

Figure A5: Number of projects by starting year


[[KC_IMAGE_021]]

Figure A6: Number of projects by end year


[[KC_IMAGE_022]]

Figure A7: Number of projects by duration


[[KC_IMAGE_023]]

Figure A8: Map of geolocalized projects by donor

## B.5 Delays in World Bank projects

The following extracts come from the Implementation Completion Report (ICR), a World Bank document that closes a project by reviewing and assessing all the issues encountered during the project. This document provides the reasons why projects are delayed. For each of the following road projects from our final list, we highlighted some of the main reasons listed in ICRs explaining delays in the completion of the project.

## 1. High Priority Reopening and Maintenance Project (P101745)

“the delay in the execution of the works that were suspended for about a year after the suspension of Pro-Routes.”

"On November 27, 2017, the Bank suspended its disbursements for all road works financed under the Project due to the Borrower's noncompliance with its obligations to carry out the Project in conformity with appropriate environmental and social standards and practices, including management of gender-based violence (GBV), and to minimize the risk of additional harm to Project-affected people. The lifting of the suspension of IDA disbursements was approved on December 10, 2018, following a review that all conditions set out in had been met for works to re-start in full compliance with World Bank policies and safeguards obligations.”

“Project delivery was severely delayed by 28 months, delaying benefits to the population.”

“Slow pace of adoption of policies and institutional reforms. Delays were observed in the completion of numerous tasks connected to institutional capacity because of the weak capacity of the MIPWR, OdR, and other institutions that were responsible to review, endorse, or issue decisions concerning various activities under Component 2. Numerous institutional weaknesses were documented during implementation, including the capacity of DRC’s SMEs which requested a heavy capacity-building program to overcome the challenges to contribute effectively to the implementation of Pro-Routes. 68. Delays in the procurement process. Generally, the procurement office of the CI has been able to prepare and issue contracts for road reopening works. However, recurrent delays occurred in preparing bidding documents and contracting supervision firms. The lapse between the signing of the contracts for works and those related for monitoring resulted in considerable delays in the implementation and takeover of completed works, resulting in a Moderately Satisfactory procurement rating for CI up to AF2.”

## 2. Emergency Urban and Social Rehabilitation Project

"The extension was not triggered by the AF activities but due to delays with implementing the Roads and Water Components caused by technical difficulties and time taken to manage the resettlement process"

“During implementation, it transpired that the studies were more outdated than could have been expected, which did result in some delays.”

3. Dem Rep Congo - Western Growth Poles (P124720)

“Other important events include: (i) delays in getting SEZ legal framework in place, particularly the adoption of SEZ law (only completed in 2014)”

“because of non-adherence to WB safeguard standards with regard to resettlements and compensation of owners being displaced because of the establishment of the SEZ plus absence of an Environment and Social Management Plan - ESMP linked to the construction by the Government of a wholesale market, also was responsible for delays in project execution. 20.”

"The efforts made by the management team allowed to: (i) reduce the range of some activities; (ii) overcome the delays and difficulties encountered during the first years of implementation;"

“slow start of activities due to procurement delays with low disbursements”

4. DRC Urban Development Project FY13 (P129713)

“operational efficiency was encumbered by lengthy project implementation and delays to launch investments, in large part explained by limited capacity in the PS responsible for project implementation and multiple changes to project management. The organization of the 2018 elections (including for local government) and government reshuffles led to tensions in the country and delays in the delivery of project activities. For instance, the reshuffle of mayors and governors seriously affected the implementation of the performance-based contract, while the changes of ministers at the central level often led to changes in leadership within the PS, with ministers opting to nominate a confidant to lead the PS.”

5. Democratic Republic Of Congo Emergency Social Action Project P086874 Large Implementation delays
