import math,json,csv
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy.integrate import solve_ivp
P=Path(__file__).parent/'m10_results'; P.mkdir(exist_ok=True)
eps=3/140; mu=1.; A0=.1; omega=2*math.pi*.05
bar=math.sqrt(2); D=eps**2*mu*A0**2/4
vlim=math.sqrt(2*D*(1+math.exp(-2)))
def run(task):
 phase,eta,cycles,step,tol=task
 def rhs(s,z):
  y,v=z; A=A0*math.exp(-y*y/2); sn=math.sin(s+phase); th=math.tanh(A*sn)
  return v,mu*eps*y*A*sn*(1-th*th)/(1+eps*th)
 def out(s,z): return abs(z[0])-bar
 def ret(s,z): return abs(z[0])-bar
 def outer(s,z): return abs(z[0])-3
 out.direction=1; ret.direction=-1; outer.direction=1
 sol=solve_ivp(rhs,(0,cycles*2*math.pi),(0,eta*vlim),method='DOP853',events=[out,ret,outer],max_step=step,rtol=tol,atol=tol*.01)
 if not sol.success: raise RuntimeError(sol.message)
 ev=sol.t_events; returns=ev[1][ev[1]>ev[0][0]] if len(ev[0]) else []
 row=dict(phase=phase,eta=eta,cycles=cycles,max_step=step,rtol=tol,barrier=bool(len(ev[0])),outer=bool(len(ev[2])),returned=bool(len(returns)),t_barrier=float(ev[0][0]/omega) if len(ev[0]) else None,t_outer=float(ev[2][0]/omega) if len(ev[2]) else None,t_return=float(returns[0]/omega) if len(returns) else None,y_final=float(sol.y[0,-1]),v_final=float(sol.y[1,-1]),nfev=sol.nfev)
 return row
 def_unused=0
def sig(r): return r['barrier'],r['outer'],r['returned']
def save(name,rows):
 if not rows:return
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
if __name__=='__main__':
 phases=[2*math.pi*i/16 for i in range(16)]
 tasks=[(p,round(float(e),12),500,.4,1e-9) for p in phases for e in np.linspace(.8,1.2,21)]
 rows=[]
 with ProcessPoolExecutor(max_workers=8) as pool:
  for i,r in enumerate(pool.map(run,tasks)):
   rows.append(r)
   if (i+1)%21==0: print('base',i+1,'/336',flush=True);save('trajectories.csv',rows)
  cache={(r['phase'],r['eta']):r for r in rows}
  brackets=[]
  for p in phases:
   seq=sorted([r for r in rows if r['phase']==p],key=lambda r:r['eta'])
   brackets.extend((p,a['eta'],b['eta']) for a,b in zip(seq,seq[1:]) if sig(a)!=sig(b))
  final=[]
  while brackets:
   todo=[];wide=[]
   for p,a,b in brackets:
    if b-a<=.001:final.append((p,a,b))
    else: wide.append((p,a,b));todo.append((p,round((a+b)/2,12),500,.4,1e-9))
   results=list(pool.map(run,todo));rows.extend(results)
   for r in results:cache[r['phase'],r['eta']]=r
   brackets=[]
   for (p,a,b),r in zip(wide,results):
    m=r['eta']
    if sig(cache[p,a])!=sig(r):brackets.append((p,a,m))
    if sig(r)!=sig(cache[p,b]):brackets.append((p,m,b))
   print('refinement',len(rows),'remaining',len(brackets),flush=True)
  save('trajectories.csv',rows)
  save('transitions.csv',[dict(phase=p,eta_low=a,eta_high=b,low_sig=str(sig(cache[p,a])),high_sig=str(sig(cache[p,b]))) for p,a,b in sorted(final)])
  points=sorted(set((p,e) for p,a,b in final for e in (a,b)))
  checks=[]
  for config in [(500,.2,1e-11),(1000,.2,1e-11),(500,.1,1e-12)]:
   jobs=[(p,e,*config) for p,e in points]
   checks.extend(pool.map(run,jobs));print('validation',config,'done',flush=True);save('validation.csv',checks)
 print('FINISHED',len(rows),len(checks),flush=True)
