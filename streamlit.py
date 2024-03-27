import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import plotly.express as px
import json
from datetime import datetime, timedelta

# parent dir import
# import sys
# from pathlib import Path
# parent_folder = Path(__file__).parent.parent.absolute()
# sys.path.append(str(parent_folder))

# from keys import *

today = datetime.now().strftime('%Y-%m-%d')
tomorrow = datetime.now() + timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')

st.set_page_config( layout='wide')

chosen_dest = 'AMS'




def get_db_engine():
    endpoint = f'postgresql://{st.secrets.PAGILA_USER}:{st.secrets.PAGILA_PWD}@{st.secrets.PAGILA_HOST}:5432/pagila'
    return create_engine(endpoint)

def get_something():
    pass

def return_query(query):
    engine = get_db_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

st.text("AMS - Amsterdam | CDG - Paris | FRA - Frankfurt | MAD - Madrid | BCN - Barcelona")
st.text("FCO - Rome | MUC - Munich | LIS - Lisbon | DUB - Dublin")

chosen_dest = st.selectbox(
   "Choose Destination",
   ('AMS','CDG','FRA','MAD','BCN','FCO','MUC','LIS','DUB'),
   index=0,
   placeholder="Select destination...",
)


st.header("Some data:")


def get_colA():
    conn = get_db_engine()


# Cols Top:
colA, colB, colC, colD, colE, colF = st.columns([1,1,1,1,1,1])

with colA:
    st.text("Today API calls:")
    st.text(return_query(f"SELECT count(search_id) FROM fu_flight_project_head ffpr WHERE created_at >= '{today}'::date;").iloc[0].values[0])

with colB:
    st.text("Lifetime calls API:")
    st.text(return_query("SELECT count(search_id) FROM fu_flight_project_head;").iloc[0].values[0])

with colC:
    st.text("First API execution:")
    first_db_upd = str(return_query("SELECT created_at::date FROM student.fu_flight_project_head ffph WHERE created_at = (SELECT MIN(created_at) FROM student.fu_flight_project_head);").iloc[0].values[0])
    first_db_upd += " " + str(return_query("SELECT TO_CHAR(created_at::time, 'HH24:MI:SS')  FROM student.fu_flight_project_head ffph WHERE created_at = (SELECT MIN(created_at) FROM student.fu_flight_project_head);").iloc[0].values[0])
    st.text(first_db_upd)

with colD:
    st.text("Latest DB update:")
    latest_db_upd = str(return_query("SELECT created_at::date FROM student.fu_flight_project_head ffph WHERE created_at = (SELECT MAX(created_at) FROM student.fu_flight_project_head);").iloc[0].values[0])
    latest_db_upd += " " + str(return_query("SELECT TO_CHAR(created_at::time, 'HH24:MI:SS')  FROM student.fu_flight_project_head ffph WHERE created_at = (SELECT MAX(created_at) FROM student.fu_flight_project_head);").iloc[0].values[0])
    st.text(latest_db_upd)

with colE:
    st.text("Most expensive ticket:")
    q_e = f"SELECT MAX(price) FROM student.fu_flight_project WHERE fly_to = '{chosen_dest}';"
    st.text("£" + f"{return_query(q_e).iloc[0].values[0]:.2f}")

with colF:
    st.text("Least expensive ticket:")
    q_f = f"SELECT MIN(price) FROM student.fu_flight_project WHERE fly_to = '{chosen_dest}';"
    st.text("£" + f"{return_query(q_f).iloc[0].values[0]:.2f}")


col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Hourly price for  ")
    # st.line_chart(data)
    
    df_hourly = return_query(f"""
        SELECT local_departure,AVG(price), MIN(price), MAX(price)
        FROM student.fu_flight_project ffp
        JOIN student.fu_flight_project_head ffph
        ON ffp.search_id = ffph.search_id
        WHERE fly_to = '{chosen_dest}'
        GROUP BY local_departure;""")
    # Plotting
    fig = px.line(df_hourly, x='local_departure', y='avg', title='Prices Over Time', markers=True)
    fig.data[0].name = 'Avg'
    fig.add_scatter(x=df_hourly['local_departure'], y=df_hourly['min'], mode='lines+markers', name='Min')
    fig.add_scatter(x=df_hourly['local_departure'], y=df_hourly['max'], mode='lines+markers', name='Max')
    fig.update_layout(showlegend=True)
    # Display the plot
    st.plotly_chart(fig)

with col2:
    st.subheader("Cheapest flight - tomorrow onwards")
    details_cheapest = return_query(f"""
    SELECT local_departure, fly_from, airlines, city_from, fly_to, city_to, duration_departure/60 AS duration_departure_m, duration_return/60 AS duration_return_m,  price, route, availability_seats, created_at 
    FROM student.fu_flight_project ffp
    JOIN student.fu_flight_project_head ffph
    ON ffp.search_id = ffph.search_id
    WHERE fly_to = '{chosen_dest}' 
        AND price = (SELECT MIN(price) FROM student.fu_flight_project WHERE fly_to = '{chosen_dest}')
        AND local_departure >= '{tomorrow}'::date
    LIMIT 1;""")

    # route details:
    st.text("Route Details")
    df_detail_route = pd.DataFrame(json.loads(details_cheapest.loc[0]['route']))

    st.text("Quoted on: " + str(details_cheapest.loc[0]['created_at']))
    st.text("Departing from : " + str(details_cheapest.loc[0]['city_from']) +"/"+ str(details_cheapest.loc[0]['fly_from']))
    st.text("Local Departure : " + str(details_cheapest.loc[0]['local_departure']))
    st.text("Duration(m) : " + str(details_cheapest.loc[0]['duration_departure_m']))
    st.text("Returning from : " + str(details_cheapest.loc[0]['city_to']) + "/" +str(details_cheapest.loc[0]['fly_to']))
    st.text("Returning on : " + df_detail_route[df_detail_route['flyFrom'] == chosen_dest]['local_departure'].values[0].split('T')[0] + " " +df_detail_route[df_detail_route['flyFrom'] == chosen_dest]['local_departure'].values[0].split('T')[1].split('.')[0])
    st.text("Duration(m) : " + str(details_cheapest.loc[0]['duration_return_m']))
    st.text("Seats Available : " + str(details_cheapest.loc[0]['availability_seats']))
    st.text("Price : " + f"£{details_cheapest.loc[0]['price']:.2f}")
    st.text("Airline(s) : " + str(details_cheapest.loc[0]['airlines']))



    if df_detail_route.shape[0] == 2:
        st.text("Outgoing and Incoming direct flights.")
    else:
        if df_detail_route[df_detail_route['flyTo'] == chosen_dest].index[0] == 0:
            st.text("Outgoing flight is direct.")
        else: 
            st.text(f"Outgoing flight has {df_detail_route[df_detail_route['flyTo'] == chosen_dest].index[0]} stop(s)")
        if df_detail_route[df_detail_route['cityTo'] == 'London'].index[0] - df_detail_route[df_detail_route['flyFrom'] == chosen_dest].index[0] == 1:
            st.text("Returning flight is direct.")
        else:
            st.text(f"Returning flight has {df_detail_route[df_detail_route['cityTo'] == 'London'].index[0] - df_detail_route[df_detail_route['flyFrom'] == chosen_dest].index[0]} stop(s)")





