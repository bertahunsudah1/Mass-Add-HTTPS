#!/usr/bin/env python3
# realistic example ~140 lines trimmed for brevity
import argparse, base64, hashlib, json, random, sys

def encode_b64(s): return base64.b64encode(s.encode()).decode()
def decode_b64(s): return base64.b64decode(s.encode()).decode(errors='ignore')
def md5(s): return hashlib.md5(s.encode()).hexdigest()
def sha256(s): return hashlib.sha256(s.encode()).hexdigest()

def simple_generation(schema):
    # small pseudo-random generator based on schema dict
    out = {}
    for k,v in schema.items():
        t = v.get("type","str")
        if t=="int":
            out[k] = random.randint(v.get("min",0), v.get("max",100))
        elif t=="enum":
            out[k] = random.choice(v.get("choices",["a","b"]))
        else:
            out[k] = v.get("example", "example-"+k)
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode", choices=["run","gen","hash","encode"], default="run")
    p.add_argument("--data", help="data or string", default="hello")
    p.add_argument("--schema", help="json schema file", default="")
    args=p.parse_args()
    if args.mode=="encode":
        print(encode_b64(args.data))
    elif args.mode=="hash":
        print(md5(args.data))
    elif args.mode=="gen" and args.schema:
        import json
        s=json.load(open(args.schema))
        print(json.dumps(simple_generation(s), indent=2))
    else:
        print("OK")
if __name__=="__main__":
    main()
