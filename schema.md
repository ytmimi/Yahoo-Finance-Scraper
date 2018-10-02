# Schema Types

<details>
  <summary><strong>Table of Contents</strong></summary>

  * [Query](#query)
  * [Objects](#objects)
    * [Option](#option)
    * [OptionChain](#optionchain)
    * [StockOverview](#stockoverview)
    * [StockPrice](#stockprice)
    * [Ticker](#ticker)
  * [Scalars](#scalars)
    * [Boolean](#boolean)
    * [Float](#float)
    * [Int](#int)
    * [String](#string)

</details>

## Query 
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ticker</strong></td>
<td valign="top"><a href="#ticker">Ticker</a></td>
<td>

Data for a single stock.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">ticker</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A valid stock ticker.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">startDate</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A date in the form mm/dd/yyyy. Defaults to 365 days prior to the current date.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">endDate</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A date in the form mm/dd/yyyy. Defaults to the current date.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">frequency</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A given frequency for stock data. Values must be one of the following: 1d,  1wk, or, 1mo.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tickers</strong></td>
<td valign="top">[<a href="#ticker">Ticker</a>]</td>
<td>

Data for a list of stocks.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tickers</td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

A list of valid stock tickers.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">startDate</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A date in the form mm/dd/yyyy. Defaults to 365 days prior to the current date.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">endDate</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A date in the form mm/dd/yyyy. Defaults to the current date.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">frequency</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A given frequency for stock data. Values must be one of the following: 1d,  1wk, or, 1mo.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>calls</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

Data on all call options for the given (optional) expiration date will be returned. By default calls from the current expiration month will be returned.If the data provided is not an exact expiration date the closest expiration following the provided date with be returned. If there aren't any options expiring after the provided date, the query will resolve to its default behavior.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">underlying</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ticker of the underlying stock.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">expiration</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The expiration date of the option contract in mm/dd/yyyy format. Defauts to the closest expiration.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>puts</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

Data on all put options for the given (optional) expiration date will be returned. By default puts from the current expiration month will be returned.If the data provided is not an exact expiration date the closest expiration following the provided date with be returned. If there aren't any options expiring after the provided date, the query will resolve to its default behavior.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">underlying</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ticker of the underlying stock.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">expiration</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The expiration date of the option contract in mm/dd/yyyy format. Defauts to the closest expiration.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>optionStrikes</strong></td>
<td valign="top">[<a href="#float">Float</a>]</td>
<td>

A list of all available strikes for the given expiration date will be returned.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">underlying</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ticker of the underlying stock.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">expiration</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The expiration date of the option contract in mm/dd/yyyy format. Defauts to the closest expiration.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>optionExpirationDates</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

A list of all currently available option expiration dates are return in mm/dd/yy format.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">underlying</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ticker of the underlying stock.

</td>
</tr>
</tbody>
</table>

## Objects

### Option

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>contractSymbol</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

A unique identifier giving information on the type, expiration, and strike of an option contract.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>expiration</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The expiration date of the option contract.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>change</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Decimal value representing the change in price.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastPrice</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The last price at which a contract was bought and sold.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>inTheMoney</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td>

Defines whether the option contract has intrinsic value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>impliedVolatility</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

A measure of the markets expectation of price movements in the underlying asset prior to the option's expiration.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>openInterest</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The number of open contracts for the underlying at the given strike

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>percentChange</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Percentage representing the change in price.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>bid</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The price offered to buy the option.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ask</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The price offered to sell the option.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>volume</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

the total number of contracts for each strike that traded during the day.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastTradeDate</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Date showing the last time the contract was traded.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>currency</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The currency the option contract trades in.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>strike</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The price at which the underlying asset can be bought or sold.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>contractSize</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The units of underlying that is represented by one contract. Typically one option contract covers 100 shares of stock.

</td>
</tr>
</tbody>
</table>

### OptionChain

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>underlying</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ticker of the underlying stock.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>date</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The expiration date of the option contract.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>strikes</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

A list of all available stike prices for the given expiration date.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>calls</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

A list of all call options for the given expiration date.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>puts</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

A list of all put options for the given expiration date.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>allOptions</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

A list of all call and put options for the given expiration date.

</td>
</tr>
</tbody>
</table>

### StockOverview

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>symbol</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

A valid stock ticker.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>openToday</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Todays price when the stock opened.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>highToday</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The highest price the stock reached today.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lowToday</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The lowest price the stock reached today.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>closePrevious</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The last trading days closing price.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>recentPrice</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The most recent stock price available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>volumeToday</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The number of shares traded today.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sharesOtstanding</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The total number of shares availabe.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>marketCap</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The value of a companies equity.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>fiftyTwoWeekHigh</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The stockes highest price over the last year.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>fiftyTwoWeekLow</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The stocks lowest price over the last year.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>fiftyTwoWeekRange</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The low-high range over the last year.

</td>
</tr>
</tbody>
</table>

### StockPrice

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>date</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The date when the stock traded.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The share price when the market opened.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>high</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The highest share price on the given day.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>low</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The lowest share price on the given day.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>close</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The share price when the market closed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>volume</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The total amount of shares traded during the day.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>adjclose</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The close price adjusted for dividends and stock splits.

</td>
</tr>
</tbody>
</table>

### Ticker

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ticker</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A valid stock ticker.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>startDate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The first date requested for stock data.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>endDate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The last date requested for stock data.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>frequency</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Determins the frequency of stock price data. 1d for daily, 1wk for weekly, and 1mo for monthly 

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stockPrices</strong></td>
<td valign="top">[<a href="#stockprice">StockPrice</a>]</td>
<td>

A list of stock price data.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stockOverview</strong></td>
<td valign="top"><a href="#stockoverview">StockOverview</a></td>
<td>

Basic information on the stock price performace on the day and over the year

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relatedStocks</strong></td>
<td valign="top">[<a href="#stockoverview">StockOverview</a>]</td>
<td>

Current and yearly performance information on a list of related stock tickers

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>calls</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

A list of near term call options for the given stock

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>puts</strong></td>
<td valign="top">[<a href="#option">Option</a>]</td>
<td>

A list of near term put options for the given stock.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>optionChains</strong></td>
<td valign="top">[<a href="#optionchain">OptionChain</a>]</td>
<td>

A list of all option contracts that expire on the same day.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Limit the number of results returned. Must be > 0.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The `Boolean` scalar type represents `true` or `false`.

### Float

The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point). 

### Int

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31 - 1) and 2^31 - 1 since represented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).

### String

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

