## OECD Education Working Papers No. 348
# OECD EDUCATION WORKING PAPERS SERIES

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.


This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.


## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this license (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Abstract

This paper applies the Collective Intelligence Model for Education (CIME) to Thailand's Programme for International Student Assessment (PISA) 2022 mathematics data and assessment materials to generate fine-grained diagnostic evidence for curriculum review and instructional support. The study combines AI-assisted scoring, expert review and psychometric scaling, using bilingual item-facet rubrics with Thai serving as the operational scoring language. The resulting profiles examine student performance across 12 content topics and 17 cognitive operators. Findings indicate relative strengths in geometry-related content, measurement, estimation, Chance and probability, and selected procedural tasks. More demanding areas include Formulating situations mathematically, interpreting results in context, recognising functional relationships, and working with algebraic, functional and data-representation content. The analysis also identifies limited gender differences in most areas, alongside substantial variation by economic, social and cultural status. Overall, the paper shows how large-scale assessment data can be translated into competency-oriented evidence for Thailand's ongoing education reform.

## Acknowledgements

This paper was prepared by Tomoya Okubo (OECD) and Fabrice Blais-Savoie (OECD) as part of the project Developing an International Large-Scale AI Tool for Educational Assessment and Personalised Learning, undertaken within the Programme of Work of the OECD Centre for Educational Research and Innovation (CERI). The authors are grateful to their OECD colleagues Elizabeth Fordham, Caitlyn Guthrie and Lucia Alonso for their insightful contributions and discussions. They also thank Masaki Uto and Yoshimitsu Miyazawa for their valuable expert feedback and comments. The authors would further like to thank officials at Thailand's Institute for the Promotion of Teaching Science and Technology for their feedback on earlier versions of this paper. Finally, they wish to thank Rachel Linden for editorial and publication support.

## Table of contents

OECD EDUCATION WORKING PAPERS SERIES 2
Abstract 3
Acknowledgements 4
1 Introduction 7
Background and rationale 7
Study objectives and analytical focus 7
Thailand in PISA 2022 mathematics 8
2 Methodological framework and study design 10
Analytical foundations of the CIME model 10
Adaptation of the framework to Thai-language assessment materials 11
Construct specification and rubric development 11
Scoring procedures, scaling and profile estimation 12
3 Profile analysis of mathematics in Thailand: PISA 2022 14
Structural dimensions of the mathematics profile 14
Patterns of performance across cognitive operators 14
Patterns of performance across content topics 19
4 Variation in mathematics performance profiles by gender and ESCS 22
Differential performance by gender in cognitive operators 22
Differential performance by gender in content topics 24
Differential performance by ESCS in cognitive operators 25
Differential performance by ESCS in content topics 28
5 Discussion and policy-relevant implications 30
Substantive insights from the Thai-language application of CIME 30
Implications for curriculum design and implementation 31
Analytical boundaries with respect to curriculum and policy evaluation 32
6 Conclusion 34
References 35
Annex A. Cognitive operators and content topics 38

## FIGURES

Figure 1. Performance across Formulating situations mathematically 16
Figure 2. Performance across Employing mathematical concepts, facts and procedures 17
Figure 3. Performance across Interpreting, applying and evaluating mathematical outcomes 18
Figure 4. Performance across Mathematical reasoning 19
Figure 5. Performance across content topics 21
Figure 6. Gender differences in score across cognitive operators 23
Figure 7. Gender differences in score across content topics 25
Figure 8. Score differences between $1^{\text{st}}$ and $4^{\text{th}}$ quartile ESCS groups across cognitive operators 27
Figure 9. Score differences between $1^{\text{st}}$ and $4^{\text{th}}$ quartile ESCS groups across content topics. 29

## TABLES

Table 1. Mathematics and subdomain scores for Thailand and the OECD average in PISA 2022 9
Table 2. Scores by Cognitive operator and the difference from overall mathematics score 15
Table 3. Scores by content topic and differences from overall mathematics score 20
Table 4. Scores by cognitive operator and gender 23
Table 5. Scores by content topic and gender 24
Table 6. Scores by cognitive operator and ESCS group 27
Table 7. Scores by content topic and ESCS group 28
Table 8. Cognitive operators in Formulating situations mathematically 38
Table 9. Cognitive operators in Employing mathematical concepts, facts and procedures 38
Table 10. Cognitive operators in Interpreting, applying and evaluating mathematical outcomes 39
Table 11. Cognitive operators in Mathematical reasoning 39
Table 12. Content topics in Mathematical literacy 40

# 1 Introduction

## Background and rationale

Since enshrining access to education in its 1997 constitution and implementing compulsory education in its 1999 National Education Act, Thailand has transformed its education system into a regional paragon of education access (Das and Narayanan, 2023[1]; OECD and UNESCO, 2016[2]). As access has expanded, policy attention has increasingly focused on the quality, relevance and equity of learning opportunities. Previous studies and policy reviews have identified several areas that are central to this agenda, including curriculum design, student assessment, teacher preparation and school leadership (Fry and Bi, 2013[3]; OECD and UNESCO, 2016[2]; World Bank, 2024[4]; OECD, 2025[5]). These areas are closely related to Thailand's broader skills agenda, as initial education plays an important role in helping young people acquire foundational skills, develop higher-level competencies and build positive attitudes towards lifelong learning (OECD, 2025[5]). Recent evidence on foundational skills among youth and adults also underlines the importance of strengthening reading literacy, digital skills and socio-emotional skills as part of a broader learning agenda (World Bank, 2024[4]).


This analysis comes at an important moment for Thailand's education system, around the midpoint of the National Scheme of Education and during an ongoing period of curriculum review. In line with recent OECD analytical work, the study uses more granular assessment information to complement aggregate performance indicators and examine students' mathematical proficiency in relation to specific content areas and cognitive processes. By providing diagnostic evidence closer to curriculum design and classroom practice, the analysis can support Thailand's ongoing work on competency-based education and contribute to the evidence base for monitoring future curriculum implementation.

## Study objectives and analytical focus

This study aims to provide Thailand's policymakers, curriculum developers, assessment specialists and teachers with diagnostic evidence that can inform curriculum review, instructional planning and targeted student support. Building on the Collective Intelligence Model for Education (CIME) approach applied in the analysis of Ireland's PISA 2022 mathematics profile, this study uses student item-response data and assessment materials to translate large-scale assessment data into multidimensional competency profiles (Okubo and Reinertsen, 2025[8]). In the Ireland application, CIME (Okubo, 2025[9])

complemented within-country analysis with more granular learning progressions analysis and generated fine-grained, policy-relevant diagnostics. In the Thai context, a similar approach can help identify mathematical content areas, cognitive processes and transversal competencies in which students show relative strengths, as well as areas where additional instructional support may be beneficial. It complements conventional analysis with an educationally interpretable framework that is more closely aligned with curriculum design and classroom practice.

