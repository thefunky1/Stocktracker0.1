# coding: utf-8


# Stock Tracker
# 1. Download all stock symbols - save to database
# 2. Download prices for symbols - save to database


import urllib

ini_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head id="ctl00_ctl00_HeaderOfMasterPage"><title>
<input type="hidden" name="__VIEWSTATE17" id="__VIEWSTATE17" value="L0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMDAxMjk3NTYyJmV4dGVybmFsaWR0eXBlPUlTSU4iPkJyaXRpc2ggQXNzZXRzIFRydXN0IFBMQzwvYT5kZAIBDw8WAh8EBQYxMjEuMDVkZAICDw8WAh8EBQQwLjg4ZGQCAw8PFgIfBAUEMC43M2RkAgQPDxYCHwQFBjEyMC4yMGRkAgUPZBYCAgEPDxYCHwQFBTU5LjY1ZGQCVw9kFgxmDw8WAh8EBc0BPGEgdGl0bGU9IkJyaXRpc2ggRW1waXJlIFNlY3VyaXRpZXMgJiBHZW5lcmFsIFRydXN0IFBMQyIgaHJlZj0iaHR0cDovL3Rvb2xzLm1vcm5pbmdzdGFyLmNvLnVrL3Q5Mnd6MHNqN2MvQFJFUE9SVC9kZWZhdWx0LmFzcHg/ZXh0ZXJuYWxpZD1HQjAwMDEzMzUwODEmZXh0ZXJuYWxpZHR5cGU9SVNJTiI+QnJpdGlzaCBFbXBpcmUgU2VjdXJpdGllcyAmLi4uPC9hPmRkAgEPDxYCHwQFBjQ0OS44MGRkAgIPDxYCHwQFBDMuNzBkZAIDDw8WAh8EBQQwLjgzZGQCBA8PFgIfBAUGNDQ2LjAwZGQCBQ9kFgICAQ8PFgIfBAUGMTE1Ljk4ZGQCWA9kFgxmDw8WAh8EBagBPGEgdGl0bGU9IkJyaXRpc2ggTGFuZCBDbyBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMDAxMzY3MDE5JmV4dGVybmFsaWR0eXBlPUlTSU4iPkJyaXRpc2ggTGFuZCBDbyBQTEM8L2E+ZGQCAQ8PFgIfBAUGNTMxLjI1ZGQCAg8PFgIfBAUEMC4wMGRkAgMPDxYCHwQFBDAuMDBkZAIEDw8WAh8EBQY1MzEuNTBkZAIFD2QWAgIBDw8WAh8EBQY2ODcuMjRkZAJZD2QWDGYPDxYCHwQFwAE8YSB0aXRsZT0iQnJpdGlzaCBQb2x5dGhlbmUgSW5kdXN0cmllcyBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMDA3Nzk3NDI1JmV4dGVybmFsaWR0eXBlPUlTSU4iPkJyaXRpc2ggUG9seXRoZW5lIEluZHVzdHJpZS4uLjwvYT5kZAIBDw8WAh8EBQYzNzcuNTBkZAICDw8WAh8EBQQxLjAwZGQCAw8PFgIfBAUEMC4yNmRkAgQPDxYCHwQFBjM4MC4wMGRkAgUPZBYCAgEPDxYCHwQFBTM0Ljg0ZGQCWg9kFgxmDw8WAh8EBcIBPGEgdGl0bGU9IkJyaXRpc2ggU2t5IEJyb2FkY2FzdGluZyBHcm91cCBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMDAxNDExOTI0JmV4dGVybmFsaWR0eXBlPUlTSU4iPkJyaXRpc2ggU2t5IEJyb2FkY2FzdGluZyBHci4uLjwvYT5kZAIBDw8WAh8EBQY3MTguNzVkZAICDw8WBh8EBQUtMC41MB8FCo0BHwYCBGRkAgMPDxYGHwQFBS0wLjA3HwUKjQEfBgIEZGQCBA8PFgIfBAUGNzE5LjAwZGQCBQ9kFgICAQ8PFgIfBAUIMSwwOTYuMTZkZAJbD2QWDGYPDxYCHwQFmAE8YSB0aXRsZT0iQnJpdHZpYyBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBP" />
<input type="hidden" name="__VIEWSTATE18" id="__VIEWSTATE18" value="UlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMEIwTjhRRDU0JmV4dGVybmFsaWR0eXBlPUlTSU4iPkJyaXR2aWMgUExDPC9hPmRkAgEPDxYCHwQFBjM2MS4xNWRkAgIPDxYCHwQFBDIuNjBkZAIDDw8WAh8EBQQwLjczZGQCBA8PFgIfBAUGMzU4LjUwZGQCBQ9kFgICAQ8PFgIfBAUGMTg4LjE3ZGQCXA9kFgxmDw8WAh8EBagBPGEgdGl0bGU9IkJyb3duIChOKSBHcm91cCBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMEIxUDZaUjExJmV4dGVybmFsaWR0eXBlPUlTSU4iPkJyb3duIChOKSBHcm91cCBQTEM8L2E+ZGQCAQ8PFgIfBAUGMzMwLjI1ZGQCAg8PFgIfBAUENS40MGRkAgMPDxYCHwQFBDEuNjZkZAIEDw8WAh8EBQYzMjUuMDBkZAIFD2QWAgIBDw8WAh8EBQYxMzMuMjNkZAJdD2QWDGYPDxYCHwQFwgE8YSB0aXRsZT0iQnJ1bm5lciBJbnZlc3RtZW50IFRydXN0IChUaGUpIFBMQyIgaHJlZj0iaHR0cDovL3Rvb2xzLm1vcm5pbmdzdGFyLmNvLnVrL3Q5Mnd6MHNqN2MvQFJFUE9SVC9kZWZhdWx0LmFzcHg/ZXh0ZXJuYWxpZD1HQjAwMDE0OTAwMDEmZXh0ZXJuYWxpZHR5cGU9SVNJTiI+QnJ1bm5lciBJbnZlc3RtZW50IFRydXN0IChULi4uPC9hPmRkAgEPDxYCHwQFBjQxOS43NWRkAgIPDxYCHwQFBDAuMDBkZAIDDw8WAh8EBQQwLjAwZGQCBA8PFgIfBAUGNDE4LjUwZGQCBQ9kFgICAQ8PFgIfBAUDLjAwZGQCXg9kFgxmDw8WAh8EBZABPGEgdGl0bGU9IkJURyBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMDAxMDAxNTkyJmV4dGVybmFsaWR0eXBlPUlTSU4iPkJURyBQTEM8L2E+ZGQCAQ8PFgIfBAUGMzQ5LjAwZGQCAg8PFgIfBAUEMi4wMGRkAgMPDxYCHwQFBDAuNThkZAIEDw8WAh8EBQYzNDYuODBkZAIFD2QWAgIBDw8WAh8EBQYxMDIuMjhkZAJfD2QWDGYPDxYCHwQFmgE8YSB0aXRsZT0iQlQgR3JvdXAgUExDIiBocmVmPSJodHRwOi8vdG9vbHMubW9ybmluZ3N0YXIuY28udWsvdDkyd3owc2o3Yy9AUkVQT1JUL2RlZmF1bHQuYXNweD9leHRlcm5hbGlkPUdCMDAzMDkxMzU3NyZleHRlcm5hbGlkdHlwZT1JU0lOIj5CVCBHcm91cCBQTEM8L2E+ZGQCAQ8PFgIfBAUGMjE3LjQwZGQCAg8PFgIfBAUEMC4wNGRkAgMPDxYCHwQFBDAuMDJkZAIEDw8WAh8EBQYyMTcuMzBkZAIFD2QWAgIBDw8WAh8EBQg3LDAwMC4yNmRkAmAPZBYMZg8PFgIfBAWSATxhIHRpdGxlPSJCdW1pIFBMQyIgaHJlZj0iaHR0cDovL3Rvb2xzLm1vcm5pbmdzdGFyLmNvLnVrL3Q5Mnd6MHNqN2MvQFJFUE9SVC9kZWZhdWx0LmFzcHg/ZXh0ZXJuYWxpZD1HQjAwQjVCTFhUNjImZXh0ZXJuYWxpZHR5cGU9SVNJTiI+QnVtaSBQTEM8L2E+ZGQCAQ8PFgIfBAUGMjUxLjUwZGQCAg8PFgYfBAUFLTUuNDAfBQqNAR8GAgRkZAIDDw8WBh8EBQUtMi4xMB8FCo0BHwYC" />
<input type="hidden" name="__VIEWSTATE19" id="__VIEWSTATE19" value="BGRkAgQPDxYCHwQFBjI1Ny42MGRkAgUPZBYCAgEPDxYCHwQFBjExNy42M2RkAmEPZBYMZg8PFgIfBAWUATxhIHRpdGxlPSJCdW56bCBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0IwMEIwNzQ0QjM4JmV4dGVybmFsaWR0eXBlPUlTSU4iPkJ1bnpsIFBMQzwvYT5kZAIBDw8WAh8EBQcxMDI2LjAwZGQCAg8PFgIfBAUENi4wMGRkAgMPDxYCHwQFBDAuNTlkZAIEDw8WAh8EBQcxMDIwLjAwZGQCBQ9kFgICAQ8PFgIfBAUGMTk1LjMwZGQCYg9kFgxmDw8WAh8EBaYBPGEgdGl0bGU9IkJ1cmJlcnJ5IEdyb3VwIFBMQyIgaHJlZj0iaHR0cDovL3Rvb2xzLm1vcm5pbmdzdGFyLmNvLnVrL3Q5Mnd6MHNqN2MvQFJFUE9SVC9kZWZhdWx0LmFzcHg/ZXh0ZXJuYWxpZD1HQjAwMzE3NDMwMDcmZXh0ZXJuYWxpZHR5cGU9SVNJTiI+QnVyYmVycnkgR3JvdXAgUExDPC9hPmRkAgEPDxYCHwQFBzExMzkuMDBkZAICDw8WBh8EBQUtMi4wMB8FCo0BHwYCBGRkAgMPDxYGHwQFBS0wLjE3HwUKjQEfBgIEZGQCBA8PFgIfBAUHMTE0My4wMGRkAgUPZBYCAgEPDxYCHwQFBjQzNC4xMWRkAmMPZBYMZg8PFgIfBAXEATxhIHRpdGxlPSJid2luLnBhcnR5IGRpZ2l0YWwgZW50ZXJ0YWlubWVudCBQTEMiIGhyZWY9Imh0dHA6Ly90b29scy5tb3JuaW5nc3Rhci5jby51ay90OTJ3ejBzajdjL0BSRVBPUlQvZGVmYXVsdC5hc3B4P2V4dGVybmFsaWQ9R0kwMDBBME1WNzU3JmV4dGVybmFsaWR0eXBlPUlTSU4iPmJ3aW4ucGFydHkgZGlnaXRhbCBlbnRlcnRhaS4uLjwvYT5kZAIBDw8WAh8EBQYxMjQuODBkZAICDw8WAh8EBQQ3LjMwZGQCAw8PFgIfBAUENi4yMWRkAgQPDxYCHwQFBjExNy42MGRkAgUPZBYCAgEPDxYCHwQFCDQsNDI3LjIzZGQCZA9kFgxmDw8WAh8EBcMBPGEgdGl0bGU9IkNhYmxlICYgV2lyZWxlc3MgQ29tbXVuaWNhdGlvbnMgUExDIiBocmVmPSJodHRwOi8vdG9vbHMubW9ybmluZ3N0YXIuY28udWsvdDkyd3owc2o3Yy9AUkVQT1JUL2RlZmF1bHQuYXNweD9leHRlcm5hbGlkPUdCMDBCNUtLVDk2OCZleHRlcm5hbGlkdHlwZT1JU0lOIj5DYWJsZSAmIFdpcmVsZXNzIENvbW11bmljYXQuLi48L2E+ZGQCAQ8PFgIfBAUFMzcuNTBkZAICDw8WAh8EBQQwLjI1ZGQCAw8PFgIfBAUEMC42N2RkAgQPDxYCHwQFBTM3LjI1ZGQCBQ9kFgICAQ8PFgIfBAUIMSw0MDAuNzJkZAJlD2QWAmYPDxYCHwQFIURhdGEgYXMgb2YgIDI1IE9jdG9iZXIgMjAxMiAxNDo0MmRkAmYPZBYCZg9kFgQCAQ8PFgIeB0VuYWJsZWRoZGQCAw8PFgIfB2hkZAIHDw9kDxAWA2YCAQICFgMWAh4OUGFyYW1ldGVyVmFsdWVkFgIfCAUORlRTRV9BTExfU0hBUkUWAh8IZBYDAgNmAgNkZAIJD2QWAgIBDw8WAh8EBQ5GVFNFIEFsbCBTaGFyZWRkGAEFSGN0bDAwJGN0bDAwJE1haW5Db250ZW50JEVxdWl0eUNvbnRlbnQkSW5kZXhTdG9ja1ByaWNlc0NDMSRJbmRleFN0b2NrVmlldw88KwAKAQgCBmQ=" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWDwLgstbBAQKiudCACgKI15ypDgKB2fu/CwKB2f+/CwKkzILICgLM66CgBwKi7JjsCwKdmZyDDgK1pZrwCwL1l47jDwLsj8rdDgLNpp1GArG40NMDAvbl5JUC" />
</div> 
            

