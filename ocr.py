
import cv2 , os 
import pytesseract
from PIL import Image
import spacy
import dict
import pyttsx3
import dataframe_image as dfi
import pandas as pd

engine = pyttsx3.init()
engine.setProperty('rate', 165)

df = pd.DataFrame(dict.plans_dict)
df_styled = df.style.background_gradient()
dfi.export(df.style.hide(axis='index'), "./img/plans.png")

img2 = cv2.imread("./img/plans.png")
nlp = spacy.load("en_ner_bc5cdr_md") 
files=os.listdir("./img/")
for filename in files:
    filename="./img/"+filename
    if filename.endswith(".jpg"): 
        image=cv2.imread(filename)
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(Image.open(filename))
        p_id=text[text.index("ID:"):text.index("ID:")+10].strip()
        text=nlp(text.lower())
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        speak=""
        for ents in text.ents:
            if(ents.label_=="DISEASE"):
                d=ents.text
                y=dict.yoga_dict.get(d)
                if(y is not None):
                    org = (200, 1200)
                    res='FINDINGS'
                    image = cv2.putText(image, res, org, font, fontScale, color, thickness, cv2.LINE_AA)
                    org = (200, 1300)
                    res='The patient is diagonsed for '+d
                    speak+=res
                    image = cv2.putText(image, res, org, font, fontScale, color, thickness, cv2.LINE_AA)
                    org = (200, 1400)
                    res='The patient is advised to perform '+"".join(y)
                    speak+=res
                    image = cv2.putText(image, res, org, font, fontScale, color, thickness, cv2.LINE_AA)
                    org = (200, 1500)
                    p=dict.customer_dict.get(p_id)
                    if d in dict.plans_dict.get(p): res='The patient is already covered under  '+p
                    else: res='The patient is not covered under  '+p+" and  needs to upgrade the plan to "+(dict.get_plan(str(d)))
                    speak+=res
                    image = cv2.putText(image, res, org, font, fontScale, color, thickness, cv2.LINE_AA)
                    org = (220, 1570)
                    image = cv2.putText(image, 'PLAN LIST', org, font, fontScale, color, thickness, cv2.LINE_AA)
        image = cv2.resize(image, (768, 1366),interpolation = cv2.INTER_NEAREST)
        image[1000:1000+54,100:100+200,:] = img2[0:54,0:200,:]
        cv2.imshow("Prescrption",image)
        cv2.waitKey(delay=100)
        engine.say(speak)
        engine.runAndWait()
        cv2.waitKey(delay=5000)