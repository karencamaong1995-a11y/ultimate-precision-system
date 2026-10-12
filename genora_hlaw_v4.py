#!/usr/bin/env python3
"""GENORA H-law v4 verifier; archive hashes are not physical or financial attestations."""
import hashlib, json, pathlib, sys
from decimal import Decimal
ROOT=pathlib.Path(__file__).resolve().parent
ARCHIVE=ROOT/"docs"/"H-law"
def digest(data): return hashlib.sha256(data).hexdigest()
def jcs_like(v): return json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(",",":"),allow_nan=False).encode()
def merkle(ds):
    leaves=[hashlib.sha256(b"\x00"+bytes.fromhex(d)).digest() for d in ds]
    if not leaves: raise ValueError("empty tree")
    while len(leaves)>1:
        if len(leaves)%2: leaves.append(leaves[-1])
        leaves=[hashlib.sha256(b"\x01"+leaves[i]+leaves[i+1]).digest() for i in range(0,len(leaves),2)]
    return leaves[0].hex()
def load():
    formulas=json.loads((ARCHIVE/"H_FORMULAS.json").read_text())
    if list(formulas)!=[f"H{i:03}" for i in range(1,88)]: raise ValueError("missing/extra H formula")
    return formulas
def calc():
    D=Decimal
    spread,fill,vb,f,fees=D("14.5"),D(".89"),D("80"),D(".115"),D("65")
    kwh,c,nc,pr,opex,up=D("2800"),D(".22"),D("80"),D("8.5"),D("320"),D(".94")
    vel=spread*fill*vb*f-fees
    energy=kwh*c
    risk=nc*pr*fill
    gross=vel+energy+risk-opex
    net=gross*up*D(".75")
    return {"gross_model_per_hour":str(gross),"net_model_per_hour":str(net),
            "net_model_per_second":str(net/D(3600)),"actual_cash_received":None,
            "verified_paymongo_settlement":None,"verified_gotyme_deposit":None,
            "classification":"UNVALIDATED_ASSUMPTION_FORECAST"}
def build():
    f=load()
    eq={k:digest(x.encode("utf-8")) for k,x in f.items()}
    parent="0"*64; chain={}
    for k in f:
        change=digest(jcs_like({"change":"original_import","id":k,"release":"H-LAW-V4"}))
        lid=digest(bytes.fromhex(parent)+bytes.fromhex(eq[k])+bytes.fromhex(change))
        chain[k]={"EQHASH":eq[k],"EQLID":lid,"Parent":parent,"ChangeSetHash":change,"Canonical":f[k]}
        parent=lid
    root=merkle(list(eq.values()))
    outcome={"release":"GENORA_H_LAW_CANONICAL_V4","formula_count":len(f),
     "equation_merkle_root_sha256":root,"model":calc(),
     "truth_gates":{"SEALED":False,"VALID_GLOBAL":False,"PROMOTE":False,"SEAL_PV":False,
      "independent_host":"ABSTAIN","merchant_bank_settlement":"ABSTAIN",
      "historical_CI":"NOT_RERUN_BY_THIS_ARCHIVE_STEP"},
     "scope":"FORMULA_ARCHIVE_AND_ASSUMPTION_MODEL_ONLY"}
    return eq,chain,outcome
def run():
    eq,chain,outcome=build()
    assert len(eq)==87 and not any(outcome["truth_gates"][k] for k in ("SEALED","VALID_GLOBAL","PROMOTE","SEAL_PV"))
    if "--write" in sys.argv:
        for name,obj in (("H_EQHASH.json",eq),("H_CHAIN.json",chain),("CANONICAL_OUTCOME.json",outcome)):
            (ARCHIVE/name).write_text(json.dumps(obj,sort_keys=True,ensure_ascii=False,indent=2)+"\n")
        (ARCHIVE/"H_ROOT.txt").write_text(outcome["equation_merkle_root_sha256"]+"\n")
    if "--verify" in sys.argv:
        for name,obj in (("H_EQHASH.json",eq),("H_CHAIN.json",chain),("CANONICAL_OUTCOME.json",outcome)):
            if json.loads((ARCHIVE/name).read_text())!=obj: raise ValueError(name+" integrity mismatch")
        if (ARCHIVE/"H_ROOT.txt").read_text().strip()!=outcome["equation_merkle_root_sha256"]:raise ValueError("H_ROOT mismatch")
    print(json.dumps(outcome,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=="__main__":run()
