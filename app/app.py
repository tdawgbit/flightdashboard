import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="Flight Dashboard", page_icon="✈️", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Recommendations", "About"])

# Home Page
if page == "Home":
    st.title("Welcome to the Flight Operations Dashboard! ✈️")

    st.markdown("""
    ## About this Project
    This dashboard provides an interactive look at flight data from major U.S. airports.  
    It focuses on analyzing airport traffic, flight delays, cancellations, and operational efficiency.

    Explore the dashboard to view:
    - 📈 Airport traffic trends
    - 🛬 Arrival and departure delay patterns
    - ❌ Cancellation rates
    - 📅 Flight volume over time

    **Goal:**  
    To better understand flight operations and airline performance at the busiest U.S. airports.

    ---
    """)

    st.success("Use the sidebar to navigate to the Dashboard or About sections!")


# Dashboard Page
elif page == "Dashboard":
    st.title("Flight Data Dashboard 📊")

    # First Row
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Average Arrival Delay by Airport")
        image1 = Image.open('charts/average_arrival_delay.png')
        st.image(image1, use_container_width=True)
        st.markdown("**Insight:** Seattle (SEA) shows relatively low average arrival delays compared to busier hubs like ATL and ORD.")

    with col2:
        st.subheader("Share of Flights by Airport")
        image2 = Image.open('charts/share_of_flights.png')
        st.image(image2, use_container_width=True)
        st.markdown("**Insight:** ATL handles the largest share of total flights among the analyzed airports, reinforcing its role as a major U.S. hub.")

    st.markdown("---")  # Divider between rows

    # Second Row
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Number of Flights by Airport")
        image3 = Image.open('charts/number_of_flights.png')
        st.image(image3, use_container_width=True)
        st.markdown("**Insight:** Airports like ATL and DFW dominate in total flight volume, while SEA holds a steady mid-range position.")

    with col4:
        st.subheader("Departure Delay vs Arrival Delay")
        image4 = Image.open('charts/dep_vs_arr_delay.png')
        st.image(image4, use_container_width=True)
        st.markdown("**Insight:** There is a strong positive relationship between departure and arrival delays — late departures often lead to late arrivals.")

    st.markdown("---")  # Divider between rows

    # Third Row
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Flights Over Time (Monthly)")
        image5 = Image.open('charts/flights_over_time.png')
        st.image(image5, use_container_width=True)
        st.markdown("**Insight:** Flight volumes show seasonal patterns, with dips likely related to external events (e.g., holidays, disruptions).")

    with col6:
        st.subheader("Cancellation Rate by Airport (%)")
        image6 = Image.open('charts/cancellation_rate_by_airport.png')
        st.image(image6, use_container_width=True)
        st.markdown("**Insight:** Some airports experience higher cancellation rates, possibly due to regional weather patterns or congestion.")


# Recommendations Page
elif page == "Recommendations":
    st.title("What to Do With the Data We Found 💡")

    st.markdown("""
    ## Key Takeaways:
    - Airports like ATL and DFW handle a massive volume of flights and experience notable delays. **Improving ground operations** or **scheduling buffers** at these airports could reduce ripple effects across the country.
    - Seattle (SEA) shows strong on-time performance relative to bigger hubs. **Maintaining SEA's operational efficiency** should remain a priority even as passenger numbers grow.
    - A strong correlation exists between **departure and arrival delays**. Investing in **on-time departures** could automatically improve overall airline reliability.
    - Cancellation rates at certain airports suggest vulnerability to **weather** or **congestion issues**. **Contingency planning** (e.g., flexible staffing, rerouting strategies) could mitigate these risks.

    ## Strategic Actions:
    - Airlines should **analyze high-cancellation airports** to adjust flight schedules during vulnerable periods (winter storms, peak holidays).
    - Airports should **invest in faster ground turnaround** for flights at congested hubs.
    - Data monitoring tools could alert operations teams when delay trends emerge — allowing **real-time mitigation**.

    ---
    > **Summary:**  
    Turning data insights into operational improvements can boost on-time performance, passenger satisfaction, and overall system reliability.
    """)


# About Page
elif page == "About":
    st.title("About This Project 🛠️")
    st.write("""
        **Tools Used:** Python, Pandas, Matplotlib, Jupyter Notebook, Streamlit  
        **Role:** Data Collection, Cleaning, Analysis, and Visualization  
        **Data Source:** Sample Flight Data

        This dashboard was built to visualize airport and airline performance in a simple, interactive way.
    """)
    st.write("For more information, please contact the project team at: tdiep@zagmail.gonzaga.edu")
