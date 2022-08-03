
import cv2 , os 
import pytesseract
from PIL import Image
import spacy
import dict
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 165)

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
        org = (200, 1400)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        for ents in text.ents:
            if(ents.label_=="DISEASE"):
                d=dict.yoga_dict.get(ents.text)
                if(d is not None):
                    res='The patient is advised to perform '+"".join(d)
                    image = cv2.putText(image, res, org, font, fontScale, color, thickness, cv2.LINE_AA)
                    org = (200, 1500)
                    d=dict.customer_dict.get(p_id)
                    res='The patient is covered under  '+d
                    image = cv2.putText(image, res, org, font, fontScale, color, thickness, cv2.LINE_AA)

        image = cv2.resize(image, (768, 1366),interpolation = cv2.INTER_NEAREST)
        cv2.imshow("Prescrption",image)
        cv2.waitKey(delay=100)
        engine.say(res)
        engine.runAndWait()
        cv2.waitKey(delay=5000)