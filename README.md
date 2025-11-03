# 🕷️ Cleverleben Scrapy Spider

This repository contains a **Scrapy framework project** written in **Python 3**, designed to extract product data from [cleverleben.at](https://www.cleverleben.at/produktauswahl).

---

## 📄 Project Overview

- **Framework:** Scrapy  
- **Language:** Python 3  
- **Data Items Extracted:** 1,000+  
- **Outputs:** JSON and CSV  
- **Code Style:** PEP8 Compliant  
- **Custom Delay:** 0.5 seconds (to respect site rules)  

---

## ⚙️ Spider Details

**Spider Name:** `cleverleben`  
**Start URL:** `https://www.cleverleben.at/produktauswahl`  
**Output Files:**
- `cleverleben_output.json`
- `cleverleben_output.csv`

---

## 📂 Dropbox Links (Download Outputs)

- [⬇️ JSON Output File](https://www.dropbox.com/scl/fi/4a67ntdd2cz0b0ktd5pg5/cleverleben_output.json?rlkey=b46f2syxc605id2fgc2upwopr&st=nam969vf&dl=0)
- [⬇️ CSV Output File](https://www.dropbox.com/scl/fi/4a67ntdd2cz0b0ktd5pg5/cleverleben_output.json?rlkey=b46f2syxc605id2fgc2upwopr&st=xb5qel13&dl=0)

---

##  Run Instructions

Run the spider from your project root folder:

```bash
scrapy crawl cleverleben
# spider-project
