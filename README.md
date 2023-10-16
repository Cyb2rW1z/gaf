![Image Alt Text]()
# GAF - Get All URLs and Resources

GAF (Get All URLs and Resources) is a Python tool that enables you to analyze a web page by tracking and listing the resources (e.g., images, scripts, styles) found on the page and the domains from which they are loaded.

## Usage
1. Ensure you have Python installed on your system.

2. Install the required Python libraries by running the following commands:

   ```bash
   pip install requests
   pip install beautifulsoup4

Run the script using the following command:
```
python3 gaf.py -u <URL> -heads "Header1=Value1,Header2=Value2"
```
Replace gaf.py with the name of the Python script.
Replace <URL> with the URL of the web page you want to analyze.
You can include custom headers as a comma-separated list in the format "Header=Value".

## Example
```
python3 gaf.py -u https://example.com -heads "User-Agent=my-user-agent,Accept-Language=en-US"
```
