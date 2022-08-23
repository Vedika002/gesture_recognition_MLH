# gesture_recognition_MLH
Gesture recognition to solve CAPTCHAs
CAPTCHA can be solved by human beings only and not by bots and thus helps in stopping hackers and especially their crawlers also called spiders from acceding un-perplexed areas of the net. CAPTCHAs used till date have now become time-consuming and need more human efforts so that program could not crack it and this has become a major issue to consider as lead to time wastage. This paper has proposed a better model to generate CAPTCHA with the help of hand gesture recognition techniques which is more efficient than the traditional CAPTCHAs.
Index Terms—CAPTCHAs, security, computer vision, gesture recognition, CNN, sign recognition

Problem Definition - CAPTCHAs are used by websites to restrict bots and give access to humans(users). Bots are basically computer programmes that are usually set to either extract information from a database or hack into systems. CAPTCHAs provide challenges that are difficult for computer programs to break but relatively easy for humans. For example, identifying stretched letters or numbers, or clicking in a specific area.
The goal of captcha is to differentiate users from computer programs and give access accordingly. Traditional CAPTCHA technology leads to human inconvenience by
Requiring them to solve either a mathematical or puzzle based problem.Thus increasing difficulty and computation time.

Methodology -
The proposed model is a real-time hand gesture-based CAPTCHA system. The user is prompted to replicate the gesture displayed on the screen in front of their camera. The captured input video is passed to the server for further operations.
After preprocessing of the images, it is compared with the given gesture, if a match (model accuracy score) of over 95% is found, the user is declared human. Otherwise, the user gets 2 more turns to authenticate themselves.

Overview of Project - The project is designed as a simple user friendly CAPTCHA system, which does not require much computation on the user’s end. Gesture based models are less time consuming and more result oriented. Our model accesses real-time input through the front camera of a device wherein users are required to do some trivial hand gestures like waving etc.
The project uses 36 different kinds of hand gestures which were used to train the CNN model with an accuracy of 100%. The CNN model of 2 hidden layers with one input and one output layer. In the testing part we randomly choose a gesture from dataset and it will be displayed as a CAPTCHA test, the user is given three chances, if the user will be able to pass the CAPTCHA the code will display “LOGIN SUCCESSFUL” else it will show “TRY AGAIN”.



