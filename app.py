from flask import Flask, render_template, request


app = Flask(__name__, static_folder='static')

length = ["Meter(m)", "Decimeter(dm)" , "Centimeter(cm)", "Mellimeter(mm)", "Kilometer(km)", "Yard", "Inches" , "feet(ft)"]
weight = ["Gram(m)", "Kilogram(kg)", "tonne(t)", "Milligram(mg)", "Pound(lb)", "Long Ton", "Short Ton", "Ounce(oz)"]
temp = ["Celsius (°C)", "Kelvin (K)", "Fahrenheit (°F)"]
time = ["Second(s)", "Millisecond(ms)", "Microsecond", "Picosecond", "Minute(min)", "Hour", "Day", "Week", "Month", "Year"]
volume = ["Cubic meter", "Cubic millimeters", "Cubic centimeters", "Cubic decimeter", "Milliliter(mL)", "Centiliter(cL)", "Deciliter(dL)", "Liter(L)", "Decaliter(dL)", "Hectoliter(hL)"]
area = ["Square millimeters", "Square centimeters", "Square decimeter", "Square meter", "square dekameter", "square kilometer", "hectare"]
velocity = ["m/s", "cm/s", "km/s", "m/h", "cm/h", "km/h"]
acceleration = ["m/(s^2)", "cm/(s^2)", "km/(s^2)"]
force = ["Newton(N) or kg.m/(s^2)", "Millinewton(mN)", "dyne(dyn)", "gram-force(gf)", "poundal(pdl)", "pound-force(lbf)", "kilogram-force(kgf)"]
work = ["N.m or Joule", "Dyne-cm or erg"]


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        if request.form.get("convert_units.html"):
            return render_template("convert_units.html")
        elif request.form.get("calculator.html"):
            return render_template("calculator.html")
    else:
       return render_template("/index.html")

@app.route("/convert_units", methods=["GET", "POST"])
def convert_units():
    if request.method == "POST":
        length = request.form.get("length")
        weight = request.form.get("weight")
        time = request.form.get("time")
        temp = request.form.get("temp")
        area = request.form.get("area")
        volume = request.form.get("volume")
        velocity = request.form.get("velocity")
        acceleration = request.form.get("acceleration")
        force = request.form.get("force")
        work = request.form.get("work")

        if length:
            return render_template("length.html")
        if weight:
            return render_template("weight.html")
        if time:
            return render_template("time.html")
        if temp:
            return render_template("temp.html")
        if area:
            return render_template("area.html")
        if volume:
            return render_template("volume.html")
        if velocity:
            return render_template("velocity.html")
        if acceleration:
            return render_template("acceleration.html")
        if force:
            return render_template("force.html")
        if work:
            return render_template("work.html")

    else:
        return render_template("convert_units.html")

@app.route("/calculator")
def calculator():
    return render_template('calculator.html')

