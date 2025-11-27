**`Tehisintellekt.ee` Q&A rakendus (proovitöö)**

See projekt on lahendus proovitööle, mille eesmärk on:

Luua rakendus, mis suudab vastata kasutaja küsimustele `tehisintellekt.ee` veebilehelt kogutud informatsiooni põhjal.

Rakendus koosneb kolmest osast:

1. Scraper – käib `tehisintellekt.ee` lehe läbi ja salvestab tekstilise info
2. Backend – töötleb kasutaja päringut ja genereerib vastuse
3. Frontend – lihtne UI küsimuse esitamiseks ja vastuse kuvamiseks

*Enne projekti käivitamist veendu, et sul oleks paigaldatud:*

* Python 3
* Node.js (versioon 20.19+)
* pip ja npm
* OpenAI API key (tuleb luua .env fail projekti juurkaustas näitefaili alusel)

*Enne backendi alustamist tuleb käivitada Scrapy scraper info kogumiseks veebilehelt. Selleks:*

1. Aktiveeri virtuaalkeskkond:
    `cd tehisintellekti_proovitoo`
    `.venv\Scripts\activate       (Windows)`

2. Paigalda sõltuvused (esmasel käivitamisel):
    `pip install -r requirements.txt`

3. Käivita scraper (esmasel käivitamisel, et koguda andmeid):
    `cd scraper`
    `scrapy crawl tehisintellekt`
    `cd ..`

Tulemusena tekkib fail `scraped.json` kausta `data`. Seal on puhastatud info igast selle domeeni veebilehest.

*Käivita backend:*
    `cd tehisintellekti_proovitoo`
    `.venv\Scripts\activate`
    `uvicorn app.main:app --reload`

Backend käivitub aadressil http://localhost:8000
Swagger (API testimiseks): http://localhost:8000/docs

*Käivita frontend:*
    (teises terminalis)
    `cd frontend`
    `npm install` (esmasel käivitamisel)
    `npm run dev`

Frontend käivitub aadressil http://localhost:5173/

**Tehnoloogiate valik:**

1. Python - peamine stack on minu teada Pythonis ja lisaks saab sellega peaaegu kõige lihtsamalt seda ülesannet lahendada.
2. Scrapy (info kogumiseks) - sobis hästi siia, kuna lehed pole dünaamilised ning Scrapy saab staatiliste lehtedega ideaalselt hakkama, ei ole mõtet mingit Playwrighti kasutama. Samuti on Scrapy-ga kogemust sarnase probleemi juures.
3. React (frontendi jaoks) - ei ole mulle kõige tuttavam framework, aga kuna teie stack on peamiselt Reacti peal, otsustasin proovida sellega teha.