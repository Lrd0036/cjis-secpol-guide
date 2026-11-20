# Illinois CJIS guide

**Reviewed November 19, 2026.** Illinois State Police (ISP) is the state’s CJIS Systems Agency. It administers the **Law Enforcement Agencies Data System (LEADS)**. An Illinois assessment starts with who grants access, which system supplies the information and why the recipient wants it. Criminal justice information (CJI) includes criminal history record information (CHRI). ISP’s Bureau of Identification maintains the state criminal-history repository. A police department connecting a records system to LEADS, a city checking a liquor license applicant and a county buying website hosting each follow a different route. [ISP Criminal Justice Services Command][il-isp-cjis-unit] · [ISP audit bulletin][il-leads-auditbulletin] · [LEADS rules, §§1240.30–.40][il-leads-admincode] · [Municipal employment and licensing bulletin][il-leads-ncj-employment] · [DuPage County exhibit, §§1 and 10][il-dupage-exhibit]

| If you need to know… | Start here |
|---|---|
| Which FBI edition will my Illinois auditor use? | ISP posts **v6.1**. The public material reviewed does not establish a statewide audit cutover. Confirm the edition and scope of the assigned audit. [ISP security index][il-leads-security] · [Audit assignments and previews][il-isp-cjis-audits] |
| Can our dispatch or records system connect to LEADS? | Check eligibility, the signed agreement and ISP approval. Allow **at least 90 days** for the written request for a new or changed connection. [20 Ill. Adm. Code §§1240.30–.40][il-leads-admincode] |
| Can a cloud vendor reuse another Illinois agency’s review? | ISP’s cloud FAQ allows the reviewer to accept parts of earlier vetting and calls for review of each implementation before purchase. Identify the deployment, data location and people able to access it. [ISP cloud FAQ, questions 2–5][il-leads-cloud] |
| Can a police officer run an employment or public background check in LEADS? | ISP directs ordinary noncriminal-justice requests to the Bureau of Identification. Public conviction searches use CHIRP. Public housing has a specifically limited result. [March 31 bulletin][il-crim-justice-bulletin] · [Housing bulletin][il-leads-chri-public-housing] |
| Where do we report a LEADS incident? | The local agency security officer reports to the state CJIS information security officer using the ISP form. Additional deadlines depend on the actor, affected data and contract. [LEADS policy §5.3.1][il-leads-statepolicy] · [Current reporting form][il-leads-incident] |

## Authority, agreements and audits

The ISP Director sets LEADS policy. The LEADS Administrator is the state CJIS Systems Officer. The participating agency designates a certified LEADS Agency Coordinator (LAC) and a Local Agency Security Officer (LASO). The same person may fill both local roles. Illinois’ Department of Innovation and Technology (DoIT) adopts the FBI policy as the minimum and expressly covers systems that DoIT or its client agencies develop, procure or use as a service when those systems contain CJIS-regulated information. [20 Ill. Adm. Code §§1240.10, .20, .90][il-leads-admincode] · [LEADS supplement §§1–3][il-leads-statepolicy] · [DoIT supplement §§3–5][il-doit-cjis-supplement]

**Version evidence needs a date and a purpose.** ISP’s website labels the Illinois supplement “v2.2 feb2017.” The linked PDF has February 2021 on the outer cover and February 2017 on the internal title and pages. ISP’s own CJI-access directive cites FBI v5.9.2 with a provision for the current version. The assigned audit edition still requires confirmation. For training, ISP issued a dated instruction on November 19, 2026. [ISP directory][il-leads-security] · [LEADS v2.2][il-leads-statepolicy] · [ISP directive SRV-223 §II][il-isp-leads-directive] · [November training bulletin][il-leads-aware]