<style type="text/css">
     #IndexStockPrices1_IndexStockView td.left,
     #IndexStockPrices1_IndexStockView th.left {
     	width:auto;
     }
</style>

<select name="ctl00$ctl00$MainContent$EquityContent$IndexStockPricesCC1$FilterDropDownList" onchange="javascript:setTimeout('__doPostBack(\'ctl00$ctl00$MainContent$EquityContent$IndexStockPricesCC1$FilterDropDownList\',\'\')', 0)" id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_FilterDropDownList">
	<option value="FTSE_100">FTSE 100</option>
	<option value="FTSE_250">FTSE 250</option>
	<option value="FTSE_350">FTSE 350</option>
	<option selected="selected" value="FTSE_ALL_SHARE">FTSE All Share</option>
	<option value="FTSE_AIM_100">FTSE AIM 100</option>
	<option value="FTSE_AIM_ALL_SHARE">FTSE AIM All Share</option>
	<option value="FTSE_AIM_UK_50">FTSE AIM UK 50</option>
	<option value="FTSE_FLEDGLING">FTSE Fledgling</option>
	<option value="FTSE_SMALLCAP">FTSE Smallcap</option>
	<option value="FTSE_TECHMARK_ALL_SHARE">FTSE Techmark All Share</option>
	<option value="FTSE_TECHMARK_100">FTSE Techmark 100</option>