This paper analyses Thailand's PISA 2022 mathematics data and assessment materials to provide system-level, competency-specific insights into students' mathematical proficiency. The analysis builds on the PISA 2022 assessment and sampling design, which provides comparable information on 15-year-old students' knowledge and skills and is accompanied by technical procedures intended to support the validity and reliability of the results (OECD, 2024[10]). Since mathematics was the major domain of PISA 2022, the assessment provides a particularly rich basis for examining students' mathematical literacy across content areas, processes and contexts. By linking these data to the CIME analytical framework, the study seeks to make visible patterns of proficiency that may not be apparent from overall mathematics scores alone.

This type of diagnostic evidence is particularly relevant to Thailand's current reform context. Curriculum design in Thailand is guided at the national level, while curriculum implementation, assessment practices and teacher professional learning involve multiple administrative levels and institutional actors (OECD and UNESCO, 2016[2]). A competency-oriented analysis of large-scale assessment (LSA) data and materials can therefore provide a shared evidence base for dialogue among national agencies, education service areas, schools and teachers. It can also support the use of large-scale assessment evidence for more targeted purposes, including the refinement of curriculum materials, the development of teacher guidance, the design of formative assessment resources and the prioritisation of professional learning.

The study also has an equity-oriented analytical focus. By translating large-scale assessment results from international scores into competency-oriented profiles, the analysis can examine whether patterns of mathematical proficiency vary across students and help inform differentiated support, moving beyond broad performance categories. More generally, the study aims to make LSA evidence more actionable for educators by presenting results in an educational language linked to competencies, learning progressions and classroom practice. In this way, it contributes to Thailand's ongoing work on competency-based education by providing a bridge between international assessment data, curriculum priorities and the instructional decisions that shape students' learning opportunities.

## Thailand in PISA 2022 mathematics


Table 1 provides a more detailed view of Thailand's mathematics profile in PISA 2022, as presented in OECD (2023[12]). Thailand's overall mathematical literacy score was 393.9 points, compared with the OECD average of 472.4 points. Across the Cognitive Processes, Thailand's scores were relatively closely clustered around the overall mathematics score, suggesting a broadly balanced mathematical profile. As for content areas, Uncertainty and data appears as a content area that may merit closer examination, particularly in relation to students' opportunities to work with data, probability, variation and statistical reasoning.

Table 1. Mathematics and subdomain scores for Thailand and the OECD average in PISA 2022


Source: OECD (2023), PISA 2022 Results (Volume I), https://doi.org/10.1787/53f23881-en. Table I.2.7. Comparing countries and economies on the mathematics-process subscales

Between 2018 and 2022, the performance gap between students at the higher and lower ends of Thailand's mathematics performance distribution narrowed (OECD, $2023_{[12]}$ ). However, the underlying trend suggests declining performance by high-performers, while low-performers remained resilient. Nevertheless, over the same period, the proportion of students performing below Level 2, the PISA baseline proficiency level, increased by 19 percentage points in mathematics and science, and by 32 percentage points in reading (OECD, $2023_{[12]}$ ). These developments have contributed to wider scholarly and policy discussions on how large-scale assessment evidence can be interpreted and used to support education improvement (Rowley et al., $2019_{[13]}$ ; OECD, $2023_{[11]}$ ; UNESCO, $2023_{[14]}$ ; Alali and Wardat, $2024_{[15]}$ ). For Thailand, the relatively even profile across most mathematics subdomains, together with the descriptive difference observed in Uncertainty and data, points to the potential value of a more granular competency analysis to obtain insights more relevant to curriculum design, teacher professional learning and targeted support for students.

# 2 Methodological framework and study design

## Analytical foundations of the CIME model

This section describes the analytical framework used to generate fine-grained profiles of mathematics performance in Thailand using PISA 2022 response data and assessment materials. The analysis applies the Collective Intelligence Model for Education (CIME), an AI-enhanced assessment modelling framework that combines expert judgement, large language models (LLMs) and psychometric scaling to extract multidimensional evidence from student responses and assessment materials (Okubo, 2025[9]). The objective is to complement the assessment reports that focus on overall scores with more detailed diagnostic information on the mathematical content and cognitive operations reflected in students' responses.

CIME treats each item response as potential evidence of multiple underlying competencies. Rather than assigning a response only to a single overall correctness category, the framework decomposes assessment items into item-facet rubrics. Each rubric corresponds to a specific construct, such as a mathematical content topic or a cognitive operator, and specifies the observable evidence required to infer different levels of achievement for that construct. In this way, a single response can contribute evidence to several proficiency dimensions. In this study, some cognitive operators are more frequently associated with items of higher difficulty; however, such item characteristics are taken into account when estimating proficiency scores.

The PISA 2022 mathematics framework defines mathematical literacy as the capacity to reason mathematically and to formulate, employ and interpret mathematics in order to solve problems in a variety of real-world contexts (OECD, 2023[16]). Consistent with this framework, CIME analysis focuses on content topics and cognitive operators that can be linked both to assessment evidence and to curriculum-relevant interpretation. The proficiency scores used in this study are estimated using item response theory (Lord and Novick, 1968[17]), which accounts for item characteristics such as item difficulty when locating students on the proficiency scale. In the CIME framework, the relevance of a cognitive operator to a given item can also be represented through a discrimination-like parameter: cognitive operators that are more central to the solution process provide stronger evidence for the corresponding proficiency dimension. This mechanism is analogous to the way item parameters are used in estimating domain-level cognitive proficiency, while extending the interpretation to finer-grained constructs within mathematics.

A central feature of CIME is its expert-in-loop methodology. LLMs are used as part of a constrained scoring process, but they do not independently define constructs, generate final rubrics, or produce scores that are accepted without review. Human experts supervise the LLM outputs, examine ambiguous and borderline cases, refine scoring rubrics, and validate the resulting scales. The role of AI is therefore complementary: it supports the scalable and systematic processing of large volumes of responses, while expert judgement and psychometric checks address the limitations of automated scoring.

This expert-in-loop design is important in light of recent work on AI-assisted scoring in international large-scale assessments. This work has shown the promise of AI-assisted scoring, but also points to methodological challenges such as translation quality, human-machine disagreement, scoring-guide ambiguity, prompt complexity, hallucination risk, fairness, and validity. For example, Jung, Tyack and von Davier (2024[18]) examined the value of pre-emptive machine translation and artificial neural networks to score multilingual constructed responses, while Jung, Tyack and von Davier (2025[19]) considered automated scoring as a secondary quality-control mechanism in multilingual scoring – both in the context of the Trends in International Mathematics and Science Study (TIMSS) (TIMSS & PIRLS International Study Center, 2026[20]); in a different assessment context, Jung, Bezirhan and von Davier (2025[21]; 2026[22]) examined input optimisation and prompt compression for LLM-based scoring of reading assessment responses. CIME addresses these issues through a different modelling logic: LLM outputs are treated as provisional and are iteratively reviewed, corrected and refined through expert supervision and psychometric validation.

## Adaptation of the framework to Thai-language assessment materials

The application of CIME to Thailand required adapting the analytical workflow to the Thai PISA 2022 assessment context while preserving alignment with the international PISA mathematics framework. In this study, scoring rubrics were generated in both English and Thai. The English rubrics supported alignment with the PISA framework, item metadata and international construct terminology. The Thai rubrics supported scoring in the language in which students encountered the items and expressed their Mathematical literacy.

