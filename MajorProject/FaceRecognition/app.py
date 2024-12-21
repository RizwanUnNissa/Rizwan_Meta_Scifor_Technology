import streamlit as st 
import cv2
import face_recognition as fr 
from add_data import get_data
from model import recognize





#---------------------------------------Page Configuration---------------------------------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="icon.png",
    layout="centered"
    )

st.title(":green[Face Recognition App]")



st.sidebar.title("Menu")

options = st.sidebar.radio(" ", options = ["About","Upload Image", "Face Recognition"])


#---------------------------------------About---------------------------------------------------

if options == "About":
	st.write(" ")
	st.write(" ")
	st.subheader("Welcome to the Face Recognition App :material/Person:", divider="green")
	st.write(" ")
	st.write(" ")
	st.markdown('''This is a face recognition app.  \n The sidebar menu contains two options: upload image and face recognition.  \n Upload image allows you to add a photo image to the database from your computer or webcam.  \n Face recognition allows you to upload any image from your browser or take a photo from webcam and returns the name of the recognized faces if available in the database.''')
	st.write(" ")
	st.write(" ")
	st.markdown("Have Fun!\
	 :confetti_ball:")

#---------------------------------------Dataset---------------------------------------------------
#### Upload image to database 

if options == "Upload Image":

	name = st.text_input("Enter your name", placeholder = "Name")
	values = ["Picture", "WebCam"]
	upload = st.selectbox("Select an option", options = values, index = values.index("Picture"))

	if upload == "Picture":
		uploaded_image = st.file_uploader("Upload", type = ["jpg","png","jpeg"])
		if uploaded_image is not None:
			st.image(uploaded_image)

			submit = st.button("Submit")

			if submit:
				if name == "":
					st.error("Please enter name")
				else:
					result = get_data(name, uploaded_image)
					if result:
						st.success("Image added to folder")



	if upload == "WebCam":

		uploaded_web_image = st.camera_input("Take a Picture")
		submit = st.button("Submit")

		if submit:
			if name == "":
				st.error("Please enter name")
			else:
				result = get_data(name, uploaded_web_image)
				if result:
					st.success("Image added to folder")


#---------------------------------------Face Recognition---------------------------------------------------

if options == "Face Recognition":
	values = ["Picture", "WebCam"]
	img_input = st.selectbox("Select an option", options = values, index=values.index("Picture"))
	tolerance = st.select_slider("Select Tolerance Value", options=(0.3,0.4,0.5,0.6), value=0.6)

	if img_input == "Picture":
		uploaded_image = st.file_uploader("Upload", type = ["jpg","png","jpeg"], accept_multiple_files=True)

		if len(uploaded_image) != 0:
			for img in uploaded_image:
				img = fr.load_image_file(img)
				image,name = recognize(img,tolerance)
				st.image(image)


	if img_input == "WebCam":

		uploaded_web_image = st.camera_input("Take a Picture")
		if uploaded_web_image:
			img = fr.load_image_file(uploaded_web_image)
			image,name = recognize(img,tolerance)
			st.image(image)

		


