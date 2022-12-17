default: run

setup:
	pip3 install streamlit

run:
	streamlit run app.py --server.address 0.0.0.0 --server.port 9999

splunk:
	docker run -d -v $(pwd):/data/ -p 80:8000 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=Admin321" --name splunk splunk/splunk:latest

sample:
	curl -Lo btc-usd.csv "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1639116169&period2=1670652169&interval=1d&events=history&includeAdjustedClose=true"