| Decision | What the Illinois source requires or describes |
|---|---|
| Participation and changes | Qualify under a route in §1240.30 and execute the interagency agreement. Send the LEADS Administrator the proposed date, equipment and method at least 90 days before a connection or a change in how the agency connects. ISP approves the configuration. The participation agreement also calls for advance written approval of covered changes and current network and terminal inventories. [Part 1240][il-leads-admincode] · [Agreement §IV][il-leads-agreement] |
| Public service agency or private supplier | A management control agreement documents continuing criminal justice agency control where a government service provider is involved. For private personnel with CJI access, the agency retains individual signed addenda. ISP’s interface checklist asks for the contract, the applicable agreements, fingerprint-check evidence and training. It gives separate instructions for an agency using another agency’s interface. [LEADS §§5.1.2–.3][il-leads-statepolicy] · [Management control agreement][il-leads-mca] · [Interface checklist][il-leads-interface] |
| Screening and training | The employing agency submits Illinois and FBI applicant fingerprints for direct LEADS access. An employee moving agencies needs a submission under the new employer’s identifier. ISP requires security awareness **before access and annually**, including covered contractors and people with unescorted access. LEADS operator recertification is **every two years**. A new operator’s six-month supervised training period begins after passing awareness. [§1240.50][il-leads-admincode] · [New employee instructions][il-leads-finger] · [November 19 bulletin][il-leads-aware] |
| Audit and correction | ISP conducts three types of review of LEADS agencies on a three-year cycle, covering NCIC administrative, LEADS record and IT security. Different auditors may visit at different times. Within **30 days of receiving a report of noncompliance**, the agency head sends a corrective plan to the administrator and later confirms completion in writing. [Audit bulletin][il-leads-auditbulletin] · [§1240.100][il-leads-admincode] |
| Record quality | Keep supporting authority for an entry available around the clock. A second person checks the entry within 24 hours. Correct reported errors by the end of the shift or work period and remove invalid records immediately. [§§1240.60–.70][il-leads-admincode] |

The ISP audit portal distinguishes administrative, technical, noncriminal-justice and data-use reviews. Its CHRI usage preview, printed July 25, 2018, asks for the reason for each sampled inquiry, any case or warrant number, and the agency receiving a secondary disclosure. The current questionnaire and findings are in the assigned agency account. [Public audit list][il-isp-cjis-audits] · [CHRI example][il-audit-chri-preview] · [ISP audit instructions][il-isp-audit-instructions]

## Vendors, cloud services and AI

**A LEADS deployment.** ISP’s posted FAQ places CJI storage and transmission within the United States and says ISP does not certify particular providers. Before purchase, document where this service stores and transmits CJI, who can read it, who controls the keys and what earlier review ISP accepts. The FAQ uses older cryptography terminology, so record the current applicable controls and the authority’s decision for the deployment. [ISP cloud FAQ, questions 2–8][il-leads-cloud]

**A State cloud contract.** When incorporated, the Chief Procurement Office’s Cloud Hosting Appendix V.26.1 requires assurance at award and annually, State control of at-rest keys, privileged-account MFA, timely log delivery and a usable data export. It prohibits training or fine-tuning AI with State data, including anonymized or aggregated data. Its incident clause has its own deadlines. [Contract template directory][il-cpo-template-directory] · [Cloud Hosting Appendix §§1–9, 23–24][il-cpo-cloud-appendix]

**Work for ISP.** Supervisors retain form ISP 2-683 for contractual employees with CJI access and authorize system permissions according to job duties. ISP evaluates personally owned devices case by case. Its AI directive prohibits ISP personnel from entering CJI, LEADS information or personal information into public AI from any device. The directive also governs AI-assisted reports and requires human validation of official work. [SRV-223 §IV][il-isp-leads-directive] · [SRV-230 §§V.A–D][il-isp-technology-directive]

**A county contract.** DuPage County approved a content-management and hosting contract with Revize on April 14, 2026. Its CJI clauses apply when **both parties sign for a CJI-handling deliverable**. The exhibit requires prior vendor approval before the county intentionally sends CJI. If §10 applies, it requires screening, signed addenda and county authority to approve or reject a cloud provider. Section 10.3 gives six months from assignment for initial awareness training. For personnel who will access LEADS, ISP requires awareness before access. Verify the signed CJI deliverable for this deployment. [Board action][il-dupage-action] · [Exhibit §§1, 10.2–.3, 10.7, 10.9][il-dupage-exhibit] · [ISP training bulletin][il-leads-aware]

## Incident reporting and breach notification

One event can activate several rows. Match the reporting party, discovery or awareness trigger and recipient. The Illinois LEADS form and the federal internal notification clause address different steps. [FBI v6.1 IR-6][fbi-policy-6.1] · [ISP form][il-leads-incident]

