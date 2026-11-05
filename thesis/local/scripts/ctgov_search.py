import urllib.request,urllib.parse,json,csv,sys
B="https://clinicaltrials.gov/api/v2/studies"
def g(u): return json.loads(urllib.request.urlopen(u,timeout=60).read())
def row(s):
    p=s["protocolSection"]; i=p["identificationModule"]; st=p["statusModule"]; d=p.get("designModule",{})
    sp=p.get("sponsorCollaboratorsModule",{}).get("leadSponsor",{}).get("name","")
    refs=p.get("referencesModule",{}).get("references",[])
    pubs="; ".join(f'{r.get("pmid","")}:{r.get("citation","")[:90]}' for r in refs if r.get("type") in ("RESULT","DERIVED"))
    return [i["nctId"],i.get("briefTitle",""),sp,st.get("overallStatus",""),st.get("startDateStruct",{}).get("date",""),st.get("completionDateStruct",{}).get("date",""),d.get("enrollmentInfo",{}).get("count",""),"yes" if s.get("hasResults") else "no",pubs]
H=["nct","title","sponsor","status","start","completion","enrollment","results_posted","linked_pubs(RESULT/DERIVED)"]
ids="NCT06060496,NCT03932149,NCT06320366,NCT03470480,NCT05271175,NCT04990375,NCT06959342".split(",")
w=csv.writer(open(sys.argv[1]+"/search-exports/ctgov_named_trials.csv","w",newline="",encoding="utf-8")); w.writerow(H)
for n in ids:
    try: r=row(g(f"{B}/{n}")); w.writerow(r); print(" | ".join(map(str,r))[:300])
    except Exception as e: print(n,"ERR",e)
q={"query.cond":"alcohol use disorder","query.intr":'"theta burst" OR iTBS OR cTBS OR accelerated',"filter.advanced":"AREA[StartDate]RANGE[2020-01-01,MAX]","pageSize":100,"countTotal":"true"}
r=g(B+"?"+urllib.parse.urlencode(q)); print("SEARCH total",r.get("totalCount"))
w=csv.writer(open(sys.argv[1]+"/search-exports/ctgov_aud_tbs_2020on.csv","w",newline="",encoding="utf-8")); w.writerow(H)
for s in r["studies"]:
    x=row(s); w.writerow(x); print(" | ".join(map(str,x))[:220])
