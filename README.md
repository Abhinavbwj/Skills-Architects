# Architect Skills

### A Claude Code Skills Plugin by Abhinav Bhardwaj

29 interconnected skills covering building architecture from design theory through construction documentation, **plus 10 country-specific regulatory dossiers** providing clause-level precision for India, UAE, Saudi Arabia, USA, UK, Germany, Singapore, Japan, China, and Australia (v1.1.0). Draws from 50+ architects and theorists, 20+ architectural movements, **10+ country code systems with state/emirate/Land/prefecture-level granularity**, 8+ sustainability certifications, and hundreds of numeric benchmarks across structural, environmental, acoustic, fire, accessibility, and jurisdictional-regulatory domains. Includes 7 Python calculators for area scheduling, U-value computation, daylight estimation, egress compliance, structural loading, energy demand, and cost estimation.

**v1.1.0** | **18 core skills + 1 geographic router + 10 country dossiers = 29 skills** | **7 Python calculators**

## What's New in v1.1.0 -- Country-Specific Precision

- **`geographic-foundations`** -- auto-activated router that detects geographic context (country, city, code reference, currency cue) and routes to the correct country dossier. Routes IBC/Eurocodes/ASCE/ISO as international fallback.
- **`country-india`** -- NBC 2016, ECBC 2017, IS codes (456, 800, 875, 1893, 13920), MoHUA Harmonised Guidelines 2021, state DCRs (Mumbai DCPR 2034, Delhi MPD 2041, Bangalore BBMP, Chennai TNCDBR 2019, Hyderabad GHMC, Kolkata KMC, Pune UDCPR 2020, Ahmedabad GDCR 2017), GRIHA, IGBC, RERA, EIA, CRZ, DGCA NOCAS
- **`country-uae`** -- Dubai Building Code 2021, ADIBC 2013, UAE Fire & Life Safety Code 2018, Estidama Pearl Rating, Al Sa'fat 2016, Dubai Universal Design Code 2017, Federal Law 29/2006 People of Determination
- **`country-saudi-arabia`** -- SBC 201-1001 nine-part series 2018, Mostadamah Green Building, Saudi Universal Accessibility Code, NEOM + Qiddiya + Red Sea + Diriyah + AlUla + RCRC special jurisdictions, Mecca/Medina Hajj building rules
- **`country-usa`** -- IBC/IRC/IECC/IFC 2024, NFPA 101 2024, NFPA 70 NEC 2023, ADA 2010 + ANSI A117.1-2017, Fair Housing Act + HUD, ASCE 7-22, ACI 318-19, AISC 360-22, AWC NDS 2024, California Title 24 Parts 1-12, NYC BC 2022 + LL97 + LL11/98, Florida HVHZ, Chicago Construction Codes 2019, Massachusetts 9th Edition, Washington Energy Code
- **`country-uk`** -- Building Regulations 2010 + Approved Documents A-S, Building Safety Act 2022 + BSR + Higher-Risk Building regime, post-Grenfell AD-B amendments, BS 9991:2024 + BS 9999:2017, BS 8300-1/-2:2018, Future Homes/Buildings Standard 2025, MEES + EPC + SAP 10.2 + SBEM, BREEAM, London Plan 2021, NPPF 2024, Scotland/Wales/NI parallel regimes
- **`country-germany`** -- MBO 2002/2019 + 16 Landesbauordnungen (BayBO, BauO NRW, BauO Bln, HBauO, etc.), GEG 2023 + 2024 Heizungsgesetz amendments, DIN 18040-1/-2/-3 accessibility, DIN 4109 acoustics, DIN 4108 thermal, DIN 4102/EN 13501 fire, Eurocodes with German National Annexes, Sonderbau ordinances, DGNB, Effizienzhaus 40/55, BAFA/KfW, Passivhaus
- **`country-singapore`** -- BCA Building Control Act 1989 + Regulations 2003, SCDF Fire Code 2018, BCA Green Mark 2021 (mandatory minimum since 2008), BCA Code on Accessibility 2019, Code on Environmental Sustainability of Buildings 2018, URA Master Plan 2019, SS EN Eurocodes with Singapore NAs, ETTV/RTTV envelope metrics, Universal Design Mark
- **`country-japan`** -- Building Standards Act 1950 (revised 1998 performance-based, 2007 structural review reform), two-level seismic design (Level 1 + Level 2, Shintaishin 1981+), Fire Service Act parallel statute, Sho-Energy Ho 2015 + 2022 amendments, Heart Building Law 2006, AIJ Recommendations for Loads 2015, BCJ structural performance evaluation, CASBEE, City Planning Act 13 use districts + yoseki-ritsu/kenpei-ritsu + sun-right + sky-right setback regulations, ZEH/ZEB programs
- **`country-china`** -- GB 50352-2019 Civil Buildings Unified Design, GB 50016-2014 (2018 ed.) Fire Protection, GB 50011-2010 Seismic, GB 50009-2012 Loads, GB 55015-2021 + GB 50189-2015 Energy, JGJ 26/75/134 residential energy by zone, GB 50763-2012 Accessibility, sunlight rights (Rizhao), 5 thermal climate zones + 8 seismic intensity zones, DB local supplements (DB11 Beijing, DGJ08 Shanghai, DBJ Guangdong), Green Building Label 3-star, NZEB. Hong Kong + Macao SARs noted as separate
- **`country-australia`** -- NCC 2022 Vol 1 (BCA Class 2-9) + Vol 2 (Housing) + Vol 3 (PCA Plumbing), AS/NZS 1170.0-5 loads, AS 1170.4 seismic, AS 3600 concrete, AS 4100 steel, AS 1684 timber, AS 1428.1-2021 accessibility, AS 5113 cladding, Disability (Access to Premises) Standards 2010, NatHERS 7-star (mandatory 2023), BASIX NSW, Green Star + NABERS, 8 climate zones, wind regions A-D (cyclonic), state-specific overlays (NSW SEPP 65, VIC Better Apartments, QLD QDC, WA R-Codes)