This bilingual rubric-generation process followed a Thai-centred logic. The PISA framework and item metadata provided the construct definitions, while the Thai item texts and Thai student responses informed the observable indicators used in scoring. Experts reviewed the English and Thai versions to ensure that the Thai rubrics preserved the intended construct meaning while also capturing the linguistic, symbolic and explanatory features of Thai student responses.

This design differs from multilingual automated-scoring approaches that translate responses into a common scoring language before scoring. Such approaches can be valuable when the objective is to develop a scalable scoring pipeline across multiple countries and languages, as done in some TIMSS-related studies (Jung, Tyack and von Davier, 2024[18]). At the same time, recent evidence suggests that multilingual language models can perform robustly in automated-scoring contexts, indicating that translation into a common scoring language may not always be necessary (Okubo et al., 2023[23]). The present study has a different analytical purpose: to generate diagnostic profiles from Thai-language items and Thai student responses. By analysing item content, rubric descriptors and student responses in Thai, the study aims to preserve construct meaning in the language of assessment and reduce the risk that evidence of competence is altered or obscured through translation. This approach is especially relevant for this analysis as the principal target is domestic. If the model is to be used for international comparisons, an additional layer of validation should be conducted to examine whether language-related factors affect scoring outcomes.

## Construct specification and rubric development

Construct specification was guided by the PISA 2022 mathematics framework and by the CIME procedure applied in the Ireland study. The analysis distinguishes between two main families of constructs: cognitive operator constructs and content-related constructs. cognitive operator constructs describe the mathematical actions students are expected to perform when engaging with an item, while content-related constructs describe the mathematical knowledge, concepts and ideas involved. The full set of cognitive operators is reported in Tables 8-11, and the content topics are reported in Table 12, all in Annex A. To note, these operators and topics were provided as guidance for the development of items in the PISA 2022 assessment framework and thus purposefully not ranked in difficulty or evenly represented in the test (OECD, 2023[16]).

For each item, relevant content topics and cognitive operators were operationalised through bilingual item-facet rubrics. Per the PISA ternary marking approach, each rubric described the observable response evidence required to classify a response as providing insufficient (0), partial (1) or sufficient (2) evidence of achievement for the targeted construct.

The CIME rubrics were not intended to reproduce the original assessment scoring guides. Rather, they provide additional diagnostic layers by identifying whether a response demonstrates a targeted mathematical idea or cognitive action. The original assessment scores remain the basis for official PISA reporting, while the CIME rubrics are used to generate complementary construct-level information for diagnostic analysis.

Rubric development followed an iterative expert-in-the-loop process. Initial English and Thai rubrics were generated using the PISA framework descriptors, item metadata, item materials and observed student response patterns. These rubrics were then applied to Thai student responses, and the resulting AI-assisted scoring outputs were reviewed by experts. Where the review identified ambiguous descriptors, inconsistent scoring patterns, insufficient evidence criteria or disagreement between the intended construct and model output, the rubrics and decision rules were revised. This iterative review ensured that AI-assisted outputs were treated as provisional evidence and were retained only when they supported substantively meaningful and psychometrically stable item-facet scores.

Constructs were retained for substantive analysis only when they were represented by sufficient item and response evidence to support stable interpretation. Specifically, cognitive operators and content topics represented by fewer than eight items were excluded from the reported construct-level analysis. In addition, item-facet combinations with fewer than 200 valid responses were excluded before scaling and profile estimation. These inclusion criteria were applied to improve the stability and interpretability of the resulting proficiency estimates.

## Scoring procedures, scaling and profile estimation

Each response–item-facet combination was scored multiple times using distinct model configurations. The models selected were GPT 5.4 mini ("reasoning" = Medium), Mistral 3 Large, Deepseek V4 Flash, and Kimi K2.6 (all three, "temperature" = 0.7, "topP" = 0.3). This repeated-scoring design was used to examine the stability of AI-assisted scoring and to reduce dependence on the output of any single model. Generalisability theory (Brennan and Johnson, 1995[24]; Brennan, 2001[25]) was used to evaluate the reliability of the scoring process by estimating the extent to which score variation was attributable to substantive differences in student responses, item facets, scoring configurations, and residual error. In this analysis, the variance component attributable to the LLM model facet was 1.2%, indicating that the choice of LLM explained little variation in the scores. The largest source of variance was the student-by-item interaction term (41.5%), followed by students (19.5%) and items (7.5%). These findings suggest that a substantial proportion of score variation can be explained by differences among students and items, as theoretically expected.

Where the repeated-scoring outputs showed sufficient stability, final item-facet scores were assigned using the modal category across scoring occasions. During the factor structure validation process, scoring rubrics with negative factor loadings were excluded from subsequent analyses. Based on this criterion, 12% of the item-by-facet rubrics were removed. These results provide evidence supporting the validity of the scoring rubrics and the consistency of the scores generated by the LLMs.

The resulting item-facet scores were scaled using item-response theory. Item-facet parameters were estimated using a generalised partial credit model (Muraki, 1992 $^{[26]}$ ). The CIME-derived scales should be interpreted as diagnostic extensions of the mathematics assessment rather than as new international scales: they use PISA mathematics scale as an anchor but introduce finer-grained construct definitions at the level of content topics and cognitive operators. The results are therefore best interpreted as within-country profiles of relative performance across constructs, rather than as replacements for the published mathematics results.

Population-level proficiency profiles were estimated using procedures aligned with large-scale assessment practice. Plausible values (PVs) were generated for each retained construct, final student weights were applied and standard errors were estimated to reflect the sampling design. When subgroup analyses were conducted, the same procedures were used to estimate profiles by gender and by economic, social and cultural status (ESCS).

Several consistency checks were conducted before the results were interpreted. Population means derived from PVs were compared with estimates from the underlying scaling model; subgroup means were checked across estimation procedures; and residual distributions from the latent regression model were examined to identify potential sources of systematic bias (Okubo, 2022[27]). Constructs and item facets showing unstable scoring behaviour or insufficient empirical support were reviewed before inclusion in the final reporting set.


# 3 Profile analysis of mathematics in Thailand: PISA 2022

## Structural dimensions of the mathematics profile

This section introduces the structure of the fine-grained mathematics profile estimated for Thailand using the Collective Intelligence Model for Education (CIME). Building on the methodological framework described in Section 2, the analysis reports performance across retained content-topic and cognitive-operator scales.

The reporting framework is organised into five reporting groups: one group of content-topic scales and four groups of cognitive-operator scales corresponding to the four PISA 2022 mathematical processes. After applying the inclusion criteria described in Section 2, the reported profile includes 12 content-topic scales and 17 cognitive-operator scales. The cognitive-operator scales comprise four operators under Formulating situations mathematically, Employing mathematical concepts, facts and procedures, and Mathematical reasoning, and five under Interpreting, applying and evaluating mathematical outcomes.

The results should be read as a diagnostic profile of constructs that could be estimated with sufficient empirical support. The full set of cognitive operators and content topics used to structure the analysis is reported in Annex A, while the results in this section focus on the constructs that met the study's minimum evidence requirements. This distinction helps preserve transparency about the broader analytical framework while reducing the risk of overinterpreting constructs with limited item or response coverage.

