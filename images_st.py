import streamlit as st
import cv2  
image =cv2.imread('cam103_person_70.jpg')
st.image(image, caption='Original Image', use_column_width=True)
transformation = st.sidebar.selectbox("Select a transformation",["gray","blur","edge"])
def apply_gray(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray
def apply_edge(image,threshold1,threshold2):
    edge = cv2.Canny(image,threshold1,threshold2)
    return edge
def apply_blur(image,radius):
    blur = cv2.GaussianBlur(image,(radius,radius),0)
    return blur
if transformation == "blur":
    radius = st.sidebar.slider("blur radius",1,10,5)
elif transformation == "edge":
    threshold1 = st.sidebar.slider("Edge Threshold1",0,255,100)
    threshold2 = st.sidebar.slider("Edge Threshold2",0,255,200)
    
    
#apply trasformation
if st.sidebar.button("Apply transformation"):
    transformed = None
    if transformation == "gray":
        transformed = apply_gray(image)
    elif transformation == "blur":
        transformed = apply_blur(image,radius)
    elif transformation == "edge":
        transformed = apply_edge(image,threshold1,threshold2)
    if transformed is not None :
        st.image(transformed,caption = "Transformed Image")
        