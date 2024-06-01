
import sqlite3

con = sqlite3.connect("workout_agent/workoutlib.db")
cur = con.cursor()


def insert_muscle_category(name: str, description: str):
    cur.execute(
        f"""
        INSERT INTO muscle_category(name, description) 
               VALUES ('{name}', '{description}')
        """
    )
    con.commit()



def insert_exercise_type(name: str, description: str):
    cur.execute(
        f"""
        INSERT INTO exercise_type(name, description) 
               VALUES ('{name}', '{description}')
        """
    )
    con.commit()
    return "Succesful insertion"


cur.execute("""
            CREATE TABLE muscle_category(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL
            ) STRICT;
            """)

cur.execute("""
            CREATE TABLE exercise_type(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL
            ) STRICT;""")

cur.execute("""
            CREATE TABLE exercises(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL,
                description TEXT,
                muscle_category_id INTEGER NOT NULL,
                exercise_type_id INTEGER NOT NULL,
                parent_id INTEGER,
                FOREIGN KEY (parent_id) REFERENCES exercises(id),
                FOREIGN KEY (exercise_type_id) REFERENCES exercise_type(id),
                FOREIGN KEY (muscle_category_id) REFERENCES muscle_category(id)
            ) STRICT;""")

exercise_categories =  {
"Vertical Pull": """Vertical pulling exercises target the muscles responsible for pulling movements in a vertical plane, primarily the lats, upper back, and the muscles of the back. These exercises are essential for developing back strength, improving posture, and achieving a well-balanced physique. Examples include pull-ups, lat pulldowns, and pullovers.""",
"Horizontal Pull": """Horizontal pulling exercises involve pulling movements in a horizontal plane, targeting the back, shoulders, and biceps muscles. These exercises are crucial for developing upper body strength, improving posture, and achieving a balanced physique. Examples include rows (barbell, dumbbell, cable), seated cable rows, and face pulls.""",
"Vertical Push": """Vertical pushing exercises primarily target the shoulder and triceps muscles. These exercises are beneficial for developing upper body strength, particularly in overhead pressing movements. They are commonly used in strength training programs to build muscle mass and power in the shoulders and arms. Examples include overhead presses, military presses, and push presses.""",
"Horizontal Push": """Horizontal pushing exercises are primarily focused on working the chest, shoulders, and triceps muscles. These exercises are essential for building upper body strength and developing a muscular chest and shoulders. They are commonly incorporated into strength training routines for both muscle building and overall upper body development. Examples include bench presses, chest presses, and push-ups.""",
"Posterior Chain": """The posterior chain exercises target the muscles on the backside of the body, including the hamstrings, glutes, lower back, and upper back. These exercises are crucial for developing overall strength, power, and stability, as well as improving posture and reducing the risk of injuries. Examples include deadlifts, hip thrusts, back extensions, and deadlift variations.""",
"Anterior Chain": """Anterior chain exercises target the muscles on the front side of the body, such as the quadriceps, hip flexors, and abdominals. These exercises are essential for developing lower body strength, core stability, and functional movement patterns. They are commonly used in strength training programs for athletes and individuals seeking improved performance in activities that involve running, jumping, and other dynamic movements. Examples include squats, lunges, leg raises, and crunches.""",
"Core": """Core exercises target the muscles that stabilize the trunk and spine, including the abdominals, lower back muscles, and hip muscles. These exercises are crucial for developing overall strength, stability, and injury prevention. A strong core is essential for maintaining proper posture, transferring force effectively during compound movements, and reducing the risk of back injuries. Examples include planks, anti-rotation movements, and compound lifts like squats and deadlifts.""",
"Arm Extension": """Arm extension exercises target the triceps muscles, which are responsible for extending the arms. These exercises are essential for developing arm strength and achieving well-defined triceps. Examples include triceps extensions (with dumbbells, cables, or machines), dips, and close-grip bench presses.""",
"Arm Flexion": """Arm flexion exercises target the biceps muscles, which are responsible for flexing or bending the arms. These exercises are crucial for developing arm strength and achieving well-developed biceps. Examples include biceps curls (with dumbbells, barbells, or cables), hammer curls, and chin-ups.""",
"Shoulder Isolation": """Shoulder isolation exercises target the deltoid muscles (anterior, lateral, and posterior deltoids) and are essential for developing well-rounded shoulder strength and definition. These exercises are often used to address muscle imbalances or target specific areas of the shoulders. Examples include lateral raises, front raises, and reverse flies."""
}

exercise_types = {
"Isolation": "Exercises that target a specific muscle group or individual muscle, allowing for focused development and muscle hypertrophy.",
"Compound": "Exercises that involve multiple muscle groups and joints working together, leading to a more comprehensive and functional workout for strength and hypertrophy.",
"Variations": "Variations of basic compound exercises that target specific muscle groups or provide a different challenge or range of motion for strength and hypertrophy.",
"Cardio": "Exercises that primarily target cardiovascular endurance and improve overall fitness and heart health.",
"GPP (General Physical Preparedness)": "Exercises that develop overall physical fitness, including strength, endurance, flexibility, and coordination, encompassing various training modalities like functional training, plyometrics, and others.",
}



for name, description in exercise_categories.items():
    insert_muscle_category(name, description)

for name, description in exercise_types.items():
    insert_exercise_type(name, description)

con.close()