All results in this section are reported on the PISA mathematics scale. In Tables 2 and 3, $\Delta$ indicates the difference between each cognitive-operator score and Thailand's overall mathematics score of 393.9. Positive $\Delta$ values indicate performance above the national mathematics mean, while negative values indicate performance below that mean.

## Patterns of performance across cognitive operators

Thailand's performance across cognitive operators in PISA 2022 mathematics is presented in Table 2 and Figures 1-4. Across the cognitive operators, Thailand's scores range from 382.0 to 402.0, giving a spread of 20.0 score points. The highest score is observed for Selecting an appropriate strategy from a list (402.0, $\Delta = 8.1$ ), while the lowest score is observed for Recognising functional relationships between quantities (382.0, $\Delta = -12.0$ ). Overall, the profile suggests relative strengths in selecting strategies from given options, making generalisations from procedures, and using mathematical and computational thinking. Relative weaknesses are more evident in representing situations mathematically, interpreting mathematical results in real-world contexts, identifying mathematical structures, and recognising functional relationships. Although these may be meaningful differences, only three are significant (Table 2)

Table 2. Scores by Cognitive operator and the difference from overall mathematics score


\*, \*\* denote the statistical significance of $\Delta$ at the 10% and 5% levels, respectively.

## Performance profiles in Formulating situations mathematically

Figure 1 presents the cognitive-operator scores for Formulating situations mathematically. This process shows a relatively negative profile, with all operators below the overall mean.

The highest score within this process is for identifying the mathematical aspects of a problem situated in a real-world context (390.4, $\Delta = -3.6$ ). The remaining operators show slightly larger negative differences: selecting an appropriate model from a list (389.0, $\Delta = -5.0$ ), representing a problem in a different way, including organising it according to mathematical concepts (389.0, $\Delta = -5.0$ ), and Representing a situation mathematically using appropriate variables, symbols, and diagrams (387.8, $\Delta = -6.2$ ).

The results suggest the possibility of particular difficulty in transforming contextual problems into mathematical forms. Although students perform somewhat better when asked to identify mathematical aspects in real-world situations, they appear less secure when required to construct or reorganise mathematical representations. The lowest score in this group, for representing a situation mathematically, points to a relative challenge in encoding situations through variables, symbols, diagrams, or other mathematical structures.

Figure 1. Performance across Formulating situations mathematically

[[KC_IMAGE_001]]


## Performance profiles in Employing mathematical concepts, facts and procedures

Figure 2 shows the results for the cognitive operators of Employing mathematical concepts, facts and procedures. Compared with the Formulating process, this set of operators displays a more positive profile.

The strongest result in this process is for Selecting an appropriate strategy from a list (402.0, $\Delta = 8.1$ ). This is also the highest score among all cognitive operators reported in Table 2. Students also perform above the overall mathematics score on Making generalisations and conjectures based on the results of applying mathematical procedures to find solutions (399.2, $\Delta = 5.3$ ). Drawing a simple conclusion is close to the overall mathematics score (394.5, $\Delta = 0.6$ ), while Using and switching between different representations in the process of finding solutions is slightly below it (393.4, $\Delta = -0.6$ ).

These results suggest that Thai students perform relatively well when the task requires them to choose a strategy from available alternatives or extend results from mathematical procedures. The profile is less strong for moving flexibly between representations, but the difference from the overall mathematics score is small. Taken together, the Employing results indicate that students are comparatively more successful when working within already established mathematical procedures than when initially formulating a situation mathematically.

Figure 2. Performance across Employing mathematical concepts, facts and procedures

[[KC_IMAGE_002]]


## Performance profiles in Interpreting, applying and evaluating mathematical outcomes

Figure 3 presents the profile for the cognitive operators of Interpreting, applying and evaluating mathematical outcomes. The results for this process are mixed. One operator is clearly above the overall mathematics score, while several others fall below it.

The highest score in this group is for Using mathematical thinking and computational thinking (399.7, $\Delta = 5.8$ ). This indicates a relative strength in applying mathematical and computational reasoning. In contrast, the other operators in this process are below the overall mathematics score. The largest negative difference is observed for Interpreting a mathematical result back into the real-world context (388.4, $\Delta = -5.6$ ). Other lower-scoring operators include Interpreting information presented in graphical form and/or diagrams (389.2, $\Delta = -4.9$ ), Evaluating the reasonableness of a mathematical solution in the context of a real-world problem (389.9, $\Delta = -4.1$ ), and Evaluating a mathematical outcome in terms of the context (392.6, $\Delta = -1.4$ ).

The profile suggests that Thai students show relative strength in mathematical and computational thinking, but experience more difficulty when mathematical results must be connected back to contextual meaning. In particular, the lower score for interpreting a result in a real-world context indicates that students may find it challenging to move from a mathematical answer to an interpretation of what that answer means in the situation described by the problem. The results therefore point to a distinction between carrying out Mathematical reasoning and evaluating or explaining the result in relation to context.

Figure 3. Performance across Interpreting, applying and evaluating mathematical outcomes

[[KC_IMAGE_003]]


## Performance profiles in Mathematical reasoning

Figure 4 reports the scores for the cognitive operators of Mathematical reasoning. This process shows the widest contrast between relative strengths and weaknesses.

The highest score in Mathematical reasoning is for Using mathematical modelling as a lens onto the real world (394.5, $\Delta = 0.6$ ), which is slightly above the overall mathematics score. Understanding quantity, number systems and their algebraic properties is below the overall score (390.1, $\Delta = -3.9$ ). The two lowest scores are for Seeing mathematical structures and their regularities (384.3, $\Delta = -9.6$ ) and Recognising functional relationships between quantities (382.0, $\Delta = -12.0$ ). The latter is the lowest score across all cognitive operators.

These findings indicate that Thai students are relatively less confident with reasoning that requires the recognition of structure, regularity, and functional relationships. The low score for recognising functional relationships is particularly notable because this operator involves identifying how quantities vary together or depend on one another. Similarly, the lower score for seeing mathematical structures and regularities suggests difficulty in detecting underlying patterns or relationships that may not be immediately visible in the problem statement. By contrast, the score for using mathematical modelling as a lens onto the real world is close to the national mathematics mean, suggesting that model-oriented reasoning is not among the weakest operators in this profile.

Figure 4. Performance across Mathematical reasoning

[[KC_IMAGE_004]]


## Patterns of performance across content topics

This section examines Thailand's PISA 2022 mathematics performance at the level of content topics. The results are shown in Table 3 and Figure 5

Thailand's strongest content-topic results are found in Space and shape. Relationships among 2 and 3-dimensional geometric objects has the highest score across all content topics (415.2, $\Delta = 21.3$ ). Measurement also performs above the overall mathematics score (400.3, $\Delta = 6.4$ ). The result for relationships among geometrical objects is particularly notable: its score is more than 20 points above Thailand's overall mathematics mean, making it the clearest relative strength in the content-topic profile. This suggests that Thai students perform comparatively well on tasks involving spatial relationships, properties of 2- and 3-dimensional figures, and connections among geometrical objects.

