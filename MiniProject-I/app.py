#----------------------------------------Requirements------------------------------------------------------
import streamlit as st
import pandas as pd, numpy as np
import yfinance as yf 
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import ta


#---------------------------------------Page Configuration---------------------------------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="MiniProject-I/icon.png",
    layout="centered"
    )

st.title("Stock Market Dashboard :material/Dashboard:")

#--------------------------------Data--------------------------------------------------------------
@st.cache_data
def get_data(ticker, period, interval):

	return yf.download(ticker, period=period, interval=interval)

def additional_data(ticker):
	return yf.Ticker(ticker)

#------Stock Tickers----------
stocks = ('AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'LLY','V', 'TSM', 'UNH', 'AVGO', 'NVO', 'JPM', 'WMT', 'XOM', 'MA', 'JNJ','PG', 'ORCL', 'HD', 'ADBE', 'ASML', 'CVX', 'COST', 'TM', 'MRK','KO', 'ABBV', 'BAC', 'PEP', 'FMX', 'CRM', 'SHEL', 'ACN', 'NFLX',
       'MCD', 'AMD', 'LIN', 'NVS', 'AZN', 'CSCO', 'TMO', 'BABA', 'INTC','PDD', 'SAP', 'ABT', 'TMUS', 'PFE', 'DIS', 'NKE', 'CMCSA', 'DHR','INTU', 'TTE', 'WFC', 'VZ', 'BHP', 'HDB', 'HSBC', 'PM', 'QCOM',       'IBM', 'AMGN', 'TXN', 'NOW', 'BA', 'COP', 'UNP', 'BX', 'SPGI',
       'UPS', 'GE', 'MS', 'HON', 'CAT', 'AMAT', 'BUD', 'AXP', 'RY', 'NEE','UL', 'SNY', 'RTX', 'T', 'LOW', 'SBUX', 'RIO', 'TD', 'SYK', 'BLK','LMT', 'GS', 'ELV', 'ISRG', 'BKNG', 'SONY', 'MDT', 'PLD', 'SCHW','DE', 'MUFG', 'BP', 'TJX', 'BMY', 'PBR', 'MMC', 'MDLZ', 'AMT',
       'PGR', 'LRCX', 'SHOP', 'ADP', 'EQNR', 'GILD', 'CB', 'ADI', 'PANW','VRTX', 'ETN', 'UBS', 'CVS', 'C', 'REGN', 'KKR', 'MU', 'SNPS','CI', 'MELI', 'BSX', 'ZTS', 'IBN', 'DEO', 'FI', 'CME', 'SO','EQIX', 'CDNS', 'KLAC', 'SLB', 'MO', 'CNI', 'ENB', 'NTES', 'INFY','ITW',
       'RELX', 'GSK', 'EOG', 'CNQ', 'BTI', 'SHW', 'NOC', 'DUK','WDAY', 'BDX', 'ANET', 'WM', 'GD', 'HCA', 'RACE', 'STLA', 'MCO','CP', 'SAN', 'SMFG', 'AON', 'FDX', 'VALE', 'CL', 'TRI', 'PYPL','ICE', 'CSX', 'ITUB', 'HUM', 'MCK', 'TGT', 'CMG', 'MAR', 'APD',
       'CHTR', 'USB', 'BN', 'BMO', 'EPD', 'CTAS', 'BBVA', 'SCCO', 'PH','LULU', 'MMM', 'DELL', 'APH', 'PXD', 'PSX', 'ECL', 'E', 'MSI','AJG', 'NXPI', 'FCX', 'OXY', 'TDG', 'BNS', 'PNC', 'APO', 'TEAM',       'TT', 'RSG', 'EMR', 'HMC', 'CCI', 'WELL', 'MRVL',
       'NGG', 'ING','CPRT', 'NSC', 'AFL', 'PCAR', 'MET', 'BSBR', 'NEM', 'SPG', 'SRE','ADSK', 'ET', 'AZO', 'AIG', 'PSA', 'MCHP', 'EL', 'HES', 'KDP','WMB', 'CRH', 'ROST', 'TAK', 'PAYX', 'DXCM', 'PCG', 'STZ', 'GM','TFC', 'MFG', 'KHC', 'ABEV', 'LNG', 'JD', 'HLT', 'STM', 'SU',
       'DHI', 'ODFL', 'VLO', 'COF', 'AEP', 'F', 'DLR', 'MSCI', 'BIDU','KMB', 'EW', 'FTNT', 'TEL', 'TRV', 'SGEN', 'COR', 'NUE', 'SQ', 'D','O', 'ADM', 'OKE', 'IQV', 'IDXX', 'WDS', 'CNC', 'KMI', 'TRP','EXC', 'GWW', 'HSY', 'A', 'EA', 'BK', 'GIS', 'MPLX', 'SYY', 'CM',
       'AMP', 'LEN', 'LHX', 'BCE', 'JCI', 'ALL', 'BBD', 'SPOT', 'CTSH','AME', 'YUM', 'MFC', 'PRU', 'LVS', 'LYG', 'FIS', 'VRSK', 'TTD','CSGP', 'FERG', 'WCN', 'FAST', 'IT', 'ARES', 'BIIB', 'BKR', 'XEL','HAL', 'CVE', 'PPG', 'ORAN', 'NDAQ', 'URI', 'IMO', 'IBKR', 'PEG','CMI',
       'KR', 'ED', 'ON', 'QSR', 'ACGL', 'ROK', 'DD', 'LYB', 'VICI','GPN', 'GOLD', 'PUK', 'ZS', 'MDB', 'CHT', 'SLF', 'CQP', 'HPQ','DVN', 'MLM', 'CDW', 'PKX', 'ELP', 'DG', 'EXR', 'VMC', 'IR','VEEV', 'FANG', 'NTR', 'CCEP', 'FICO', 'BCS', 'RCL', 'RYAAY',
       'PWR', 'EFX', 'MPWR', 'TTWO', 'SBAC', 'WEC', 'AEM', 'EC', 'DLTR','ARGX', 'CAH', 'WBD', 'WST', 'ANSS', 'TU', 'AWK', 'EIX', 'SPLK','XYL', 'WIT', 'WTW', 'DB', 'HUBS', 'AVB', 'KEYS', 'VOD', 'CBRE','TEF', 'GLW', 'TLK', 'ZBH', 'FTV', 'MTD', 'RMD', 'DAL', 'APTV',
       'CHD', 'NWG', 'HIG', 'GRMN', 'GIB', 'WY', 'DFS', 'TCOM', 'TROW','BR', 'RCI', 'WPM', 'FNV', 'STT', 'ICLR', 'TSCO', 'VRSN', 'RJF','EQR', 'DTE', 'HPE', 'ETR', 'FE', 'SE', 'HWM', 'MTB', 'SNAP','EBAY', 'ES', 'IX', 'FCNCA', 'MOH', 'BRO', 'MT', 'ULTA', 'WAB','HEI',
       'AEE', 'GMAB', 'INVH', 'ALNY', 'BGNE', 'UMC', 'DOV', 'TS','NOK', 'TRGP', 'CTRA', 'FTS', 'STE', 'NVR', 'CCL', 'ROL', 'PPL','FITB', 'IFF', 'CCJ', 'LYV', 'MRNA', 'PDX', 'DOW', 'TW', 'ALC','PINS', 'ZM', 'UBER', 'CTVA', 'CRWD', 'NET', 'DDOG', 'BNTX','CARR', 'OTIS',
       'LI', 'BEKE', 'SNOW', 'PLTR', 'DASH', 'ABNB','SYM', 'RBLX', 'CPNG', 'COIN', 'GFS', 'NU', 'CEG', 'HLN', 'MBLY','GEHC', 'KVUE', 'ARM')

