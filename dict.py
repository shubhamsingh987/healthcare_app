
# yoga and disease dictonary

yoga_dict={
"asthama":["Kapalabhati"],
"arthritis":["Trikonasana","Vrikshaasana","Gomukhasana"],
"anxiety":["veerbhadrasana","veerbhadrasana II"],
"spondylitis":["Tadasana(Mountain Pose)"],
"sciatica":["Vrikshasana(Tree Pose)"],
"Back Pain":["Adho Mukha Svanasana(Dog Pose)"],
"Weak Quadriceps":["Utkatasana(Chair Pose)"],
"Type 2 diabetes":["Supta Matsyendrasana"],
"Hair Loss":["Adho Mukha Savasana"],
"Acid Reflux":["Paschimottanasana"],
"High Cholestrol":["Sarvangasana"]

}

#client and pla dict
customer_dict={
"ID: P1234":"Plan B",
"ID: P9876":"Plan A",
"ID: P4567":"Plan C"


}

#plan descrtion

plans_dict={
    "Plan A":["anxiety"],
    "Plan B":["sciatica"],
    "Plan C":["spondylitis"]
}

def get_plan(val):
    for key, value in plans_dict.items():
         if val in value:
             return key