The Quantity-related topics show a mixed pattern. Estimation is clearly above the overall mathematics score (401.3, $\Delta = 7.4$ ), while Percents, ratios and proportions is slightly below it (391.5, $\Delta = -2.5$ ) although it is not statistically different. Two other topics are further below the national mathematics mean: Numbers and units (387.3, $\Delta = -6.7$ ) and Arithmetic operations (387.8, $\Delta = -6.2$ ).

The Uncertainty and data topics also show variation. Chance and probability is above the overall mathematics score (397.0, $\Delta = 3.1$ ), while Data variability and its description is below it (389.4, $\Delta = -4.6$ ), and Data collection, representation and interpretation is lower still (386.5, $\Delta = -7.5$ ).

The result for Chance and probability indicates a modest relative strength. Thai students appear to perform somewhat better on tasks involving probability, randomness, or the likelihood of events than on other data-related topics. Although the differences are not statistically significant, the lower scores for Data collection, representation and interpretation and for Data variability and its description implies the possibility that students are less successful when working with data displays, interpreting collected data, or describing variation within data sets.

This pattern indicates that performance in Uncertainty and data is not uniform. Probability-related content is slightly above the national mathematics mean, whereas data representation and variability are below it. The results therefore suggest that Thai students may be more comfortable with probability concepts than with interpreting data representations or reasoning about variation.

The content-topic results provide a more detailed account of Thailand's mathematics performance than the overall PISA mathematics score alone. The strongest relative performance is concentrated in Relationships among 2 and 3-dimensional geometric objects, followed by Estimation, Measurement, and Chance and probability. These results suggest that Thai students show relative strengths in spatial-geometrical content, approximate quantitative reasoning, measurement, and probability.

The weakest relative performance is found in Algebraic expressions, functions, Data collection, representation and interpretation, Equations and inequalities, Numbers and units, and Arithmetic operations. These results point to relative difficulties in algebraic and functional content, data interpretation, and some foundational aspects of number and arithmetic.

Overall, Thailand's content-topic profile is characterised by a clear contrast between stronger performance in geometry-related topics and weaker performance in algebraic, functional, and data-representation topics. This pattern complements the cognitive-operator results. In particular, the lower scores for Functions and Algebraic expressions align with the weaker performance observed for recognising functional relationships and seeing mathematical structures. Similarly, the lower score for Data collection, representation and interpretation is consistent with the weaker performance observed for interpreting information presented in graphs or diagrams. The content-topic results therefore reinforce the conclusion that Thai students' relative strengths are more evident in spatial and estimation-based tasks, while relative weaknesses are more apparent in symbolic, relational, and data-interpretation tasks.

Table 3. Scores by content topic and differences from overall mathematics score


\*, \*\* denote the statistical significance of $\Delta$ at the 10% and 5% levels, respectively.

Figure 5. Performance across content topics

[[KC_IMAGE_005]]


# 4 Variation in mathematics performance profiles by gender and ESCS

## Differential performance by gender in cognitive operators

This section examines gender differences in Thailand's PISA 2022 mathematics performance across cognitive operators. The results are reported in Table 4 and Figure 6. The value of $\Delta$ represents the difference between girls' and boys' scores for each cognitive operator. Positive values indicate higher performance among girls, while negative values indicate higher performance among boys.

The clearest gender differences appear in Formulating situations mathematically. Girls scored higher than boys on all four operators in this process, with statistically significant advantages in Selecting an appropriate model from a list and identifying the mathematical aspects of a problem situated in a real-world context. The other two Formulating operators also favoured girls – Representing a situation mathematically ( $\Delta = 9.9$ ) and Representing a problem in a different way ( $\Delta = 8.8$ ) – but these were not statistically significant.

In Employing mathematical concepts, facts and procedures, there is little evidence of gender differentiation. None of the four differences is statistically significant, and all gaps are small. Boys scored slightly higher on Drawing a simple conclusion ( $\Delta = -0.5$ ) and Selecting an appropriate strategy from a list ( $\Delta = -1.2$ ), while girls scored slightly higher on Using and switching between representations ( $\Delta = 1.1$ ) and Making generalisations and conjectures ( $\Delta = 0.4$ ).

Similarly, no statistically significant gender differences are observed in Interpreting, applying and evaluating mathematical outcomes. Girls scored higher on four of the five operators, with the largest descriptive difference in Interpreting information presented in graphical form and/or diagrams ( $\Delta = 6.4$ ). Boys scored slightly higher only on Using mathematical thinking and computational thinking ( $\Delta = -0.7$ ).

In Mathematical reasoning, girls scored higher than boys on all four operators. The largest and only statistically significant difference in this process is for Understanding quantity, number systems and their algebraic properties (girls = 397.2; boys = 382.4; $\Delta = 14.8$ ). Girls also had higher descriptive scores for Seeing mathematical structures and their regularities ( $\Delta = 3.4$ ), Recognising functional relationships between quantities ( $\Delta = 7.3$ ), and Using mathematical modelling as a lens onto the real world ( $\Delta = 8.7$ ), although these differences were not statistically significant.

Overall, gender differences in Thailand's cognitive-operator profile are concentrated in selected aspects of mathematical formulation and reasoning. Girls show statistically significant advantages in identifying or selecting mathematical structures in contextual problems and in reasoning about quantity, number systems, and algebraic properties. By contrast, performance is broadly similar between girls and boys in employing procedures and interpreting mathematical outcomes.

Table 4. Scores by cognitive operator and gender


\*, \*\* denote the statistical significance of $\Delta$ at the 10% and 5% levels, respectively.

Figure 6. Gender differences in score across cognitive operators

[[KC_IMAGE_006]]


## Differential performance by gender in content topics

This section examines gender differences in Thailand's PISA 2022 mathematics performance across content topics, as reported in Table 5 and Figure 7. The value of $\Delta$ represents the difference between girls' and boys' scores for each content topic. Positive values indicate higher performance among girls, while negative values indicate higher performance among boys.

In Change and relationships, girls scored higher than boys on all three content topics. The largest and only statistically significant difference in this area is in Algebraic expressions (girls = 391.4; boys = 376.4; $\Delta = 15.0$ ). Girls also scored higher in Functions ( $\Delta = 7.7$ ) and Equations and inequalities ( $\Delta = 3.8$ ), although these differences were not statistically significant. These results suggest that the clearest gender difference in this content area is concentrated in Algebraic expressions.

In Space and shape, boys scored slightly higher than girls on both topics, but neither difference is statistically significant. Boys had higher scores in Relationships within and among geometrical objects in two and three dimensions ( $\Delta = -4.1$ ) and Measurement ( $\Delta = -1.8$ ). These small differences suggest broadly similar performance between girls and boys in geometry-related content.

In Quantity, the pattern is mixed. Boys showed a statistically significant advantage in Estimation (girls = 394.7; boys = 408.4; $\Delta = -13.7$ ). In contrast, girls scored higher in Numbers and units ( $\Delta = 5.3$ ), $o(\Delta = 6.6)$ , and Percents, Ratios and Proportions ( $\Delta = 4.0$ ), but these differences were not statistically significant. Thus, gender differences in Quantity are not uniform: boys show a clear advantage in estimation, while girls have higher descriptive scores in the other quantitative topics.

