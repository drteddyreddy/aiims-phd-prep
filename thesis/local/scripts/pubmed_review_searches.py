import urllib.request,urllib.parse,json,csv,sys,time
E="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(u):
    for i in range(6):
        try:
            d=json.loads(urllib.request.urlopen(u+"&tool=thesisprep",timeout=60).read())
            if "esearchresult" in d and "idlist" not in d["esearchresult"]: raise ValueError(d)
            return d
        except Exception as e: print("retry",i,str(e)[:80]); time.sleep(3+3*i)
    raise SystemExit("pubmed down")
Q={"reviewA":'("theta burst" OR iTBS OR cTBS OR "transcranial magnetic" OR rTMS OR "transcranial direct current" OR tDCS) AND (alcohol OR "substance use" OR addiction OR craving) AND (detox* OR withdrawal OR inpatient) AND (random* OR sham)',
"reviewB":'("Allen Carr" OR Easyway OR "expectancy challenge" OR "counter-attitudinal" OR "cognitive restructuring" OR "belief change" OR "outcome expectanc*") AND (alcohol OR smoking OR nicotine OR "substance use") AND (random* OR trial OR intervention)'}
out=sys.argv[1]
for k,q in Q.items():
    r=get(E+"esearch.fcgi?"+urllib.parse.urlencode({"db":"pubmed","term":q,"retmax":50,"retmode":"json","sort":"relevance"}))["esearchresult"]
    ids=r["idlist"]; print(k,"count",r["count"],"translation:",r.get("querytranslation","")[:150])
    time.sleep(0.4)
    s=get(E+"esummary.fcgi?"+urllib.parse.urlencode({"db":"pubmed","id":",".join(ids),"retmode":"json"}))["result"]
    with open(f"{out}/search-exports/{k}_pubmed_top50.csv","w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["rank","pmid","first_author","year","title","journal","doi"])
        for i,p in enumerate(ids,1):
            d=s[p]; doi=next((a["value"] for a in d.get("articleids",[]) if a["idtype"]=="doi"),"")
            w.writerow([i,p,(d.get("authors") or [{"name":""}])[0]["name"],d.get("pubdate","")[:4],d.get("title",""),d.get("source",""),doi])
    time.sleep(0.4)
