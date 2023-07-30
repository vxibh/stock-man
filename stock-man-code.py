import yfinance as yf
import streamlit as st
from google_images_search import GoogleImagesSearch

# Function to fetch company logo URL using Google Images Search
def get_company_logo_url(tickerSymbol):
    search_params = {
        'q': tickerSymbol + ' logo',
        'num': 1,
        'fileType': 'png',
    }
    gis = GoogleImagesSearch("AIzaSyC3sxaKXEtuibak-NeWtOdToLYgI3sWXTg", "41abd66df595642b6"
)
    gis.search(search_params=search_params)
    results = gis.results()
    if results:
        return results[0].url
    return None

# Streamlit App
def main():
    st.write("""
    # Stock-Man

    Shown are the stock **closing price** and **volume** of the chosen company!
    """)

    # Input fields
    tickerSymbol = st.text_input("Enter the company's name (e.g., TSLA):")
    start_date = st.date_input("Enter the start date:")
    end_date = st.date_input("Enter the end date:")
    period = st.selectbox("Select the period", ["1d", "1wk", "1mo"])

    # Show graphs button
    if st.button("Show Graphs"):
        if not tickerSymbol:
            st.warning("Please enter a valid company name.")
            return

        # Getting data
        tickerData = yf.Ticker(tickerSymbol)
        if not tickerData:
            st.error("Data not available for the provided company.")
            return

        # Retrieve data
        tickerDf = tickerData.history(period=period, start=start_date, end=end_date)

        # Fetch company logo URL
        company_logo_url = get_company_logo_url(tickerSymbol)

        if company_logo_url:
            # Display company logo and name
            st.image(company_logo_url, caption=tickerSymbol + ' logo', use_column_width=True)

        # Closing price graph
        st.write("""
        ## Closing Price
        """)
        st.line_chart(tickerDf.Close)

        # Volume graph
        st.write("""
        ## Volume Price
        """)
        st.line_chart(tickerDf.Volume)

        # Major Holders information
        st.write("""## Major Holders""")
        st.write(tickerData.major_holders)

#for only code run
if __name__ == '__main__':
    main()
