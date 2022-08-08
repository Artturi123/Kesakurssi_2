import math
from cmath import sin, cos, tan
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/trig/<func>/')
def trigonometry(func):
    
    angle = request.args['angle']
    unit = request.args.get('unit', default=None)
    
    try:
        angle = float(angle)
    except ValueError:
        abort(400)
    else:
        pass
    
    if unit == "degree":
        angle = math.radians(angle)
    elif unit != None:
        abort(400)
    else:
        pass
    
    if func == "sin":
        sinVar = sin(angle)
        sinVar = sinVar.real
        sinVar = round(sinVar, 3)
        sinVar = str(sinVar)
        return sinVar
    elif func == "cos":
        cosVar = cos(angle)
        cosVar = cosVar.real
        cosVar = round(cosVar, 3)
        cosVar = str(cosVar)
        return cosVar
    elif func == "tan":
        tanVar = tan(angle)
        tanVar = tanVar.real
        tanVar = round(tanVar, 3)
        tanVar = str(tanVar)
        return tanVar
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)   