@app.route("/length",  methods=["GET","POST"])
def LENGTH():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("length.html",apology="Enter number!", length=length)

        if fromnumber < 1:
            return render_template("length.html", apology="Enter positive number!", length=length)

        if not fromtext or not totext:
             return render_template("length.html", apology="FILL THE GAPS!", length=length)

        if (fromtext == length[0] and totext == length[0]) or (fromtext == length[1] and totext == length[1]) or (fromtext == length[2] and totext == length[2]) or (fromtext == length[3] and totext == length[3]) or(fromtext == length[4] and totext == length[4]) or(fromtext == length[5] and totext == length[5]) or (fromtext == length[6] and totext == length[6]) or (fromtext == length[7] and totext == length[7]):
            tonumber = fromnumber
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[0] and totext == length[1]) or (fromtext == length[1] and totext == length[2]) or (fromtext == length[2] and totext == length[3]):
            tonumber = fromnumber * 10
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[0] and totext == length[2]) or (fromtext == length[1] and totext == length[3]) :
            tonumber = fromnumber * 100
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[0] and totext == length[3]) or (fromtext == length[4] and totext == length[0]):
            tonumber = fromnumber * 1000
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[0] and totext == length[4]) or (fromtext == length[3] and totext == length[0]):
            tonumber = fromnumber * 0.001
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[0] and totext == length[5]):
            tonumber = fromnumber * 1.0936133
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[0] and totext == length[6]:
            tonumber = fromnumber * 39.3700787
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[0] and totext == length[7]:
            tonumber = fromnumber * 3.2808399
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[1] and totext == length[0]) or (fromtext == length[2] and totext == length[1]) or (fromtext == length[3] and totext == length[2]):
            tonumber = fromnumber * 0.1
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[1] and totext == length[4]:
            tonumber = fromnumber * 0.0001
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[1] and totext == length[5]:
            tonumber = fromnumber * 0.10936133
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[1] and totext == length[6]:
            tonumber = fromnumber * 3.937007874
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[1] and totext == length[7]:
            tonumber = fromnumber * 0.32808399
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == length[2] and totext == length[0]) or (fromtext == length[3] and totext == length[1]):
            tonumber = fromnumber * 0.01
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[2] and totext == length[4]:
            tonumber = fromnumber * 0.00001
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[2] and totext == length[5]:
            tonumber = fromnumber * 0.010936133
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[2] and totext == length[6]:
            tonumber = fromnumber * 0.393700787
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[2] and totext == length[7]:
            tonumber = fromnumber * 0.032808399
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[3] and totext == length[4]:
            tonumber = fromnumber * 0.000001
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[3] and totext == length[5]:
            tonumber = fromnumber * 0.0010936133
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[3] and totext == length[6]:
            tonumber = fromnumber * 0.0393700787
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[3] and totext == length[7]:
            tonumber = fromnumber * 0.0032808399
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[3] and totext == length[7]:
            tonumber = fromnumber * 0.0032808399
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[4] and totext == length[1]:
            tonumber = fromnumber * 10000
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[4] and totext == length[2]:
            tonumber = fromnumber * 100000
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[4] and totext == length[3]:
            tonumber = fromnumber * 1000000
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[4] and totext == length[5]:
            tonumber = fromnumber * 1093.6133
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[4] and totext == length[6]:
            tonumber = fromnumber * 39370.0787
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[4] and totext == length[7]:
            tonumber = fromnumber * 3280.8399
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[0]:
            tonumber = fromnumber * 0.9144
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[1]:
            tonumber = fromnumber * 9.14400
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[2]:
            tonumber = fromnumber * 91.44
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[3]:
            tonumber = fromnumber * 914.4
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[4]:
            tonumber = fromnumber * 0.0009144
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[6]:
            tonumber = fromnumber * 36
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[5] and totext == length[7]:
            tonumber = fromnumber * 3
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[0]:
            tonumber = fromnumber * 0.0254
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[1]:
            tonumber = fromnumber * 0.254
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[2]:
            tonumber = fromnumber * 2.54
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[3]:
            tonumber = fromnumber * 25.4
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[4]:
            tonumber = fromnumber * 0.0001524
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[5]:
            tonumber = fromnumber * 0.0833333333
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[6] and totext == length[7]:
            tonumber = fromnumber * 0.0833333333
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[0]:
            tonumber = fromnumber * 0.3048
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[1]:
            tonumber = fromnumber * 3.04800
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[2]:
            tonumber = fromnumber * 30.48
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[3]:
            tonumber = fromnumber * 304.8
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[4]:
            tonumber = fromnumber * 0.0003048
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[5]:
            tonumber = fromnumber * 0.333333333
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == length[7] and totext == length[6]:
            tonumber = fromnumber * 12
            return render_template("length.html",tonumber=tonumber, length=length, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("length.html",length = length)


@app.route("/weight", methods=["GET", "POST"])
def WEIGHT():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")


        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("weight.html",apology="Enter number!", weight=weight)

        if fromnumber < 1:
            return render_template("weight.html", apology="Enter positive number!", weight= weight)

        if not fromtext or not totext:
            return render_template("weight.html", apology="Fill the fields!", weight= weight)


        if (fromtext == weight[0] and totext == weight[0]) or (fromtext == weight[1] and totext == weight[1]) or (fromtext == weight[2] and totext == weight[2]) or (fromtext == weight[3] and totext == weight[3]) or (fromtext == weight[4] and totext == weight[4]) or (fromtext == weight[5] and totext == weight[5]) or (fromtext == weight[6] and totext == weight[6]) or (fromtext == weight[7] and totext == weight[7]):
            tonumber = fromnumber
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == weight[0] and totext == weight[1]) or ( fromtext == weight[1] and totext == weight[2]) or (fromtext == weight[3] and totext == weight[0]):
            tonumber = fromnumber * 0.001
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == weight[0] and totext == weight[2]) or (fromtext == weight[3] and totext == weight[1]):
            tonumber = fromnumber * 0.000001
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == weight[0] and totext == weight[3]) or (fromtext == weight[1] and totext == weight[0]) or (fromtext == weight[2] and totext == weight[1]):
            tonumber = fromnumber * 1000
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[0] and totext == weight[4]:
            tonumber = fromnumber * 0.00220462262
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[0] and totext == weight[5]:
            tonumber = fromnumber * (9.84206528 * 10**-7)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[0] and totext == weight[6]:
            tonumber = fromnumber * (1.10231131 * 10**-6)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[0] and totext == weight[7]:
            tonumber = fromnumber * 0.0352739619
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == weight[1] and totext == weight[3]) or (fromtext == weight[2] and totext == weight[0]):
            tonumber = fromnumber * 1000000
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[1] and totext == weight[4]:
            tonumber = fromnumber * 2.20462262
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[1] and totext == weight[5]:
            tonumber = fromnumber * 0.000984206528
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[1] and totext == weight[6]:
            tonumber = fromnumber * 0.00110231131
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[1] and totext == weight[7]:
            tonumber = fromnumber * 35.2739619
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[2] and totext == weight[3]:
            tonumber = fromnumber * 1000000000
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[2] and totext == weight[4]:
            tonumber = fromnumber * 2204.62262
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[2] and totext == weight[5]:
            tonumber = fromnumber * 0.984206528
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[2] and totext == weight[6]:
            tonumber = fromnumber * 1.10231131
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[2] and totext == weight[7]:
            tonumber = fromnumber * 35273.9619
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[3] and totext == weight[2]:
            tonumber = fromnumber * (1.0 * 10**-9)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[3] and totext == weight[4]:
            tonumber = fromnumber * (2.20462262 * 10**-6)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[3] and totext == weight[5]:
            tonumber = fromnumber * (9.84206528 * 10**-10)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[3] and totext == weight[6]:
            tonumber = fromnumber * (1.10231131 * 10**-9)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[3] and totext == weight[7]:
            tonumber = fromnumber * (3.52739619 * 10**-5)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[0]:
            tonumber = fromnumber * 453.59237
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[1]:
            tonumber = fromnumber * 0.45359237
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[2]:
            tonumber = fromnumber * 0.00045359237
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[3]:
            tonumber = fromnumber * 453592.37
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[5]:
            tonumber = fromnumber * 0.000446428571
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[6]:
            tonumber = fromnumber * 0.0005
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[4] and totext == weight[7]:
            tonumber = fromnumber * 16
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[0]:
            tonumber = fromnumber * 1016046.91
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[1]:
            tonumber = fromnumber * 1016.04691
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[2]:
            tonumber = fromnumber * 1.01604691
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[3]:
            tonumber = fromnumber * (1.01604691 * 10**9)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[4]:
            tonumber = fromnumber * 2240
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[6]:
            tonumber = fromnumber * 1.12
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[5] and totext == weight[7]:
            tonumber = fromnumber * 35840
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[0]:
            tonumber = fromnumber * 907184.74
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[1]:
            tonumber = fromnumber * 907.18474
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[2]:
            tonumber = fromnumber * 0.90718474
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[3]:
            tonumber = fromnumber * 907184740
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[4]:
            tonumber = fromnumber * 2000
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[5]:
            tonumber = fromnumber * 0.892857143
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[6] and totext == weight[7]:
            tonumber = fromnumber * 32000
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[0]:
            tonumber = fromnumber * 28.3495231
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[1]:
            tonumber = fromnumber * 0.0283495231
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[2]:
            tonumber = fromnumber * (2.83495231 * 10**-5)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[3]:
            tonumber = fromnumber * 28349.5231
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[4]:
            tonumber = fromnumber * 0.0625
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[5]:
            tonumber = fromnumber * (2.79017857 * 10**-5)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == weight[7] and totext == weight[6]:
            tonumber = fromnumber * (3.12500 * 10**-5)
            return render_template("weight.html",tonumber=tonumber,weight=weight, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("weight.html", weight=weight)


@app.route("/temp", methods=["GET", "POST"])
def TEMP():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("temp.html",apology="Enter number!", temp=temp)

        if not fromtext or not totext:
            return render_template("temp.html", apology="Fill the fields!", temp=temp)


        if (fromtext == temp[0] and totext == temp[0]) or (fromtext == temp[1] and totext == temp[1]) or (fromtext == temp[2] and totext == temp[2]):
            tonumber = fromnumber
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == temp[0] and totext == temp[1]:
            tonumber = fromnumber * 274.15
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == temp[0] and totext == temp[2]:
            tonumber = fromnumber * 33.8
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == temp[1] and totext == temp[0]:
            tonumber = fromnumber * -272.15
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == temp[1] and totext == temp[2]:
            tonumber = fromnumber * -457.87
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == temp[2] and totext == temp[0]:
            tonumber = fromnumber * -17.2222222
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == temp[2] and totext == temp[1]:
            tonumber = fromnumber * 255.927778
            return render_template("temp.html", tonumber=tonumber, temp=temp, fromtext=fromtext, totext=totext, fromnumber=fromnumber)
    else:
        return render_template("temp.html", temp=temp)


@app.route("/time", methods=["GET", "POST"])
def TIME():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("time.html",apology="Enter number!", time=time)

        if fromnumber < 1:
            return render_template("time.html", apology="Enter positive number!", time=time)

        if not fromtext or not totext:
            return render_template("time.html", apology="Fill the fields!", time=time)


        if (fromtext == time[0] and totext == time[0]) or (fromtext == time[1] and totext == time[1]) or (fromtext == time[2] and totext == time[2]) or (fromtext == time[3] and totext == time[3]) or (fromtext == time[4] and totext == time[4]) or (fromtext == time[5] and totext == time[5]) or (fromtext == time[6] and totext == time[6]) or (fromtext == time[7] and totext == time[7]) or (fromtext == time[8] and totext == time[8]) or (fromtext == time[9] and totext == time[9]):
            tonumber = fromnumber
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == time[0] and totext == time[1]) or (fromtext == time[1] and totext == time[2]):
            tonumber = fromnumber * 1000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == time[0] and totext == time[2]) or (fromtext == time[2] and totext == time[3]):
            tonumber = fromnumber * 1000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[3]:
            tonumber = fromnumber * 1000000000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[4]:
            tonumber = fromnumber * 0.0166666667
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[5]:
            tonumber = fromnumber * 0.000277777778
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[6]:
            tonumber = fromnumber * (1.15740741 * 10**-5)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[7]:
            tonumber = fromnumber * (1.65343915 * 10**-6)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[8]:
            tonumber = fromnumber * (3.80265176 * 10**-7)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[0] and totext == time[9]:
            tonumber = fromnumber * (3.16887646 * 10**-8)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == time[1] and totext == time[0]) or (fromtext == time[2] and totext == time[1]):
            tonumber = fromnumber * 0.001
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[3]:
            tonumber = fromnumber * 1000000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[4]:
            tonumber = fromnumber * (1.66666667 * 10**-5)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[5]:
            tonumber = fromnumber * (2.77777778 * 10**-7)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[6]:
            tonumber = fromnumber * (1.15740741 * 10**-8)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[7]:
            tonumber = fromnumber * (1.65343915 * 10**-9)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[8]:
            tonumber = fromnumber * (3.80265176 * 10**-10)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[1] and totext == time[9]:
            tonumber = fromnumber * (3.16887646 * 10**-11)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[0]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[4]:
            tonumber = fromnumber * (1.66666667 * 10**-8)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[5]:
            tonumber = fromnumber * (2.77777778 * 10**-10)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[6]:
            tonumber = fromnumber * (1.15740741 * 10**-11)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[7]:
            tonumber = fromnumber * (1.65343915 * 10**-12)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[8]:
            tonumber = fromnumber * (3.80265176 * 10**-13)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[2] and totext == time[9]:
            tonumber = fromnumber * (3.16887646 * 10**-14)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[0]:
            tonumber = fromnumber * (1.0 * 10**-12)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[1]:
            tonumber = fromnumber * (1.0 * 10**-9)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[2]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[4]:
            tonumber = fromnumber * (1.66666667 * 10**-14)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[5]:
            tonumber = fromnumber * (2.77777778 * 10**-16)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[6]:
            tonumber = fromnumber * (1.15740741 * 10**-17)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[7]:
            tonumber = fromnumber * (1.65343915 * 10**-18)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[8]:
            tonumber = fromnumber * (3.80265176 * 10**-19)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[3] and totext == time[9]:
            tonumber = fromnumber * (3.16887646 * 10**-20)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == time[4] and totext == time[0]) or (fromtext == time[5] and totext == time[4]):
            tonumber = fromnumber * 60
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[1]:
            tonumber = fromnumber * 60000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[2]:
            tonumber = fromnumber * 60000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[3]:
            tonumber = fromnumber * (6.0 * 10**13)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[5]:
            tonumber = fromnumber * 0.0166666667
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[6]:
            tonumber = fromnumber * 0.000694444444
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[7]:
            tonumber = fromnumber * (9.92063492 * 10**-5)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[8]:
            tonumber = fromnumber * (2.28159105 * 10**-5)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[4] and totext == time[9]:
            tonumber = fromnumber * (1.90132588 * 10**-6)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[0]:
            tonumber = fromnumber * 3600
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[1]:
            tonumber = fromnumber * 3600000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[2]:
            tonumber = fromnumber * 3600000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[3]:
            tonumber = fromnumber * (3.6 * 10**15)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[6]:
            tonumber = fromnumber * 0.0416666667
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[7]:
            tonumber = fromnumber * 0.00595238095
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[8]:
            tonumber = fromnumber * 0.00136895463
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[5] and totext == time[9]:
            tonumber = fromnumber * 0.000114079553
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[0]:
            tonumber = fromnumber * 86400
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[1]:
            tonumber = fromnumber * 86400000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[2]:
            tonumber = fromnumber * 86400000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[3]:
            tonumber = fromnumber * (8.64 * 10**16)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[4]:
            tonumber = fromnumber * 1440
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[5]:
            tonumber = fromnumber * 24
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[7]:
            tonumber = fromnumber * 0.142857143
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[8]:
            tonumber = fromnumber * 0.0328549112
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[6] and totext == time[9]:
            tonumber = fromnumber * 0.00273790926
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[0]:
            tonumber = fromnumber * 604800
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[1]:
            tonumber = fromnumber * 604800000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[2]:
            tonumber = fromnumber * 604800000000
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[3]:
            tonumber = fromnumber * (6.04800 * 10**17)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[4]:
            tonumber = fromnumber * 10080
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[5]:
            tonumber = fromnumber * 168
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[6]:
            tonumber = fromnumber * 7
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[8]:
            tonumber = fromnumber * 0.229984378
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[7] and totext == time[9]:
            tonumber = fromnumber * 0.0191653649
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[0]:
            tonumber = fromnumber * 2629743.83
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[1]:
            tonumber = fromnumber * (2.62974383 * 10**9)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[2]:
            tonumber = fromnumber * 2629743831225
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[3]:
            tonumber = fromnumber * (2.62974383 * 10**18)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[4]:
            tonumber = fromnumber * 43829.0639
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[5]:
            tonumber = fromnumber * 730.484398
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[6]:
            tonumber = fromnumber * 30.4368499
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[7]:
            tonumber = fromnumber * 4.34812141
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[8] and totext == time[9]:
            tonumber = fromnumber * 0.0833333333
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[0]:
            tonumber = fromnumber * 31556926
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[1]:
            tonumber = fromnumber * (3.1556926 * 10**10)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[2]:
            tonumber = fromnumber * (3.1556926 * 10**13)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[3]:
            tonumber = fromnumber * (3.1556926 * 10**19)
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[4]:
            tonumber = fromnumber * 525948.766
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[5]:
            tonumber = fromnumber * 8765.81277
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[6]:
            tonumber = fromnumber * 365.242199
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[7]:
            tonumber = fromnumber * 52.177457
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == time[9] and totext == time[8]:
            tonumber = fromnumber * 12
            return render_template("time.html", tonumber= tonumber, time=time, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("time.html" , time=time)


@app.route("/volume" , methods=["GET", "POST"])
def VOLUME():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("volume.html",apology="Enter number!", volume=volume)

        if fromnumber < 1:
            return render_template("volume.html", apology="Enter positive number!", volume= volume)

        if not fromtext or not totext:
            return render_template("volume.html", apology="Fill the fields!", volume=volume)


        if (fromtext == volume[0] and totext == volume[0]) or (fromtext == volume[1] and totext == volume[1]) or (fromtext == volume[2] and totext == volume[2]) or (fromtext == volume[3] and totext == volume[3]) or (fromtext == volume[4] and totext == volume[4]) or (fromtext == volume[5] and totext == volume[5]) or (fromtext == volume[6] and totext == volume[6]) or (fromtext == volume[7] and totext == volume[7]) or (fromtext == volume[8] and totext == volume[8]) or (fromtext == volume[9] and totext == volume[9]):
            tonumber = fromnumber
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[0] and totext == volume[1]:
            tonumber = fromnumber *  1000000000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[0] and totext == volume[2]) or (fromtext == volume[0] and totext == volume[4]) or (fromtext == volume[3] and totext == volume[1]) or (fromtext == volume[7] and totext == volume[1]):
            tonumber = fromnumber * 1000000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[0] and totext == volume[3]) or (fromtext == volume[0] and totext == volume[7]) or (fromtext == volume[2] and totext == volume[1]) or (fromtext == volume[3] and totext == volume[2]) or (fromtext == volume[3] and totext == volume[4]) or (fromtext == volume[4] and totext == volume[1]) or (fromtext == volume[7] and totext == volume[2]) or (fromtext == volume[7] and totext == volume[4]) or (fromtext == volume[9] and totext == volume[6]):
            tonumber = fromnumber * 1000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[0] and totext == volume[5]) or (fromtext == volume[6] and totext == volume[1]) or (fromtext == volume[9] and totext == volume[2]) or (fromtext == volume[9] and totext == volume[4]):
            tonumber = fromnumber * 100000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[0] and totext == volume[6]) or (fromtext == volume[5] and totext == volume[1]) or (fromtext == volume[8] and totext == volume[2]) or (fromtext == volume[8] and totext == volume[4]) or (fromtext == volume[9] and totext == volume[5]):
            tonumber = fromnumber * 10000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[0] and totext == volume[8]) or (fromtext == volume[3] and totext == volume[5]) or (fromtext == volume[6] and totext == volume[2]) or (fromtext == volume[6] and totext == volume[4]) or (fromtext == volume[7] and totext == volume[5]) or (fromtext == volume[8] and totext == volume[6]) or (fromtext == volume[9] and totext == volume[3]) or (fromtext == volume[9] and totext == volume[7]):
            tonumber = fromnumber * 100
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[0] and totext == volume[9]) or (fromtext == volume[3] and totext == volume[6]) or (fromtext == volume[5] and totext == volume[2]) or (fromtext == volume[5] and totext == volume[4]) or (fromtext == volume[6] and totext == volume[5]) or (fromtext == volume[7] and totext == volume[6]) or (fromtext == volume[8] and totext == volume[3]) or (fromtext == volume[8] and totext == volume[5]) or (fromtext == volume[8] and totext == volume[7]) or (fromtext == volume[9] and totext == volume[8]):
            tonumber = fromnumber * 10
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[1] and totext == volume[0]:
            tonumber = fromnumber * (1.0 * 10**-9)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[1] and totext == volume[2]) or (fromtext == volume[1] and totext == volume[4]) or (fromtext == volume[2] and totext == volume[3]) or (fromtext == volume[2] and totext == volume[7]) or (fromtext == volume[3] and totext == volume[0]) or (fromtext == volume[4] and totext == volume[3]) or (fromtext == volume[4] and totext == volume[7]) or (fromtext == volume[5] and totext == volume[8]) or (fromtext == volume[6] and totext == volume[9]) or (fromtext == volume[7] and totext == volume[0]):
            tonumber = fromnumber * 0.001
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[1] and totext == volume[3]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[1] and totext == volume[5]) or (fromtext == volume[2] and totext == volume[8]) or (fromtext == volume[4] and totext == volume[8]) or (fromtext == volume[5] and totext == volume[9]) or (fromtext == volume[6] and totext == volume[0]):
            tonumber = fromnumber * 0.0001
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[1] and totext == volume[6]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[1] and totext == volume[7]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[1] and totext == volume[8]:
            tonumber = fromnumber * (1.0 * 10**-7)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[1] and totext == volume[9]:
            tonumber = fromnumber * (1.0 * 10**-8)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[2] and totext == volume[0]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[2] and totext == volume[4]) or (fromtext == volume[3] and totext == volume[7]) or (fromtext == volume[4] and totext == volume[2]):
            tonumber = fromnumber * 1
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[2] and totext == volume[5]) or (fromtext == volume[3] and totext == volume[8]) or (fromtext == volume[4] and totext == volume[5]) or (fromtext == volume[5] and totext == volume[6]) or (fromtext == volume[6] and totext == volume[3]) or (fromtext == volume[6] and totext == volume[7]) or (fromtext == volume[7] and totext == volume[8]) or (fromtext == volume[8] and totext == volume[9]) or (fromtext == volume[9] and totext == volume[0]):
            tonumber = fromnumber * 0.1
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if (fromtext == volume[2] and totext == volume[6]) or (fromtext == volume[3] and totext == volume[9]) or (fromtext == volume[4] and totext == volume[6]) or (fromtext == volume[5] and totext == volume[3]) or (fromtext == volume[5] and totext == volume[7]) or (fromtext == volume[6] and totext == volume[8]) or (fromtext == volume[7] and totext == volume[9]) or (fromtext == volume[8] and totext == volume[0]):
            tonumber = fromnumber * 0.01
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[2] and totext == volume[9]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[4] and totext == volume[0]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[4] and totext == volume[9]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[5] and totext == volume[0]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[8] and totext == volume[1]:
            tonumber = fromnumber * 10000000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == volume[9] and totext == volume[1]:
            tonumber = fromnumber * 100000000
            return render_template("volume.html", tonumber=tonumber, volume=volume, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("volume.html", volume=volume)

@app.route("/area" , methods=["GET" , "POST"])
def AREA():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("area.html",apology="Enter number!", area=area)

        if fromnumber < 1:
            return render_template("area.html", apology="Enter positive number!", area=area)

        if not fromtext or not totext:
            return render_template("area.html", apology="Fill the fields!", area=area)


        if fromtext == area[0] and totext == area[0]:
            tonumber = fromnumber
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[0] and totext == area[1]:
            tonumber = fromnumber * 0.01
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[0] and totext == area[2]:
            tonumber = fromnumber * 0.0001
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[0] and totext == area[3]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[0] and totext == area[4]:
            tonumber = fromnumber * (1.0 * 10**-8)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[0] and totext == area[5]:
            tonumber = fromnumber * (1.0 * 10**-12)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[0] and totext == area[6]:
            tonumber = fromnumber * (1.0 * 10**-10)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[0]:
            tonumber = fromnumber * 100
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[1]:
            tonumber = fromnumber
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[2]:
            tonumber = fromnumber * 0.001
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[3]:
            tonumber = fromnumber * 0.0001
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[4]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[5]:
            tonumber = fromnumber * (1.0 * 10**-10)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[1] and totext == area[6]:
            tonumber = fromnumber * (1.0 * 10**-8)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[0]:
            tonumber = fromnumber * 10000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[1]:
            tonumber = fromnumber * 100
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[2]:
            tonumber = fromnumber
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[3]:
            tonumber = fromnumber * 0.01
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[4]:
            tonumber = fromnumber * 0.0001
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[5]:
            tonumber = fromnumber * (1.0 * 10**-8)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[2] and totext == area[6]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[0]:
            tonumber = fromnumber * 1000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[1]:
            tonumber = fromnumber * 10000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[2]:
            tonumber = fromnumber * 100
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[3]:
            tonumber = fromnumber
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[4]:
            tonumber = fromnumber * 0.01
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[5]:
            tonumber = fromnumber * (1.0 * 10**-6)
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[3] and totext == area[6]:
            tonumber = fromnumber * 0.0001
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[0]:
            tonumber = fromnumber * 100000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[1]:
            tonumber = fromnumber * 1000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[2]:
            tonumber = fromnumber * 10000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[3]:
            tonumber = fromnumber * 100
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[4]:
            tonumber = fromnumber
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[5]:
            tonumber = fromnumber * 0.0001
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[4] and totext == area[6]:
            tonumber = fromnumber * 0.01
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[0]:
            tonumber = fromnumber * 1000000000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[1]:
            tonumber = fromnumber * 10000000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[2]:
            tonumber = fromnumber * 100000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[3]:
            tonumber = fromnumber * 1000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[4]:
            tonumber = fromnumber * 10000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[5]:
            tonumber = fromnumber
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[5] and totext == area[6]:
            tonumber = fromnumber * 100
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[0]:
            tonumber = fromnumber * 10000000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[1]:
            tonumber = fromnumber * 100000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[2]:
            tonumber = fromnumber * 1000000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[3]:
            tonumber = fromnumber * 10000
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[4]:
            tonumber = fromnumber * 100
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[5]:
            tonumber = fromnumber * 0.01
            return render_template("area.html" , tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == area[6] and totext == area[6]:
            tonumber = fromnumber
            return render_template("area.html", tonumber=tonumber, area=area, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("area.html", area=area)

@app.route("/velocity" , methods=["GET" , "POST"])
def VILOCITY():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("velocity.html",apology="Enter number!", velocity=velocity)

        if not fromtext or not totext:
            return render_template("velocity.html", apology="Fill the fields!", velocity=velocity)

        if fromtext == velocity[0] and totext == velocity[0]:
            tonumber = fromnumber
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[0] and totext == velocity[1]:
            tonumber = fromnumber * 100
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[0] and totext == velocity[2]:
            tonumber = fromnumber * 0.001
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[0] and totext == velocity[3]:
            tonumber = fromnumber * 3600
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[0] and totext == velocity[4]:
            tonumber = fromnumber * 360000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[0] and totext == velocity[5]:
            tonumber = fromnumber * 3.6
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[1] and totext == velocity[0]:
            tonumber = fromnumber * 0.01
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[1] and totext == velocity[1]:
            tonumber = fromnumber
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[1] and totext == velocity[2]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[1] and totext == velocity[3]:
            tonumber = fromnumber * 36
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[1] and totext == velocity[4]:
            tonumber = fromnumber * 3600
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[1] and totext == velocity[5]:
            tonumber = fromnumber * 0.036
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[2] and totext == velocity[0]:
            tonumber = fromnumber * 1000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[2] and totext == velocity[1]:
            tonumber = fromnumber * 100000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[2] and totext == velocity[2]:
            tonumber = fromnumber
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[2] and totext == velocity[3]:
            tonumber = fromnumber * 3600000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[2] and totext == velocity[4]:
            tonumber = fromnumber * 360000000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[2] and totext == velocity[5]:
            tonumber = fromnumber * 3600
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[3] and totext == velocity[0]:
            tonumber = fromnumber * 0.0002777778
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[3] and totext == velocity[1]:
            tonumber = fromnumber * 0.02778
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[3] and totext == velocity[2]:
            tonumber = fromnumber * (1/3600000)
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[3] and totext == velocity[3]:
            tonumber = fromnumber
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[3] and totext == velocity[4]:
            tonumber = fromnumber * 100
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[3] and totext == velocity[5]:
            tonumber = fromnumber * 0.001
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[4] and totext == velocity[0]:
            tonumber = fromnumber * (1/360000)
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[4] and totext == velocity[1]:
            tonumber = fromnumber * 0.0002777778
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[4] and totext == velocity[2]:
            tonumber = fromnumber * (1/360000000)
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[4] and totext == velocity[3]:
            tonumber = fromnumber * 0.01
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[4] and totext == velocity[4]:
            tonumber = fromnumber
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[4] and totext == velocity[5]:
            tonumber = fromnumber * 0.00001
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[5] and totext == velocity[0]:
            tonumber = fromnumber * 0.277777778
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[5] and totext == velocity[1]:
            tonumber = fromnumber * 27.7777778
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[5] and totext == velocity[2]:
            tonumber = fromnumber * 0.000277777778
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[5] and totext == velocity[3]:
            tonumber = fromnumber * 1000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[5] and totext == velocity[4]:
            tonumber = fromnumber * 100000
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == velocity[5] and totext == velocity[5]:
            tonumber = fromnumber
            return render_template("velocity.html", tonumber= tonumber, velocity=velocity, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("velocity.html" ,velocity=velocity)

@app.route("/acceleration", methods=["GET", "POST"])
def ACCELERATION():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("acceleration.html",apology="Enter number!", acceleration=acceleration)

        if not fromtext or not totext:
            return render_template("acceleration.html", apology="Fill the fields!", acceleration=acceleration)

        if fromtext == acceleration[0] and totext == acceleration[0]:
            tonumber = fromnumber
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[0] and totext == acceleration[1]:
            tonumber = fromnumber * 100
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[0] and totext == acceleration[2]:
            tonumber = fromnumber * 0.001
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[1] and totext == acceleration[0]:
            tonumber = fromnumber * 0.01
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[1] and totext == acceleration[1]:
            tonumber = fromnumber
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[1] and totext == acceleration[2]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[2] and totext == acceleration[0]:
            tonumber = fromnumber * 1000
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[2] and totext == acceleration[1]:
            tonumber = fromnumber * 100000
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == acceleration[2] and totext == acceleration[2]:
            tonumber = fromnumber
            return render_template("acceleration.html", tonumber=tonumber, acceleration=acceleration, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("acceleration.html", acceleration=acceleration)

@app.route("/force", methods= ["GET", "POST"])
def FORCE():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("force.html",apology="Enter number!", force=force)

        if not fromtext or not totext:
            return render_template("force.html", apology="Fill the fields!", force=force)


        if fromtext == force[0] and totext == force[0]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[0] and totext == force[1]:
            tonumber = fromnumber * 1000
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[0] and totext == force[2]:
            tonumber = fromnumber * 100000
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[0] and totext == force[3]:
            tonumber = fromnumber * 101.9716212978
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[0] and totext == force[4]:
            tonumber = fromnumber * 7.2330138512
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[0] and totext == force[5]:
            tonumber = fromnumber * 0.224808943
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[0] and totext == force[6]:
            tonumber = fromnumber * 0.101971621
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[0]:
            tonumber = fromnumber * 0.001
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[1]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[2]:
            tonumber = fromnumber * 100
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[3]:
            tonumber = fromnumber * 0.1019716213
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[4]:
            tonumber = fromnumber * 0.0072330139
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[5]:
            tonumber = fromnumber * 0.000224808943
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[1] and totext == force[6]:
            tonumber = fromnumber * 0.000101971621
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[0]:
            tonumber = fromnumber * (1.0 * 10**-5)
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[1]:
            tonumber = fromnumber * 0.01
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[2]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[3]:
            tonumber = fromnumber * 0.0010197162
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[4]:
            tonumber = fromnumber * 0.0000723301
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[5]:
            tonumber = fromnumber * (2.24808943 * 10**-6)
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[2] and totext == force[6]:
            tonumber = fromnumber * (1.01971621 * 10**-6)
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[0]:
            tonumber = fromnumber * 0.00980665
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[1]:
            tonumber = fromnumber * 9.80665
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[2]:
            tonumber = fromnumber * 980.665
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[3]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[4]:
            tonumber = fromnumber * 0.0709316353
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[5]:
            tonumber = fromnumber * 0.0022046226
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[3] and totext == force[6]:
            tonumber = fromnumber * 0.001
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[0]:
            tonumber = fromnumber * 0.138255
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[1]:
            tonumber = fromnumber * 138.25495438
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[2]:
            tonumber = fromnumber * 13825.495438
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[3]:
            tonumber = fromnumber * 14.0980818502
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[4]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[5]:
            tonumber = fromnumber * 0.0310809502
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[4] and totext == force[6]:
            tonumber = fromnumber * 0.014098
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[0]:
            tonumber = fromnumber * 4.44822162
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[1]:
            tonumber = fromnumber * 4448.22162
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[2]:
            tonumber = fromnumber * 444822.162
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[3]:
            tonumber = fromnumber * 453.5923699994
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[4]:
            tonumber = fromnumber * 32.17
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[5]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[5] and totext == force[6]:
            tonumber = fromnumber * 0.45359237
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[0]:
            tonumber = fromnumber * 9.80665
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[1]:
            tonumber = fromnumber * 9806.65
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[2]:
            tonumber = fromnumber * 980665
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[3]:
            tonumber = fromnumber * 1000
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[4]:
            tonumber = fromnumber * 70.931635284
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[5]:
            tonumber = fromnumber * 2.20462262
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == force[6] and totext == force[6]:
            tonumber = fromnumber
            return render_template("force.html", tonumber=tonumber, force=force, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

    else:
        return render_template("force.html", force=force)

@app.route("/work", methods= ["GET", "POST"])
def WORK():
    if request.method == "POST":
        fromtext = request.form.get("from1")
        fromnumber = request.form.get("from2")
        totext = request.form.get("to1")

        try:
            fromnumber = int(fromnumber)
        except ValueError:
            return render_template("work.html",apology="Enter number!", work=work)

        if not fromtext or not totext:
            return render_template("work.html", apology="Fill the fields!", work=work)

        if (fromtext == work[0] and totext == work[0]) or (fromtext == work[1] and totext == work[1]):
            tonumber = fromnumber
            return render_template("work.html", tonumber=tonumber, work=work, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == work[0] and totext == work[1]:
            tonumber = fromnumber * 10000000
            return render_template("work.html", tonumber=tonumber, work=work, fromtext=fromtext, totext=totext, fromnumber=fromnumber)

        if fromtext == work[1] and totext == work[0]:
            tonumber = fromnumber * 0.001
            return render_template("work.html", tonumber=tonumber, work=work, fromtext=fromtext, totext=totext, fromnumber=fromnumber)
    else:
        return render_template("work.html", work=work)


if __name__ == '__main__':
    app.run(debug=True)
