import streamlit as st
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image
import os

# 🧠 Initiera state för canvas
if "canvas_key" not in st.session_state:
    st.session_state["canvas_key"] = "canvas"

# 📦 Ladda modellen lokalt
try:
    model_path = r'C:\Users\Player1\Desktop\EC Utbildning\Machine_Learning\kunskapskontroll_2_ml_ds24\my_trained_model.h5'
    model = load_model(model_path)
    st.write("Modellen har laddats framgångsrikt.")
except Exception as e:
    st.write(f"Det gick inte att ladda modellen: {e}")

# 🖌️ Titel
st.markdown('<h1 class="title">Handskriven Sifferigenkänning med CNN och Kalkylator</h1>', unsafe_allow_html=True)

# 🖼️ Ladda upp bild
uploaded_file = st.file_uploader("Ladda upp en egen bild av en siffra", type=["png", "jpg", "jpeg"])

# 🖊️ Rit-område och förutsägelse
col1, col2 = st.columns(2)

with col1:
    st.write("Här kan du rita siffror.")
    canvas_result = st_canvas(
        fill_color="white",
        stroke_width=20,
        stroke_color="white",
        background_color="black",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key=st.session_state["canvas_key"]
    )

    # 🧼 Rensa canvas genom att byta key
    if st.button("Rensa Canvas"):
        st.session_state["canvas_key"] = str(np.random.randint(1000000))
        st.experimental_rerun()

with col2:
    predicted_label = None
    image_array = None

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("L")
        image = image.resize((28, 28))
        image_array = np.array(image)
        st.image(image, caption="Uppladdad bild", use_container_width=True)

    elif canvas_result.image_data is not None and np.sum(canvas_result.image_data) > 0:
        image = Image.fromarray(canvas_result.image_data.astype("uint8"))
        image = image.convert("L")
        image = image.resize((28, 28))
        image_array = np.array(image)

    if image_array is not None:
        image_array = image_array.reshape(1, 28, 28, 1)
        image_array = image_array.astype("float32") / 255.0

        try:
            prediction = model.predict(image_array)
            predicted_label = int(np.argmax(prediction, axis=1)[0])
            st.write(f"Modellen förutspår att detta är siffran: {predicted_label}")
        except Exception as e:
            st.write(f"Fel vid förutsägelse: {e}")

# 📟 Kalkylator
if predicted_label is not None:
    st.sidebar.header("Kalkylator")
    num2 = st.sidebar.number_input("Ange ett annat tal", value=0.0)
    operation = st.sidebar.selectbox("Välj operation", ["Addition", "Subtraktion", "Multiplikation", "Division"])

    try:
        if operation == "Addition":
            result = predicted_label + num2
        elif operation == "Subtraktion":
            result = predicted_label - num2
        elif operation == "Multiplikation":
            result = predicted_label * num2
        elif operation == "Division":
            result = predicted_label / num2 if num2 != 0 else "Kan inte dela med 0"

        st.write(f"**Resultat**: {int(result) if isinstance(result, float) and result.is_integer() else result}")
    except Exception as e:
        st.write(f"Fel vid beräkningen: {e}")

# 🖼️ Sidomeny
st.sidebar.image("https://nyesteventuretech.com/images/Machine-Learning.jpg", use_container_width=True)
st.sidebar.write("Välkommen till handskrivna sifferigenkänning och kalkylator!")
