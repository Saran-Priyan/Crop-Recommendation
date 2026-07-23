# Importing the required packages
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from sklearn.model_selection import train_test_split
from streamlit_lottie import st_lottie
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle


#Configuring the page details
st.set_page_config(page_title="Crop Prediction", page_icon=":seedling:", layout="wide",initial_sidebar_state="expanded")

#Function for loading Animations from Lottie
def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#Loading the required Datasets
SoilData=pd.read_csv("Soil.csv")
CropData=pd.read_csv("Crop.csv")
RainfallData=pd.read_csv("Rainfall.csv")

#Defining attributes and lists
lottie1 = load_lottie("https://assets2.lottiefiles.com/packages/lf20_xd9ypluc.json")
lottie2 = load_lottie("https://assets8.lottiefiles.com/private_files/lf30_4lyswkde.json")
Columns=["Nitrogen","Phosphorous","Potassium","Temperature","Humidity","pH","Rainfall","Final_Crop"]
InputColumns=["Nitrogen","Phosphorous","Potassium","Temperature","Humidity","pH","Rainfall"]
MLType=["Logistic Regression","Random Forest","Decision Tree","Naive Bayes","Support Vector Classifier"]
districts = {"Kancheepuram","Cuddalore","Villupuram","Vellore","Tiruvannamalai","Salem","Namakkal","Dharmapuri","Krishnagiri",
"Coimbatore","Tiruppur","Erode","Trichy","Perambalur","Ariyalur","Pudukkottai","Thanjavur","Thiruvarur","Madurai","Theni",
"Dindigul","Ramanathapuram","Sivagangai","Virudhunagar","Tirunelveli","Tuticorin","Kanyakumari","Nilgiris",}
tp = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER",
"ANNUAL"]

#Visualizing the Data using different Graphs and Charts
def scatterPlotDrawer(x,y,df):
    fig = plt.figure(figsize=(20,15))
    sns.set_style("darkgrid")
    sns.scatterplot(data=df, x=x, y=y,hue="Final_Crop", size="Final_Crop", palette="deep", sizes=(20, 200), legend="full")
    plt.xlabel(x, fontsize=22)
    plt.ylabel(y, fontsize=22)
    plt.xticks(rotation=90, fontsize=18)
    plt.legend(prop={'size': 18})
    plt.yticks(fontsize=16)
    st.write(fig)

def scatterPlotDrawer2(x,y,df):
    fig = plt.figure(figsize=(20,15))
    sns.set_style("darkgrid")
    sns.scatterplot(data=df, x=x, y=y,hue="District", size="District", palette="deep", sizes=(100, 500), legend="full")
    plt.xlabel(x, fontsize=22)
    plt.ylabel(y, fontsize=22)
    plt.xticks(rotation=90, fontsize=18)
    plt.legend(prop={'size': 18})
    plt.yticks(fontsize=16)
    st.write(fig)

def barPlotDrawer(x,y,df):
    fig = plt.figure(figsize=(20,15))
    sns.set_style("darkgrid")
    sns.barplot(data=df, x=x, y=y, color='lightgreen')
    plt.xlabel(x, fontsize=22)
    plt.ylabel(y, fontsize=22)
    plt.xticks(rotation=90, fontsize=18)
    plt.legend(prop={'size': 18})
    plt.yticks(fontsize=16)
    st.write(fig)

