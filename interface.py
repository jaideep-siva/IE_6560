import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import time

def load_data(file_path):
    """
    Load the location data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing location data.
    """
    return pd.read_csv(file_path)

def advanced_dynamic_programming_trip_planning(budget, time, locations):
    """
    Perform dynamic programming to select locations that maximize satisfaction
    while minimizing budget usage and fitting within the time constraint.

    Parameters:
    budget (int): Total budget available.
    time (int): Total time available.
    locations (pd.DataFrame): DataFrame containing location data.

    Returns:
    tuple: dp table, decision table, selected locations, explanations, optimal budget, optimal satisfaction
    """
    n = len(locations)
    dp = np.zeros((n + 1, budget + 1, time + 1))
    decision = np.zeros((n + 1, budget + 1, time + 1), dtype=int)

    for i in range(1, n + 1):
        for b in range(budget + 1):
            for t in range(time + 1):
                if locations['cost'][i - 1] <= b and locations['travel_time'][i - 1] <= t:
                    without_location = dp[i - 1][b][t]
                    with_location = dp[i - 1][b - locations['cost'][i - 1]][t - locations['travel_time'][i - 1]] + locations['satisfaction'][i - 1]
                    if with_location > without_location:
                        dp[i][b][t] = with_location
                        decision[i][b][t] = 1
                    else:
                        dp[i][b][t] = without_location
                        decision[i][b][t] = 0
                else:
                    dp[i][b][t] = dp[i - 1][b][t]
                    decision[i][b][t] = 0

    selected = []
    explanations = []
    b = budget
    t = time
    for i in range(n, 0, -1):
        if decision[i][b][t] == 1:
            selected.append(locations['location'][i - 1])
            explanations.append(f"Selected {locations['location'][i - 1]} with a cost of ${locations['cost'][i - 1]} and a satisfaction score of {locations['satisfaction'][i - 1]}.")
            b -= locations['cost'][i - 1]
            t -= locations['travel_time'][i - 1]

    selected.reverse()
    explanations.reverse()

    optimal_budget = budget - b
    optimal_satisfaction = dp[len(locations)][budget][time]

    return dp, decision, selected, explanations, optimal_budget, optimal_satisfaction

def display_city_info(locations):
    """
    Display a dropdown menu for city selection and show city details.

    Parameters:
    locations (pd.DataFrame): DataFrame containing location data.
    """
    city_info = st.selectbox("Select a city to view details:", locations['location'])
    city_details = locations[locations['location'] == city_info].iloc[0]
    st.markdown(f"**{city_details['location']}**:{city_details['description']}")

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="IE 6560 : Final project", layout="wide")

    st.title("Jaideep Siva Senthil: Dynamic programming based trip planner.")

    st.markdown("""
    ## This is an interactive user interface for my class IE 6560,
    ## which follows a dynamic programming model to optimize satisfaction while minimizing costs
    ## for a vacation in Michigan with artificial data.

    ### How to Use
    1. **View City Details:**
        - Use the dropdown menu to select and view details of the cities being considered.
        - Each city will display its cost, satisfaction score, and travel time.

    2. **Set Preferences:**
        - Use the slider to set your maximum available time in hours for the trip.

    3. **Plan Trip:**
        - Click the "Plan Trip" button to compute the optimal trip plan based on your inputs.
        - The algorithm will minimize the budget while maximizing satisfaction within your time constraints.

    4. **View Results:**
        - The results will display the selected locations, the optimal satisfaction score, the minimum budget, and explanations for the decisions.
        - You can also view a satisfaction matrix and decision matrix for different budget and time constraints.
        - The selected locations will be shown on an interactive map.
    """)

    locations = load_data('michigan_locations.csv')

    st.markdown("### City Consideration")
    display_city_info(locations)

    budget = st.slider("Select your budget in $:", 100, 5000, 1000, step=100)
    time_available = st.slider("Select your available time (in hours):", 1, 48, 24)

    start_button = st.button("Plan Trip")

    if start_button:
        start_time = time.time()
        
        dp, decision, selected, explanations, optimal_budget, optimal_satisfaction = advanced_dynamic_programming_trip_planning(budget, time_available, locations)
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        st.markdown(f"**Processing Time:** {processing_time:.2f} seconds")
        st.markdown("### Optimal Trip Plan")
        st.write(f"**Budget Used:** ${optimal_budget}")
        st.write(f"**Optimal Satisfaction:** {optimal_satisfaction}")
        st.write("**Selected Locations:**", ", ".join(selected))

        # Display DP table in budget ranges
        budget_ranges = range(0, budget + 1, max(1, budget // 10))
        dp_df = pd.DataFrame(dp[len(locations)][budget_ranges, :], columns=[f'{i} hrs' for i in range(time_available + 1)], index=[f'${i}' for i in budget_ranges])
        st.markdown("### Dynamic Programming Table (Last Stage):")
        st.dataframe(dp_df)


        # Visualize selected locations on a map
        st.markdown("### Selected Locations on Map")
        m = folium.Map(location=[44.3148, -85.6024], zoom_start=6)  # Centered on Michigan

        for loc in selected:
            location_data = locations[locations['location'] == loc]
            folium.Marker(
                location=[location_data['latitude'].values[0], location_data['longitude'].values[0]],
                popup=f"{loc}: {location_data['description'].values[0]}",
                tooltip=loc
            ).add_to(m)

        folium_static(m)

        # Explanation of decisions
        st.markdown("### Explanation of Decisions")
        for explanation in explanations:
            st.write(explanation)

if __name__ == "__main__":
    main()
