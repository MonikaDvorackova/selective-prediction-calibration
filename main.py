import math
def evaluate(y,p,thresholds=(0,.25,.5,.75,1)):
    if len(y)!=len(p) or not y:raise ValueError('equal non-empty inputs required')
    if any(not 0<=x<=1 for x in p):raise ValueError('probabilities must be in [0,1]')
    brier=sum((a-b)**2 for a,b in zip(y,p))/len(y);ece=0.0
    bins=10
    for k in range(bins):
        ix=[i for i,v in enumerate(p) if min(int(v*bins),bins-1)==k]
        if ix:ece+=len(ix)/len(y)*abs(sum(p[i] for i in ix)/len(ix)-sum(y[i] for i in ix)/len(ix))
    curve=[]
    for t in thresholds:
        kept=[i for i,v in enumerate(p) if abs(v-.5)>=t/2]
        err=sum((p[i]>=.5)!=bool(y[i]) for i in kept)/len(kept) if kept else None
        curve.append({'threshold':t,'coverage':len(kept)/len(y),'risk':err})
    return {'brier':brier,'ece_10_bins':ece,'risk_coverage':curve}
if __name__=='__main__':
    print(evaluate([1,0,1,0,1,0],[.91,.18,.63,.31,.55,.49]))
