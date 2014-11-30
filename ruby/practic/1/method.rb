# Ruby Sample program from www.sapphiresteel.com

def showstring
	puts( "Hello" )
end

def showname( aName )
	puts( "Hello #{aName}" )
end


def return_name( aFirstName, aSecondName )
	return "Hello #{aFirstName} #{aSecondName}"
end

def return_name2 aFirstName, aSecondName 
	return "Hello #{aFirstName} #{aSecondName}"
end

showstring
showname( "Fred" )
puts( return_name( "Mary Mary", "Quite-Contrary"  ) )
puts( return_name( "Little Jack", "Horner"  ) )