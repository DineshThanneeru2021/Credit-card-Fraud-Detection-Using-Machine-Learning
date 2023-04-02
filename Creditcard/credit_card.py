import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Dinesh.settings')
import django
django.setup()
from Dinesh.settings import BASE_DIR
source_path=os.path.join(BASE_DIR,'data')
final_path=os.path.join(source_path,'creditcard.csv')
def credit_card(amount,path=final_path):
    import pandas as pd
    import numpy as np
    #import matplotlib.pyplot as plt
    #import seaborn as sns
    #from termcolor import colored as style # for text customization
    #pip install imblearn
    #data = pd.read_csv('creditcard.csv')
    data = pd.read_csv(path)
    y= data['Class']
    x= data.drop(columns=['Class'],axis=1)
    #splitting the data into train test
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.3,random_state=0)
    # fitting randomforest model
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier()
    #model_1
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=20,criterion='entropy', random_state=0,max_depth=10)
    classifier.fit(x_train,y_train)
    #f11=[1000.0,-1.3598071336738,-0.0727811733098497,-0.0727811733098497,-0.07278117330987,-0.0727811733098497,-0.0727811733098497,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,1.80049938079263,0.592940745385545,-0.270532677192282,0.817739308235294,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439-0.410430432848439-0.410430432848439-0.410430432848439-0.410430432848439-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,-0.410430432848439,0]
    f11=[-2.3122265423263,1.95199201064158,3.9979055875468,-0.522187864667764,-1.60985073229769,-1.426545319
    ,-2.537387306,1.391657248,-2.770089277,-2.772272145,3.202033207,-2.899907388,-0.595221881,-4.289253782,0.38972412,-1.14074718
    ,-2.830055675,-0.016822468,0.416955705,0.126910559,0.517232371,-0.035049369,-0.465211076,0.320198199,0.044519167,0.177839798,
     0.261145003,-0.143275875,-2.770089277,-1000]
    f11=[-2.312226542,-2.312226542,-2.312226542,1.951992011,-1.609850732,3.997905588,-0.522187865,-1.426545319,-2.537387306,1.391657248,-2.770089277,-2.772272145,3.202033207,-2.899907388	-0.595221881,-4.289253782,0.38972412,-1.14074718,-2.830055675,-0.016822468,0.416955705,0.126910559,0.517232371,-0.035049369,-0.465211076,0.320198199,0.044519167,0.177839798,0.261145003,-0.143275875]
    f11.append(amount)
    #print(len(f11))
    features = np.array([f11])
    prediction = classifier.predict(features)
    print("Prediction: {}".format(prediction))
    return prediction