In Uncertainty and data, girls scored higher than boys on all three topics, although none of the differences is statistically significant. The differences were 6.1 points for Data collection, representation and interpretation, 5.4 points for Data variability and its description, and 6.3 points for Chance and probability. These results indicate a descriptive pattern favouring girls, but not one that provides statistically significant evidence of gender differences.

Overall, gender differences in content-topic performance are selective rather than widespread. Girls show a statistically significant advantage in Algebraic expressions, while boys show a statistically significant advantage in Estimation.

Table 5. Scores by content topic and gender


\*, \*\* denote the statistical significance of $\Delta$ at the 10% and 5% levels, respectively.

Figure 7. Gender differences in score across content topics

[[KC_IMAGE_007]]


## Differential performance by ESCS in cognitive operators

This section examines differences in Thailand's PISA 2022 mathematics performance across cognitive operators by students' economic, social and cultural status (ESCS), as reported in Table 6 and Figure 8. The value of $\Delta$ represents the score difference between students in the top ESCS group and those in the bottom ESCS group.

In Formulating situations mathematically, ESCS gaps range from 74.4 to 81.1 points. The largest gap in this process is for representing a situation mathematically using appropriate variables, symbols and diagrams (top = 447.8; bottom = 366.7; $\Delta = 81.1$ ). A similarly large gap is observed for representing a problem in a different way ( $\Delta = 80.5$ ). The gaps are slightly smaller, but still substantial, for selecting an appropriate model from a list ( $\Delta = 77.3$ ) and identifying the mathematical aspects of a real-world problem ( $\Delta = 74.4$ ). These results suggest that socio-economic differences are clearly visible in tasks requiring students to identify, select or construct mathematical representations of contextual problems.

In Employing mathematical concepts, facts and procedures, the ESCS gaps are particularly large and consistent. Differences range from 83.2 to 85.9 points, making this the cognitive process with the largest overall gaps. The largest difference is for making generalisations and conjectures (top = 464.2; bottom = 378.3; $\Delta = 85.9$ ), followed by using and switching between different representations ( $\Delta = 85.3$ ), drawing a simple conclusion ( $\Delta = 84.6$ ), and selecting an appropriate strategy from a list ( $\Delta = 83.2$ ). These results indicate that students from higher ESCS backgrounds have a strong advantage when applying procedures, selecting strategies, working across representations and extending procedural results.

In Interpreting, applying and evaluating mathematical outcomes, the gaps also remain large, ranging from 76.9 to 82.3 points. The largest gap is found in evaluating a mathematical outcome in terms of the context ( $\Delta = 82.3$ ). This is followed by using mathematical thinking and computational thinking ( $\Delta =$

80.8), interpreting a mathematical result back into the real-world context ( $\Delta = 78.7$ ), interpreting information presented in graphical form and/or diagrams ( $\Delta = 77.5$ ), and evaluating the reasonableness of a mathematical solution ( $\Delta = 76.9$ ). These findings suggest that ESCS-related differences are also evident when students must interpret, evaluate or contextualise mathematical outcomes.

In Mathematical reasoning, the gaps range from 68.3 to 84.8 points. The largest difference in this process is for seeing mathematical structures and their regularities (top = 447.5; bottom = 362.7; $\Delta = 84.8$ ). The gap is also substantial for understanding quantity, number systems and their algebraic properties ( $\Delta = 75.7$ ). The two smallest gaps across all cognitive operators are found in this process: using mathematical modelling as a lens onto the real world ( $\Delta = 70.3$ ) and Recognising functional relationships between quantities ( $\Delta = 68.3$ ). Although these are the smallest ESCS gaps in Table 7, they still represent large differences in performance between the top and bottom ESCS groups.

Overall, the results show that ESCS-related performance differences are large across all cognitive operators. The gaps are especially pronounced in Employing mathematical concepts, facts and procedures, where all differences exceed 83 score points. The smallest differences are found in selected Mathematical reasoning operators, but even these remain substantial. This pattern indicates that socio-economic background is strongly associated with students' performance across the full range of mathematical cognitive processes.

Table 6. Scores by cognitive operator and ESCS group


\*, \*\* denote the statistical significance of $\Delta$ at the $10\%$ and $5\%$ levels, respectively.

Figure 8. Score differences between 1 $^{st}$ and 4 $^{th}$ quartile ESCS groups across cognitive operators

[[KC_IMAGE_008]]


## Differential performance by ESCS in content topics

This section examines differences in Thailand's PISA 2022 mathematics performance across content topics by students' ESCS, as reported in Table 7 and Figure 9. $\Delta$ represents the score difference between students in the top ESCS group and those in the bottom ESCS group.

In Change and relationships, ESCS gaps are large. The largest difference in this area is in Algebraic expressions ( $\Delta = 91.2$ ), followed by Functions ( $\Delta = 85.0$ ) and Equations and inequalities ( $\Delta = 83.7$ ). These results indicate that students from higher ESCS backgrounds have a substantial advantage in algebraic and functional content, including symbolic expressions, functions, Equations and inequalities.

In Space and shape, the gaps are also large, though slightly smaller than in other content areas. The difference for Relationships among 2 and 3-dimensional geometric objects is 80.3 points, while the difference for Measurement is 84.6 points. These results show that Thailand's strongest overall content area still displays a large socio-economic gap.

In Quantity, ESCS gaps range from 77.6 to 82.8 points. The largest difference in this area is for Numbers and units ( $\Delta = 82.8$ ), followed by Arithmetic operations ( $\Delta = 81.3$ ), Percents, ratios and proportions ( $\Delta = 79.7$ ), and Estimation ( $\Delta = 77.6$ ). Although these are among the smaller gaps in Table 7, they remain large, suggesting that ESCS differences are evident.

In Uncertainty and data, the pattern is mixed but still marked by substantial ESCS differences. The largest gap across all content topics is found in Chance and probability ( $\Delta = 96.7$ ). By contrast, the gaps for Data Collection, Representation and Interpretation ( $\Delta = 78.9$ ) and Data variability and its description ( $\Delta = 76.8$ ) are among the smallest in the table. Thus, within Uncertainty and data, the ESCS gap is especially pronounced for probability, while data representation and variability show relatively smaller differences.

Overall, the content-topic results show that ESCS-related performance gaps are consistently large. Students in the top ESCS group outperform those in the bottom ESCS group, especially in Chance and probability and Algebraic expressions.

Table 7. Scores by content topic and ESCS group


\*, \*\* denote the statistical significance of $\Delta$ at the 10% and 5% levels, respectively.

Figure 9. Score differences between 1 $^{st}$ and 4 $^{th}$ quartile ESCS groups across content topics.

[[KC_IMAGE_009]]


# 5 Discussion and policy-relevant implications

## Substantive insights from the Thai-language application of CIME