| Who and what triggered notice | Recipient and timing |
|---|---|
| Personnel discover a suspected incident under FBI v6.1 IR-6(a) | Report to the agency’s incident-response capability immediately, within **one hour of discovery**. [FBI IR-6(a), printed p. 171][fbi-policy-6.1] |
| LEADS agency has a system security incident in its area of responsibility | The LASO sends the computer security incident form to the **state CJIS information security officer (CSA ISO/LEADS)**. The standalone form lists `ISP.LEADSISO@Illinois.gov`. Neither the form nor §5.3.1 assigns a separate numeric deadline to that handoff. [LEADS §5.3.1][il-leads-statepolicy] · [ISP form][il-leads-incident] |
| Personnel, contractors or providers discover a security incident in a DoIT or covered client-agency environment | Report to the DoIT Division of Information Security without delay, within **24 hours of discovery**. [DoIT incident policy §§3, 5.1, 6.4][il-doit-incident-policy] |
| A vendor under the State cloud appendix becomes aware of an actual or reasonably suspected incident affecting State data | Email the State CISO within **24 hours of awareness**, deliver an initial report within **five business days of the incident** and a final report at resolution. [Cloud Hosting Appendix §1][il-cpo-cloud-appendix] |
| A vendor under the activated DuPage §10 clause discovers an incident involving or potentially involving CJI | Report to **both the county CIO and the ISP CJIS Systems Officer within one hour of discovery**. [DuPage exhibit §10.7][il-dupage-exhibit] |
| A data collector has a qualifying breach of Illinois residents’ personal information | Owners and licensees promptly notify affected residents. A maintainer immediately notifies the owner or licensee. Where §10 requires notice to **more than 500** residents, notice to the Attorney General is due no later than consumer notice, subject to the statutory exceptions. [815 ILCS 530/5][il-pipa-5] · [§10][il-pipa-10] · [Attorney General filing instructions][il-ag-breach] |
| A state agency experiences a breach, or an agency reporting to the Governor encounters aggravated computer tampering | For a single breach involving **more than 250** Illinois residents, notify the Attorney General by the earlier of resident notice or **45 days after discovery**, subject to §12(e)’s exceptions. Agencies directly responsible to the Governor have another duty for a breach over that threshold or aggravated computer tampering, including a reasonable belief either occurred. Notify the DoIT CISO and Attorney General without delay, within **72 hours**. Section 25 separately requires a General Assembly report within **five business days** for a covered state-agency breach. [815 ILCS 530/12(e), (g)][il-pipa-12] · [§25][il-pipa-25] |

Local governments also have general cybersecurity duties. Illinois requires annual cybersecurity training for county and municipal employees. Every county and every municipality of at least 35,000 residents designates a local cybersecurity contact and reports the contact details to the Statewide CISO. [20 ILCS 1375/5-30][il-security-improvement-5-30] · [§5-35][il-security-improvement-5-35]

## Criminal history, biometrics and public records

