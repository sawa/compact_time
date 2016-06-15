#frozen-string-literal: true

module CompactTime
	def compact_date_time; "#{compact_date} #{compact_time}" end
	def compact_date; "%04d%s%02d%s" % compact_date_array end
	def compact_time; strftime("%T.%L%:z") end
	def compact_date_array; [ctn_year, ctn_quatery, ctn_week, ctn_day] end
	Alph = [nil, "A", "B", "C", "D", "E", "F", "G"]
	protected def ctn_year; strftime("%G").to_i end
	protected def ctn_quatery; Alph[strftime("%V").to_i.-(1)./(13).+(1)] end
	protected def ctn_week; strftime("%V").to_i.-(1).%(13).+(1) end
	protected def ctn_day; Alph[strftime("%u").to_i] end
end

class Time
	include CompactTime
end

class Date
	include CompactTime
end