Overall, the CIME-based profiles suggest a broadly coherent mathematics performance pattern, with most Cognitive operator and content-topic scores clustered relatively close to Thailand's overall mathematics mean. This underlines the value of building subskills to improve overall performance and is consistent with both the previous analysis of Ireland and the theoretical presuppositions of the PISA framework (OECD, 2023[16]; Okubo and Reinertsen, 2025[8]). Within this profile, students appear comparatively more secure when working with explicit mathematical procedures, particularly when selecting appropriate strategies from available alternatives. Tasks involving the formulation of contextual situations and reasoning about underlying structures, regularities and functional relationships appear relatively more demanding. A similar pattern is observed across content topics: comparatively higher scores are evident in relationships among 2- and 3-dimensional geometric objects and Estimation, while algebraic and functional topics, including Functions, Algebraic expressions, and Equations and inequalities, sit below the overall mathematics mean. Taken together, these findings suggest that further support may be useful for helping students connect contextual problems to symbolic, relational and data-based representations, and for interpreting mathematical results in relation to real-world contexts.


Methodologically, beyond the curriculum and educational insights, this study provides supporting evidence for the applicability of the CIME model to Thai-language responses and to languages that may be less represented in web-scale digital corpora (Pimienta, Blanco and de Oliveira, 2023[29]). It also underscores the value of disaggregating domain-level scores for policy-relevant analysis. In addition to being broadly consistent with the overall PISA mathematics profile, the disaggregated CIME results provide greater detail on patterns of variation by gender and socio-economic background, as well as differences between students' relative performance in employing mathematical procedures and their performance in reasoning mathematically and formulating mathematical problems.

## Implications for curriculum design and implementation

In interpreting these profiles, it is important to distinguish between minor descriptive variation and differences that are more likely to be meaningful for curriculum and classroom practice. Most differences across cognitive processes and operators are modest, suggesting that the results should be read primarily as a broad diagnostic profile rather than as evidence of highly differentiated performance across every construct.

One curriculum-facing interpretation is that algebra-related learning may serve as a bridge between specific content knowledge and broader mathematical sense-making. The comparatively lower scores observed in algebraic and functional content areas – such as Algebraic expressions, Functions, and Equations and inequalities – appear alongside lower relative performance on cognitive operators closely connected to algebraic thinking, including recognising functional relationships, seeing mathematical structures and regularities, and representing situations mathematically. This pattern suggests that algebra may be linked not only to mastery of particular content areas, but also to students' opportunities to express relationships, identify underlying structures, and model situations using mathematical representations. Strengthening fluency with Algebraic expressions, functions, and related symbolic representations could therefore support learning in Change and relationships, while also contributing to broader competencies in mathematical formulation, modelling, and reasoning.


This study reinforces previous findings on the relatively high degree of gender parity in mathematics performance within the Thai education system. As reflected in the headline PISA results (OECD, 2023[12]), the overall performance difference between Thai girls and boys is considerably smaller than the OECD average, and performance on most cognitive operators and content topics is broadly similar. Within this generally balanced profile, the statistically significant gender-related differences in cognitive operators are concentrated in selected aspects of Formulating and Mathematical reasoning, with higher average scores among girls: Selecting an appropriate model from a list (girls= 393.7; boys= 383.8; $\Delta$ = +9.9), Identifying the mathematical aspects and variables in context (girls= 395.3; boys= 385.0; $\Delta$ = +10.3), and Understanding quantity, number systems and their algebraic properties (girls= 397.2; boys= 382.4; $\Delta$ = +14.8). A related pattern is observed in content topics, where Algebraic expressions shows a statistically significant difference with higher average performance among girls (girls= 391.4; boys= 376.4; $\Delta$ = +15.0). By contrast, Estimation is the only content topic showing a statistically significant difference with higher average performance among boys (girls=394.7; boys=408.4; $\Delta=-13.7$ ). These findings suggest that targeted instructional support may be useful in specific areas of mathematical formulation, algebraic reasoning and estimation. As with all group-level comparisons, these results should be interpreted as descriptive patterns in average performance and learning opportunities, rather than as evidence of fixed differences in mathematical capacity between girls and boys.

Similarly, for most cognitive operators, the score difference between students from higher and lower-ESCS groups remains narrower in Thailand than the OECD average for the headline mathematics score, in both relative and absolute terms. Within this overall pattern, the ESCS-related difference is somewhat more pronounced for Employing operators, suggesting that continued attention to procedural fluency, strategy selection and the application of established mathematical methods may be useful across school contexts (Wood, Bruner and Ross, 1976[30]; Belland, 2014[31]). However, one possible underlying mechanism is that opportunity to learn, curriculum coverage, or instructional situation mediates the association between ESCS and performance. In this interpretation, ESCS is not the mediator itself; rather, students' background may be associated with unequal access to school-based learning opportunities, which in turn may contribute to differences in performance. This could produce a strong observed correlation between ESCS and scores even if the more immediate source of the gap is variation in curriculum exposure or instructional implementation rather than students' out-of-school characteristics alone (Welner and Carter, 2013[32]; Pokropek, Borgonovi and Jakubowski, 2015[33]; Marks, Cresswell and Ainley, 2006[34]; Xie and Ma, 2019[35]). An example of this mechanism may be visible in the performance of students on items relating to Chance and probability. This topic presents one of the largest gaps in between bottom and top ESCS groups while some studies have linked it more closely with student's social and cultural than economic context (Sharma, 2012[36]; Amir and Williams, 1999[37]). Nevertheless, the present analysis cannot test this mediation pathway directly. Evidence on curriculum coverage, instructional time, teacher preparation, school resources, or classroom implementation would be needed before concluding that lower-ESCS schools provide fewer opportunities to learn these topics. Overall, these findings suggest that ESCS-related patterns should be interpreted as signals for strengthening equitable learning opportunities and general teaching practices, rather than as evidence of differences in students' potential to learn mathematics.

## Analytical boundaries with respect to curriculum and policy evaluation

As with the previous analysis of Ireland's PISA data, curriculum-wide conclusions should be drawn with caution, given the specific empirical scope of the analysis and its focus on the mathematics performance of 15-year-old students. While PISA is methodologically rigorous and follows internationally recognised statistical approaches, the assessment measures the performance of a student sample at a single point in time. This is particularly important in the present case because the analysis is based on PISA 2022 data, while Thailand has continued its curriculum reform efforts since then. The results should therefore be interpreted as diagnostic evidence based on the 2022 assessment cycle, rather than as an evaluation of subsequent curriculum or policy developments.

A further methodological boundary concerns the AI-assisted scoring and scaling design. Although expert review, repeated scoring and statistical checks were used to support reliability, additional human verification in future applications could further strengthen confidence in the interpretation of construct-level scores (Huang and Whipple, 2023[38]). The construct-level profiles are also narrower than the full mathematics framework, since constructs with limited item or response coverage were excluded to support stable estimation. In addition, newly estimated item-facet parameters were anchored to PISA parameters originally estimated under a unidimensional mathematics framework. This supports alignment with the established PISA metric, but the resulting construct-level scores should be interpreted as diagnostic estimates rather than definitive subdomain measures. Finally, because responses from other language versions and cultural contexts were not analysed, and cross-language invariance was not tested, the CIME-derived scales should be interpreted as within-country diagnostic evidence for Thailand rather than as standalone internationally comparable subscales.

