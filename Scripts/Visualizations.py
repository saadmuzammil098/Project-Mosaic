import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns

#Load dataset_1
df_healthcare = pd.read_csv("healthcare_dataset.csv")

#Box Plot: Billing Amount by Insurance Provider
plt.figure(figsize=(10, 5))
sns.boxplot(x="Insurance Provider", y="Billing Amount", data=df_healthcare, palette="magma")
plt.xticks(rotation=45)
plt.title("Billing Amount Distribution by Insurance Provider")
plt.show()


#Load dataset_2
df = pd.read_csv("healthcare_stock_data.csv")

#Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

#Create Candlestick Chart
fig = go.Figure(data=[
    go.Candlestick(
        x=df["Date"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Stock Price"
    )
])

fig.update_layout(
    title="Stock Price Movement (Candlestick Chart)",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
)

fig.show()


#Load dataset_3
df = pd.read_csv("reddit_healthcare_posts.csv")

#Create Bar Chart
fig = px.bar(
    df,
    x="Title",
    y="Score",
    text="Score",
    hover_data=["URL"],
    labels={"Title": "Reddit Posts", "Score": "Upvotes"},
    title="Reddit Healthcare-Related Posts and Their Scores",
    template="plotly_dark"
)


fig.update_traces(marker_color='blue', textposition='outside')
fig.update_layout(xaxis_tickangle=-45)


fig.show()
