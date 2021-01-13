# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from funkc import tr_ga

app = Flask(__name__)

@app.route('/pogasall', methods=['GET'])
def rut():
  aa=request.args.get('a',default=0,type=str)
  bb=request.args.get('b', default=0, type=str)
  a=int(aa)
  b=int(bb)
  Sar=[]
  for k in range(a):
    for j in range(b):
      P=2*(k+1+j+1)
      S=(k+1)*(j+1)
      rinda="Mala a ir "
      rinda=rinda+str(k+1)+", mala b ir "+str(j+1)+"; "
      rinda=rinda+"perimetrs(P)="+str(P)+" laukums(S)="+str(S)
      Sar.append(rinda)
  return render_template('sveikaPasaule.html', vards="Egil",rezultats=Sar)


@app.route('/pogas')
def pogas():
  return render_template('pogas.html', rezultats="rezits")

@app.route('/a',methods=['GET'])
def pogasall():
    aa=float(request.args.get('a',default='0',type=str))
    bb=float(request.args.get('b',default='0',type=str))
    cc=float(request.args.get('c',default='0',type=str))

    
    rez="perimetrs "+str(aa+bb+cc)
    return render_template('sveikaPasaule.html', vards="Trijstura parametri",rezultats=rez)


@app.route('/tests')
def health():
  return "Serveris darbojas Uh!"

if __name__ == '__main__':
  app.run()
