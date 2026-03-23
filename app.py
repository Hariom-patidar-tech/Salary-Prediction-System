import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="SalaryAI Pro",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>

/* Animated Gradient Background */

.stApp{
background: linear-gradient(-120deg,#8e2de2,#4a00e0,#6a11cb,#2575fc);
background-size:400% 400%;
animation:gradientBG 10s ease infinite;
font-family:'Segoe UI';
}

@keyframes gradientBG{
0%{background-position:0% 50%}
50%{background-position:100% 50%}
100%{background-position:0% 50%}
}

/* Title */

.main-title{
text-align:center;
font-size:50px;
font-weight:900;
color:white;
text-shadow:2px 2px 12px rgba(0,0,0,0.3);
}

.sub-title{
text-align:center;
color:white;
font-size:18px;
margin-bottom:40px;
}

/* Glass Panel */

.glass{
background:rgba(255,255,255,0.9);
padding:35px;
border-radius:20px;
box-shadow:0 15px 40px rgba(0,0,0,0.2);
backdrop-filter: blur(10px);
transition:0.3s;
}

.glass:hover{
transform:translateY(-5px);
}

/* Inputs */

.stNumberInput input{
height:50px;
border-radius:10px;
border:2px solid #6a11cb;
font-size:16px;
}

div[data-baseweb="select"] > div{
height:50px;
border-radius:10px;
border:2px solid #6a11cb;
}

/* Button */

.stButton>button{
width:100%;
height:55px;
border-radius:12px;
font-size:18px;
font-weight:700;
background:linear-gradient(135deg,#ffb347,#ffcc33);
color:black;
border:none;
transition:0.3s;
box-shadow:0 10px 25px rgba(0,0,0,0.3);
}

.stButton>button:hover{
transform:scale(1.05);
}

/* Animated Cards */

.info-card{
background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);
background-size:300% 300%;
animation:cardGradient 6s ease infinite;

padding:30px;
border-radius:20px;
text-align:center;
color:white;

box-shadow:0 15px 40px rgba(0,0,0,0.35);
transition:0.4s;
}

@keyframes cardGradient{
0%{background-position:0% 50%}
50%{background-position:100% 50%}
100%{background-position:0% 50%}
}

.info-card:hover{
transform:translateY(-10px) scale(1.03);
box-shadow:0 25px 60px rgba(0,0,0,0.45);
}

.card-title{
font-size:22px;
font-weight:700;
margin-bottom:10px;
}

.card-value{
font-size:42px;
font-weight:900;
}

/* Coin Animation */

.coin{
font-size:120px;
text-align:center;
animation:spinCoin 4s linear infinite;
}

@keyframes spinCoin{
0%{transform:rotateY(0deg)}
100%{transform:rotateY(360deg)}
}

.footer{
text-align:center;
color:white;
margin-top:40px;
font-size:15px;
}

</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_assets():
    model = joblib.load("salary_prediction_model.pkl")
    poly = joblib.load("poly_transform.pkl")
    columns = joblib.load("model_columns.pkl")
    return model, poly, columns

model, poly, model_columns = load_assets()


st.markdown("<div class='main-title'> Salary Prediction </div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>AI Powered Market Salary Estimation</div>", unsafe_allow_html=True)


col1, col2 = st.columns([1,1.2], gap="large")

with col1:

    st.markdown("<div class='coin'>🪙</div>", unsafe_allow_html=True)

    st.info("This is Predict Your Salary by using AI ")

with col2:

    

    st.subheader("User Information")

    c1,c2 = st.columns(2)

    with c1:
        age = st.number_input("Age",18,65,25)
        gender = st.selectbox("Gender",["Male","Female"])

    with c2:
        experience = st.number_input("Years of Experience",0,40,2)
        education = st.selectbox("Education Level",["Bachelor's","Master's","PhD"])

    job_titles = sorted([
        col.replace("Job Title_","")
        for col in model_columns
        if "Job Title_" in col
    ])

    job_title = st.selectbox("Job Title",job_titles)

    predict_btn = st.button("Predict Salary")

    st.markdown("</div>", unsafe_allow_html=True)

if predict_btn:

    gender_val = 1 if gender=="Male" else 0

    edu_map = {"Bachelor's":0,"Master's":1,"PhD":2}

    df = pd.DataFrame(0,index=[0],columns=model_columns)

    df.at[0,"Age"]=age
    df.at[0,"Gender"]=gender_val
    df.at[0,"Education Level"]=edu_map[education]
    df.at[0,"Years of Experience"]=experience

    job_col=f"Job Title_{job_title}"

    if job_col in df.columns:
        df.at[0,job_col]=1

    try:

        poly_input = poly.transform(df)

        prediction = model.predict(poly_input)[0]

        st.markdown("---")

        c1,c2,c3 = st.columns(3)

        # Salary Card
        with c1:
            st.markdown(f"""
            <div class="info-card">
            <div class="card-title"> Estimated Salary</div>
            <div class="card-value">₹ {max(0,int(prediction)):,}</div>
            </div>
            """, unsafe_allow_html=True)

        # Salary Level
        level="Average"

        if prediction < 40000:
            level="Low"
        elif prediction > 90000:
            level="High"

        with c2:
            st.markdown(f"""
            <div class="info-card">
            <div class="card-title">Salary Level</div>
            <div class="card-value">{level}</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="info-card">
            <div class="card-title"> AI Insight</div>
            <p>Higher education and more experience can significantly increase salary potential in this role.</p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(e)


st.markdown("<div class='footer'>Made by Hariom Patidar © 2026 Salary Prediction</div>", unsafe_allow_html=True)