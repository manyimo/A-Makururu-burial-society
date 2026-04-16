
import json

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

from streamlit_option_menu import option_menu


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ____assests ____




# 2.horizontal menu
with st.sidebar:
    selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Services", "Contact", "Paymant"],
    icons=["house","book", "person-lines-fill","wallet2"],
    orientation="horizontal",
            styles={
                "container": {
                    "padding": "10px 0px", 
                    "background-color": "#ffffff",
                    "margin": "0px auto",  
                    "border": "1px solid #000000",
                    "border-radius": "20px", 
                },
                "icon": {
                    "color": "#0069b4",  
                    "font-size": "16px"
                },
                "nav-link": {
                    "font-size": "16px", 
                    "text-align": "left", 
                    "margin": "10px", 
                    "--hover-color": "#B3D3F0"
                },
                "nav-link-selected": {
                    "background-color": "#0069b4", 
                    "font-size": "16px",
                },
            }
    
)
   

if selected == "Home":
    st.title(f"welcome to Dr Andby Makururu burial society {selected}")
   
    left_column, right_column = st.columns(2)
    with left_column:
     st.write(
     """
        when death comes unexpectedly it leaves everyone in pain that's when you need a shoulder to cry on and someone to help you on your next step from the death of our loved one until their final memorial we guide the family through the process assuring that tier loved one is remembered the way they want
        """
)
    with right_column:
     
     lottie_coding = load_lottieurl("https://lottie.host/52f878e6-f3c2-462a-84fc-09682a9a55a9/ToskniWRux.json")
    st.write(
            """ 
        "When loss strikes, let our burial society be your family's support. We understand the pain, we share the tears, and together we bring dignity to our loved ones. Join us in building a community of care and compassion together as JOHANNE THE FIFTH OF AFRICA INTERNATIONAL CHURCH as our Philanthropist  Arch Bishop Dr Andby Makururu says' lets' bury each other with dignity."
""")
    with right_column:
      st_lottie( lottie_coding, height=None, key=None,)
      

    st.title("MISSION, VISION AND VALUES")
   
    st.header("MISSION")
    st.write("To provide affordable, dignified burial services, supporting families in need.")
     
    st.header("VISION")
    st.write("To be a trusted, compassionate support system, ensuring dignified burials and peace of mind for families, while fostering community solidarity and respect for the deceased.")
    
    st.header("VALUES")
   
    st.subheader("Compassion")
    st.write(" -Providing emotional support to grieving families") 
    st.write(" -Easing financial burdens of funeral costs")
    st.write(" -Ensuring dignified, respectful treatment of loved ones")
    st.write(" -Offering guidance through complex arrangements")           
    

      
    st.subheader("Respect")
    st.write(" -Dignified treatment of the deceased and their families")
    st.write(" -Sensitivity to cultural and personal wishes")
    st.write(" -Professional, caring service from members/staff")
    st.write(" -Honoring the memory of loved ones with dignity")
    
    
    st.subheader("Transparency")
    st.write(" -Clear, upfront costs and no hidden fees")
    st.write(" -Open communication about services and options")
    st.write(" -Fair, understandable policies and membership term")
    st.write(" -Accountability in handling funds and services")
    
    st.subheader("Community")
    st.write(" -Building solidarity among members in times of loss")
    st.write(" -Fostering support networks for grieving families")
    st.write(" -Promoting shared responsibility and care")
    st.write(" -Strengthening community bonds through shared values")

# services
if selected =="Services":
     
     st.write("---")
     
    
     st.title(f"PACKEGS")
     st.header("We offer two types of packages;"
                  "(Platinum and Diamond")
     st.write(
        """ 
             
             (1) PLATINUM;  $6.00 it covers members' spouse and children who are below the age of 21 if they're still in university or college. 

                (2) DIAMOND; $12.00 it covers members' spouse and children who are below the age of 21 if they're still in university or college 
                    
                Additional dependents will pay $2.00 per dependent.
      
              NB; all packages will mature in 3 months and there is no waiting period for all accidental death." 
 
              MEMORIAL SERVICES: We offer J.5 church memorial services led by J.5 church pastors after 3 months from the death of the deceased.
              """
    )
     
       
     
    
     st.header("OUR SERVICES")
     st.write("##")
     st.subheader(" Funeral Planning And Coordination")
     
     st.write("-Helping families choose funeral options (e.g., burial, cremation)")
     st.write("-Coordinating with funeral homes, cemeteries, or crematoria") 
     st.write("-Arranging transport for the deceased and attendees") 
     st.write("-Assisting with funeral programs, notices, or speeches")
     st.write("-Ensuring religious customs are respected")

     st.subheader("-Burial Plot Arrangement")

     st.write("_Helping families select and purchase burial plots")
     st.write("_Coordinating with cemeteries or memorial parks")
     st.write("_Handling paperwork and plot registration")
     st.write("_Ensuring plot availability and respecting family wishes")

     st.subheader("-Funeral Transport Services")

     st.write("-Arranging hearse or vehicle transport for the deceased")
     st.write("-diamond packeg we will provid transporting family members or mourners to the funeral")
     st.write("-platnum packeg will exclude transporting family members or mourners to the funeral unless you pay {$.....}")
     st.write("-Ensuring respectful, dignified transport")
     
     st.subheader("EMBALMING")
     st.write("-Preparing the body through disinfection and preservation")
     st.write("-Restoring a natural appearance")
     st.write("-Delaying decomposition for a short period")
     
     st.subheader("-Catering for mourners")

     st.write("-Providing food and refreshments for attendees")
     st.write("-Arranging for catering staff or volunteers to serve")
     st.write("-Ensuring enough food for the number of guests")

     st.subheader("-Memorial services or ceremonies")

     st.write("-Planning a service to honor the deceased")
     st.write("-Choosing a venue (e.g., church, cemetery, community hall)")
     st.write("-Arranging for speakers, music, or readings")
     st.write("-Creating a memorial book or program")
     st.write("-- Ensuring the service respects the deceased's wishes or cultural traditions")
    
# ____contact
if selected =="Contact":
    st.write("---")
    st.header("sign in/ login")
    st.write("##")
    st.write()

    # Documantation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS
    contact_form = (
        """
         <form action="https://formsubmit.co/manyimoslimkingz@email.com" method="POST">
              <input type="hidden" name="_captcha" value="false" >
              <input type="text" name="name" placeholder="Your name" required>
              <input type="text" name="age" placeholder="Your age" required>
              <input type="text" name="ID number" placeholder="Your ID number" required>
              <input type="text" name="contact details" placeholder="Your contact details" required>
              <input type="text" name="address/province" placeholder="Your address/province" required>
              <input type="text" name="assembly" placeholder="Your assembly" required>
              <input type="email" name="email" placeholder="Your email" required>
              <input type="text" name="password" placeholder="Your password" required>
              <button type="submit">Send</button>
         </form>
""")
    

    
      

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

if selected =="Paymant":
     st.header("Payment")
     st.write("---")
     
    
     st.title(f"ECOCASH")
     st.write("*151*2*2*062095*Amount #")
     
    