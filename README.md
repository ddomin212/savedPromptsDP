# Implementace pro diplomovou práci "Využití AI v softwarovém inženýrství"

## Struktura složek v `./`
- složky jsou rozděleny podle modelu
- v každé lze nalézt buď složku nebo soubor `analyza` a `navrh`, podle možnosti exportu z LLM rozhraní
- ve složce `gitCopilot` lze nalézt také složku `implementace` kde probíhají konverzace k ostatním tématům (implementace, refaktorování, testování, CI/CD), pouze pro jeden model, jak je uvedeno v diplomové práci.


## Složky v `implementace`
- `agent` obsahuje konverzace spojené s RAG agentem který má přístup ke kontextu celé projektové složky
    - `create_project` obsahuje snahu vytvořit jednoduchou repliku našeho projektu pouze s pomocí AI
- `backend` obsahuje konverzace spojené s Pythonovským backendem aplikace
    - `refactoring` obsahuje jednoduchý řetězec spojený s refactoringem, `quality_chain` poté řetězec složitější s lepšími výsledky, to samé platí i pro složku 
        - jména souborů se odkazují na jednotlivé soubory kódu v projektové složce
    - `tests` jejíž soubory se zabývají refactoringem testů nebo jejich vytváření, `quality_chain` poté řetězec složitější s lepšími výsledky, to samé platí i pro složku 
- `frontend` obsahuje konverzace spojené s JavaScript frontendem aplikace
- `cicd` obsahuje konverzace spojené s CICD a nasazením aplikace do hostovaných služeb

## Ostatní vysvětlivky
- Každý soubor obsahuje shrnutí tématiky konverzace, popsané klíčovými slovy, většinou uvnitř `()`.
- Doporučuji zobrazovat soubory přímo v GitHubu, díky zobrazování formátu Markdown, dělá je to podstatně čitelnějšími
- Občasné HTML si je potřeba stahnout a otevřít lokálně, zde zobrazení neprobíhá