| Request or decision | Illinois route |
|---|---|
| Public name-based conviction check | The Uniform Conviction Information Act (UCIA) covers publicly accessible conviction information maintained by ISP. CHIRP is the name-based route. Name matches can be ambiguous. For employment or licensing under UCIA, keep the signed release for at least **two years**, give the person ISP’s response and allow **seven working days** after receipt to report errors to the requester. Further dissemination ordinarily requires a fresh request after **30 days**. [Bureau of Identification][il-isp-background] · [UCIA §7][il-ucia-7] · [§11][il-ucia-11] · [§13][il-ucia-13] |
| Noncriminal-justice request to a police department | An ordinary requester cannot obtain a LEADS printout or verbal CHRI. Municipal employment and liquor licensing use the authorized fingerprint route. A public housing authority may seek the designated adult screening check and receive only a possible-record or no-record result. An agency electing tow-rotation checks uses a noncriminal-justice identifier and the BOI agreement. [General bulletin][il-crim-justice-bulletin] · [Municipal bulletin][il-leads-ncj-employment] · [Housing bulletin][il-leads-chri-public-housing] · [Tow bulletin][il-leads-tow-rotation] |
| Review or correct your own record | A facility forwards identifiers and prints within **five days**. ISP’s response is due within **seven days** for compliant electronic prints or **45 days** for a compliant card. If sent to the facility, it has **two days** to notify the subject and must destroy the result if unclaimed **45 days after notification**. The rule permits delivery to the subject’s residence. ISP provides a written challenge and administrative appeal route. [20 Ill. Adm. Code §1210.20][il-access-procedures] · [§1210.40][il-access-challenge] · [ISP instructions][il-isp-access-review] |
| Commercial fingerprinting | Illinois licenses fingerprint vendors, requires approved training, screening and certified equipment, and requires work orders to be kept **two years**. Statutory exemptions turn on the actor and the work. The Biometric Information Privacy Act separately excludes a state or local government contractor, subcontractor or agent while it performs that government work. [Licensure][il-fingerprint-vendor-31-10] · [Equipment][il-fingerprint-vendor-31-15] · [Work orders][il-fingerprint-vendor-31-25] · [Exemptions][il-fingerprint-vendor-31-5] · [740 ILCS 14/25(e)][il-bipa-exceptions] |
| Criminal-history reporting and relief | Arresting agencies submit covered arrest information daily. The default charge and disposition reporting window is **30 days**. Juvenile access and expungement have their own rules. Three enacted changes have later start dates. Qualifying pretrial-services agencies may submit with ISP approval in **2027**. Covered municipal ordinance and Class C sealing starts in **2028**. The broader, appropriations-dependent sealing process begins in **2029**. [20 ILCS 2630/2.1][il-identification-2-1] · [§5.2][il-identification-5-2] · [Juvenile disclosure][il-juvenile-1-7] · [Juvenile expungement][il-juvenile-5-915] |
| Freedom of Information Act request | ISP directs agencies to withhold exclusively LEADS-generated output and remove or redact direct LEADS material in responsive files. In a nonbinding determination, the Attorney General found the LEADS rationale alone insufficient for general information incorporated into an agency investigative report. Review the responsive record and the source of the specific information. [ISP September 30 bulletin][il-leads-foia] · [Public Access Bureau review 69962, p. 7][il-leads-foia-review] |
| Federal civil immigration enforcement and database access | The Illinois TRUST Act restricts direct access to law enforcement databases or data-sharing platforms and agreements for that access. Section 15(h) specifies the federal criminal warrant and federal-law exceptions. Section 15(i) preserves criminal-investigation cooperation. Officers may confirm whether a LEADS or NCIC alert is civil or criminal. [5 ILCS 805/15][il-trust-act-limits] · [§5][il-trust-act-scope] · [Attorney General guidance, p. 4][il-trust-guidance] |

For interstate noncriminal-justice exchange, the FBI’s **July 2025** Compact map classifies Illinois as a **memorandum-of-understanding signatory**. For an individual requester, the applicable statute, agreement and authorized purpose determine access. [FBI Compact map, p. 2][il-fbi-compact-map] · [Fingerprint request authority, 20 ILCS 2630/3][il-identification-3]

## Retention depends on the record

| Record, system and custodian | Retention or release decision |
|---|---|
| LEADS criminal history dissemination | The coordinator reviews the primary report monthly and keeps it **one year**. Keep a secondary dissemination log **three years**. The longer period applies if one log serves both purposes. ISP distinguishes a query bearing the receiving agency’s identifier from passing a result to another authorized agency afterward. [Monthly report bulletin][il-leads-monthly] · [Dissemination bulletin][il-leads-dissem] · [Retention schedule][il-isp-leads-retention] |
| LEADS hot files and validations | Keep validation packets **18 months**. Valid-hit supporting documents have **one-year or seven-year** periods depending on the file category. For example, the schedule places wanted-person and stolen-vehicle hits in the seven-year group and protection-order hits in the one-year group. [ISP schedule, p. 1][il-isp-leads-retention] |
| State and local automated license plate reader (ALPR) sharing | State law restricts transfers for investigations or enforcement involving protected lawful health care or immigration status. Before sharing with an out-of-state law enforcement agency, obtain its written declaration on use. The Secretary of State’s 2025 sample of 12 local agencies uncovered CBP access to Illinois Flock cameras and led to a stop-access order. [625 ILCS 5/2-130][il-plate-law] · [Secretary of State audit release][il-sos-audit] |
| ISP plate-reader data | In VehicleManager, ISP retains detections for **90 days** and search and hit/alert records permanently. FlockOS detections are purged every **30 days**. Separately, Expressway Camera Act images exported through a law enforcement database must be deleted from that database within **120 days** unless relevant to an ongoing investigation or pending criminal trial. [ISP ENF-051 §V.C][il-isp-plate-directive] · [605 ILCS 140/5(b)][il-expressway-act] · [FY26 program report][il-isp-plate-report] |
| Naperville Police plate-reader data | The department purges routine reads after **30 days**. It preserves evidence and records subject to a hold or other retention duty, and documents a monthly sample of searches. The order also governs vendor safeguards and ongoing access by outside agencies. [Naperville General Order 41.16.2, .6, .11][il-naperville-order] |
| Officer-worn body cameras | The agency or its camera vendor keeps ordinary recordings **90 days**. Protect a flagged recording for **two years from flagging**. If used in criminal, civil or administrative proceedings, destruction requires final disposition and a court order. The Act separately addresses early alteration, destruction and supervisor-designated training copies. [50 ILCS 706/10-20(a)(7)–(8)][il-body-camera-law] |
| Local public records and police misconduct | Local disposal generally needs commission authority. The applicable rule requires a disposal certificate **30 days before destruction** and return of the approved certificate. Public and nonpublic records relating to police misconduct complaints, investigations and adjudications are retained permanently. [50 ILCS 205/7][il-local-records-7] · [§25][il-local-records-25] · [Commission rule][il-records-rule-4000] · [Cook County rule][il-records-rule-4500] |

