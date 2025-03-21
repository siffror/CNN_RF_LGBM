MNIST Sifferklassificering

Detta projekt handlar om att klassificera handskrivna siffror från MNIST-datasetet med hjälp av Random Forest, LightGBM och CNN. Projektet innehåller en Streamlit-app 
där användaren kan rita en siffra eller ladda upp en bild för klassificering.


 Funktioner:

Klassificering av handritade siffror

Tre modeller: Random Forest, LightGBM och CNN

Möjlighet att testa modellen på slumpmässiga MNIST-bilder

Rita en siffra direkt i appen+ en kalkylator (CNN är den använda modellen: ) => https://ds24cnn.streamlit.app/


Modellbeskrivning

Random Forest 

- Enkel men kraftfull modell för klassificering

Används för att jämföra med mer avancerade modeller

LightGBM 

- Gradient boosting-modell optimerad för hastighet och prestanda

- Kan hantera stora datamängder effektivt

CNN (Convolutional Neural Network) Den uppladdade modellen (cnn_model.h5)

- Djupinlärningsmodell byggd med TensorFlow/Keras

- Högsta noggrannhet på testdata


 Licens & Tack:

Kod och dataset är öppna för alla att använda och modifiera. MNIST-datasetet är tillgängligt under en fri licens.

Byggt med Streamlit, Scikit-Learn, LightGBM, och TensorFlow.