## 6 Conclusion

This study extends the analysis initiated with Ireland's PISA 2022 mathematics profile to the Thai context. Situated during an important phase of Thailand's long-term education reform, the study set out to provide policymakers, curriculum developers, assessment specialists and teachers with diagnostic evidence that can inform curriculum review, instructional planning, classroom assessment and targeted student support. By applying CIME to Thailand's PISA 2022 mathematics response data and assessment materials, the paper complements aggregate mathematics scores with multidimensional competency profiles across content topics and cognitive operators.

The CIME-based profiles suggest a broadly coherent mathematics performance pattern, with most Cognitive operator and content-topic scores clustered relatively close to Thailand's overall mathematics mean. Because the assessment materials analysed in this study were developed within the PISA mathematics framework, which treats each assessment domain as broadly coherent at the domain level, only a limited number of cognitive-operator scores showed statistically significant deviations from Thailand's overall mathematics score. This pattern is consistent with the intended structure of the assessment and provides supportive evidence for the technical robustness of the CIME procedure: the method identifies meaningful relative differences where they emerge, while avoiding overinterpretation of minor or construct-irrelevant variation. Within this profile, students appear comparatively more secure in tasks that involve working within established mathematical procedures, particularly selecting appropriate strategies from available alternatives, extending results through generalisation or conjecture, and applying mathematical and computational thinking. At the same time, tasks requiring students to translate contextual situations into mathematical representations, interpret mathematical outcomes in relation to real-world contexts, and recognise underlying structures, regularities and functional relationships between quantities appear relatively more demanding. Overall, the pattern suggests that students may be more secure when applying mathematical procedures once the mathematical structure of a task is available, while continued instructional attention could further support connections between real-world contexts, mathematical representations and contextual interpretation.


Methodologically, the study provides further support for the value of applying CIME in different linguistic contexts. By developing and using Thai-language operational scoring rubrics, the analysis generated diagnostic evidence within the language in which students encountered the assessment and expressed their Mathematical reasoning. Together with the Indonesia and Ireland applications, this paper provides further evidence that CIME can be adapted across languages, including those that may be less represented in web-scale digital corpora, when supported by expert review, careful rubric development and psychometric validation. Within the analytical boundaries of PISA 2022, the study therefore offers a practical bridge between international assessment data, competency-based curriculum priorities and evidence-informed efforts to strengthen mathematics learning in Thailand.

Brennan, R. (2001), Generalizability theory, Springer-Verlag, New York. [25]

## References

Alali, R. and Y. Wardat (2024), “Low PISA Performance Students: Factors, Perceptions, and Improvement Strategies”, International Journal of Religion, pp. 334-348, https://doi.org/10.61707/nve8gj33.


Das, S. and B. Narayanan (2023), “An Assessment of Education Divide and Measuring the Potential Impact of Its Elimination”, Journal of Southeast Asian Economies, Vol. 39, pp. S80-S101, https://doi.org/10.1355/ae39-Sf.


Lord, F. and M. Novick (1968), Statistical theories of mental test scores, Addison-Wesley, Menlo Park.


OECD (2025), OECD Skills Strategy Thailand: Assessment and Recommendations, OECD Skills Studies, OECD Publishing, https://doi.org/10.1787/153a1fe6-en.

OECD (2024), PISA 2022 Technical Report, OECD Publishing, https://doi.org/10.1787/01820d6d-en.

OECD (2023), PISA 2022 Assessment and Analytical Framework, OECD Publishing, https://doi.org/10.1787/dfe0bf9c-en.

OECD (2023), PISA 2022 Results (Volume I): The State of Learning and Equity in Education, [12] PISA, OECD Publishing, https://doi.org/10.1787/53f23881-en.

OECD (2023), PISA 2022 Results Factsheets Thailand, [11] https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/11/pisa-2022-results-volume-i-and-ii-country-notes\_2fca04b9/thailand\_b136aea5/6138f4af-en.pdf (accessed on 24 March 2026).


Office of the Education Council (n.d.), National Scheme of Education, https://www.onec.go.th/us.php/home/category/CAT0001145.

Okubo, T. (2025), “Collective Intelligence Model for Education (CIME)”, OECD Education Working Papers, Vol. 325, pp. 1-35, https://doi.org/10.1787/c673cc25-en. [9]

Okubo, T. (2022), “Theoretical considerations on scaling methodology in PISA”, OECD Education Working Papers, No. 282, OECD Publishing, Paris, https://doi.org/10.1787/c224dbeb-en.

Okubo, T. et al. (2023), “AI scoring for international large-scale assessments using a deep learning model and multilingual data”, OECD Education Working Papers, No. 287, OECD Publishing, Paris, https://doi.org/10.1787/9918e1fb-en. [23]

Okubo, T. and N. Reinertsen (2025), “Analysing Ireland’s PISA 2022 mathematics profile using AI-enhanced assessment modelling”, OECD Education Working Papers, Vol. 337, pp. 1-31, https://doi.org/10.1787/ef218dc4-en.


Rowley, K. et al. (2019), “Trends in International PISA Scores over Time: Which Countries Are Actually Improving?”, Social Sciences 2019, Vol. 8, Page 231, Vol. 8/8, p. 231, https://doi.org/10.3390/SOCSCI8080231.


Sarasean, T. (2024), “Challenges and Opportunities: Reforming the Thai Education System for Global Competitiveness”, Journal of Exploration in Interdisciplinary Methodologies, Vol. 1/3, https://so19.tci-thaijo.org/index.php/JEIM. [28]

Sharma, S. (2012), “Cultural Influences in Probabilistic Thinking”, Journal of Mathematics Research, Vol. 4/5, https://doi.org/10.5539/jmr.v4n5p63. [36]

TIMSS & PIRLS International Study Center (2026), TIMSS: Trends in International Mathematics and Science Study, https://timss.bc.edu/timss-landing.html. [20]

UNESCO (2023), UNESCO calls for action in the education sector following the low, https://www.unesco.org/en/articles/unesco-calls-action-education-sector-following-low-results-latin-america-and-caribbean-pisa-2022 (accessed on 13 May 2026). [14]


Wilson, J., C. Ormerod and M. Beiting Parrish (eds.) (2025), Input Optimization for Automated Scoring in Reading Assessment, National Council on Measurement in Education (NCME), Wyndham Grand Pittsburgh, Downtown, Pittsburgh, Pennsylvania, United States, https://aclanthology.org/2025.aimecon-main.1/. [21]


Xie, C. and Y. Ma (2019), “The mediating role of cultural capital in the relationship between socioeconomic status and student achievement in 14 economies”, British Educational Research Journal, Vol. 45/4, pp. 838-855, https://doi.org/10.1002/berj.3528.

# Annex A. Cognitive operators and content topics

Table 8. Cognitive operators in Formulating situations mathematically


Table 9. Cognitive operators in Employing mathematical concepts, facts and procedures


Table 10. Cognitive operators in Interpreting, applying and evaluating mathematical outcomes


Table 11. Cognitive operators in Mathematical reasoning


Table 12. Content topics in Mathematical literacy
