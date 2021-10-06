//@version=4

// Revision:        1
// Author:          @millerrh
// Strategy:  
//      Entry: Buy when Donchian Channel breaks out
//      Exit: Trail a stop with the lower Donchian Channel band
// Conditions/Variables:
//    1. Can add a filter to only take setups that are above a user-defined moving average (helps avoid trading counter trend) 
//    2. Manually configure which dates to back test
//    3. User-Configurable DC Channel length, with independent settings for top and bottom (Similar to Jessee Livermore Trading System where he used 150/50)


// === CALL STRATEGY/STUDY, PROGRAMATICALLY ENTER STRATEGY PARAMETERS HERE SO YOU DON'T HAVE TO CHANGE THEM EVERY TIME YOU RUN A TEST ===
// (STRATEGY ONLY) - Comment out srategy() when in a study() 
strategy("Donchian Breakout", overlay=true, initial_capital=10000, currency='USD', 
   default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1)
// (STUDY ONLY) - Comment out study() when in a strategy() 
//study("Donchian Breakout", overlay=true)


// === BACKTEST RANGE ===
From_Year  = input(defval = 2010, title = "From Year")
From_Month = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
From_Day   = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
To_Year    = input(defval = 9999, title = "To Year")
To_Month   = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
To_Day     = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
Start  = timestamp(From_Year, From_Month, From_Day, 00, 00)  // backtest start window
Finish = timestamp(To_Year, To_Month, To_Day, 23, 59)        // backtest finish window

// == INPUTS ==
trigInput = input(title = "Execute Trades On...", defval = "Close", options=["Wick","Close"]) // Useful for comparing standing stop orders vs. waiting for candle closes prior to action
stopTrail = input(title = "Trail Stops On...", defval = "ATR", options = ["ATR","Bottom of DC Channel","Midline of DC Channel","Tightest of ATR/Bot DC Channel"])
dcPeriodHigh = input(title="DC period Upper", type=input.integer, defval=150)
dcPeriodLow = input(title="DC period Lower", type=input.integer, defval=50)

// === PLOT THE DONCHIAN CHANNEL ===
// Logic
dcUpper = highest(high, dcPeriodHigh)[1]
dcLower = lowest(low, dcPeriodLow)[1]
dcMid = avg(dcUpper, dcLower)

// Plotting
dcUplot = plot(dcUpper, color=color.blue, linewidth=1, title="Upper Channel Line")
dcLplot = plot(dcLower, color=color.blue, linewidth=1, title="Lower Channel Line")
dcMidPlot = plot(dcMid, color=color.gray, linewidth=1, title="Mid-Line Average")
fill(dcUplot, dcLplot, color=color.gray, transp=90)

// == FILTERING ==
// Inputs
useMaFilter = input(title = "Use MA for Filtering?", type = input.bool, defval = true)
maType = input(defval="SMA", options=["EMA", "SMA"], title = "MA Type For Filtering")
maLength   = input(defval = 100, title = "MA Period for Filtering", minval = 1)

// Declare function to be able to swap out EMA/SMA
ma(maType, src, length) =>
    maType == "EMA" ? ema(src, length) : sma(src, length) //Ternary Operator (if maType equals EMA, then do ema calc, else do sma calc)
maFilter = ma(maType, close, maLength)
plot(maFilter, title = "Trend Filter MA", color = color.green, linewidth = 3, style = plot.style_line, transp = 50)

// Check to see if the useMaFilter check box is checked, this then inputs this conditional "maFilterCheck" variable into the strategy entry 
maFilterCheck = if useMaFilter == true
    maFilter
else
    0

// == ENTRY AND EXIT CRITERIA ==
// Trigger stop based on candle close or High/Low (i.e. Wick) - If doing daily timeframe, can do candle close.  Intraday should use wick.
trigResistance = trigInput == "Close" ? close : trigInput == "Wick" ? high : na
trigSupport = trigInput == "Close" ? close : trigInput == "Wick" ? low : na
buySignal = trigResistance >= dcUpper[1] // The [1] looks at the previous bar's value as it didn't seem to be triggering correctly without it (likely) DC moves with each bar
sellSignal = trigSupport <= dcLower[1]

buy = buySignal and time > Start and time < Finish and dcUpper[1] > maFilterCheck // All these conditions need to be met to buy


// (STRATEGY ONLY) Comment out for Study
// This string of code enters and exits at the close
if (trigInput == "Close")
    strategy.entry("Long", strategy.long, when = buy)
    strategy.close("Long", when = sellSignal)

// This string of code enters and exits at the wick (i.e. with pre-set stops)
if (trigInput == "Wick")
    strategy.entry("Long", strategy.long, stop = dcUpper[1], when = time > Start and time < Finish and dcUpper[1] > maFilterCheck)
    strategy.exit("Exit Long", from_entry = "Long", stop = dcLower[1])



