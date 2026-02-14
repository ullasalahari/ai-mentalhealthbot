Mental Health Companion Chatbot
A safe and supportive AI-based chatbot designed to help students express their emotions, reduce stress, and improve mental well-being through empathetic responses, relaxation tips, encouragement, and light humor.
________________________________________
->Project Overview
Students often experience stress, anxiety, loneliness, and academic pressure but hesitate to approach professional counselors due to stigma or fear of judgment.
This project aims to provide a safe, non-judgmental, and easily accessible mental health companion using Artificial Intelligence.
The chatbot detects user emotions from text input and responds with appropriate emotional support.
________________________________________
-> Objectives
•	To detect user emotions using text-based input
•	To provide empathetic and motivational responses
•	To suggest relaxation techniques during stress
•	To encourage users when they are happy
•	To uplift mood using jokes (with user permission)
•	To provide emergency guidance when critical keywords are detected
________________________________________
-> System Type
•	AI-Based System
•	Uses Machine Learning + Natural Language Processing (NLP)
•	Supervised Learning approach (labeled dataset)
________________________________________
📊->Dataset
•	Dataset downloaded from Kaggle
•	Contains text messages labeled with emotions
•	Used to train a supervised ML classifier
•	Dataset includes emotions like:
o	Happy
o	Sad
o	Stress
o	Neutral
o	Anxiety
________________________________________
->System Approach
1.	User enters text describing their feelings
2.	Keyword-based emotion detection is applied
3.	If keywords are not found, ML model predicts emotion
4.	Emotion is classified as:
o	Positive
o	Negative
o	Neutral
o	Emergency
5.	Chatbot generates an appropriate response:
o	Encouragement
o	Empathy + relaxation tips
o	Optional jokes (with permission)
o	Emergency support guidance
6.	User feedback is collected
________________________________________
->Algorithm
Training Phase
1.	Download dataset from Kaggle
2.	Preprocess text data
3.	Convert text to numerical form using TF-IDF
4.	Train supervised ML classifier
5.	Save trained model and vectorizer
Execution Phase
1.	Accept user input
2.	Detect emotion using keywords / ML model
3.	Generate response based on emotion
4.	Display output via Streamlit
5.	Collect feedback
________________________________________
->Technologies Used
•	Python 3.11
•	Streamlit
•	Scikit-learn
•	NLP (TF-IDF Vectorizer)
•	Pandas
•	NumPy
  ->Project Structure
mental/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── README.md

->Results

Accurate emotion detection from text input

Real-time empathetic chatbot responses

Improved user engagement using relaxation tips and humor

Emergency keywords trigger immediate support guidance

->Future Scope

Voice-based interaction

Mobile application deployment

Deep learning-based emotion detection

Multilingual chatbot support

Integration with professional counselors

->Conclusion

This project demonstrates how AI and Machine Learning can be used to support mental health awareness among students. The Mental Health Companion Chatbot provides immediate emotional assistance, reduces hesitation in sharing feelings, and promotes positive mental well-being.

->Acknowledgement

I sincerely thank my faculty, mentors, and Edunet Foundation for their guidance and support throughout this project.

_Author

Name: ullasalahari
Course: B.Tech (3rd Year)
Project: Mental Health Companion Chatbot
