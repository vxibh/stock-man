import yfinance as yf #library for Stock Data
import streamlit as st #StreamLit library
from google_images_search import GoogleImagesSearch #Google Search Engine library

st.write("""
# Stock-Man 
       
Shown are the stock **closing price** and **volume** of the chosen company!

""")

# Defining ticker symbol
tickerSymbol = st.text_input("Enter the company's name (e.g., TSLA):")

if st.button("Show Graphs"):
    # Getting data
    tickerData = yf.Ticker(tickerSymbol)

    # Checking if the input is not empty and the data is available
    if tickerSymbol and tickerData:
        # retrieve data
        tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

        # Searching logo for the company
        company_logo = {
            'q': tickerSymbol + ' logo',  # Search query using the company name and "logo" keyword
            'num': 1,                      # Number of images to fetch
            'fileType': 'png',
        }

        # Perform Google image search for the company's logo
        gis = GoogleImagesSearch("AIzaSyC3sxaKXEtuibak-NeWtOdToLYgI3sWXTg", "41abd66df595642b6")
        gis.search(search_params=company_logo)
        image_result = gis.results()[0].url

        # Displaying the company logo and name using the fetched image
        st.markdown(
            f'<img src="{image_result}" alt="{tickerSymbol} logo" style="width: 150px;">',
            unsafe_allow_html=True
        )
        
        #closing graph
        st.write("""
        ## Closing Price
        """)
        st.line_chart(tickerDf.Close)

        #volume graph
        st.write("""
        ## Volume Price
        """)
        st.line_chart(tickerDf.Volume)

