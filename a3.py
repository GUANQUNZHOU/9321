import read as rd
import feature_selection as fs
import q3 as q
import bonus_part as bp
from flask_wtf import Form
from flask import Flask, render_template, request, flash
from wtforms import IntegerField, SubmitField, SelectField
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def hello_world():
    df = rd.read_data()
    return render_template('index.html')

@app.route('/fig/viewall')
def viewall():
    df = rd.read_data()
    q3 = rd.draw_chest_pain_type(df)
    q4 = rd.draw_resting_blood_pressure(df)
    q5 =rd.draw_serum_cholestoral(df)
    q6 = rd.draw_fasting_blood_sugar(df)
    q7 = rd.draw_RER(df)
    q8 = rd.draw_Mhra(df)
    q9 = rd.draw_exercise_induced_angina(df)
    q10 = rd.draw_ST_Depression(df)
    q11 = rd.draw_slope_exercise_ST_segment(df)
    q12 = rd.draw_major_vessels(df)
    q13 = rd.draw_thal(df)
    return render_template('part1_viewall.html', q3 = q3, q4 = q4, q5 = q5, q6 = q6, q7 = q7, q8 = q8\
        ,q9 = q9,q10 =q10,q11 = q11, q12 = q12, q13 = q13)

@app.route('/part1')
def part_1_main():
    return render_template('part1.html')

@app.route('/fig/<chart_no>')
def produce_chart(chart_no):
    df = rd.read_data()
    chart_no = int(chart_no)
    chart_produce = {1: ['rd.draw_chest_pain_type(df)', 'Chest Pain Type'],
            2: ['rd.draw_resting_blood_pressure(df)','Resting Blood Pressure'],
            3: ['rd.draw_serum_cholestoral(df)', 'Serum Cholestoral'],
            4: ['rd.draw_fasting_blood_sugar(df)','Fasting Blood Sugar'],
            5: ['rd.draw_RER(df)','Resting Electrocardiographic Results'],
            6: ['rd.draw_Mhra(df)', 'Maximum Heart Rate Achieved'],
            7: ['rd.draw_exercise_induced_angina(df)', 'Exercise Induced Angina'],
            8: ['rd.draw_ST_Depression(df)','ST Depression'],
            9: ['rd.draw_slope_exercise_ST_segment(df)','Slope of the Peak Exercise ST Segment'],
            10:[ 'rd.draw_major_vessels(df)','Number of Major Vessels'],
            11:[ 'rd.draw_thal(df)', 'Thal(Thalassemia)']
            }

    title = chart_produce[chart_no][1]
    graph = eval(chart_produce[chart_no][0])
    return render_template('specific_graph.html', graph = graph, graph_no = chart_no, title=title)

@app.route('/part2')
def part_2_main():
    chi_chart = fs.do_univariate()
    return render_template('part2.html', chi_chart = chi_chart)

@app.route('/cluster', methods=['GET','POST'])
def clusters():
    graph = bp.bonus_cluserting()
    return render_template('clusters.html', graph = graph)

class ContactForm(Form):
    age = IntegerField("age")
    sex = SelectField('sex', choices=[('M', 'Male'), ('F', 'Female')])
    chest_pain_type = SelectField('chest pain type', choices=[('1', 'Typical'), ('2', 'Atypical'),
                                                             ('3', 'Non-anginal'), ('4', 'Aymptotic')])
    resting_blood_pressure = IntegerField("resting blood pressure")
    serum_cholesterol = IntegerField("serum cholesterol")
    fasting_blood_sugar = SelectField('Fasting Blood Sugar', choices=[('0', '< 120mg/dl'), ('1', '> 120mg/dl')])
    resting_electrocardio_results = SelectField('Resting Electrocardio Results', choices=[('0', '< normal'),
                                                                                         ('1', 'having ST-T wave abnormality'),
                                                                                         ('2', 'showing probable or definite left ventricular hypertrophy by Estes’criteria')])
    maximum_heart_rate = IntegerField("Max Heart Rate")
    exercise_induced_angina = SelectField("Exercise Induced Angina", choices=[('0', 'no'), ('1', 'yes')])
    st_depression = IntegerField("ST Depression")
    slope_peak = SelectField("Slope of Peak Exercise ST Segment", choices=[('1', '1'),
                                                    ('2', '2'),
                                                    ('3', '3')])
    major_vessels = SelectField("Major Vessels Colored by Flourosopy", choices=[('0', '0'),
                                                    ('1', '1'),
                                                    ('2', '2'),
                                                    ('3', '3')])
    thalassemia = SelectField("Thalassemia", choices=[('3', 'normal'),
                                                     ('6', 'fixed defect'),
                                                     ('7', 'reversable defect')])
    submit = SubmitField("Predict")

@app.route('/part3', methods=['GET', 'POST'])
def part_3_main():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            error = "all fields required"
            return render_template('part3.html', form=form, error = error)
        else:
            print(form.data)
            for key in ['age', 'sex', 'submit', 'csrf_token']:
                 if key in form.data:
                    form.data.pop(key) 
            rankings = list(fs.do_univariate().values())
            graph = q.accuracy_selection(rankings)         
            heart_disease = q.predict(rankings,form.data)
            return render_template('part3.html', heart_disease = heart_disease, graph = graph)
    elif request.method == 'GET':
        return render_template('part3.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


