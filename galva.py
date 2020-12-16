# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from funkc import tr_ga

app = Flask(__name__)

@app.route('/a',methods=['GET'])
def root():
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
