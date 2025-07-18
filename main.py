import streamlit as st
from PIL import Image, ExifTags

def correct_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif = image._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation, None)

            if orientation_value == 3:
                image = image.rotate(180, expand=True)
            elif orientation_value == 6:
                image = image.rotate(270, expand=True)
            elif orientation_value == 8:
                image = image.rotate(90, expand=True)
    except Exception:
        pass
    return image


# Load a local audio file (replace with your file path)



def path_to_byes(path: str):
    """Convert a file path to a bytes object."""
    with open(f"vidimg/{path}", "rb") as f:
        return f.read()

def get_img(path: str):
    image = Image.open(f"vidimg/{path}")
    return image

# Play audio when button is clicked

def main():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Happy Birthday, baby <3")

        st.write("")
        st.write("")

        if st.button("Introduction"):
            st.audio(path_to_byes("intro.mp3"), format="audio/mp3")

        st.write("")
        st.write("")

        st.image(get_img("IMG_5245.jpeg"), caption="A little peck", width=300)
        st.image(get_img("IMG_5066.jpg"), caption="Sweet Treat!", width=300)

        st.write("")
        st.write("")

        if st.button("19"):
            st.audio(path_to_byes("18.mp3"), format="audio/mp3")
        
        st.write("")
        st.write("")

        st.image(get_img("IMG_5248.jpeg"), caption="Retroreflective and introspective", width=300)
        st.image(get_img("IMG_5246.jpeg"), caption="Incomparable Swagger", width=300)
        
        st.write("")
        st.write("")

        if st.button("A Wintry Ballad"):
            st.audio(path_to_byes("december.mp3"), format="audio/mp3")
        
        st.write("")
        st.write("")

        st.image(get_img("IMG_5252.jpeg"), caption="A midly upset cutie patootie", width=300)
        st.image(get_img("IMG_5274.jpeg"), caption="A midly enchanted cutie patootie", width=300)
        
        st.write("")
        st.write("")

        if st.button("A Springtime Ballad"):
            st.audio(path_to_byes("pigeon.mp3"), format="audio/mp3")
        
        st.write("")
        st.write("")

        st.image(get_img("IMG_6454 2.JPG"), caption="Two lovers in twine", width=300)
        st.image(correct_orientation(get_img("IMG_6107.JPG")), caption="Two lovers who love to whine", width=300)
        
        st.write("")
        st.write("")

        if st.button("We're the ones who change"):
            st.audio(path_to_byes("night.mp3"), format="audio/mp3")
        
        st.write("")
        st.write("")

        st.image(correct_orientation(get_img("IMG_6383.JPG")), caption="Three silly meese", width=300)
        st.image(get_img("IMG_5005.jpg"), caption="A sleepy grumpasaurus", width=300)
        
        st.write("")
        st.write("")
        
        if st.button("I love you."):
            st.audio(path_to_byes("love.mp3"), format="audio/mp3")

        st.write("")
        st.write("")


# Set your password here
CORRECT_PASSWORD = "pumpkinmuffin"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Login Required")
    password = st.text_input("Enter password", type="password")
    if st.button("Login"):
        if password == CORRECT_PASSWORD:
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Incorrect password.")
else:
    main()