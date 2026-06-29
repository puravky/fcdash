# ⚽ fcdash — Football Clubs Insights Dashboard

> An interactive data dashboard to explore stats of top football clubs across the world — built with Python, Streamlit, and Plotly.

🔗 **Live App:** [fcdash.streamlit.app](https://fcdash.streamlit.app/)

---

## 📌 Overview

**fcdash** is a web-based analytics dashboard that visualizes key financial and infrastructural statistics of top football clubs worldwide. Users can filter clubs by country and instantly see dynamic charts and KPIs update in real time.

Whether you're a football fan or a data nerd (or both), fcdash gives you a clean, interactive way to compare your favorite clubs side by side.

---

## ✨ Features

- **Country Filter** — Multi-select sidebar to filter clubs by their home country
- **KPI Metrics** — At-a-glance summary cards showing:
  - Average Revenue (Billion USD)
  - Average Club Value (Billion USD)
  - Average Stadium Capacity
- **Revenue Bar Chart** — Compare annual revenue across clubs, color-coded by country
- **Club Value Line Chart** — Track and compare market valuations across clubs
- **Clubs per Country Pie Chart** — See the distribution of top clubs by nation
- **Stadium Capacity Scatter Plot** — Bubble chart where size represents capacity, hoverable for club names

All charts are interactive — hover for details, zoom, pan, and filter on the fly using Plotly.

---

## 🗂️ Project Structure

```
fcdash/
│
├── fc_dashboard.py      # Main Streamlit application
├── clubs_data.csv       # Dataset: top football clubs with financial & stadium data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📊 Dataset

The dataset `clubs_data.csv` contains records for top football clubs with the following columns:

| Column | Description |
|---|---|
| `Club` | Club name (e.g., Manchester United, Real Madrid) |
| `Country` | Country the club is based in |
| `Revenue (in Billion USD)` | Annual revenue in billion USD |
| `Club Value (in Billion USD)` | Estimated market/brand value in billion USD |
| `Stadium Capacity` | Maximum seating capacity of the home stadium |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [Python](https://www.python.org/) | Core programming language |
| [Streamlit](https://streamlit.io/) | Web app framework for rapid data app development |
| [Pandas](https://pandas.pydata.org/) | Data loading and manipulation |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Interactive charting (bar, line, pie, scatter) |

---

## 🚀 Running Locally

**Prerequisites:** Python 3.8+

1. **Clone the repository**
   ```bash
   git clone https://github.com/puravky/fcdash.git
   cd fcdash
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Run the app**
   ```bash
   streamlit run fc_dashboard.py
   ```

4. Open your browser at `http://localhost:8501`

---

## 📁 How It Works

The app is a single-file Streamlit script (`fc_dashboard.py`). Here's the flow:

1. **Data Loading** — `clubs_data.csv` is loaded using pandas with `@st.cache_data` to avoid reloading on every interaction.
2. **Sidebar Filters** — A multiselect widget lets users pick one or more countries; the dataframe is filtered accordingly.
3. **KPI Cards** — Three `st.metric()` cards display computed averages from the filtered data.
4. **Charts** — Four Plotly Express charts render interactively inside the Streamlit layout using `st.plotly_chart()`.

All charts respond dynamically to sidebar filter changes — no page reload needed.

---

## 🌐 Deployment

The app is deployed on **Streamlit Community Cloud**. To deploy your own fork:

1. Push your code to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub account and select the repo
4. Set the main file path to `fc_dashboard.py`
5. Click **Deploy**

Streamlit automatically reads `requirements.txt` and installs dependencies on the cloud.

---

## 🔮 Possible Improvements

- Add more clubs and expand the dataset
- Include additional stats: titles won, squad size, player market value
- Add a search bar to filter by club name
- Add year-over-year comparison if historical data is available
- Connect to a live football data API for real-time updates

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ⚽ and Python by [puravky](https://github.com/puravky)