Four ALPR bills are in the legislative watchlist. Their status pages record committee referrals. The search data keeps these proposals outside operative requirements. [SB3816][il-b-sb3816] · [HB5151][il-b-hb5151] · [HB5231][il-b-hb5231] · [SB3257][il-b-sb3257]

## Search Illinois

From the repository root, this example returns reporting instructions for Illinois, including source, recipient and applicability. Change `incident-reporting` to `cloud-hosting`, `training`, `public-records` or `records-retention`. For Naperville’s retention orders, use `--arg topic records-retention --arg locality Naperville`. Check `coverage_gaps` for questions still with the responsible authority and `watchlist` for pending proposals. [Search data](../../data/state-search-pilot.json) · [Dated source register](../../sources/manifests/illinois-2026-11-19.md)

```sh
jq -r --arg topic incident-reporting --arg locality "" --arg date 2026-11-19 '
  . as $guide | .records[]
  | select(.jurisdiction == "US-IL" and (.effective_from // "") <= $date)
  | select($locality == "" or .locality == $locality)
  | select(.topic == $topic or ((.related_topics // []) | index($topic)))
  | [.program // .locality // $guide.sources[.source].issuer,
     .applies_when, .summary, .locator, $guide.sources[.source].url] | @tsv
' data/state-search-pilot.json
```

