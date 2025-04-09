import seaborn as sns
import matplotlib.pyplot as plt

def plot_region_sales(df):
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()
    sns.barplot(data=region_sales, x='Region', y='Sales')
    plt.title('Total Sales by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_monthly_sales_trend(df):
    df_monthly = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
    df_monthly['Date'] = pd.to_datetime(df_monthly[['Year', 'Month']].assign(DAY=1))
    
    sns.lineplot(data=df_monthly, x='Date', y='Sales')
    plt.title('Monthly Sales Trend')
    plt.tight_layout()
    plt.show()