#-----------------Data Cleaning--------------------------------------------------------------------------

def clean_data(data):
	#resetting index
	data.reset_index(inplace=True)
	#Renameing Datetime column to Date
	data.rename(columns={"Datetime":"Date"}, inplace=True)
	#Removing multiindexing'
	data = data.droplevel("Ticker", axis=1)
	return data

#-----------------Adding Technical Indicators--------------------------------------------------------------------------
def change(data, add_data):
	change = ( add_data.fast_info['lastPrice'] - data['Close'].iloc[-2])
	pct_change = (change/data['Close'].iloc[-2]) *100
	return change,pct_change

def technical_indicators(data):
	data["SMA"] = ta.trend.sma_indicator(data["Close"], window=20)
	data["EMA"] = ta.trend.ema_indicator(data["Close"], window=20)
	data["SMA_Volume"] = ta.trend.sma_indicator(data["Volume"], window=20)

	return data

#-------------------------------------Visualization Functions----------------------------------------------------------


def line_plot():
	
	fig = px.line(data_frame=user_data, x="Date",y=["High","Low","Open","Close"])
	fig.update_layout(title=f"{ticker} Stock Price",
						xaxis_title="Date",
						yaxis_title="Price (USD)",
						template="plotly_dark",
						showlegend=True)
	
	st.plotly_chart(fig, use_container_width=True)

	