</select>


    <div>
	<table class="grid-view" cellspacing="0" cellpadding="4" border="0" id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView" style="border-collapse:collapse;">
		<caption>
			FTSE All Share Index Share Prices
		</caption><tr class="header">
			<th class="left" scope="col">Company Name</th><th scope="col">Current (p)</th><th scope="col">Change (p)</th><th scope="col">Change (%)</th><th scope="col">Last Close (p)</th><th scope="col">Net Vol (000's)</th>
		</tr><tr class="normal">
			<td class="left"><a title="3i Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B1YW4409&externalidtype=ISIN">3i Group PLC</a></td><td>221.80</td><td>4.20</td><td>1.93</td><td>217.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl02_NetVolLabel">1,051.00</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="3i Infrastructure PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=JE00B1RJLF86&externalidtype=ISIN">3i Infrastructure PLC</a></td><td>125.95</td><td>0.29</td><td>0.23</td><td>125.70</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl03_NetVolLabel">298.37</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="4imprint Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0006640972&externalidtype=ISIN">4imprint Group PLC</a></td><td>348.75</td><td style="color:Red;">-1.25</td><td style="color:Red;">-0.36</td><td>351.25</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl04_NetVolLabel">2.70</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="888 Holdings PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GI000A0F6407&externalidtype=ISIN">888 Holdings PLC</a></td><td>109.12</td><td>0.50</td><td>0.46</td><td>108.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl05_NetVolLabel">136.85</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Aberdeen Asian Income Fund Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0P6J834&externalidtype=ISIN">Aberdeen Asian Income Fund Ltd</a></td><td>207.75</td><td>0.50</td><td>0.24</td><td>207.25</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl06_NetVolLabel">60.56</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Aberdeen Asian Smaller Companies Inv Tr PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000100767&externalidtype=ISIN">Aberdeen Asian Smaller Comp...</a></td><td>860.00</td><td style="color:Red;">-6.35</td><td style="color:Red;">-0.74</td><td>863.75</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl07_NetVolLabel">24.26</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Aberdeen Asset Management PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000031285&externalidtype=ISIN">Aberdeen Asset Management PLC</a></td><td>324.20</td><td>5.90</td><td>1.85</td><td>318.20</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl08_NetVolLabel">1,658.74</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Aberdeen New Dawn Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000056852&externalidtype=ISIN">Aberdeen New Dawn Investmen...</a></td><td>842.50</td><td style="color:Red;">-0.89</td><td style="color:Red;">-0.11</td><td>841.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl09_NetVolLabel">20.84</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Aberforth Smaller Companies Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000066554&externalidtype=ISIN">Aberforth Smaller Companies...</a></td><td>674.75</td><td>9.99</td><td>1.50</td><td>665.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl10_NetVolLabel">39.03</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Absolute Return Trust Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B05PYY10&externalidtype=ISIN">Absolute Return Trust Ltd</a></td><td>122.38</td><td style="color:Red;">-0.13</td><td style="color:Red;">-0.11</td><td>122.38</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl11_NetVolLabel">8.29</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="AcenciA Debt Strategies Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0MSB420&externalidtype=ISIN">AcenciA Debt Strategies Ltd</a></td><td>83.62</td><td style="color:Red;">-0.23</td><td style="color:Red;">-0.28</td><td>83.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl12_NetVolLabel">.95</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Admiral Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B02J6398&externalidtype=ISIN">Admiral Group PLC</a></td><td>1105.00</td><td>0.00</td><td>0.00</td><td>1105.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl13_NetVolLabel">106.17</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Advance Developing Markets Fund Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GG00B45L2K95&externalidtype=ISIN">Advance Developing Markets ...</a></td><td>423.00</td><td style="color:Red;">-1.50</td><td style="color:Red;">-0.35</td><td>424.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl14_NetVolLabel">4.03</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Aegis Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B4JV1B90&externalidtype=ISIN">Aegis Group PLC</a></td><td>236.40</td><td>1.10</td><td>0.47</td><td>235.30</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl15_NetVolLabel">2,067.87</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Afren PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0672758&externalidtype=ISIN">Afren PLC</a></td><td>136.95</td><td>1.30</td><td>0.96</td><td>135.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl16_NetVolLabel">1,297.96</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="African Barrick Gold PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B61D2N63&externalidtype=ISIN">African Barrick Gold PLC</a></td><td>493.25</td><td>6.90</td><td>1.42</td><td>486.40</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl17_NetVolLabel">247.15</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="AGA Rangemaster Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B2QMX606&externalidtype=ISIN">AGA Rangemaster Group PLC</a></td><td>56.12</td><td style="color:Red;">-0.20</td><td style="color:Red;">-0.35</td><td>56.38</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl18_NetVolLabel">246.35</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Aggreko PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B4WQ2Z29&externalidtype=ISIN">Aggreko PLC</a></td><td>2087.00</td><td>41.00</td><td>2.00</td><td>2046.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl19_NetVolLabel">520.52</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Alliance Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B11V7W98&externalidtype=ISIN">Alliance Trust PLC</a></td><td>370.85</td><td>0.50</td><td>0.13</td><td>370.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl20_NetVolLabel">103.10</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Alternative Investment Strategies Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B06GDT12&externalidtype=ISIN">Alternative Investment Stra...</a></td><td>112.88</td><td>1.00</td><td>0.89</td><td>112.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl21_NetVolLabel">10.00</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="AMEC PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000282623&externalidtype=ISIN">AMEC PLC</a></td><td>1037.50</td><td style="color:Red;">-11.00</td><td style="color:Red;">-1.05</td><td>1049.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl22_NetVolLabel">984.54</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Amlin PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B2988H17&externalidtype=ISIN">Amlin PLC</a></td><td>380.00</td><td style="color:Red;">-0.95</td><td style="color:Red;">-0.25</td><td>381.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl23_NetVolLabel">775.18</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Anglo American PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B1XZS820&externalidtype=ISIN">Anglo American PLC</a></td><td>1879.00</td><td>2.50</td><td>0.13</td><td>1877.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl24_NetVolLabel">2,406.30</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Anglo-Eastern Plantations PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000365774&externalidtype=ISIN">Anglo-Eastern Plantations PLC</a></td><td>726.00</td><td>10.00</td><td>1.39</td><td>720.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl25_NetVolLabel">6.61</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Anglo Pacific Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0006449366&externalidtype=ISIN">Anglo Pacific Group PLC</a></td><td>256.25</td><td style="color:Red;">-0.42</td><td style="color:Red;">-0.16</td><td>256.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl26_NetVolLabel">90.38</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Anite PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B3KHXB36&externalidtype=ISIN">Anite PLC</a></td><td>141.30</td><td>6.30</td><td>4.67</td><td>135.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl27_NetVolLabel">778.11</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Antofagasta PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000456144&externalidtype=ISIN">Antofagasta PLC</a></td><td>1282.50</td><td>2.00</td><td>0.16</td><td>1280.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl28_NetVolLabel">735.98</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Aquarius Platinum Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=BMG0440M1284&externalidtype=ISIN">Aquarius Platinum Ltd</a></td><td>37.62</td><td>1.04</td><td>2.85</td><td>36.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl29_NetVolLabel">1,029.81</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="ARM Holdings PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000595859&externalidtype=ISIN">ARM Holdings PLC</a></td><td>663.25</td><td style="color:Red;">-12.50</td><td style="color:Red;">-1.85</td><td>675.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl30_NetVolLabel">3,373.70</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Artemis Alpha Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0004355946&externalidtype=ISIN">Artemis Alpha Trust PLC</a></td><td>293.75</td><td>1.50</td><td>0.52</td><td>289.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl31_NetVolLabel">9.71</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Ashley (Laura) Holdings PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000533728&externalidtype=ISIN">Ashley (Laura) Holdings PLC</a></td><td>27.75</td><td style="color:Red;">-0.40</td><td style="color:Red;">-1.42</td><td>28.25</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl32_NetVolLabel">159.09</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Ashmore Global Opportunities Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GG00B1YWTR89&externalidtype=ISIN">Ashmore Global Opportunitie...</a></td><td>&nbsp;</td><td>0.00</td><td>0.00</td><td>446.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl33_NetVolLabel">.00</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Ashmore Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B132NW22&externalidtype=ISIN">Ashmore Group PLC</a></td><td>368.50</td><td>1.10</td><td>0.30</td><td>367.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl34_NetVolLabel">734.80</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Ashtead Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000536739&externalidtype=ISIN">Ashtead Group PLC</a></td><td>364.00</td><td>13.70</td><td>3.91</td><td>350.20</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl35_NetVolLabel">771.57</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Associated British Foods PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0006731235&externalidtype=ISIN">Associated British Foods PLC</a></td><td>1370.50</td><td>9.00</td><td>0.66</td><td>1362.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl36_NetVolLabel">225.15</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="AstraZeneca PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0009895292&externalidtype=ISIN">AstraZeneca PLC</a></td><td>2910.50</td><td>26.00</td><td>0.90</td><td>2884.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl37_NetVolLabel">1,387.83</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Atkins (W S) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000608009&externalidtype=ISIN">Atkins (W S) PLC</a></td><td>695.25</td><td>8.00</td><td>1.16</td><td>687.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl38_NetVolLabel">28.74</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="AVEVA Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B15CMQ74&externalidtype=ISIN">AVEVA Group PLC</a></td><td>2021.50</td><td>4.00</td><td>0.20</td><td>2017.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl39_NetVolLabel">55.60</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Aviva PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0002162385&externalidtype=ISIN">Aviva PLC</a></td><td>336.70</td><td>6.50</td><td>1.97</td><td>330.30</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl40_NetVolLabel">2,401.45</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Avocet Mining PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000663038&externalidtype=ISIN">Avocet Mining PLC</a></td><td>77.12</td><td style="color:Red;">-1.00</td><td style="color:Red;">-1.28</td><td>78.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl41_NetVolLabel">573.71</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Avon Rubber PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000667013&externalidtype=ISIN">Avon Rubber PLC</a></td><td>310.00</td><td>0.00</td><td>0.00</td><td>310.13</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl42_NetVolLabel">.00</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="AZ Electronic Materials SA" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=LU0552383324&externalidtype=ISIN">AZ Electronic Materials SA</a></td><td>338.35</td><td>22.50</td><td>7.12</td><td>316.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl43_NetVolLabel">370.48</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Babcock International Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0009697037&externalidtype=ISIN">Babcock International Group...</a></td><td>954.75</td><td>15.00</td><td>1.60</td><td>940.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl44_NetVolLabel">157.73</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BAE Systems PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0002634946&externalidtype=ISIN">BAE Systems PLC</a></td><td>311.75</td><td style="color:Red;">-0.60</td><td style="color:Red;">-0.19</td><td>312.20</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl45_NetVolLabel">1,373.18</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Baillie Gifford Japan Trust (The) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000485838&externalidtype=ISIN">Baillie Gifford Japan Trust...</a></td><td>196.50</td><td>2.12</td><td>1.09</td><td>195.38</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl46_NetVolLabel">9.63</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Balfour Beatty PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000961622&externalidtype=ISIN">Balfour Beatty PLC</a></td><td>314.25</td><td>2.12</td><td>0.68</td><td>312.10</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl47_NetVolLabel">542.68</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Bankers Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000767003&externalidtype=ISIN">Bankers Investment Trust PLC</a></td><td>441.25</td><td>0.90</td><td>0.20</td><td>441.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl48_NetVolLabel">34.00</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Bank of Georgia Holdings PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B759CR16&externalidtype=ISIN">Bank of Georgia Holdings PLC</a></td><td>1188.50</td><td>8.00</td><td>0.68</td><td>1178.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl49_NetVolLabel">21.20</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Barclays PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0031348658&externalidtype=ISIN">Barclays PLC</a></td><td>235.67</td><td>5.75</td><td>2.50</td><td>229.90</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl50_NetVolLabel">23,948.49</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Baring Emerging Europe PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0032273343&externalidtype=ISIN">Baring Emerging Europe PLC</a></td><td>692.75</td><td>2.00</td><td>0.29</td><td>690.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl51_NetVolLabel">5.25</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Barr (A G) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B6XZKY75&externalidtype=ISIN">Barr (A G) PLC</a></td><td>443.00</td><td>9.04</td><td>2.06</td><td>438.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl52_NetVolLabel">7.66</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Barratt Developments PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000811801&externalidtype=ISIN">Barratt Developments PLC</a></td><td>190.55</td><td>4.60</td><td>2.47</td><td>186.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl53_NetVolLabel">1,444.62</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BATM Advanced Communications Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=IL0010849045&externalidtype=ISIN">BATM Advanced Communication...</a></td><td>15.88</td><td>0.45</td><td>2.90</td><td>15.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl54_NetVolLabel">50.63</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BBA Aviation PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B1FP8915&externalidtype=ISIN">BBA Aviation PLC</a></td><td>207.80</td><td style="color:Red;">-0.80</td><td style="color:Red;">-0.38</td><td>208.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl55_NetVolLabel">108.52</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Beazley PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=JE00B64G9089&externalidtype=ISIN">Beazley PLC</a></td><td>174.10</td><td>0.80</td><td>0.46</td><td>173.40</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl56_NetVolLabel">103.06</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Bellway PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000904986&externalidtype=ISIN">Bellway PLC</a></td><td>1009.50</td><td>17.00</td><td>1.71</td><td>993.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl57_NetVolLabel">134.65</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Berendsen PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0F99717&externalidtype=ISIN">Berendsen PLC</a></td><td>572.50</td><td>8.00</td><td>1.42</td><td>564.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl58_NetVolLabel">24.95</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Berkeley Group Holdings (The) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B02L3W35&externalidtype=ISIN">Berkeley Group Holdings (Th...</a></td><td>1498.50</td><td>18.00</td><td>1.22</td><td>1480.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl59_NetVolLabel">168.60</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Betfair Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B44JTH01&externalidtype=ISIN">Betfair Group PLC</a></td><td>751.50</td><td>1.50</td><td>0.20</td><td>750.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl60_NetVolLabel">10.45</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BG Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0008762899&externalidtype=ISIN">BG Group PLC</a></td><td>1314.50</td><td style="color:Red;">-2.65</td><td style="color:Red;">-0.20</td><td>1317.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl61_NetVolLabel">1,391.86</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BH Global Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GG00B2QQPT96&externalidtype=ISIN">BH Global Ltd</a></td><td>1131.50</td><td>6.00</td><td>0.53</td><td>1126.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl62_NetVolLabel">47.63</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BH Macro Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GG00B1NP5142&externalidtype=ISIN">BH Macro Ltd</a></td><td>1991.00</td><td>8.99</td><td>0.45</td><td>1986.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl63_NetVolLabel">10.24</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BHP Billiton PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000566504&externalidtype=ISIN">BHP Billiton PLC</a></td><td>2006.75</td><td>13.50</td><td>0.68</td><td>1993.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl64_NetVolLabel">2,216.84</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Big Yellow Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0002869419&externalidtype=ISIN">Big Yellow Group PLC</a></td><td>341.30</td><td>5.00</td><td>1.49</td><td>335.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl65_NetVolLabel">201.24</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Bilfinger Berger Global Infrastructure SICAV SA" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=LU0686550053&externalidtype=ISIN">Bilfinger Berger Global Inf...</a></td><td>107.88</td><td>0.20</td><td>0.19</td><td>108.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl66_NetVolLabel">105.55</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Biotech Growth Trust (The) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000385517&externalidtype=ISIN">Biotech Growth Trust (The) PLC</a></td><td>288.75</td><td style="color:Red;">-0.90</td><td style="color:Red;">-0.31</td><td>290.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl67_NetVolLabel">86.38</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BlackRock Commodities Income Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0N8MF98&externalidtype=ISIN">BlackRock Commodities Incom...</a></td><td>124.12</td><td style="color:Red;">-0.82</td><td style="color:Red;">-0.66</td><td>124.38</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl68_NetVolLabel">12.45</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BlackRock Frontiers Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B3SXM832&externalidtype=ISIN">BlackRock Frontiers Investm...</a></td><td>81.12</td><td>0.13</td><td>0.16</td><td>81.25</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl69_NetVolLabel">19.79</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BlackRock Greater Europe Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B01RDH75&externalidtype=ISIN">BlackRock Greater Europe In...</a></td><td>182.00</td><td style="color:Red;">-0.50</td><td style="color:Red;">-0.27</td><td>182.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl70_NetVolLabel">12.37</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BlackRock Latin American Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0005058408&externalidtype=ISIN">BlackRock Latin American In...</a></td><td>515.75</td><td style="color:Red;">-3.25</td><td style="color:Red;">-0.63</td><td>514.75</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl71_NetVolLabel">16.11</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BlackRock New Energy Investment Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0009737932&externalidtype=ISIN">BlackRock New Energy Invest...</a></td><td>31.50</td><td style="color:Red;">-0.62</td><td style="color:Red;">-1.96</td><td>31.63</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl72_NetVolLabel">299.42</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BlackRock Smaller Companies Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0006436108&externalidtype=ISIN">BlackRock Smaller Companies...</a></td><td>527.25</td><td>0.00</td><td>0.00</td><td>527.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl73_NetVolLabel">21.49</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BlackRock World Mining Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0005774855&externalidtype=ISIN">BlackRock World Mining Trus...</a></td><td>588.50</td><td>4.11</td><td>0.70</td><td>584.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl74_NetVolLabel">189.30</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Bloomsbury Publishing PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0033147751&externalidtype=ISIN">Bloomsbury Publishing PLC</a></td><td>131.00</td><td style="color:Red;">-6.02</td><td style="color:Red;">-4.35</td><td>138.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl75_NetVolLabel">196.59</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BlueCrest AllBlue Fund Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B13YVW48&externalidtype=ISIN">BlueCrest AllBlue Fund Ltd</a></td><td>166.55</td><td>0.20</td><td>0.12</td><td>166.30</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl76_NetVolLabel">375.94</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Bluecrest Bluetrend Ltd" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GG00B7MSX903&externalidtype=ISIN">Bluecrest Bluetrend Ltd</a></td><td>100.75</td><td>0.34</td><td>0.34</td><td>100.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl77_NetVolLabel">38.10</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Bodycote PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B3FLWH99&externalidtype=ISIN">Bodycote PLC</a></td><td>372.90</td><td>9.80</td><td>2.70</td><td>363.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl78_NetVolLabel">104.25</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Booker Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B01TND91&externalidtype=ISIN">Booker Group PLC</a></td><td>99.27</td><td>0.90</td><td>0.92</td><td>98.35</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl79_NetVolLabel">1,261.03</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Boot (Henry) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001110096&externalidtype=ISIN">Boot (Henry) PLC</a></td><td>132.75</td><td>2.25</td><td>1.73</td><td>129.75</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl80_NetVolLabel">2.47</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Bovis Homes Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001859296&externalidtype=ISIN">Bovis Homes Group PLC</a></td><td>526.75</td><td>8.50</td><td>1.64</td><td>518.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl81_NetVolLabel">88.32</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BP PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0007980591&externalidtype=ISIN">BP PLC</a></td><td>432.45</td><td style="color:Red;">-2.60</td><td style="color:Red;">-0.60</td><td>435.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl82_NetVolLabel">8,774.72</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Braemar Shipping Services PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0000600931&externalidtype=ISIN">Braemar Shipping Services PLC</a></td><td>416.00</td><td style="color:Red;">-6.30</td><td style="color:Red;">-1.51</td><td>416.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl83_NetVolLabel">6.17</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Brammer PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001195089&externalidtype=ISIN">Brammer PLC</a></td><td>241.50</td><td style="color:Red;">-2.75</td><td style="color:Red;">-1.12</td><td>244.75</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl84_NetVolLabel">27.29</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Brewin Dolphin Holdings PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001765816&externalidtype=ISIN">Brewin Dolphin Holdings PLC</a></td><td>179.15</td><td>1.66</td><td>0.93</td><td>177.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl85_NetVolLabel">32.63</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="British American Tobacco PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0002875804&externalidtype=ISIN">British American Tobacco PLC</a></td><td>3156.25</td><td>2.50</td><td>0.08</td><td>3154.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl86_NetVolLabel">1,193.69</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="British Assets Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001297562&externalidtype=ISIN">British Assets Trust PLC</a></td><td>121.05</td><td>0.88</td><td>0.73</td><td>120.20</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl87_NetVolLabel">59.65</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="British Empire Securities & General Trust PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001335081&externalidtype=ISIN">British Empire Securities &...</a></td><td>449.80</td><td>3.70</td><td>0.83</td><td>446.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl88_NetVolLabel">115.98</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="British Land Co PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001367019&externalidtype=ISIN">British Land Co PLC</a></td><td>531.25</td><td>0.00</td><td>0.00</td><td>531.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl89_NetVolLabel">687.24</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="British Polythene Industries PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0007797425&externalidtype=ISIN">British Polythene Industrie...</a></td><td>377.50</td><td>1.00</td><td>0.26</td><td>380.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl90_NetVolLabel">34.84</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="British Sky Broadcasting Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001411924&externalidtype=ISIN">British Sky Broadcasting Gr...</a></td><td>718.75</td><td style="color:Red;">-0.50</td><td style="color:Red;">-0.07</td><td>719.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl91_NetVolLabel">1,096.16</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Britvic PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0N8QD54&externalidtype=ISIN">Britvic PLC</a></td><td>361.15</td><td>2.60</td><td>0.73</td><td>358.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl92_NetVolLabel">188.17</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Brown (N) Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B1P6ZR11&externalidtype=ISIN">Brown (N) Group PLC</a></td><td>330.25</td><td>5.40</td><td>1.66</td><td>325.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl93_NetVolLabel">133.23</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Brunner Investment Trust (The) PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001490001&externalidtype=ISIN">Brunner Investment Trust (T...</a></td><td>419.75</td><td>0.00</td><td>0.00</td><td>418.50</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl94_NetVolLabel">.00</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="BTG PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0001001592&externalidtype=ISIN">BTG PLC</a></td><td>349.00</td><td>2.00</td><td>0.58</td><td>346.80</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl95_NetVolLabel">102.28</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="BT Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0030913577&externalidtype=ISIN">BT Group PLC</a></td><td>217.40</td><td>0.04</td><td>0.02</td><td>217.30</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl96_NetVolLabel">7,000.26</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Bumi PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B5BLXT62&externalidtype=ISIN">Bumi PLC</a></td><td>251.50</td><td style="color:Red;">-5.40</td><td style="color:Red;">-2.10</td><td>257.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl97_NetVolLabel">117.63</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="Bunzl PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B0744B38&externalidtype=ISIN">Bunzl PLC</a></td><td>1026.00</td><td>6.00</td><td>0.59</td><td>1020.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl98_NetVolLabel">195.30</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Burberry Group PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB0031743007&externalidtype=ISIN">Burberry Group PLC</a></td><td>1139.00</td><td style="color:Red;">-2.00</td><td style="color:Red;">-0.17</td><td>1143.00</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl99_NetVolLabel">434.11</span>
                </td>
		</tr><tr class="normal">
			<td class="left"><a title="bwin.party digital entertainment PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GI000A0MV757&externalidtype=ISIN">bwin.party digital entertai...</a></td><td>124.80</td><td>7.30</td><td>6.21</td><td>117.60</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl100_NetVolLabel">4,427.23</span>
                </td>
		</tr><tr class="alternate">
			<td class="left"><a title="Cable & Wireless Communications PLC" href="http://tools.morningstar.co.uk/t92wz0sj7c/@REPORT/default.aspx?externalid=GB00B5KKT968&externalidtype=ISIN">Cable & Wireless Communicat...</a></td><td>37.50</td><td>0.25</td><td>0.67</td><td>37.25</td><td>
                <span id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl101_NetVolLabel">1,400.72</span>
                </td>
		</tr><tr>
			<td class="left footer" colspan="6">Data as of  25 October 2012 14:42</td>
		</tr><tr class="paging">
			<td colspan="6">
        <a id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl103_ButtonFirst" disabled="disabled">First</a> |
        <a id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl103_ButtonPrev" disabled="disabled">Previous</a> |
        <a id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl103_ButtonNext" href="javascript:__doPostBack('ctl00$ctl00$MainContent$EquityContent$IndexStockPricesCC1$IndexStockView$ctl103$ButtonNext','')">Next</a> |
        <a id="ctl00_ctl00_MainContent_EquityContent_IndexStockPricesCC1_IndexStockView_ctl103_ButtonLast" href="javascript:__doPostBack('ctl00$ctl00$MainContent$EquityContent$IndexStockPricesCC1$IndexStockView$ctl103$ButtonLast','')">Last</a>
        </td>
		</tr>
	</table>
</div>


<br />





    

        </form>
        
        
    
                    </div>
                    
             
                </td>
                
              </tr>
          </table>
        </div>   
        <div class="layout_right_col_h">
            <script type="text/javascript">
                 WebAdsWriteTag('160', '600','EquitiesRight');
            </script>
        </div> 
        
        <!-- bottom ads -->
          
                
                

   <!-- bottom ads -->
  <div class="bottomAd layout_content_right" style="margin-top:10px; margin-bottom:10px;">
        <div id="ctl00_ctl00_MainContent_BottomAd_panelBottomAdLeft">
	
            <div style="float:left;">
                <div class="LayerFatter LayerFatterDKBanner">
                    <script type="text/javascript">
                        WebAdsWriteTag('300', '250', 'EquitiesMPU');                    
                    </script>
                </div>
            </div>
        
</div>
        <div id="ctl00_ctl00_MainContent_BottomAd_panelBottomAdRight">
	
            <div  style="float:right; width:370px;" >
            
            
            <div  class="bottomRightAd" >
            
				<div class="LayerFatterTitle2  LayerFatter2">
				   <img ID="TitleImage" class="noborder" src="/includes/images/spotlight_centre.gif" />
				</div>
                <div class="item">
                    <script type="text/javascript">
                        WebAdsWriteTag('300', '150', 'QuickRankBottomRightTop');                    
                    </script>
                </div>
                
                <div  class="item last">
                    <script type="text/javascript">
                        WebAdsWriteTag('300', '150', 'QuickRankBottomRightBottom');                    
                    </script>
                </div>
                </div>
            </div>
           
        
</div>
        
	</div>



<script type="text/javascript">
	if (showOverlay == true) {
		showDialog();
	}
</script>

	</div>
</body>
</html>
"""

all_share_url ='http://www.morningstar.co.uk/uk/equities/indexstockprices.aspx?index=FTSE_ALL_SHARE'
aim_all_share_url ='http://www.morningstar.co.uk/uk/equities/indexstockprices.aspx?index=FTSE_AIM_ALL_SHARE'

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_target(page):
#####
# only look for pages inside the starting domain
#    start_link = page.find('<a href="' + start_page)
#####
    start_link = page.find(' href="')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q): 
    for e in q:
        if e not in p:
            p.append(e)

def start_end_point(page,aStr):
    start = page.find(aStr) # place to start searching for links
    if start == -1: 
        return 0, 0
    end = page.find('</tr><tr>') # place to end
    if start == -1: 
        return 0, 0
    print start
    print end
    return start, end

def extract_stock_links(page_html):
    page_links = []
    start,end = start_end_point(page_html,'FTSE All Share Index Share Prices')
    
    page_html = page_html[start:end]
    while True:
        url,endpos = get_next_target(page_html)
        if url:
            page_links.append(url)
            page_html = page_html[endpos:]
        else:
            break
    return page_links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    stock_links = []
    stock_crawled = []
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            # extract links to stock details on current page
            #content = get_page(page)
            #outlinks = get_all_links(content)
            stock_detail_links = extract_stock_links(ini_html)
            union(stock_links,stock_detail_links)

            # extract link to next page
            #next_page = next_page_link(ini_html)
            #union(tocrawl, next_page)
            #crawled.append(page)
    
    #while stock_links: 
        #page = tocrawl.pop()
        #if page not in crawled:
            ##content = get_page(page)
            ##outlinks = get_all_links(content)
            #outlinks = stock_links(ini_html)
            #union(stock_links, next_page)

            #next_page = next_page_link(ini_html)
            #union(tocrawl, next_page)
            #crawled.append(page)
    return stock_links

print crawl_web(all_share_url)