[il-isp-cjis-unit]: https://isp.illinois.gov/JusticeServices/CriminalJustice
[il-leads-auditbulletin]: https://isp.illinois.gov/LawEnforcement/GetFile/34a138cf-587b-4c50-b950-cbdf8f1c37c7
[il-leads-admincode]: https://my.ilga.gov/agencies/JCAR/EntirePart?titlepart=02001240
[il-leads-ncj-employment]: https://isp.illinois.gov/LawEnforcement/GetFile/9751a68e-8859-4178-8bc7-b57453f7ad80
[il-dupage-exhibit]: https://dupage.legistar.com/View.ashx?GUID=D287291C-9EEF-4F36-8619-4FA79809F357&ID=15380699&M=F
[il-leads-security]: https://isp.illinois.gov/LawEnforcement/LEADSSecurity
[il-isp-cjis-audits]: https://isp.illinois.gov/lawenforcement/cjisaudits
[il-leads-cloud]: https://isp.illinois.gov/LawEnforcement/GetFile/63eba5dc-06db-4a7c-a713-85bbdb802a46
[il-crim-justice-bulletin]: https://web-akamai.isp.illinois.gov/LawEnforcement/GetFile/c1a17c09-aaeb-43a1-a340-13191d16e633
[il-leads-chri-public-housing]: https://isp.illinois.gov/LawEnforcement/GetFile/78313122-68bb-480b-90c7-d3661c1016e9
[il-leads-statepolicy]: https://isp.illinois.gov/LawEnforcement/GetFile/dd6b6bd1-5f5f-4a54-80e9-a606a51ab75a
[il-leads-incident]: https://isp.illinois.gov/LawEnforcement/GetFile/63ee8d54-396f-4e59-a157-7ef1f6d1d44c
[il-doit-cjis-supplement]: https://doit.illinois.gov/content/dam/soi/en/web/doit/documents/support/policies/2021/cjis-supplemental-policy.pdf
[il-isp-leads-directive]: https://isp.illinois.gov/StaticFiles/docs/DepartmentDirectives/SRV-223%20DIR.pdf
[il-leads-aware]: https://isp.illinois.gov/LawEnforcement/GetFile/620e964d-738c-40d0-8690-0b66d1161326
[il-leads-agreement]: https://isp.illinois.gov/LawEnforcement/GetFile/335ef268-9788-45af-b466-2ae9a4a1fc8a
[il-leads-mca]: https://isp.illinois.gov/LawEnforcement/GetFile/5d8bf656-559b-48d4-b9d2-d40942e03f4e
[il-leads-interface]: https://isp.illinois.gov/LawEnforcement/GetFile/ab889635-443c-421f-bda4-a207cea5ed44
[il-leads-finger]: https://isp.illinois.gov/LawEnforcement/GetFile/09045bda-5cad-438c-bc8a-86ee85dd7916
[il-audit-chri-preview]: https://isp.illinois.gov/LawEnforcement/GetFile/7da021f4-5c45-43d5-949b-cdc908561369
[il-isp-audit-instructions]: https://isp.illinois.gov/LawEnforcement/GetFile/7bd11f3e-6ac9-4401-b9d2-8838c479c167
[il-cpo-template-directory]: https://cpo-general.illinois.gov/solicitation-and-contract-templates.html
[il-cpo-cloud-appendix]: https://cpo-general.illinois.gov/content/dam/soi/en/web/cpo-general/documents/cloud-hosting-appendix-v.26.1.pdf
[il-isp-technology-directive]: https://isp.illinois.gov/StaticFiles/docs/DepartmentDirectives/SRV-230%20DIR.pdf
[il-dupage-action]: https://dupage.legistar.com/ViewReport.ashx?GID=919&GUID=199E6ACF-5A48-4C53-8D8E-9D8DF003D9A1&ID=7978336&M=R&N=Master&Title=Legislation+Details
[fbi-policy-6.1]: https://le.fbi.gov/file-repository/cjis_security_policy_v6-1_20260625-1.pdf
[il-doit-incident-policy]: https://doit.illinois.gov/content/dam/soi/en/web/doit/documents/support/policies/2021/information-security-incident-management-policy.pdf
[il-pipa-5]: https://ftp.ilga.gov/ILCS/Ch%200815/Act%200530/081505300K5.html
[il-pipa-10]: https://ftp.ilga.gov/ILCS/Ch%200815/Act%200530/081505300K10.html
[il-ag-breach]: https://illinoisattorneygeneral.gov/Consumer-Protection/For-Businesses/Data-Breach/
[il-pipa-12]: https://ftp.ilga.gov/ILCS/Ch%200815/Act%200530/081505300K12.html
[il-pipa-25]: https://ftp.ilga.gov/ILCS/Ch%200815/Act%200530/081505300K25.html
[il-security-improvement-5-30]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%201375/002013750K5-30.html
[il-security-improvement-5-35]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%201375/002013750K5-35.html
[il-isp-background]: https://isp.illinois.gov/BureauOfIdentification/BackgroundChecks
[il-ucia-7]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%202635/002026350K7.html
[il-ucia-11]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%202635/002026350K11.html
[il-ucia-13]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%202635/002026350K13.html
[il-leads-tow-rotation]: https://isp.illinois.gov/LawEnforcement/GetFile/f6b28a8d-c310-4ed9-b964-7b5085530308
[il-access-procedures]: https://ftp.ilga.gov/JCAR/AdminCode/020/020012100000200R.html
[il-access-challenge]: https://ftp.ilga.gov/JCAR/AdminCode/020/020012100000400R.html
[il-isp-access-review]: https://isp.illinois.gov/BureauOfIdentification/MyRecord
[il-fingerprint-vendor-31-10]: https://ftp.ilga.gov/ILCS/Ch%200225/Act%200447/022504470K31-10.html
[il-fingerprint-vendor-31-15]: https://ftp.ilga.gov/ILCS/Ch%200225/Act%200447/022504470K31-15.html
[il-fingerprint-vendor-31-25]: https://ftp.ilga.gov/ILCS/Ch%200225/Act%200447/022504470K31-25.html
[il-fingerprint-vendor-31-5]: https://ftp.ilga.gov/ILCS/Ch%200225/Act%200447/022504470K31-5.html
[il-bipa-exceptions]: https://my.ilga.gov/legislation/ilcs/fulltext?DocName=074000140K25
[il-identification-2-1]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%202630/002026300K2.1.html
[il-identification-5-2]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%202630/002026300K5.2.html
[il-juvenile-1-7]: https://ftp.ilga.gov/ILCS/Ch%200705/Act%200405/070504050K1-7.html
[il-juvenile-5-915]: https://ftp.ilga.gov/ILCS/Ch%200705/Act%200405/070504050K5-915.html
[il-leads-foia]: https://isp.illinois.gov/LawEnforcement/GetFile/3ebc717e-5477-4b4d-bd1b-93c42a76e075
[il-leads-foia-review]: https://illinoisattorneygeneral.gov/Page-Attachments/FOIAPAC/Non-Binding-PAC-Opinions/FOIA/7_1/Exemptions-which-permit-redacting-withholding-exempt-information-records/7_1_d-5/69962%2C%20issued%20May%2015%2C%202024.pdf
[il-trust-act-limits]: https://www.ilga.gov/Documents/legislation/ilcs/documents/000508050K15.htm
[il-trust-act-scope]: https://www.ilga.gov/Documents/legislation/ilcs/documents/000508050K5.htm
[il-trust-guidance]: https://www.illinoisattorneygeneral.gov/rights/ImmigrationLawGuidancetoLawEnforcement.pdf
[il-fbi-compact-map]: https://www.fbi.gov/file-repository/cjis/compact-council-states-territories-map.pdf
[il-identification-3]: https://ftp.ilga.gov/ILCS/Ch%200020/Act%202630/002026300K3.html
[il-leads-monthly]: https://isp.illinois.gov/LawEnforcement/GetFile/34c17255-9e3d-486c-afe6-ae6ecb9c5848
[il-leads-dissem]: https://isp.illinois.gov/LawEnforcement/GetFile/f89870e7-cb00-4d15-9e68-24ddbdbd6f8e
[il-isp-leads-retention]: https://isp.illinois.gov/LawEnforcement/GetFile/9882d753-7d9f-4277-8cc6-4a279a26adaf
[il-plate-law]: https://my.ilga.gov/legislation/ilcs/fulltext?DocName=062500050K2-130
[il-sos-audit]: https://www.ilsos.gov/content/dam/news/2025/august/250825d1.pdf
[il-isp-plate-directive]: https://isp.illinois.gov/StaticFiles/docs/DepartmentDirectives/ENF-051%20DIR.pdf
[il-expressway-act]: https://my.ilga.gov/legislation/ilcs/fulltext?DocName=060501400K5
[il-isp-plate-report]: https://my.ilga.gov/Documents/Reports/ReportsSubmitted/7099RSGAEmail15940RSGAAttachFY26%20ALPR%20Annual%20Report-signed.pdf
[il-naperville-order]: https://www.naperville.il.us/DocumentCenter/View/1304/Automated-License-Plate-Reader-Policy---09-08-2026-PDF
[il-body-camera-law]: https://my.ilga.gov/legislation/ilcs/fulltext?DocName=005007060K10-20
[il-local-records-7]: https://ftp.ilga.gov/ILCS/Ch%200050/Act%200205/005002050K7.html
[il-local-records-25]: https://ftp.ilga.gov/ILCS/Ch%200050/Act%200205/005002050K25.html
[il-records-rule-4000]: https://ftp.ilga.gov/JCAR/AdminCode/044/044040000000400R.html
[il-records-rule-4500]: https://ftp.ilga.gov/JCAR/AdminCode/044/044045000000400R.html
[il-b-sb3816]: https://www.ilga.gov/ftp/legislation/104/BillStatus/HTML/10400SB3816.html
[il-b-hb5151]: https://www.ilga.gov/ftp/legislation/104/BillStatus/HTML/10400HB5151.html
[il-b-hb5231]: https://www.ilga.gov/ftp/legislation/104/BillStatus/HTML/10400HB5231.html
[il-b-sb3257]: https://www.ilga.gov/ftp/legislation/104/BillStatus/HTML/10400SB3257.html