def candlestick_plot():
	fig = go.Figure(data=[go.Candlestick(x=user_data["Date"],
					     open=user_data["Open"],
					     high=user_data["High"],
					     low=user_data["Low"],
					     close=user_data["Close"])])
	fig.add_trace(
		go.Scatter(x=user_data["Date"],
				    y= user_data["SMA"],
				    line=dict(color="#ff33b8"),
				    name="SMA Indicator"))
	fig.add_trace(
		go.Scatter(x=user_data["Date"],
					y= user_data["EMA"],
					line=dict(color="#33fff9 "),
					name="EMA Indicator"))

# Add the Upper Bollinger Band and Lower Bollinger Band
	
	fig.update_layout(title=f"{ticker} Stock Price",
						 xaxis_rangeslider_visible=False,
						 xaxis_title="Date",
						 yaxis_title="Price (USD)",
						 template="plotly_dark")

	st.plotly_chart(fig, use_container_width=True)

#---------------------------------Volume analysis----------------------------------------------------

def volume_analysis_plot():
	fig = px.line(user_data, x="Date", y=["Volume"])
	fig.update_layout(title=f"{ticker} Volume",
						xaxis_title="Date",
						yaxis_title="Volume",
						template="plotly_dark",
						showlegend=True)
	fig.add_trace(go.Scatter(x=user_data["Date"],
							y=user_data["SMA_Volume"],
							line=dict(color="#FF0000"),
							name="SMA Indictor"))
	st.plotly_chart(fig, use_container_width=True)



#---------------------------------Comparartive analysis-------------------------------------------------

#Function to calculate relative change in stocks
def relative_return(data):
	rel = data.pct_change()
	cumret = (1+rel).cumprod() - 1
	cumret = cumret.fillna(0)
	return cumret

def comparative_plot():
	tickers = st.multiselect("Select tickers", options=stocks, default=ticker)
	columns = user_data.select_dtypes(["float","int"]).columns
	column = st.selectbox("Select column", options=columns)

	if len(tickers)>0:
		df = relative_return(yf.download(tickers, period=period, interval="1d")[column])
		#st.write(df.index)
		fig = px.line(data_frame=df, x=df.index, y=df.columns)
		fig.update_layout(title=f"Comparative Stock Analysis",
							xaxis_title="Date",
							yaxis_title="Relative Change",
							template="plotly_dark")
		st.plotly_chart(fig, use_container_width=True)

#---------------------------------Streamlit Code----------------------------------------------------------------------------

#--------SideBar-----------

st.sidebar.title("Settings")
st.sidebar.subheader("Filters:")

with st.sidebar:
	ticker = st.selectbox("Choose a stock.", stocks)
	options = ('5d', '1mo', '3mo', '6mo', '1y','5y', 'max')
	period = st.selectbox("Period", options=options, index=options.index('5d')) # Default value = '5d'

#Stock Data

user_data = get_data(ticker, period=period, interval="1d") #Function to fetch real-time stock data
user_data = clean_data(user_data) #clean data
user_data = technical_indicators(user_data) # Adding technical indicators Simple Moving Average and Exponential Moving Average

stock = additional_data(ticker)

#Calculating Change
change,pct_change = change(user_data,stock)

st.sidebar.subheader("Select chart")
options = st.sidebar.radio("Options", options=["Stock Data","Trend Analysis", "Volume Analysis", "Comparative Analysis"])

#-----------------(First)Stock Data Tab-----------------------------------------------------------------------------

if options=="Stock Data":
	expander = st.expander("About Company.")
	expander.write(stock.get_info()['longBusinessSummary']) #Information about company

	st.metric(f'{ticker} Last Price','{:.2f} USD'.format(stock.fast_info["lastPrice"]), delta = "{:.2f}({:.2f}%)".format(change,pct_change))
	col1,col2,col3 = st.columns(3)
	col1.metric("High",'{:.2f}'.format(user_data["High"].max()))
	col2.metric("Low",'{:.2f}'.format(user_data["Low"].min()))
	col3.metric("50 Day Average",'{:.2f}'.format(stock.fast_info['fiftyDayAverage']))
	st.text("")
	st.text("")
	col1, col2, col3 = st.columns(3)
	col1.write(" ")
	col2.write("Stock Data")
	col3.write(" ")
	st.write(user_data)

#-----------------(Second)Trend Analysis Tab-----------------------------------------------------------------------------

elif options=="Trend Analysis":
	if st.checkbox(label="Candlestick"):
		candlestick_plot()
	else:
		line_plot()

#-----------------(Third)Volume Analysis Tab-----------------------------------------------------------------------------

elif options=="Volume Analysis":
	volume_analysis_plot()

#-----------------(Fourth)Comparative Analysis Tab-----------------------------------------------------------------------------

elif options=="Comparative Analysis":
	comparative_plot()
	