---

## Table of Contents

- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Skills Reference](#skills-reference)
  - [Foundation](#1-foundation-auto-activated)
  - [Design & Theory](#2-design--theory)
  - [Program & Typology](#3-program--typology)
  - [Spatial & Envelope](#4-spatial--envelope)
  - [Structure & Services](#5-structure--services)
  - [Environment & Materials](#6-environment--materials)
  - [Codes & Compliance](#7-codes--compliance)
  - [Sustainability & Production](#8-sustainability--production)
- [Architect Calculator](#architect-calculator)
- [Knowledge Base](#knowledge-base)
- [Architecture](#architecture)
- [Example Prompts](#example-prompts)
- [Tri-Scalar Ecosystem](#tri-scalar-ecosystem)
- [Stats](#stats)
- [Author & License](#author--license)

---

## Quick Start

### Option 1: Install from the plugin marketplace

In Claude Code, run:

```
/plugin marketplace add Abhinavbwj/Skills-Architects
/plugin install architect-skills@architect-skills
```

Update later with `/plugin marketplace update architect-skills`.

### Option 2: Load a local clone as a plugin

```bash
claude --plugin-dir "/path/to/Architect Skills"
```

### Option 3: Copy to Your Project

```bash
cp -r skills/ your-project/.claude/skills/
```

Once installed, just ask Claude anything about building architecture. The system activates automatically — no slash commands required for most tasks.

---

## How It Works

Architect Skills uses a **progressive disclosure architecture** to stay lean while encoding deep knowledge:

```
User asks anything about building architecture
        |
        v
architect-foundations (auto-fires, invisible to user)
  - Applies baseline knowledge from 50+ theorists and frameworks
  - Routes to specialized skills as needed
        |
        v
Specialized skill loads (e.g., building-envelope, spatial-planning)
  - Follows structured workflow
  - Loads deep reference files on demand
        |
        v
architect-calculator provides precise computations when needed
  - 7 Python scripts for area, U-value, daylight, egress,
    structural loads, energy demand, and cost estimation
```

### Three-Layer Context Management

| Layer | What Loads | When | Size |
|---|---|---|---|
| **Layer 0** | Skill names + descriptions only | Always in context | ~18KB |
| **Layer 1** | Full SKILL.md body | On skill invocation | ~450-815 lines each |
| **Layer 2** | Reference files, templates, scripts | Only when explicitly needed | Varies |

This keeps the context window efficient. Claude never loads knowledge it doesn't need for the current task.

---

## Skills Reference

### 1. Foundation (Auto-Activated)

#### `architect-foundations`

**Invocation:** Automatic (invisible to user) — Claude-only, not user-invocable

The foundation layer. Auto-fires on any building architecture context and provides:

- **Architect & Theorist Quick-Reference Matrix** — 35+ architects/theorists with key contributions, design principles, landmark buildings, and application contexts (Vitruvius through Kéré)
- **Quantitative Rules of Thumb** — 50+ metrics with min/optimal/max values across 14 categories (floor-to-floor heights, structural grids, NTG ratios, U-values, acoustic ratings, daylight factors, corridor widths, parking, elevator sizing, fire resistance)
- **Building Typology Taxonomy** — 28 sub-types across residential, commercial, institutional, industrial, and special categories
- **Design Quality Framework** — composite checklist: Firmitas, Utilitas, Venustas, Context & Place, Sustainability, Accessibility
- **Anti-Pattern Catalog** — 17 common architectural failures across 5 categories with fixes
- **Skill Router** — decision tree activating specialized skills based on user context

**Reference files (loaded on demand):**
- `theorists-and-movements.md` — 50+ architects by era, 20+ movements with manifestos and canonical buildings
- `quantitative-standards.md` — extended dimensional, structural, environmental, acoustic, and servicing standards
- `building-typology-taxonomy.md` — all building types with dimensions, metrics, and exemplar projects
- `global-codes-frameworks.md` — IBC, NFPA, ADA, ASHRAE, Eurocodes, Building Regulations, NCC, NBC worldwide

---

### 2. Design & Theory

#### `design-theory`

**Invocation:** Ask about architectural theory, design philosophy, movements, precedent analysis, or design critique

- 8 architectural design philosophies (Rationalism, Empiricism, Phenomenology, Pragmatism, Critical Regionalism, Parametricism, Ecological, Social)
- Design thinking frameworks (RIBA Plan of Work 2020, AIA phases, IDP, EBD)
- Compositional principles (proportion systems, balance, rhythm, hierarchy, unity)
- 7-step precedent analysis method with structured template
- 8-dimension design critique framework

**Reference files:** `movements-and-manifestos.md` (20+ movements), `design-philosophy.md` (Vitruvian triad through POE)

#### `concept-design`

**Invocation:** Ask about parti development, massing studies, spatial organization, or concept generation

- 12 archetypal parti types with exemplar buildings (linear, courtyard, clustered, radial, grid, pinwheel, bar, tower, podium+tower, atrium, spiral, split-level)
- Massing strategies (solar, wind, view, contextual, additive, subtractive)
- 6 spatial organization models from Francis Ching
- 8 concept-to-form translation drivers with decision tree
- Design iteration protocol with structured evaluation

**Reference files:** `parti-strategies.md` (16 strategies with 3+ built examples each), `massing-methods.md` (12 case studies, solar envelope, wind comfort)

---

### 3. Program & Typology

#### `building-programming`

**Invocation:** Ask about space programming, area schedules, adjacency matrices, or brief development

- Peña & Parshall's Problem Seeking methodology
- Space standards for 7 building types with specific area tables (NDSS, BCO, HBN, BB103)
- Adjacency matrix method with 4 worked examples (hospital, school, office, mixed-use)
- Area schedule construction with NTG ratios for 10 building types
- Brief validation methodology

**Reference files:** `area-standards.md` (exhaustive tables for 9 sectors), `adjacency-methods.md` (4 worked examples)
**Templates:** `program-brief-template.md`

#### `building-typology`

**Invocation:** Ask about building types, plan configurations, residential/office/hospital/school design, or mixed-use

- 10 residential types (detached through co-living) with plan depths, NTG, structural systems, parking
- 4 office types with BCO metrics, structural grids, floor-to-floor heights
- Healthcare typologies (4 hospital plan types, clinics, sterile flows)
- Education (primary/secondary/university with BB103 compliance)
- Cultural (museums, theaters, libraries), hospitality, and hybrid/mixed-use

**Reference files:** `residential-typologies.md` (core design, daylight access, unit mix, 15+ exemplar projects)

---

### 4. Spatial & Envelope

#### `spatial-planning`

**Invocation:** Ask about floor plan layout, circulation design, core design, stacking, or space efficiency

- 10 floor plan archetypes with plan depths, structural grids, daylight characteristics
- Circulation design (corridor widths by code, dead-end limits, travel distances, stair/elevator sizing)
- Core design (central, side, dual, distributed) with dimensioned layouts
- Vertical stacking strategy and NTG optimization (targets for 8 building types)
- Wayfinding and spatial legibility

**Reference files:** `circulation-patterns.md` (dimensional standards across 3 codes), `core-design.md` (ASCII diagrams for 5 building types, riser shaft sizing)

#### `building-envelope`

**Invocation:** Ask about wall systems, glazing, roofing, thermal performance, moisture management, or cladding

- Envelope performance requirements with climate-specific targets (5 climate zones + Passive House)
- 10 wall systems with full build-ups, U-values, fire ratings, embodied carbon
- Glazing systems (glass types, coatings, curtain wall systems, WWR guidance)
- Roof systems (warm deck, inverted, green, pitched, membrane)
- Moisture management (Glaser method, junction detailing)
- Thermal bridge prevention (psi-values, strategies, common locations)

**Reference files:** `wall-systems.md` (15 wall types layer-by-layer), `glazing-systems.md` (5 curtain wall systems, 8 commercial glass products)

---

### 5. Structure & Services

#### `structural-systems`

**Invocation:** Ask about structural design, grids, spans, lateral systems, foundations, or structural material selection

- 8 structural system types with span ranges, costs, embodied carbon, exemplars
- Structural grid design by building type
- Lateral stability systems (shear walls through mega-frames)
- Foundation types with bearing pressures
- Span-to-depth ratios for all materials
- Load path narrative and coordination checklists

**Reference files:** `structural-typologies.md` (15 systems in depth), `span-tables.md` (comprehensive tables by material)

#### `building-services`

**Invocation:** Ask about HVAC, plumbing, electrical, elevators, fire protection, or MEP coordination

- 9 HVAC system types with spatial impact on architecture (duct sizes, void depths, plant rooms)
- Plumbing and drainage (wet-room stacking, riser sizing, pipe sizes)
- Electrical systems (power distribution, loads by building type, lighting power density)
- Vertical transportation (elevator sizing formula, shaft dimensions, escalators)
- Fire protection systems (sprinklers, detection, smoke control)
- MEP coordination (zone allocation, clash detection, BIM integration)

**Reference files:** `hvac-systems.md` (12 system types with full comparison), `mep-coordination.md` (5 case studies)

---

### 6. Environment & Materials

#### `daylighting-design`

**Invocation:** Ask about daylighting, solar geometry, glare control, shading, or lighting design

- Daylight metrics (DF, sDA, ASE, UDI, DGP) with targets by space type
- 15+ daylighting strategies with effectiveness data
- Solar geometry and shading device design with sizing tables by latitude
- Glare control ranked by effectiveness
- Artificial lighting integration (zones, dimming, circadian, LPD targets)
- 8-step design workflow

**Reference files:** `daylight-strategies.md` (20+ strategies, 15+ exemplar buildings), `solar-geometry.md` (sun path diagrams, overhang sizing formulas)

#### `material-selection`

**Invocation:** Ask about materials, finishes, durability, specification, LCA, or embodied carbon

- 8-criteria evaluation framework with decision matrix
- 7 material categories: concrete, steel, timber, masonry, glass, metals/composites, insulation
- Each with: properties, fire performance, embodied carbon, costs, exemplar architects
- Life-cycle assessment (EN 15978 stages, LETI benchmarks, material passports, circular economy)

**Reference files:** `material-properties.md` (30+ materials with full property tables), `specification-guide.md` (NBS, CSI MasterFormat, testing standards)

---

### 7. Codes & Compliance

#### `building-codes`

**Invocation:** Ask about IBC, occupancy classification, construction types, height/area limits, egress, or code compliance

- All 10 IBC occupancy groups with subgroups and occupant load factors
- Construction types IA through VB plus Type IV mass timber
- Height and area limitations with sprinkler/frontage increases
- Means of egress (exits, travel distance, stair width, dead-end corridors)
- Fire separation requirements
- Plumbing fixture minimums
- International code comparison (IBC, UK Building Regs, Eurocodes, NCC, NBC)

**Reference files:** `ibc-reference.md` (key tables with 3 worked examples), `occupancy-classification.md` (mixed occupancy, atriums, high-rise, mall provisions)

#### `accessibility-design`

**Invocation:** Ask about ADA, universal design, accessible routes, inclusive environments, or DDA compliance

- Ron Mace's 7 universal design principles
- Full ADA dimensional requirements (routes, doors, ramps, stairs, elevators, toilets, parking, signage)
- Accessible sanitary facilities including Changing Places
- Sensory accessibility (visual impairment, hearing impairment)
- Inclusive design beyond compliance (neurodiversity, aging, children)
- International comparison (ADA, BS 8300, DIN 18040, AS 1428)

**Reference files:** `ada-standards.md` (chapter-by-chapter requirements), `universal-design-principles.md` (11 exemplar inclusive buildings)

#### `fire-life-safety`

**Invocation:** Ask about fire strategy, compartmentation, egress design, smoke control, sprinklers, or fire resistance

- Fire strategy development (prescriptive vs performance-based)
- Compartmentation (fire barriers, doors FD30-FD120, firestopping, cavity barriers)
- Means of egress design with international travel distance comparison
- Structural fire protection (concrete cover, intumescent coatings, mass timber charring)
- Smoke control (NSHEV, mechanical extract, stair pressurization)
- Active fire protection (sprinklers, detection, emergency lighting)

**Reference files:** `egress-design.md` (travel distance tables, 3 worked examples, 5 case studies)

#### `acoustic-design`

**Invocation:** Ask about acoustics, sound insulation, room acoustics, noise control, or STC/Rw ratings

- Acoustic fundamentals (STC, Rw, IIC, Ln,w, NRC, RT60, STI, NR)
- Sound insulation targets by adjacency type with construction solutions
- Room acoustics (Sabine equation, RT60 targets, absorption, diffusion)
- Environmental noise control (facade insulation, ventilation impact)
- Building services noise control (vibration isolation, duct attenuation)
- Guidance for 10 building types

**Reference files:** `sound-insulation.md` (15 wall + 11 floor constructions with ratings), `room-acoustics.md` (concert hall typologies, 32 material absorption coefficients, 11 exemplar spaces)

---

### 8. Sustainability & Production

#### `building-sustainability`

**Invocation:** Ask about LEED, BREEAM, Passive House, WELL, net zero carbon, embodied carbon, or green certification

- Certification system selector (LEED BD+C, BREEAM, DGNB, WELL, Passive House, Living Building Challenge)
- LEED BD+C v4.1 category-by-category breakdown (110 points, architect's influence per credit)
- Passive House standard (5 criteria, design principles, PHPP, component specifications)
- Whole-life carbon (LETI targets, RIBA 2030, reduction strategies)
- WELL Building Standard v2 (10 concepts, architect's role)
- Net zero carbon strategy and circular economy (DfD, material passports)

**Reference files:** `leed-bdc.md` (credit-by-credit analysis), `passive-house.md` (design guidance, 11 exemplar buildings)

#### `construction-documentation`

**Invocation:** Ask about drawing sets, specifications, schedules, BIM LOD, or construction administration

- Drawing set organization with sheet numbering conventions
- Drawing standards (line weights, text heights, hatching, dimensions)
- BIM LOD requirements (100-500) by element type
- CSI MasterFormat specification writing (three-part format)
- Schedule production (door, window, finish, fixture, equipment, room data)
- Construction administration (RFI, submittals, change orders, site observations, punch list)

**Reference files:** `drawing-standards.md` (AIA/ISO 19650/sheet sizes), `specification-systems.md` (MasterFormat division-by-division)
**Templates:** `drawing-checklist.md`, `specification-template.md`

#### `architect-calculator`

**Invocation:** Ask Claude to calculate, or say "use the architect calculator" for any of the 7 tools

7 Python calculators with CLI interface and `--json` output:

| Calculator | What It Computes |
|---|---|
| `area_calculator.py` | GFA, NGA, unit count, population, parking from site area + FAR |
| `uvalue_calculator.py` | U-value of multi-layer constructions with Passive House comparison |
| `daylight_calculator.py` | Daylight factor from room geometry and window size |
| `egress_calculator.py` | Occupant load, exits, stair widths, travel distance compliance |
| `structural_load_calculator.py` | Gravity loads, tributary area, preliminary column sizing |
| `energy_calculator.py` | Annual heating/cooling demand via degree-day method |
| `cost_calculator.py` | Construction cost by type, quality, and region |

**Example usage:**

```bash
python area_calculator.py --site-area 5000 --far 3.0 --ntg-ratio 0.80
python uvalue_calculator.py --layers '[{"name":"Brick","thickness_mm":102,"conductivity":0.77},{"name":"Cavity","thickness_mm":50,"conductivity":0.18},{"name":"PIR","thickness_mm":100,"conductivity":0.022},{"name":"Block","thickness_mm":100,"conductivity":0.15}]'
python egress_calculator.py --floor-area 2000 --occupancy-type B --sprinklered --num-stories 6
python energy_calculator.py --floor-area 500 --envelope-area 800 --average-u-value 0.18 --heating-degree-days 3000 --cooling-degree-days 500
```

---

## Knowledge Base

### Architects & Theorists Referenced

**Classical & Renaissance:** Vitruvius, Alberti, Brunelleschi, Palladio
**Early Modern:** Sullivan, Loos, Perret, Horta, Gaudi
**Bauhaus & International:** Gropius, Mies van der Rohe, Le Corbusier, Neutra
**Mid-Century:** Kahn, Aalto, Eames, Saarinen, Utzon, Niemeyer, Barragán
**Brutalist & Late Modern:** Smithsons, Stirling, Tange, Rudolph
**Postmodern:** Venturi, Rossi, Graves, Bofill
**Deconstructivist:** Gehry, Libeskind, Hadid, Eisenman, Tschumi
**High-Tech:** Rogers, Piano, Foster, Grimshaw, Hopkins
**Phenomenological:** Zumthor, Holl, Pallasmaa
**Contemporary:** Koolhaas, BIG, MVRDV, SANAA, Kuma, Kéré, Lacaton & Vassal, Wang Shu, Studio Gang, DS+R, Snøhetta, Heatherwick
**Theorists:** Christopher Alexander, Francis Ching, Kenneth Frampton, Christian Norberg-Schulz, Reyner Banham, Colin Rowe, Ron Mace, Cedric Price

### Standards & Codes Referenced

IBC, NFPA 101, ADA/ABA, ASHRAE 90.1, ASHRAE 62.1, ASHRAE 55, IECC, Building Regulations (England & Wales) Approved Documents A-S, Eurocodes EN 1990-1999, NCC (Australia), NBC (Canada), NBC (India), Japanese Building Standards Law

### Sustainability Frameworks

LEED BD+C v4.1, BREEAM New Construction, Passive House (PHI/PHIUS), WELL Building Standard v2, DGNB, Living Building Challenge 4.0, RIBA 2030 Climate Challenge, LETI, Architecture 2030

### Measurement Standards

Neufert Architects' Data, Architectural Graphic Standards (Ramsey/Sleeper), BCO Guide to Specification, NHS Health Building Notes (HBN), Building Bulletin 103 (BB93/BB103), NDSS (Nationally Described Space Standard), CIBSE Guides, SCI publications, Concrete Centre, TRADA

---

## Architecture

```
Architect Skills Plugin
├── architect-foundations (auto-activated, invisible)
│   ├── Theorist Matrix (35+ architects)
│   ├── Quantitative Rules (50+ metrics, 14 tables)
│   ├── Typology Taxonomy (28 building sub-types)
│   ├── Quality Framework (Firmitas/Utilitas/Venustas+)
│   ├── Anti-Pattern Catalog (17 failures)
│   └── Skill Router → dispatches to 17 specialized skills
│
├── Design & Theory
│   ├── design-theory (8 philosophies, RIBA/AIA stages, precedent method)
│   └── concept-design (12 partis, massing, organization, iteration)
│
├── Program & Typology
│   ├── building-programming (Peña method, area standards, adjacency)
│   └── building-typology (residential, office, healthcare, education, cultural, hotel, hybrid)
│
├── Spatial & Envelope
│   ├── spatial-planning (10 plan types, circulation, cores, stacking, NTG)
│   └── building-envelope (10 wall systems, glazing, roofs, moisture, thermal bridges)
│
├── Structure & Services
│   ├── structural-systems (8 systems, grids, laterals, foundations, spans)
│   └── building-services (9 HVAC types, plumbing, electrical, elevators, MEP)
│
├── Environment & Materials
│   ├── daylighting-design (metrics, 15+ strategies, solar geometry, glare)
│   └── material-selection (7 material categories, LCA, specification)
│
├── Codes & Compliance
│   ├── building-codes (IBC occupancy, construction types, egress, international)
│   ├── accessibility-design (ADA, universal design, inclusive, sensory)
│   ├── fire-life-safety (compartmentation, egress, smoke, sprinklers)
│   └── acoustic-design (STC/Rw, room acoustics, noise control, 10 building types)
│
├── Sustainability & Production
│   ├── building-sustainability (LEED, Passive House, WELL, net zero, circular)
│   ├── construction-documentation (drawings, specs, BIM LOD, CA)
│   └── architect-calculator (7 Python scripts)
│
└── Progressive Disclosure
    Layer 0: Skill names (~18KB) → always loaded
    Layer 1: SKILL.md bodies (450-815 lines) → on invocation
    Layer 2: References, templates, scripts → on explicit demand
```

---

## Example Prompts

**Design Theory & Concept:**
- "Develop a concept for a 200-bed hospital on a sloped hillside site"
- "Compare the design philosophies of Kahn and Zumthor for a museum project"
- "Generate 3 parti options for a 5,000 m² community center"

**Programming & Typology:**
- "Create a space program for a 150-room business hotel"
- "What are the key metrics for a double-loaded residential corridor building?"
- "Build an adjacency matrix for a K-8 school"

**Spatial & Envelope:**
- "Design the core layout for a 30-storey residential tower under IBC"
- "Specify a wall build-up achieving U-value 0.15 W/m²K for a Passive House"
- "What WWR should I target for a south-facing office facade in London?"

**Structure & Services:**
- "Select a structural system for a 12-storey timber office building"
- "Compare chilled beams vs VAV for a 20,000 m² open-plan office"
- "Size the elevator provision for a 15-storey, 300-unit residential building"

**Environment & Materials:**
- "Estimate the daylight factor for a 6m deep office with 2.7m ceilings"
- "Compare embodied carbon of CLT vs RC frame for a 6-storey building"
- "Design a shading strategy for west-facing glazing at latitude 35°N"

**Codes & Compliance:**
- "Classify a mixed-use building with ground-floor retail and residential above under IBC"
- "Calculate egress requirements for a 500-seat auditorium"
- "What STC rating do I need between a hotel room and corridor?"

**Sustainability & Production:**
- "Score my design against LEED BD+C v4.1 and identify quick wins"
- "What are the Passive House requirements for windows in climate zone 5?"
- "Generate a door schedule for a 20-unit apartment building"

---

## Tri-Scalar Ecosystem

Architect Skills is the **building-scale pillar** in a tri-scalar AEC knowledge system:

| Scale | Plugin | Focus |
|---|---|---|
| **City** | Urban Design Skills (v1.2.0) | Masterplanning, street design, public space, TOD, zoning, sustainability scoring |
| **Building** | **Architect Skills (v1.0.0)** | **Programming, typology, spatial planning, envelope, structure, services, codes, sustainability** |
| **Component** | Computational Design Skills (v1.0.0) | Parametric modeling, generative design, computational geometry, fabrication, BIM scripting |

Together, these three plugins encode the full spectrum of AEC design intelligence — from "How wide should the boulevard be?" to "What wall build-up achieves U=0.15?" to "How do I panelize this facade into planar quads?"

---

## Stats

| Metric | Value |
|---|---|
| **Total skills** | 18 |
| **Total files** | 80+ |
| **Total lines** | 35,000+ |
| **Python calculators** | 7 |
| **Architects/theorists referenced** | 50+ |
| **Architectural movements** | 20+ |
| **Building codes/standards** | 12+ |
| **Sustainability frameworks** | 6+ |
| **Building typologies documented** | 28+ |
| **Structural systems** | 15+ |
| **HVAC system types** | 12+ |
| **Wall constructions with ratings** | 15+ |
| **Floor constructions with ratings** | 11+ |
| **Glazing configurations** | 14+ |
| **Material absorption coefficients** | 32+ |
| **Exemplar buildings referenced** | 100+ |
| **Dimensional standards** | 200+ |

---

## Author & License

**Author:** Abhinav Bhardwaj
**License:** MIT
**Version:** 1.0.0
**Copyright:** 2026 Abhinav Bhardwaj. All rights reserved.
