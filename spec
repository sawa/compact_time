#!ruby
#frozen-string-literal: false

manage "lib/compact_time.rb"

spec nil,
	"The gem `compact_time` is a Ruby implementation of a proposal by its author to describe date and/or time in a compact and logical way. In the gem, `Time` objects are assigned a few methods for expressing them in the proposed notation.",
coda

spec "=License",
	"The MIT License (MIT)",
	"Copyright (c) 2013-2016 sawa",
	"Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:",
	"The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.",
	"THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.",
coda

spec "=Compact Time Notation",
coda

spec "==Components",
	"The design of the notation is based on the following guildlines:",
	"* Make use of the two natural units \"year\" and \"day\", which correspond to the revolution and rotation periods of the earth, respectively, and on which the concept of scheduling has widely depended on throughout human history.",
	"* Get rid of the notion \"month\", which is relatively popular today, but is nevertheless not a simple regular/logical notion as is today due to its modification over the history.",
	"* Instead, make use of the notion \"week\", which is arbitrary and has its origin in particular religion, but has neverthelss become the de facto scheduling unit of daily life throughout the developed world today.",
	"* The notions \"hour\", \"minute\", and \"second\" are arbitrary, but are not as irregular as \"month\", and are so commonly used today that it is unpractical to invent a system not based on them and expect it to be used widely. Hence, use them.",
	"For regularity, the proposed notation adopts ISO 8601's \"week-numbering year\" as the notion of year. The proposal is also based on ISO 8601 week, but such notion of week is not very useful as is. In particular, its range (1 to 52 for common years, 1 to 53 for leap years) is too large for an average person to recognize in daily life. To solve this problem, the propsed notation introduces the notion \"quatery\". A common year consists of four quateries, each consisting of thirteen ISO 8601 weeks. A leap year has a fifth quatery that consists of a single week. A week consists of seven \"days of week\".",
	"Regarding the time part, the notions \"24-hour\", \"minute\", \"second\", and \"millisecond\" are adopted, and they are displayed together with the difference from UTC.",
coda

spec "==Notation",
	"For compactness and readability, the notation does not use a delimiter within the date part. This is made possible by expressing the  elements alternatively in letters and in numbers. Particularly, quateries are expressed with \"A\" to \"E\", and the days of week are expressed with \"A\" to \"G\". For example, the time object:",
	<<~'RUBY'.code,
		time = Time.new(2000, 1, 1)
	RUBY
	"will have its date part expressed as:",
	<<~'RUBY'.code,
		time.compact_date # => "1999D13F"
	RUBY
	"For programmatic use, the elements can be acheived in an array:",
	<<~'RUBY'.code,
		time.compact_date_array # => [1999, "D", 13, "F"]
	RUBY
	"The time part uses the conventional notation. For complete date-time and just the time portion, the following expressions are available:",
	<<~'RUBY'.code,
		time = Time.new(2000, 1, 1, 15, 24, 60, 0)
		time.compact_date_time # => "1999D13F 15:25:00.000+00:00"
		time.compact_time      # => "15:25:00.000+00:00"
	RUBY
coda

class Time
	spec nil,
		"time = Time.new(2000, 1, 1, 15, 24, 60, 0)".setup,
	coda
	spec "#compact_date_time",
		{"()" => String},
		"Joins {#compact_date} and {#compact_time} with a space. For example,",
		'Time.new(2000, 1, 1, 15, 24, 60, 0).compact_date_time # => "1999D13F 15:25:00.000+00:00"'.code,
		expr('time').UT == "1999D13F 15:25:00.000+00:00",
	coda
	spec "#compact_date",
		{"()" => String},
		"Returns a string of `self` in compact date format. For example,",
		'Time.new(2000, 1, 1, 15, 24, 60, 0).compact_date # => "1999D13F"'.code,
		expr('time').UT == "1999D13F",
	coda
	spec "#compact_date_array",
		{"()" => Array},
		"Returns an array of the elements used in {#compact_date}. For example,",
		'Time.new(2000, 1, 1, 15, 24, 60, 0).compact_date_array # => [1999, "D", 13, "F"]'.code,
		expr('time').UT == [1999, "D", 13, "F"],
	coda
	spec "#compact_time",
		{"()" => String},
		"Returns a string of the time portion of `self`. It expresses 24-hour hour, minute, second, millisecond, and difference from UTC. For example,",
		'Time.new(2000, 1, 1, 15, 24, 60, 0).compact_time # => "15:25:00.000+00:00"'.code,
		expr('time').UT == "15:25:00.000+00:00",
	coda
	hide spec "::Alph",
		"!Letters used for `ctn_quatery` and `ctn_day`.",
	coda
	hide spec "#ctn_year",
		"!First element of `compact_date_array`.",
	coda
	hide spec "#ctn_quatery",
		"!Second element of `compact_date_array`.",
	coda
	hide spec "#ctn_week",
		"!Third element of `compact_date_array`.",
	coda
	hide spec "#ctn_day",
		"!Fourth element of `compact_date_array`.",
	coda
end

hide spec "::CompactTime",
coda

move spec "::Time",
coda

move spec "::Date",
coda
