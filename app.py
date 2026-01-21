from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

CSV_FILE = "survey.csv"

def get_data():
    # Read the local CSV file
    df = pd.read_csv(CSV_FILE)
    return df

def generate_chart(df, column, filename="chart.png"):
    # Generate bar chart for a column (Favorite Language)
    counts = df[column].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind='bar', color='skyblue')
    plt.title(f"{column} Distribution")
    plt.ylabel("Count")
    plt.tight_layout()
    
    # Save chart in static folder
    os.makedirs("static", exist_ok=True)
    plt.savefig(os.path.join("static", filename))
    plt.close()

@app.route("/")
def home():
    df = get_data()

    # Convert DataFrame to HTML table showing all entries
    summary = df.to_html(classes='table table-striped table-bordered text-center', index=False)

    # Generate chart for Favorite Language
    chart_file = "chart.png"
    generate_chart(df, "Favorite Language", chart_file)

    return render_template("index.html", summary=summary, chart_file=chart_file)

if __name__ == "__main__":
    app.run(debug=True)