def main():
    #Creating menu with different tabs
    choice = option_menu(
            menu_title=None,
            options=["Home", "Data", "Analyzation", "Prediction"],
            icons=["house","bar-chart","activity","graph-up-arrow"],
            orientation="horizontal")

    #Creating HomeScreen with basic informations
    if choice == "Home":
        with st.container():
            left_column, right_column = st.columns((3.5,1))
            with left_column:
                st.header("CROPS AND SOIL")
                st.write("<h1 style='font-size:18px'> Soil is a mixture of organic matter, minerals, gases, liquids, and countless microorganisms that together support life on Earth. \n" 
                "It is a complex and dynamic natural resource that is essential for growing crops and plants, supporting wildlife, and regulating the water cycle. \n"
                "Soil is formed from the weathering of rocks and minerals and the decomposition of organic matter. It is comprised of various layers, each with different physical and chemical properties. \n"
                "The top layer is called the surface soil, which is rich in organic matter and microorganisms. The subsoil is composed mainly of minerals, while the subsoil below that is composed of rock fragments. \n"
                "Soil also plays a crucial role in regulating the Earth's carbon cycle by storing carbon in the form of organic matter. Healthy soil is essential for sustainable agriculture and for maintaining the health of ecosystems and the planet as a whole.\n </h1>",unsafe_allow_html=True)
                st.write("")
            with right_column:
                st_lottie(lottie1, height=300, key="Plant-1")
        st.markdown("""---""")
        with st.container():
            left_column, right_column = st.columns((1,3.5))
            with left_column:
                st_lottie(lottie2,height=300,key="Plant-2")
            with right_column:
                st.write("")
                st.write("")
                st.subheader("Which Crops grow best in which soil?")
                st.write("<h1 style='font-size:18px'>The type of soil that a crop grows best in depends on several factors, including the crop's nutrient requirements, pH preference, and water-holding capacity. Here are some general guidelines for crops and the types of soil they prefer: \n"
                "Tomatoes, peppers, eggplants, and other vegetables in the nightshade family prefer well-drained soils with a slightly acidic pH of 6.0 to 6.5. Root crops like carrots, beets, and radishes do well in loose, well-drained soils with a pH range of 6.0 to 7.0. \n"
                "Potatoes grow best in well-drained, fertile soils with a pH range of 4.5 to 7.0. Broccoli, cauliflower, cabbage, and other cole crops prefer soils with a pH of 6.0 to 7.0 that are high in organic matter.\n"
                " Corn, beans, and other legumes are well-suited to fertile, well-drained soils with a pH. \n </h1>",unsafe_allow_html=True)

    #Creating the Data Tab
    if choice == "Data":
        with st.container():
            left_column,middle_column, right_column = st.columns((1,2,1))
            with middle_column:
                st.subheader("Overview of the Data :")
                DataSet = st.selectbox("Select The DataSet", ('Soil Data', 'Crop Data', 'Rainfall Data'))
                if DataSet == 'Soil Data':
                    
                    st.write(SoilData)
                if DataSet == 'Crop Data':
                    
                    st.write(CropData)
                if DataSet == 'Rainfall Data':
                    
                    st.write(RainfallData)

        #Information about the Parameters
        with st.container():
            left_column,middle_column, right_column = st.columns((1,3,1))
            with middle_column:
                st.write("")
                st.write("The parameters that are used as inputs in this crop prediction model to estimate the expected growth of the crop. The model could use machine learning algorithms, statistical models, or other methods to analyze the relationships between these parameters and crop growth, and make predictions based on the input values.")
                st.markdown("""---""")
                st.subheader("Parameters used for this Prediction Model :")
                st.write(" ⁕ Humidity: High humidity levels can create a favorable environment for pests and diseases, while low humidity levels can cause water stress in plants. An optimal range of humidity for crop growth varies depending on the crop and the climate.")
                st.write(" ⁕ pH: The pH of the soil affects the availability of nutrients to the plants. Most crops grow best in soil with a pH between 6.0 and 7.0, but some crops have specific requirements. For example, blueberries prefer soil with a pH between 4.0 and 5.0.")
                st.write(" ⁕ Temperature: The temperature affects plant growth by affecting metabolic processes and water uptake. Each crop has a specific range of temperatures that is optimal for growth. For example, most crops grow best between 20°C and 30°C.")
                st.write(" ⁕ District: The district within the state can have further variations in climate, soil type, and water resources, affecting crop growth.")
                st.write(" ⁕ Potassium: Potassium is an essential nutrient for plant growth, and it plays a role in water regulation, photosynthesis, and disease resistance.")
                st.write(" ⁕ Phosphorus: Phosphorus is also an essential nutrient for plant growth, and it plays a role in energy storage and transfer, root growth, and flower and seed production.")
                st.write(" ⁕ Nitrogen: Nitrogen is a key nutrient for plant growth, and it plays a role in photosynthesis, chlorophyll synthesis, and protein production.")
                st.write(" ⁕ Rainfall: Adequate rainfall is important for crop growth, as it provides the water needed for photosynthesis and other metabolic processes. Too much or too little rainfall can both be problematic for crop growth.")

    #Creating Analyzation Tab
    if choice == "Analyzation":
        with st.container():
            left_column,middle_column, right_column = st.columns((2,0.2,2))
            with left_column:
                DataSet = st.selectbox("Select The DataSet", ('Soil Data', 'Crop Data'))
                if DataSet == 'Crop Data':
                    plot_type = st.selectbox("Select The Type Of Graph", ('Bar Graph', 'Scatter Plot'))
                    st.subheader("Relation Between Soil Components")

                    if plot_type == 'Bar Graph':
                        x = "Final_Crop"
                        y = st.selectbox("Select the Parameter to plot",(["Nitrogen","Phosphorus","Potassium","Temperature","Humidity","pH","Rainfall"]))
                    if plot_type == 'Scatter Plot':
                        x = st.selectbox("Select the Parameter-1",(["Nitrogen","Phosphorus","Potassium","Temperature","Humidity","pH","Rainfall"]))
                        y = st.selectbox("Select the Parameter-2",(["Nitrogen","Phosphorus","Potassium","Temperature","Humidity","pH","Rainfall"]))
                    
                    if st.button("View The Graph"):
                        with right_column:
                            if plot_type == 'Bar Graph':
                                barPlotDrawer(x, y,CropData)
                            if plot_type == 'Scatter Plot':
                                scatterPlotDrawer(x, y,CropData)

                if DataSet == 'Soil Data':
                    plot_type = st.selectbox("Select The Type Of Graph", ('Bar Graph', 'Scatter Plot'))
                    if plot_type == 'Bar Graph':
                        x = "District"
                        y = st.selectbox("Select the Parameter to plot",(["Nitrogen","Phosphorous","Potassium","pH"]))
                    if plot_type == 'Scatter Plot':
                        x = st.selectbox("Select the Parameter-1",(["Nitrogen","Phosphorous","Potassium","pH"]))
                        y = st.selectbox("Select the Parameter-2",(["Nitrogen","Phosphorous","Potassium","pH"]))
                    
                    if st.button("View The Graph"):
                        with right_column:
                            if plot_type == 'Bar Graph':
                                barPlotDrawer(x, y,SoilData)
                            if plot_type == 'Scatter Plot':
                                scatterPlotDrawer2(x, y,SoilData)

    #Creating the Prediction Tab
    if choice == "Prediction":
        with st.container():
            left_column,middle_column, right_column = st.columns((1,3,1))
            with middle_column:
                st.header("Choose the Parameters to predict the right crop for the land")
                #Input parameters to be predicted
                district = st.selectbox("Select the District",districts)
                month = st.text_input("Enter the Month")
                year = st.text_input("Enter the Year")
                temperature = st.number_input('Enter the TEMPERATURE', 5, 45)
                humidity = st.number_input('Enter the HUMIDITY', 10, 100)

                if st.button("Submit"):               
                    def get_soil_parameters(location, dataset):
                        location_data = dataset[dataset['District'] == location]
                        if location_data.empty:
                            print(f"No data found for {location}.")
                            return None
                        # Extracting soil parameters from Soil Dataset
                        n_level = location_data['Nitrogen'].values[0]
                        k_level = location_data['Potassium'].values[0]
                        p_level = location_data['Phosphorous'].values[0]
                        ph_level = location_data['pH'].values[0]
                        return n_level, k_level, p_level, ph_level
                    # Get soil parameters for the choosen location
                    n, k, p, ph = get_soil_parameters(district, SoilData)
                    
                    # Reading the Rainfall CSV file
                    file_path = 'Rainfall.csv'
                    data = pd.read_csv(file_path)

                    # Function to predict rainfall for a given month and year
                    def predict_rainfall_for_month(month, year):
                        # Mapping months to seasons
                        months_to_season = {
                            'January': 'WINTER SEASON',
                            'February': 'WINTER SEASON',
                            'March': 'SUMMER SEASON',
                            'April': 'SUMMER SEASON',
                            'May': 'SUMMER SEASON',
                            'June': 'SOUTH-WESTMONSOON',
                            'July': 'SOUTH-WESTMONSOON',
                            'August': 'SOUTH-WESTMONSOON',
                            'September': 'NORTH-EASTMONSOON',
                            'October': 'NORTH-EASTMONSOON',
                            'November': 'NORTH-EASTMONSOON',
                            'December': 'WINTER SEASON'
                        }
                        season = months_to_season[month]
                        season_data = data.filter(regex=f'^{season}')
                        column_names = season_data.iloc[0].tolist()
                        season_data = season_data[2:]
                        season_data.columns = column_names
                        #Choosing Input and Output Parameters
                        X = season_data.index.values.reshape(-1, 1)
                        y = season_data['Normal'].values
                        # Splitting the data for training and testing
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                        # Model initialization and fitting (Random Forest)
                        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
                        rf_model.fit(X_train, y_train)
                        # Predicting rainfall for the choosen time period
                        next_year = season_data.index.max() + 1
                        predicted_rainfall_rf = rf_model.predict([[next_year]])
                        return predicted_rainfall_rf[0]
                    rainfall = predict_rainfall_for_month(month, year)

                    #Predicting the best crop using XGBoost
                    with open('xgboost_crop_model.pkl', 'rb') as file:
                        xgboost_model = pickle.load(file)
                    # Define the input parameters for prediction
                    input_parameters = [n, k, p, ph, temperature, humidity, rainfall]
                    # Reshape the input parameters
                    input_parameters = [input_parameters]
                    # Predict the crop using the loaded model
                    predicted_crop = xgboost_model.predict(input_parameters)

                    label_mapping = {
                        0: 'Rice', 1: 'Maize', 2: 'Chickpea', 3: 'Kidneybeans', 4: 'Pigeonpeas',
                        5: 'Mothbeans', 6: 'Mungbean', 7: 'Blackgram', 8: 'Lentil', 9: 'Pomegranate',
                        10: 'Banana', 11: 'Mango', 12: 'Grapes', 13: 'Watermelon', 14: 'Muskmelon',
                        15: 'Apple', 16: 'Orange', 17: 'Papaya', 18: 'Coconut', 19: 'Cotton',
                        20: 'Jute', 21: 'Coffee'
                    }
                    # Using the model prediction result
                    predicted_crop_name = label_mapping[predicted_crop[0]]
                    print(f"The predicted crop is: {predicted_crop_name}")
                    st.write("The predicted crop is:",predicted_crop_name)

if __name__=='__main__':
    main()